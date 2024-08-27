from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE="M","MALE"
        FEMALE="F","FEMALE"
        OTHER="O","OTHER"
        
        
    class USER_ROLES(models.TextChoices):
        FACILITY_OFFICER="FHO","FACILITY_HEALTH_OFFICER"
        EPIDEMIOLOGIST="EPD","EPIDEMIOLOGIST"
        NORMAL_USER="NU","NORMAL_USER"  
        
        
    first_name=models.CharField(max_length=200,null=True,blank=False)
    last_name=models.CharField(max_length=200,null=True,blank=False)
    phone_number=models.CharField(max_length=15,null=True,blank=False)
    gender=models.CharField(max_length=2,null=True,blank=False,choices=Gender.choices,default=Gender.OTHER)
    address=models.CharField(max_length=200,blank=False,null=True)
    location=models.CharField(max_length=150,blank=False,null=True)
    age=models.IntegerField(blank=False,null=True)
    role=models.CharField(max_length=10,blank=False,null=False,choices=USER_ROLES.choices,default=USER_ROLES.NORMAL_USER)
    
    
    

    
    