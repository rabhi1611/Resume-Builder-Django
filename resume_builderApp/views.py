from cProfile import Profile
from django.shortcuts import redirect, render, get_object_or_404
from requests import options
from resume_builderApp import models
# Create your views here.
from .forms import create_person_form, create_academic_form, create_areaofinterest_form, create_education_form, create_professionalskill_form,create_projectorjob_form

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
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

    education_detail = models.Education.objects.filter(person = pk)
    skill_detail = models.ProfessionalSkill.objects.filter(person = pk)
    work_detail = models.ProjectOrJob.objects.filter(person = pk)
    academic_detail = models.Academic.objects.filter(person = pk)
    interest_detail = models.AreaOfInterest.objects.filter(person = pk)
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


    
def resumes(request, *args, **kwargs):
    pk = kwargs.get('pk')
   
    person_detail = models.Person.objects.get(id = pk)
    education_detail = models.Education.objects.filter(person = pk)
    skill_detail = models.ProfessionalSkill.objects.filter(person = pk)
    work_detail = models.ProjectOrJob.objects.filter(person = pk)
    academic_detail = models.Academic.objects.filter(person = pk)
    interest_detail = models.AreaOfInterest.objects.filter(person = pk)
    context = {
        'person_detail': person_detail,
        'education_detail': education_detail,
        'skill_detail': skill_detail,
        'work_detail': work_detail,
        'academic_detail': academic_detail,
        'interest_detail': interest_detail,
        'id' : pk,
    }

    template_path = 'resume_builderApp/resume.html'
   #context = {'user': user}
   # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

   # to directly download the pdf we need attachment 
   # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # to view on browser we can remove attachment 
    response['Content-Disposition'] = 'filename="report.pdf"'

   # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    
   # create a pdf
   
    pisa_status = pisa.CreatePDF(
      html.encode("UTF-8"), dest=response, encoding='UTF-8')
   # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



