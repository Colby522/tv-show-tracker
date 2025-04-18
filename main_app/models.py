from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Tv_Show(models.Model):
    title = models.CharField(max_length=100)
    seasons = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    rating = models.DecimalField(max_digits=2, decimal_places=1, 
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    finished_watching = models.BooleanField(null=True)
    recommended = models.BooleanField(null=True)
    description = models.TextField(max_length=500)
    platforms = models. CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tvshow-detail', kwargs={'tvshow_id': self.id})
