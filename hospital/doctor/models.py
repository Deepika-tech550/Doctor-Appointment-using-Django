from django.db import models

# Create your models here.

class appointment(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	phone = models.CharField(max_length=15)
	appointment_date= models.CharField(max_length=30)
	department=models.CharField(max_length=50)
	doctor= models.CharField(max_length=50)
	message= models.TextField()