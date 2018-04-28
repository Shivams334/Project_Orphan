from django import forms

from .models import Upload_form


class UploadProject(forms.ModelForm):
    class Meta:
        model = Upload_form
        fields = ['project_name', 'project_discription', 'project_stack',
                  'project_link', 'owner_name']
