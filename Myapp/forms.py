from django import forms
from .models import Student
class PostForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=('studentid','studentname','email','phone','address','branch','attendance','eligibility','marks','result')#model fields