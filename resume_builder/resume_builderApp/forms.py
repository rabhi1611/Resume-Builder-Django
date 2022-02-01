from django.forms import ModelForm
from .models import resume

class create_resume_form(ModelForm):
    class Meta:
        model = resume
        fields = {'name', 'phone', 'email', 'school', 'degree'
        , 'university', 'skill', 'about_you', 'previous_work'}

