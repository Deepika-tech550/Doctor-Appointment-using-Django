from django.contrib import admin
from django.urls import path
from doctor import views



urlpatterns = [
	path('',views.index,name='index'),
    path('book_appointment',views.book,name='book'),
    path('index.html/',views.index,name='index')
]
 

#http://127.0.0.1:8000/ 