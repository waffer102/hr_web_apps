from django import forms
from .models import LetterCategories, LetterSections, Letters
from hr_web_app.models import TeamMember

class CategoryForm(forms.ModelForm):
    class Meta:
        model = LetterCategories
        fields = ['name', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-user'}),
        }


class SectionForm(forms.ModelForm):
    class Meta:
        model = LetterSections
        fields = ['name', 'paragraph_text', 'standard_text', 'subtemplate_indicator', 'category', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'paragraph_text': forms.Textarea(attrs={'class': 'form-control form-control-user'}),
            'standard_text': forms.CheckboxInput(attrs={'class': 'form-control form-control-user'}),
            'subtemplate_indicator': forms.CheckboxInput(attrs={'class': 'form-control form-control-user'}),
            'category': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-user'}),
        }


class StartForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['last_name']
        widgets = {
            'last_name': forms.Select(),
        }
