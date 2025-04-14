from django.db import models

class Tv_Show(models.Model):
    title = models.CharField(max_length=100)
    seasons = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    finished_watching = models.BooleanField(null=True)
    recommended = models.BooleanField(null=True)
    description = models.TextField(max_length=500)
    platforms = models. CharField(max_length=100)

    def __str__(self):
        return self.title
