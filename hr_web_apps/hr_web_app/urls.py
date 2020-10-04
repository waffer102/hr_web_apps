from django.urls import path
from . import views

app_name = 'hr_web_app'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Payroll Company URLs
    path('payrollcompany/', views.payrollcompany, name='payrollcompany'),
    path('payrollcompany/<int:payrollcompany_id>/', views.view_payrollcompany, name='view_payrollcompany'),
    path('payrollcompany/new/', views.new_payrollcompany, name='new_payrollcompany'),
    path('payrollcompany/<int:payrollcompany_id>/edit', views.edit_payrollcompany, name='edit_payrollcompany'),
    path('payrollcompany/<int:payrollcompany_id>/delete', views.delete_payrollcompany, name='delete_payrollcompany'),
    # Business Unit URLs
    path('businessunit/', views.businessunit, name='businessunit'),
    path('businessunit/<int:businessunit_id>/', views.view_businessunit, name='view_businessunit'),
    path('businessunit/new/', views.new_businessunit, name='new_businessunit'),
    path('businessunit/<int:businessunit_id>/edit', views.edit_businessunit, name='edit_businessunit'),
    path('businessunit/<int:businessunit_id>/delete', views.delete_businessunit, name='delete_businessunit'),
    # Home Department URLs
    path('homedepartment/', views.homedepartment, name='homedepartment'),
    path('homedepartment/<int:homedepartment_id>/', views.view_homedepartment, name='view_homedepartment'),
    path('homedepartment/new/', views.new_homedepartment, name='new_homedepartment'),
    path('homedepartment/<int:homedepartment_id>/edit', views.edit_homedepartment, name='edit_homedepartment'),
    path('homedepartment/<int:homedepartment_id>/delete', views.delete_homedepartment, name='delete_homedepartment'),
    # Team Member URLs
    path('teammembers/', views.team_members, name='team_members'),
    path('teammembers/<int:team_member_id>/', views.view_team_member, name='view_team_member'),
    path('teammembers/new/', views.new_team_member, name='new_team_member'),
    path('teammembers/<int:team_member_id>/edit', views.edit_team_member, name='edit_team_member'),
    path('teammembers/<int:team_member_id>/delete', views.delete_team_member, name='delete_team_member'),
]
