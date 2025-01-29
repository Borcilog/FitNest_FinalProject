from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import (Video, MembershipPlan, Trainer, ClassCategory,Schedule)

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file']  

class MembershipPlanForm(forms.ModelForm):
    class Meta:
        model = MembershipPlan
        fields = ['name', 'description']

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'bio', 'specialties']

class ClassCategoryForm(forms.ModelForm):
    class Meta:
        model = ClassCategory
        fields = ['name', 'description']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['user_name', 'membership', 'class_category', 'trainer', 'session_time']

        widgets = {
            'session_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }