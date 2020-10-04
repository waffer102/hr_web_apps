from django.contrib import admin
from .models import PayrollCompany, BusinessUnit, HomeDepartment, TeamMember, EmployeeInfoHistory
from separation_letter.models import LetterCategories, LetterSections, Letters

admin.site.register(PayrollCompany)
admin.site.register(BusinessUnit)
admin.site.register(HomeDepartment)
admin.site.register(TeamMember)
admin.site.register(EmployeeInfoHistory)
admin.site.register(LetterCategories)
admin.site.register(LetterSections)
admin.site.register(Letters)
