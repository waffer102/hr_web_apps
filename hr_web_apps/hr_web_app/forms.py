from django import forms

from .models import PayrollCompany, BusinessUnit, HomeDepartment, TeamMember


class PayrollCompanyForm(forms.ModelForm):
    class Meta:
        model = PayrollCompany
        fields = ['code', 'name', 'federal_id', 'status']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'federal_id': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-user'}),
        }


class BusinessUnitForm(forms.ModelForm):
    class Meta:
        model = BusinessUnit
        fields = ['code', 'name', 'payrollcompany', 'status']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'payrollcompany': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-user'}),
        }


class HomeDepartmentForm(forms.ModelForm):
    class Meta:
        model = HomeDepartment
        fields = ['code', 'name', 'number', 'businessunit', 'pillar', 'ta_category', 'ta_company', 'status']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'number': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'businessunit': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'pillar': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'ta_category': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'ta_company': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-user'}),
        }


class TeamMemberForm(forms.ModelForm):
    """Creates a new team member"""
    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'work_email', 'associate_id', 'homedepartment', 'hire_date', 'rehire_date', 'separation_date', 'reports_to',
                  'job_title', 'flsa', 'pay_type', 'worker_category', 'time_off_available', 'status']
        widgets = {
            'associate_id': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'work_email': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'homedepartment': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'hire_date': forms.TextInput(attrs={'type': 'date', 'class': 'form-control form-control-user'}),
            'rehire_date': forms.TextInput(attrs={'type': 'date', 'class': 'form-control form-control-user'}),
            'separation_date': forms.TextInput(attrs={'type': 'date', 'class': 'form-control form-control-user'}),
            'reports_to': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'flsa': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'pay_type': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'worker_category': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'time_off_available': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-user'}),
        }
