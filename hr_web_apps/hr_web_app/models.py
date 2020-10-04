from django.db import models
from django.urls import reverse


class PayrollCompany(models.Model):
    """Class defining the payroll companies"""

    code = models.CharField(max_length=3, unique=True, verbose_name='Payroll Company Code')
    name = models.CharField(max_length=50, verbose_name='Payroll Company Name')
    federal_id = models.CharField(max_length=10, verbose_name='Federal ID Number')
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    COMPANY_STATUS = (
        ('a', 'Active'),
        ('i', 'Inactive'),
    )

    status = models.CharField(
        max_length=1,
        choices=COMPANY_STATUS,
        default='a',
        verbose_name='Payroll Company Status',
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing model"""
        return self.name

    def get_absolute_url(self):
        """Returns URL to access detail of Payroll Company"""
        # payroll company will need updated with whatever URL ends up being
        return reverse('payrollcompany', args=[str(self.id)])


class BusinessUnit(models.Model):
    """Class defining business units"""

    code = models.CharField(max_length=3, unique=True, verbose_name='Business Unit Code')
    name = models.CharField(max_length=50, verbose_name='Business Unit Name')
    payrollcompany = models.ForeignKey(PayrollCompany, on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    BU_STATUS = (
        ('a', 'Active'),
        ('i', 'Inactive'),
    )

    status = models.CharField(
        max_length=1,
        choices=BU_STATUS,
        default='a',
        verbose_name='Business Unit Status'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing model"""
        return self.name

    def get_absolute_url(self):
        """Returns URL to access detail of Business unit"""
        # businessunit will need updated with whatever URL ends up being
        return reverse('businessunit', args=[str(self.id)])


class HomeDepartment(models.Model):
    """Class defining home department"""

    code = models.CharField(max_length=6, unique=True, verbose_name='Home Department Code')
    name = models.CharField(max_length=50, verbose_name='Home Department Name')
    number = models.IntegerField()
    businessunit = models.ForeignKey(BusinessUnit, on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    PILLAR_LIST = (
        ('i', 'Innovate and Implement'),
        ('g', 'Growth'),
    )

    pillar = models.CharField(
        max_length=1,
        choices=PILLAR_LIST,
        verbose_name='Company Pillar',
    )

    TA_CATEGORY_LIST = (
        ('a', 'Advisor Strategies'),
        ('c', 'Corporate Support'),
    )

    ta_category = models.CharField(
        max_length=1,
        choices=TA_CATEGORY_LIST,
        verbose_name='TA Category',
    )

    TA_COMPANY_LIST = (
        ('o', 'Orion 1'),
        ('r', 'Orion 2'),
    )

    ta_company = models.CharField(
        max_length=1,
        choices=TA_COMPANY_LIST,
        verbose_name='TA Company'
    )

    HD_STATUS = (
        ('a', 'Active'),
        ('i', 'Inactive'),
    )

    status = models.CharField(
        max_length=1,
        choices=HD_STATUS,
        default='a',
        verbose_name='Home Department Status',
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing model"""
        return self.name

    def get_absolute_url(self):
        """Returns URL to access detail of Home Department"""
        # homedepartment will need updated with whatever URL ends up being
        return reverse('homedepartment', args=[str(self.id)])


class TeamMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    work_email = models.EmailField()
    associate_id = models.CharField(max_length=9, unique=True, verbose_name='Associate ID')
    homedepartment = models.ForeignKey(HomeDepartment, null=True, blank=False, on_delete=models.PROTECT)
    hire_date = models.DateField(verbose_name='Hire Date')
    rehire_date = models.DateField(null=True, blank=True, verbose_name='Rehire Date')
    separation_date = models.DateField(null=True, blank=True, verbose_name='Separation Date')
    reports_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)
    job_title = models.CharField(max_length=50, verbose_name='Job Title')

    FLSA_LIST = (
        ('e', 'Exempt'),
        ('n', 'Non-Exempt'),
    )
    flsa = models.CharField(
        max_length=1,
        choices=FLSA_LIST,
        verbose_name='FLSA Status',
    )

    PAY_LIST = (
        ('s', 'Salaried'),
        ('h', 'Hourly'),
    )

    pay_type = models.CharField(
        max_length=1,
        choices=PAY_LIST,
        verbose_name='Pay Type',
    )

    WORKER_LIST = (
        ('f', 'Full-Time'),
        ('p', 'Part-Time'),
        ('t', 'Temporary'),
        ('i', 'Intern'),
    )

    worker_category = models.CharField(
        max_length=1,
        choices=WORKER_LIST,
        verbose_name='Worker Category',
    )

    TIME_OFF_LIST = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    time_off_available = models.CharField(
        max_length=1,
        choices=TIME_OFF_LIST,
        verbose_name='Is Time Off Available?'
    )

    STATUS_LIST = (
        ('a', 'Active'),
        ('t', 'Terminated'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_LIST,
        default='a',
    )

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        """String for representing model"""
        return self.first_name + ' ' + self.last_name


class EmployeeInfoHistory(models.Model):
    """Class for storing point in time data for a specific employee when an event is triggered"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    work_email = models.EmailField()
    home_department = models.CharField(max_length=50, verbose_name='Home Department')
    reports_to = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Job Title')
    flsa = models.CharField(max_length=15)
    pay_type = models.CharField(max_length=15)
    worker_category = models.CharField(max_length=20)
    time_off_available = models.CharField(max_length=3)
