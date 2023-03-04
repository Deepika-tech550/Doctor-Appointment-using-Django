"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

 #,change static in style,link,src
 #
from django.contrib import admin
from django.urls import path
from food.views import *

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('index.html/',index),
    path('index.html/book',book),
    path('book',book),
    path('about.html',about),
    path('feature.html',feature),
    path('team.html',team),
    path('menu.html',menu),
    path('booking.html',booking),
    path('blog.html',blog),
    path('single.html',single),
    path('contact.html',contactt),
    path('terms.html',term),
    path('privacy.html',privacy)

    
]
urlpatterns= urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
