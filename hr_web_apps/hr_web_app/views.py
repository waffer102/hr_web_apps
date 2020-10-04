from django.shortcuts import render, redirect
from .models import PayrollCompany, BusinessUnit, HomeDepartment, TeamMember
from .forms import PayrollCompanyForm, BusinessUnitForm, HomeDepartmentForm, TeamMemberForm


def index(request):
    """The homepage for HR Web Apps"""
    return render(request, 'hr_web_app/index.html')


def payrollcompany(request):
    """List of payroll companies"""
    payrollcompany = PayrollCompany.objects.all()
    context = {'payrollcompany': payrollcompany}
    return render(request, 'hr_web_app/payrollcompany/payrollcompany.html', context)


def view_payrollcompany(request, payrollcompany_id):
    """View of individual payroll company"""
    payrollcompany = PayrollCompany.objects.get(id=payrollcompany_id)
    context = {'payrollcompany': payrollcompany}
    return render(request, 'hr_web_app/payrollcompany/view_payrollcompany.html', context)


def new_payrollcompany(request):
    """Creat new payroll company"""
    if request.method != 'POST':
        # No data submitted, create blank form
        form = PayrollCompanyForm()
    else:
        # Post data submitted; process data.
        form = PayrollCompanyForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('hr_web_app:payrollcompany')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'hr_web_app/payrollcompany/new_payrollcompany.html', context)


def edit_payrollcompany(request, payrollcompany_id):
    """Edit an existing payroll company"""
    payrollcompany = PayrollCompany.objects.get(id=payrollcompany_id)

    if request.method != 'POST':
        # initial request, pre-fill with current entry.
        form = PayrollCompanyForm(instance=payrollcompany)
    else:
        # POST data submitted; process data
        form = PayrollCompanyForm(instance=payrollcompany, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('hr_web_app:view_payrollcompany', payrollcompany_id)

    context = {'payrollcompany': payrollcompany, 'form': form}
    return render(request, 'hr_web_app/payrollcompany/edit_payrollcompany.html', context)


def delete_payrollcompany(request, payrollcompany_id):
    """Deletes an existing payroll company"""
    payrollcompany = PayrollCompany.objects.get(id=payrollcompany_id)

    if request.method == 'POST':
        # Delete confirmed
        PayrollCompany.objects.filter(id=payrollcompany_id).delete()
        return redirect('hr_web_app:payrollcompany')

    context = {'payrollcompany': payrollcompany}
    return render(request, 'hr_web_app/payrollcompany/delete_payrollcompany.html', context)


def businessunit(request):
    """List of Business Units"""
    businessunit = BusinessUnit.objects.all()
    context = {'businessunit': businessunit}
    return render(request, 'hr_web_app/businessunit/businessunit.html', context)


def view_businessunit(request, businessunit_id):
    """View of individual business unit"""
    businessunit = BusinessUnit.objects.get(id=businessunit_id)
    context = {'businessunit': businessunit}
    return render(request, 'hr_web_app/businessunit/view_businessunit.html', context)


def new_businessunit(request):
    """Creat new Business Unit"""
    if request.method != 'POST':
        # No data submitted, create blank form
        form = BusinessUnitForm()
    else:
        # Post data submitted; process data.
        form = BusinessUnitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('hr_web_app:businessunit')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'hr_web_app/businessunit/new_businessunit.html', context)


