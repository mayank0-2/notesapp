"""
URL configuration for notesapp project.

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
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from home import views as home_views

import registration
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api-auth/', include('RestApi.urls')),
    path('register/', include('registration.urls')),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'home.html'), name = 'logout'),
    path('new_notes/', include('newnotes.urls')),
    path('delete/<int:id>', home_views.delete_notes, name='del'),
    path('edit/<int:id>', home_views.edit_notes, name='edit'),
    path('update/<int:id>', home_views.update_notes, name='update'),
    path('api/', include('RestApi.urls')),
]
