"""
URL configuration for To_Do_List project.

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
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home),
    path("about/",views.about),
    path("contact/",views.contact),
    path("dashboard/",views.dashboard),
    path("update_to_do/<int:id>",views.update),
    path("user_login/",views.user_login),
    path("user_logout/",views.user_logout),
    path("my_signup/",views.my_signup),
    path("del_data/<int:id>",views.del_data),


]
