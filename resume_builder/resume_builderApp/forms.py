from django.forms import ModelForm
from .models import Education, Person, ProjectOrJob, ProfessionalSkill, Academic, AreaOfInterest

class create_person_form(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class create_education_form(ModelForm):
    class Meta:
        model = Education
        fields = '__all__'


class create_projectorjob_form(ModelForm):
    class Meta:
        model = ProjectOrJob
        fields = '__all__'


class create_professionalskill_form(ModelForm):
    class Meta:
        model = ProfessionalSkill
        fields = '__all__'


class create_academic_form(ModelForm):
    class Meta:
        model = Academic
        fields = '__all__'

class create_areaofinterest_form(ModelForm):
    class Meta:
        model = AreaOfInterest
        fields = '__all__'

    

