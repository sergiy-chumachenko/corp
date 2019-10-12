from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class JobTitle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Job Title'
        verbose_name_plural = 'Job Titles'


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    city = models.ForeignKey(
        City,
        related_name='employee_city',
        on_delete='cascade'
    )
    job_title = models.ForeignKey(
        JobTitle,
        related_name='employee_job_title',
        on_delete='cascade'
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employes'
        index_together = [
            ['first_name', 'last_name']
        ]
