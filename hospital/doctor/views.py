from django.shortcuts import render
from doctor.models import appointment
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request):
	return render(request,'index.html')

def book(request):
	if request.method=='POST':
		name= request.POST['name']
		email = request.POST['email']
		phone= request.POST['phone']
		date=request.POST['date']
		department=request.POST['department']
		doctor=request.POST['doctor']
		message=request.POST['message']
		print(name,email,phone,date,department,doctor,message)

		user= appointment(name=name,email=email,phone=phone,appointment_date=date,department=department,doctor=doctor,message=message)
		user.save()
		appoin = 'Name '+name +' Date '+date + ' Doctor '+doctor +' Department '+department

		send_mail(
			    'Appointment',
			    appoin,

			    email,
			    ['djangop099@gmail.com'],
			    
			)
		print('mail sended')


		return render(request,'booked.html',{'detail':{'name':name,'email':email,'phone':phone,
			'date':date, 'department':department,'doctor':doctor,'message':message}})



	else:
		return render(request,'index.html')