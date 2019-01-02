from django import forms
from .models import Project,Profile
 
class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['username','post_date','design','usability','creativity','content','overall_score','avatar','country']
        widgets={
            'color':forms.CheckboxSelectMultiple(),
            'technologies':forms.CheckboxSelectMultiple(),
            'categories':forms.CheckboxSelectMultiple(),
        }




class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']