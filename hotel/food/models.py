from django.db import models

# Create your models here.

class Burger(models.Model):
	name= models.CharField(max_length=40)
	number= models.CharField(max_length=15)
	email= models.EmailField(max_length=100)
	guest= models.CharField(max_length=50)
	time= models.TimeField(max_length=100)
	date= models.CharField(max_length=30)

class chef(models.Model):
	img= models.ImageField(upload_to='pics')
	name=models.CharField(max_length=50)
	desc= models.TextField()

class dish(models.Model):
	img= models.ImageField(upload_to= 'pics')
	name=models.CharField(max_length=50)
	price=models.FloatField()
	desc=models.TextField()
class dish1(models.Model):
	img= models.ImageField(upload_to= 'pics')
	name=models.CharField(max_length=50)
	price=models.FloatField()
	desc=models.TextField()

class dish2(models.Model):
	img= models.ImageField(upload_to= 'pics')
	name=models.CharField(max_length=50)
	price=models.FloatField()
	desc=models.TextField()

class contact(models.Model):
	name=models.CharField(max_length=50)
	email= models.EmailField()
	sub= models.TextField()
	message= models.TextField()

class comment(models.Model):
	name=models.CharField(max_length=50)
	email= models.EmailField()
	
	message= models.TextField()
