"""
URL configuration for cims project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Map the root path to the home view
    path('computer_entry/', computer_entry, name='computer_entry'),
    path('list/',  computer_list, name='list'),
    path('list/<str:id>/',computer_edit, name='edit'),
    path('list/<int:id>/delete/',computer_delete, name='delete'),
     
]