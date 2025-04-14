from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Tv_Show
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

@login_required
def tv_shows(request):
    tvshows = Tv_Show.objects.filter(user=request.user)
    return render(request, 'tvShows/index.html', {'tvshows': tvshows})

def tvshow_detail(request, tvshow_id):
    tvshow = Tv_Show.objects.get(id=tvshow_id)
    return render(request, 'tvShows/detail.html', {'tvshow': tvshow})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tvshow-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class TvShowCreate(LoginRequiredMixin, CreateView):
    model = Tv_Show
    fields = ['title', 'seasons', 'rating', 'recommended', 'finished_watching', 'description', 'platforms']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TvShowUpdate(LoginRequiredMixin, UpdateView):
    model = Tv_Show
    fields = '__all__'

class TvShowDelete(LoginRequiredMixin, DeleteView):
    model = Tv_Show
    success_url = '/tvShows/'

class Home(LoginView):
    template_name = 'home.html'

