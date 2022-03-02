from django.db import models

# Create your models here.
class Film(models.Model):
    tytul = models.CharField(max_length=64,blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=2000)

    def __str__(self):
        return self.tytul + ' (' + str(self.rok) + ')'

