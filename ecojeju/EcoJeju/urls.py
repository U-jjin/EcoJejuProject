"""config URL Configuration

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
from django.urls import path, include

from EcoJeju import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('dashboard_v2', views.dashboard_v2, name="dashboard_v2"),
    path('dashboard_v3', views.dashboard_v3, name="dashboard_v3"),

    path('login', views.login, name="login"),
    path('recover',views.recover, name="recover"),
    path('register', views.register, name="register"),
    path('registerimpl', views.registerimpl, name='registerimpl'),

]
