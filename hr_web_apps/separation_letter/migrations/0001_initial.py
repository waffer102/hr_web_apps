# Generated by Django 3.0.7 on 2020-07-23 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LetterCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('a', 'Active'), ('i', 'Inactive')], default='a', max_length=1)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LetterSections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Section Name')),
                ('paragraph_text', models.TextField()),
                ('standard_text', models.BooleanField()),
                ('subtemplate_indicator', models.BooleanField(verbose_name='Sub-Template')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('a', 'Active'), ('i', 'Inactive')], default='a', max_length=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='separation_letter.LetterCategories', verbose_name='Section Category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Letters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter_date', models.DateField()),
                ('separation_date', models.DateField()),
                ('letter_text', models.TextField()),
                ('letter_notes', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('a', 'Active'), ('i', 'Inactive')], default='a', max_length=1)),
                ('delivery_method', models.CharField(choices=[('e', 'Email'), ('i', 'In Person'), ('p', 'Postal Mail')], max_length=1)),
                ('letter_is_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='letter_is_from', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='letter_for', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['separation_date'],
            },
        ),
    ]