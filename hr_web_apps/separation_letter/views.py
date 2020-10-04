from django.shortcuts import render, redirect
from .models import LetterCategories, LetterSections
from hr_web_app.models import TeamMember
from django.contrib.auth.models import User
from .forms import CategoryForm, SectionForm
from datetime import datetime
import re


def get_available_tags():
    """Gets a list of available tags"""
    tags = LetterSections.objects.filter(subtemplate_indicator=True, status='a')
    tag_list = []
    for tag in tags:
        tag_list.append(tag.name)
    return tag_list


def parse_section_tags(parsed_paragraph_text):
    """Parse out all the section tags of a section paragraph using a regular expression"""
    for x in range(6):  # loop through up to 6 times to take into account tags within sub templates
        matches = re.findall(r'\[\[(.*?)\]\]', parsed_paragraph_text)
        # For each match, grab the object by name and replace the tag in the paragraph text
        for match in matches:
            try:
                text = LetterSections.objects.get(name=match)
                parsed_paragraph_text = parsed_paragraph_text.replace('[[' + match + ']]', text.paragraph_text)
            except LetterSections.DoesNotExist:
                parsed_paragraph_text = parsed_paragraph_text.replace('[[' + match + ']]', match)
        if not re.search(r'\[\[(.*?)\]\]', parsed_paragraph_text):  # break the loop early if no sub templates are found
            break
    return parsed_paragraph_text


def parse_user_tags(parsed_paragraph_text, session_data):
    """Parse out all the user tags of a section paragraph using a regular expression"""
    # Current user tags: letter_date, separation_date, company_name, employee_name, hr_rep, hr_rep_title
    # Get date strings and turn them into formatted dates
    letter_date = datetime.strptime(session_data['letter_date'], '%Y-%m-%d')
    separation_date = datetime.strptime(session_data['separation_date'], '%Y-%m-%d')
    # Get User data for name and company name
    team_member = TeamMember.objects.get(id=session_data['team_member_selection'])
    # Get HR Rep information
    hr_rep = User.objects.get(id=session_data['hr_user_selection'])
    # Run through each tag and replace text in paragraph.
    parsed_paragraph_text = parsed_paragraph_text.replace('{{Letter Date}}', letter_date.strftime('%d/%m/%Y'))
    parsed_paragraph_text = parsed_paragraph_text.replace('{{Separation Date}}', separation_date.strftime('%d/%m/%Y'))
    parsed_paragraph_text = parsed_paragraph_text.replace('{{Employee Name}}', team_member.first_name + " " + team_member.last_name)
    parsed_paragraph_text = parsed_paragraph_text.replace('{{Company Name}}', team_member.homedepartment.businessunit.name)

    return parsed_paragraph_text


def index(request):
    """The index for Separation Letters"""
    return render(request, 'separation_letter/index.html')


def category(request):
    """List of Categories"""
    categories = LetterCategories.objects.all()
    context = {'categories': categories}
    return render(request, 'separation_letter/category/category.html', context)


def view_category(request, category_id):
    """View of individual category"""
    category = LetterCategories.objects.get(id=category_id)
    context = {'category': category}
    return render(request, 'separation_letter/category/view_category.html', context)


def new_category(request):
    """Creat new Category"""
    if request.method != 'POST':
        # No data submitted, create blank form
        form = CategoryForm()
    else:
        # Post data submitted; process data.
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('separation_letter:category')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'separation_letter/category/new_category.html', context)


