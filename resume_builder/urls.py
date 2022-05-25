"""resume_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from resume_builderApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('person_create/', views.person_create, name='person_create'),
    path('projectorjob_create/', views.projectorjob_create, name='projectorjob_create'),
    path('areaofinterest_create/', views.areaofinterest_create, name='areaofinterest_create'),
    path('academicform_create/', views.academicform_create, name='academicform_create'),
    path('educationform_create/', views.educationform_create, name='educationform_create'),
    path('professionalskill_create/', views.professionalskill_create, name='professionalskill_create'),
    path('resume/<pk>', views.view, name='view'),
    path('download/<pk>/', views.resumes, name='download'),
]
