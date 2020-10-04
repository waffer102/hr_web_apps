# Generated by Django 3.0.7 on 2020-07-04 20:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hr_web_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businessunit',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='homedepartment',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='payrollcompany',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='businessunit',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businessunit',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='homedepartment',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homedepartment',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='payrollcompany',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='businessunit',
            name='status',
            field=models.CharField(choices=[('a', 'Active'), ('i', 'Inactive')], default='a', max_length=1, verbose_name='Business Unit Status'),
        ),
        migrations.AlterField(
            model_name='homedepartment',
            name='status',
            field=models.CharField(choices=[('a', 'Active'), ('i', 'Inactive')], default='a', max_length=1, verbose_name='Home Department Status'),
        ),
        migrations.AlterField(
            model_name='payrollcompany',
            name='status',
            field=models.CharField(choices=[('a', 'Active'), ('i', 'Inactive')], default='a', max_length=1, verbose_name='Payroll Company Status'),
        ),
    ]
