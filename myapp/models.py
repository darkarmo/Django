from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=255)
    email=models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name
        
class Customer(models.Model):
    name=models.CharField(max_length=100)
    phone_num=models.CharField(max_length=10)
    address=models.CharField(max_length=255)
    email=models.EmailField(max_length=254,null=True,blank=True)
    
    def __str__(self):
        return self.name