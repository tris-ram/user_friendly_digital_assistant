from django.db import models

class user(models.Model):
    email=models.EmailField(max_length=50,primary_key=True)
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    info=models.BooleanField(default=False)
    class Meta:
        db_table="user"
    
class info(models.Model):
    email=models.EmailField(max_length=50,primary_key=True)
    name=models.CharField(max_length=30)
    DOB=models.DateField()
    language=models.CharField(max_length=20)
    b_place=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    mobile=models.IntegerField()
    EDU_CHOICES=(('S',"School"),('C','College'),)
    Education=models.CharField(max_length=1,choices=EDU_CHOICES)
    pan=models.BooleanField()
    d_license=models.BooleanField()
    passport=models.BooleanField()
    voter=models.BooleanField()
    class Meta:
        db_table="info"