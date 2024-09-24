from django import forms
from .models import Courses

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['image', 'name', 'description', 'level', 'duration', 'mode', 'price']
