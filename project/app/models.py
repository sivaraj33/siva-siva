from django.db import models

# Create your models here.
class Details(models.Model):
    Gender_choices=[
        ('M','Male'),
        ('F','Female'),
        ('O','others')
    ]

    Name=models.CharField(max_length=15)
    FirstName=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20)
    PhoneNumber = models.CharField(max_length=15)
    Gender=models.CharField(max_length=1,choices=Gender_choices,default='M')

    
    def __str__(self):
        return self.Name