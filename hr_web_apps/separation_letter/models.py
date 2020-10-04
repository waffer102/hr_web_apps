from django.db import models
from django.urls import reverse
from hr_web_app.models import EmployeeInfoHistory, TeamMember
# from django.contrib.auth.models import User


class LetterCategories(models.Model):
    """Class for the categories related to separation letters"""
    name = models.CharField(max_length=50, verbose_name='Category Name')
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    CATEGORY_STATUS = (
        ('a', 'Active'),
        ('i', 'Inactive'),
    )

    status = models.CharField(
        max_length=1,
        choices=CATEGORY_STATUS,
        default='a',
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing model"""
        return self.name

    def get_absolute_url(self):
        """Returns URL to access detail of Payroll Company"""
        # lettercategory will need updated with whatever URL ends up being
        return reverse('lettercategory', args=[str(self.id)])


class LetterSections(models.Model):
    """Defines the letters sections the belong to a letter category"""
    name = models.CharField(max_length=50, unique=True, verbose_name='Section Name')
    paragraph_text = models.TextField()
    standard_text = models.BooleanField()
    subtemplate_indicator = models.BooleanField(verbose_name='Sub-Template')
    category = models.ForeignKey(LetterCategories, on_delete=models.CASCADE, verbose_name='Section Category')
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    CATEGORY_STATUS = (
        ('a', 'Active'),
        ('i', 'Inactive'),
    )

    status = models.CharField(
        max_length=1,
        choices=CATEGORY_STATUS,
        default='a',
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing model"""
        return self.name

    def get_absolute_url(self):
        """Returns URL to access detail of Payroll Company"""
        # lettersection will need updated with whatever URL ends up being
        return reverse('lettersection', args=[str(self.id)])


class Letters(models.Model):
    """Defines all the letters created"""
    team_member = models.ForeignKey(EmployeeInfoHistory, on_delete=models.PROTECT, related_name='letter_for')
    letter_date = models.DateField()
    separation_date = models.DateField()
    letter_text = models.TextField()
    letter_notes = models.TextField(null=True, blank=True)
    letter_is_from = models.ForeignKey(TeamMember, null=True, on_delete=models.SET_NULL, related_name='letter_is_from')
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    CATEGORY_STATUS = (
        ('a', 'Active'),
        ('i', 'Inactive'),
    )

    status = models.CharField(
        max_length=1,
        choices=CATEGORY_STATUS,
        default='a',
    )

    DELIVERY_LIST = (
        ('e', 'Email'),
        ('i', 'In Person'),
        ('p', 'Postal Mail'),
    )

    delivery_method = models.CharField(
        max_length=1,
        choices=DELIVERY_LIST,
    )

    class Meta:
        ordering = ['separation_date']

    def __str__(self):
        """String for representing model"""
        return self.EmployeeInfoHistory.first_name + ' ' + self.EmployeeInfoHistory.last_name

    def get_absolute_url(self):
        """Returns URL to access detail of Payroll Company"""
        # letter will need updated with whatever URL ends up being
        return reverse('letter', args=[str(self.id)])
