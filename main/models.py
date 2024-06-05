from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User



class Car(models.Model):
    model = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    year = models.IntegerField(validators=[MinValueValidator(0)])
    odometer = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    text = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.model

# Create your models here.
