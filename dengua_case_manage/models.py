from django.db import models
from Account.models import User
# Create your models here.


class DenguaCase(models.Model):
    class Gender(models.TextChoices):
        MALE="M","MALE"
        FEMALE="F","FEMALE"
        OTHER="O","OTHER"
    class DengueSpreadStatus(models.TextChoices):
        HIGH="H","HIGH"
        MODERATE="M","MODERATE"
        LOW="L","LOW"
    id=models.AutoField(primary_key=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    fullname=models.CharField(max_length=255,null=False,)
    region=models.CharField(max_length=255,null=False,)
    district=models.CharField(max_length=255,null=False,)
    hospital=models.CharField(max_length=255,null=False,)
    dengue_spread_status=models.CharField(max_length=2,null=True,blank=False,choices=DengueSpreadStatus.choices,default=DengueSpreadStatus.MODERATE)
    age=models.IntegerField(null=False)
    temperature=models.FloatField(max_length=255,null=False)
    humidity=models.FloatField(max_length=255,null=False)
    longitude=models.FloatField(max_length=255,null=True)
    latitude=models.FloatField(max_length=255,null=True)
    precipitation=models.FloatField(max_length=255,null=False)
    gender=models.CharField(max_length=2,null=True,blank=False,choices=Gender.choices,default=Gender.OTHER)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.id}"