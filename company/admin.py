from django.contrib import admin

from company.models import JobTitle, Employee, City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ('name',)


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    fields = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'job_title', 'city')
    list_filter = ('city',)
