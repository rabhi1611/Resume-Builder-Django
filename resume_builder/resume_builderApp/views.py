from cProfile import Profile
from django.shortcuts import redirect, render
from resume_builderApp import models
# Create your views here.
from .forms import create_resume_form

from django.http import HttpResponse
from django.template import loader
import pdfkit
import io
import os


def home(request):
    details = models.resume.objects.all()
    context = {
        'details' : details
    }
    return render(request, 'resume_builderApp/home.html', context)

def create(request):
    form = create_resume_form()
    if request.method == 'POST':
        form = create_resume_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = create_resume_form()
    
    context = {
        'form': form
    }

    return render(request, 'resume_builderApp/create.html', context)


def view(request, pk):
    detail = models.resume.objects.get(id = pk)
    context = {
        'detail': detail
    }
    return render(request, 'resume_builderApp/resume.html', context)


    
def resumes(request, pk):
    user_profile = models.resume.objects.get(id = pk)
    template = loader.get_template("resume_builderApp/resume.html")
    html = template.render({'detail': user_profile})
    option = {
        'page-size' : 'Letter',
        'encoding' : 'UTF-8'
    }
    pdf = pdfkit.from_string(html,False, option)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachments'
    return response



