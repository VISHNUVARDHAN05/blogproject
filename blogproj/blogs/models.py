from django.db import models
from django.urls import reverse
class category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

temp=category.objects.all().values_list('name','name')
uncategorised = 'uncategorised'
choice=[(uncategorised,'uncategorised')]
for i in temp:
    choice.append(i)
class blog(models.Model):
    title=models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=100,choices=choice,default=uncategorised)
    image=models.ImageField(upload_to="bigimg",default="nopic.png")
    date= models.DateField(auto_now=True)


    def __str__(self):
        return self.title

# Create your models here.
