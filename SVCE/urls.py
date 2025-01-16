"""SVCE URL Configuration

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
from django.contrib import admin
from django.urls import path
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('register/', Register, name='register'),
    path('loginpage/', Login, name='loginpage'),
    path('logout/', logoutuser, name='logout'),
    path('aboutus/', Aboutus, name='aboutus'),
    path('academics/', Academics, name='academics'),
    path('contactus', Contactus, name='contactus'),
    path('cs/', CS, name='cs'),
    path('es/', EC, name='ec'),
    path('is/', IS, name='is'),
    path('civil/', CIVIL, name='civil'),
    path('ds/', DS, name='ds'),
    path('cyber/', CYBER, name='cyber'),
    path('ai/', AI, name='ai'),
    path('mech/', MECH, name='mech'),
    path('', chat, name='chat'),
    path('placements/', Placements, name='placements'),
    path('dash1/', Dash1, name='dash1'),
    path('events/', Events, name='events'),
]
