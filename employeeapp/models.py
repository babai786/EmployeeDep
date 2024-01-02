from django.db import models

# Create your models here.



class Employee(models.Model):
    name= models.CharField(max_length=100,null=True,blank=False)
    phone = models.CharField(max_length=15,null=True,blank=True)
    address= models.CharField(max_length=250,null=True,blank=True)


    def __str__(self):
        return self.name







