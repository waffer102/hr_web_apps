# Generated by Django 3.0.7 on 2020-07-04 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Business Unit Code')),
                ('name', models.CharField(max_length=50, verbose_name='Business Unit Name')),
                ('status', models.CharField(choices=[('a', 'Active'), ('i', 'Inactive')], default='i', max_length=1, verbose_name='Business Unit Status')),
            ],
        ),
        migrations.CreateModel(
            name='PayrollCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Payroll Company Code')),
                ('name', models.CharField(max_length=50, verbose_name='Payroll Company Name')),
                ('federal_id', models.CharField(max_length=10, verbose_name='Federal ID Number')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('a', 'Active'), ('i', 'Inactive')], default='i', max_length=1, verbose_name='Payroll Company Status')),
            ],
        ),
        migrations.CreateModel(
            name='HomeDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, unique=True, verbose_name='Home Department Code')),
                ('name', models.CharField(max_length=50, verbose_name='Home Department Name')),
                ('number', models.IntegerField()),
                ('pillar', models.CharField(choices=[('i', 'Innovate and Implement'), ('g', 'Growth')], max_length=1, verbose_name='Company Pillar')),
                ('ta_category', models.CharField(choices=[('a', 'Advisor Strategies'), ('c', 'Corporate Support')], max_length=1, verbose_name='TA Category')),
                ('ta_company', models.CharField(choices=[('o', 'Orion 1'), ('r', 'Orion 2')], max_length=1, verbose_name='TA Company')),
                ('status', models.CharField(choices=[('a', 'Active'), ('i', 'Inactive')], default='i', max_length=1, verbose_name='Home Department Status')),
                ('businessunit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hr_web_app.BusinessUnit')),
            ],
        ),
        migrations.AddField(
            model_name='businessunit',
            name='payrollcompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hr_web_app.PayrollCompany'),
        ),
    ]