def edit_businessunit(request, businessunit_id):
    """Edit an existing Business Unit"""
    businessunit = BusinessUnit.objects.get(id=businessunit_id)

    if request.method != 'POST':
        # initial request, pre-fill with current entry.
        form = BusinessUnitForm(instance=businessunit)
    else:
        # POST data submitted; process data
        form = BusinessUnitForm(instance=businessunit, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('hr_web_app:view_businessunit', businessunit_id)

    context = {'businessunit': businessunit, 'form': form}
    return render(request, 'hr_web_app/businessunit/edit_businessunit.html', context)


def delete_businessunit(request, businessunit_id):
    """Deletes an existing Business Unit"""
    businessunit = BusinessUnit.objects.get(id=businessunit_id)

    if request.method == 'POST':
        # Delete confirmed
        BusinessUnit.objects.filter(id=businessunit_id).delete()
        return redirect('hr_web_app:businessunit')

    context = {'businessunit': businessunit}
    return render(request, 'hr_web_app/businessunit/delete_businessunit.html', context)


def homedepartment(request):
    """List of Home Departments"""
    homedepartment = HomeDepartment.objects.all()
    context = {'homedepartment': homedepartment}
    return render(request, 'hr_web_app/homedepartment/homedepartment.html', context)


def view_homedepartment(request, homedepartment_id):
    """View of individual home departments"""
    homedepartment = HomeDepartment.objects.get(id=homedepartment_id)
    context = {'homedepartment': homedepartment}
    return render(request, 'hr_web_app/homedepartment/view_homedepartment.html', context)


def new_homedepartment(request):
    """Creat new Home Department"""
    if request.method != 'POST':
        # No data submitted, create blank form
        form = HomeDepartmentForm()
    else:
        # Post data submitted; process data.
        form = HomeDepartmentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('hr_web_app:homedepartment')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'hr_web_app/homedepartment/new_homedepartment.html', context)


def edit_homedepartment(request, homedepartment_id):
    """Edit an existing Home Department"""
    homedepartment = HomeDepartment.objects.get(id=homedepartment_id)

    if request.method != 'POST':
        # initial request, pre-fill with current entry.
        form = HomeDepartmentForm(instance=homedepartment)
    else:
        # POST data submitted; process data
        form = HomeDepartmentForm(instance=homedepartment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('hr_web_app:view_homedepartment', homedepartment_id)

    context = {'homedepartment': homedepartment, 'form': form}
    return render(request, 'hr_web_app/homedepartment/edit_homedepartment.html', context)


def delete_homedepartment(request, homedepartment_id):
    """Deletes an existing Home Department"""
    homedepartment = HomeDepartment.objects.get(id=homedepartment_id)

    if request.method == 'POST':
        # Delete confirmed
        HomeDepartment.objects.filter(id=homedepartment_id).delete()
        return redirect('hr_web_app:homedepartment')

    context = {'homedepartment': homedepartment}
    return render(request, 'hr_web_app/homedepartment/delete_homedepartment.html', context)


def team_members(request):
    """List of Team Members"""
    team_members = TeamMember.objects.all()
    context = {'team_members': team_members}
    return render(request, 'hr_web_app/team_members/team_members.html', context)


def view_team_member(request, team_member_id):
    """View of individual team member"""
    team_member = TeamMember.objects.get(id=team_member_id)
    context = {'team_member': team_member}
    return render(request, 'hr_web_app/team_members/view_team_member.html', context)


def new_team_member(request):
    """Creat new Team Member"""
    if request.method != 'POST':
        # No data submitted, create blank form
        form = TeamMemberForm()
    else:
        # Post data submitted; process data.
        form = TeamMemberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('hr_web_app:team_members')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'hr_web_app/team_members/new_team_member.html', context)


def edit_team_member(request, team_member_id):
    """Edit an existing Team Member"""
    team_member = TeamMember.objects.get(id=team_member_id)

    if request.method != 'POST':
        # initial request, pre-fill with current entry.
        form = TeamMemberForm(instance=team_member)
    else:
        # POST data submitted; process data
        form = TeamMemberForm(instance=team_member, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('hr_web_app:view_team_member', team_member_id)

    context = {'team_member': team_member, 'form': form}
    return render(request, 'hr_web_app/team_members/edit_team_member.html', context)


def delete_team_member(request, team_member_id):
    """Deletes an existing Team Member"""
    team_member = TeamMember.objects.get(id=team_member_id)

    if request.method == 'POST':
        # Delete confirmed
        TeamMember.objects.filter(id=team_member_id).delete()
        return redirect('hr_web_app:team_members')

    context = {'team_member': team_member}
    return render(request, 'hr_web_app/team_members/delete_team_member.html', context)
