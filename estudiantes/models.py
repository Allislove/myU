from django.db import models

# Create your models here.
class Estudiante(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    idNumber = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    score = models.IntegerField(null=True)
    approved = models.BooleanField(null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
       return self.firstName