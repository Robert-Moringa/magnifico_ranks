from django import forms
from .models import Image, Profile

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','project']

