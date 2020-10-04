from django.urls import path
from . import views

app_name = 'separation_letter'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Category URLs
    path('category/', views.category, name='category'),
    path('category/<int:category_id>/', views.view_category, name='view_category'),
    path('category/new/', views.new_category, name='new_category'),
    path('category/<int:category_id>/edit', views.edit_category, name='edit_category'),
    path('category/<int:category_id>/delete', views.delete_category, name='delete_category'),
    # Section URLs
    path('section/', views.section, name='section'),
    path('section/<int:section_id>/', views.view_section, name='view_section'),
    path('section/new/', views.new_section, name='new_section'),
    path('section/<int:section_id>/edit', views.edit_section, name='edit_section'),
    path('section/<int:section_id>/delete', views.delete_section, name='delete_section'),
    # Separation Letter Builder URLs
    path('builder/start', views.builder_start, name='builder_start'),
    path('builder/builder', views.builder_builder, name='builder_builder'),
    path('builder/editor', views.builder_editor, name='builder_editor'),
]
