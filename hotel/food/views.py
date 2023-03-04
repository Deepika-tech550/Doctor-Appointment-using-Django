from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail  import send_mail
from django.conf import settings
from django.contrib import messages
from food.models import Burger,chef,dish,dish1,dish2,comment
from food.models import contact
# Create your views here.

def home(request):
	return render(request,'index.html')

def index(request):
	return render (request,'index.html')

def book(request):
	if request.method == 'POST':
		name= request.POST['name']
		email= request.POST['email']
		number= request.POST['number']
		guest= request.POST['guest']
		date= request.POST['date']
		time=request.POST['time']
		print(name,email,number,guest)
		use=Burger(name=name,number=number,email=email,guest=guest,date=date,time=time)
		use.save();
		print('CREATED')
		return render(request,'index.html')
	return render(request,'booking.html')

def about(request):
	return render (request,'about.html')

def feature(request):
	return render (request,'feature.html')

def team(request):
	area= chef.objects.all()

	return render(request,'team.html',{'area':area})
def menu(request):
	area=dish.objects.all()
	area1=dish1.objects.all()
	area2=dish2.objects.all()
	
	return render(request,'menu.html',{'area':area,'area1':area1,'area2':area2})
def booking(request):
	return render(request,'booking.html')
	
def blog(request):
	return render(request,'blog.html')
def single(request):
	if request.method =='POST':
		name= request.POST['name']
		email=request.POST['email']
		message=request.POST['message']
		print(name,email,message)
		user= comment(name=name,email=email,message=message)
		user.save()
		area= comment.objects.all()
		return render(request,'single.html',{'comments':area})
	else:
		return render(request,'single.html')

def contactt(request):
	if request.method =='POST':
		name= request.POST['name']
		email= request.POST['email']
		sub= request.POST['sub']
		message= request.POST['message']
		print(name,email,sub,message)	
		use= contact(name=name,email=email,sub=sub,message=message)
		use.save()
		send_mail(
			sub ,
			message,
			
			email, #from
			
			['rdeepi1212@gmail.com'],#to mail
			
			)
		
		return render(request,'contact.html',{'name':name})
	else:
		return render(request,'contact.html')
def term(request):
	return render(request,'terms.html')
	
def privacy(request):
	return render(request,'privacy.html')