def edit_category(request, category_id):
    """Edit an existing category"""
    category = LetterCategories.objects.get(id=category_id)

    if request.method != 'POST':
        # initial request, pre-fill with current entry.
        form = CategoryForm(instance=category)
    else:
        # POST data submitted; process data
        form = CategoryForm(instance=category, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('separation_letter:view_category', category_id)

    context = {'category': category, 'form': form}
    return render(request, 'separation_letter/category/edit_category.html', context)


def delete_category(request, category_id):
    """Deletes an existing category"""
    category = LetterCategories.objects.get(id=category_id)

    if request.method == 'POST':
        # Delete confirmed
        LetterCategories.objects.filter(id=category_id).delete()
        return redirect('separation_letter:category')

    context = {'category': category}
    return render(request, 'separation_letter/category/delete_category.html', context)


def section(request):
    """List of Section"""
    sections = LetterSections.objects.all()
    context = {'sections': sections}
    return render(request, 'separation_letter/section/section.html', context)


def view_section(request, section_id):
    """View of individual section"""
    section = LetterSections.objects.get(id=section_id)
    parsed_paragraph_text = parse_section_tags(section.paragraph_text)
    context = {'section': section, 'parsed_paragraph_text': parsed_paragraph_text}
    return render(request, 'separation_letter/section/view_section.html', context)


def new_section(request):
    """Creat new section"""
    if request.method != 'POST':
        # No data submitted, create blank form
        form = SectionForm()
    else:
        # Post data submitted; process data.
        form = SectionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('separation_letter:section')

    # Get a list of available tags
    tag_list = get_available_tags()

    # Display a blank or invalid form
    context = {'form': form, 'tag_list': tag_list}
    return render(request, 'separation_letter/section/new_section.html', context)


def edit_section(request, section_id):
    """Edit an existing section"""
    section = LetterSections.objects.get(id=section_id)

    if request.method != 'POST':
        # initial request, pre-fill with current entry.
        form = SectionForm(instance=section)
    else:
        # POST data submitted; process data
        form = SectionForm(instance=section, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('separation_letter:view_section', section_id)

    # Get list of available tags
    tag_list = get_available_tags()

    context = {'section': section, 'tag_list': tag_list, 'form': form}
    return render(request, 'separation_letter/section/edit_section.html', context)


def delete_section(request, section_id):
    """Deletes an existing section"""
    section = LetterSections.objects.get(id=section_id)

    if request.method == 'POST':
        # Delete confirmed
        LetterSections.objects.filter(id=section_id).delete()
        return redirect('separation_letter:section')

    context = {'section': section}
    return render(request, 'separation_letter/section/delete_section.html', context)


def get_session_data(request):
    # Get fields from session
    session_data = {
        'team_member_selection': request.session.get('team_member_selection', 'whoops'),
        'letter_date': request.session.get('letter_date', 'whoops'),
        'separation_date': request.session.get('separation_date', 'whoops'),
        'hr_user_selection': request.session.get('hr_user_selection', 'whoops'),
        'letter_order': request.session.get('letter_order', 'whoops'),
    }
    return session_data


def builder_start(request):
    """First form in letter builder"""
    if request.method != 'POST':
        # No data submitted, create blank form
        team_members = TeamMember.objects.values('id', 'first_name', 'last_name')
        hr_users = User.objects.values('id', 'first_name', 'last_name')
    else:
        # Post data submitted; process data by setting them in the session.
        request.session['team_member_selection'] = request.POST['team_member_selection']
        request.session['letter_date'] = request.POST['letter_date']
        request.session['separation_date'] = request.POST['separation_date']
        request.session['hr_user_selection'] = request.POST['hr_user_selection']
        return redirect('separation_letter:builder_builder')

    context = {'team_members': team_members, 'hr_users': hr_users}
    return render(request, 'separation_letter/letter_builder/start.html', context)


def builder_builder(request):
    """Second form  in letter builder"""
    if request.method != 'POST':
        # Get a list of all active letter sections
        letter_sections = LetterSections.objects.all().filter(category__status='a', subtemplate_indicator=0)

        # Get unique list of Letter Categories
        letter_categories = []
        for letter_section in letter_sections:
            if letter_section.category.name not in letter_categories:
                letter_categories.append(letter_section.category.name)
        session_data = get_session_data(request)
    else:
        # Process form data
        request.session['letter_order'] = request.POST['letter_order']
        return redirect('separation_letter:builder_editor')

    context = {
        'letter_sections': letter_sections,
        'letter_categories': letter_categories,
        'session_data': session_data,
    }
    return render(request, 'separation_letter/letter_builder/builder.html', context)


def builder_editor(request):
    """Third form in letter builder"""
    if request.method != 'POST':
        # Form not submitted; generate text without saving/export.
        session_data = get_session_data(request)
        # Get data out of session data
        team_member = TeamMember.objects.get(id=session_data['team_member_selection'])
        hr_user = User.objects.get(id=session_data['hr_user_selection'])
        letter_date = session_data['letter_date']
        separation_date = session_data['separation_date']
        # Generate letter text
        parsed_text = ''
        for letter_section in session_data['letter_order']:
            if letter_section != ',':
                section_text = LetterSections.objects.get(id=letter_section)
                parsed_text += parse_section_tags(section_text.paragraph_text)
        # Parse user tags
        parsed_text = parse_user_tags(parsed_text, session_data)
    else:
        # Request to save and export
        pass

    context = {
        'team_member': team_member,
        'hr_user': hr_user,
        'letter_date': letter_date,
        'separation_date': separation_date,
        'parsed_text': parsed_text,
    }
    return render(request, 'separation_letter/letter_builder/editor.html', context)
# need to finish parsing the hrRep section