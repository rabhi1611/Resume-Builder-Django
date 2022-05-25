from django.contrib import admin

# Register your models here.
from resume_builderApp import models

admin.site.register(models.Person)
admin.site.register(models.AreaOfInterest)
admin.site.register(models.Education)
admin.site.register(models.ProjectOrJob)
admin.site.register(models.ProfessionalSkill)
admin.site.register(models.Academic)