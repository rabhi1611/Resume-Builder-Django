from cProfile import Profile
from django.shortcuts import redirect, render
from resume_builderApp import models
# Create your views here.
from .forms import create_person_form, create_academic_form, create_areaofinterest_form, create_education_form, create_professionalskill_form,create_projectorjob_form

from django.http import HttpResponse
from django.template import loader
import pdfkit
import io
import os


def home(request):
    details = models.Person.objects.all()
    context = {
        'details' : details
    }
    return render(request, 'resume_builderApp/home.html', context)

    
    #
    #
    #
    #
    #
    
def person_create(request):
    person_form = create_person_form()

    if request.method == 'POST':
        person_form = create_person_form(request.POST)
        if person_form.is_valid():
            person_form.save()
            return redirect('home')
    else:
        person_form = create_person_form()
    
    context = {
        'personform': person_form
    }

    return render(request, 'resume_builderApp/create.html', context)

def projectorjob_create(request):
    projectorjob_form = create_projectorjob_form()

    if request.method == 'POST':
        projectorjob_form = create_projectorjob_form(request.POST)
        if projectorjob_form.is_valid():
            projectorjob_form.save()
            return redirect('home')
    else:
        projectorjob_form = create_projectorjob_form()
    
    context = {
        'personform': projectorjob_form
    }

    return render(request, 'resume_builderApp/create.html', context)


def areaofinterest_create(request):
    areaofinterest_form = create_areaofinterest_form()

    if request.method == 'POST':
        areaofinterest_form = create_areaofinterest_form(request.POST)
        if areaofinterest_form.is_valid():
            areaofinterest_form.save()
            return redirect('home')
    else:
        form = create_areaofinterest_form()
    
    context = {
        'personform': areaofinterest_form
    }

    return render(request, 'resume_builderApp/create.html', context)


def academicform_create(request):
    academic_form = create_academic_form()

    if request.method == 'POST':
        academic_form = create_academic_form(request.POST)
        if academic_form.is_valid():
            academic_form.save()
            return redirect('home')
    else:
        academic_form = create_academic_form()
    
    context = {
        'personform': academic_form
    }

    return render(request, 'resume_builderApp/create.html', context)


def educationform_create(request):
    education_form = create_education_form()

    if request.method == 'POST':
        education_form = create_education_form(request.POST)
        if education_form.is_valid():
            education_form.save()
            return redirect('home')
    else:
        education_form = create_education_form()
    
    context = {
        'personform': education_form
    }

    return render(request, 'resume_builderApp/create.html', context)


def professionalskill_create(request):
    professionalskill_form = create_professionalskill_form()

    if request.method == 'POST':
        professionalskill_form = create_professionalskill_form(request.POST)
        if professionalskill_form.is_valid():
            professionalskill_form.save()
            return redirect('home')
    else:
        professionalskill_form = create_professionalskill_form()
    
    context = {
        'personform': professionalskill_form
    }

    return render(request, 'resume_builderApp/create.html', context)




def view(request, pk):
    person_detail = models.Person.objects.get(id = pk)

    education_detail = models.Education.objects.get(person = pk)
    skill_detail = models.ProfessionalSkill.objects.get(person = pk)
    work_detail = models.ProjectOrJob.objects.get(person = pk)
    academic_detail = models.Academic.objects.get(person = pk)
    interest_detail = models.AreaOfInterest.objects.get(person = pk)
    context = {
        'person_detail': person_detail,
        'education_detail': education_detail,
        'skill_detail': skill_detail,
        'work_detail': work_detail,
        'academic_detail': academic_detail,
        'interest_detail': interest_detail,
        'id' : pk,
    }
    #print(pk)
    return render(request, 'resume_builderApp/resume.html', context)


    
def resumes(request, pk):
    print(pk)
    #user_profile = models.Person.objects.get(id = pk)

    person_detail = models.Person.objects.get(id = pk)
    education_detail = models.Education.objects.get(person = pk)
    skill_detail = models.ProfessionalSkill.objects.get(person = pk)
    work_detail = models.ProjectOrJob.objects.get(person = pk)
    academic_detail = models.Academic.objects.get(person = pk)
    interest_detail = models.AreaOfInterest.objects.get(person = pk)
    context = {
        'person_detail': person_detail,
        'education_detail': education_detail,
        'skill_detail': skill_detail,
        'work_detail': work_detail,
        'academic_detail': academic_detail,
        'interest_detail': interest_detail,
        'id' : pk,
    }

    template = loader.get_template("resume_builderApp/resume.html")
    html = template.render(context)
    option = {
        'page-size' : 'Letter',
        'encoding' : 'UTF-8'
    }

    #C:\Program Files\wkhtmltopdf\bin
    #config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html,False, option)
    #url = 'https://rohit-resume-builder.herokuapp.com/resume/' + pk
    #pdf = pdfkit.from_url(url, 'out-test.pdf', configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachments'
    return response



