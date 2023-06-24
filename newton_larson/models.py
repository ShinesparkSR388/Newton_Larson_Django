from django.db import models

# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key= True)
    username = models.CharField(max_length= 120, unique= True, null= False)
    email = models.CharField(max_length= 120, unique= True, null= False)
    password = models.CharField(max_length= 120, null= False)
    superuser = models.BooleanField(default= False)
    
class SESSION(models.Model):
    id_user = models.IntegerField(null=False)
    username = models.CharField(max_length= 120, null= False)
    superuser = models.BooleanField(null= False)

class problem(models.Model):
    id = models.AutoField(primary_key= True)
    id_user = models.ForeignKey(user, null= False, on_delete=models.CASCADE)
    problem = models.CharField(max_length= 220, null= False)
    x = models.FloatField(max_length= 90, null= False)
    error = models.FloatField(max_length=5, null= False)
    