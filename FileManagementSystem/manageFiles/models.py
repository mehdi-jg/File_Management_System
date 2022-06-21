from asyncio.windows_events import NULL
from django.db import models
from . import dropdownChoices

# Create your models here.

class JGDivision(models.Model):
    DivisionName = models.CharField(max_length=200, blank=True, null=True)
    NothiCode = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.DivisionName or ' '


class JGDepartment(models.Model):
    DepartmentName = models.CharField(max_length=200, blank=True, null=True)
    JGDivision = models.ForeignKey(
        JGDivision, blank=True, null=True, on_delete=models.CASCADE)
    NothiCode = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.DepartmentName or ' '


class JGSection(models.Model):
    SectionName = models.CharField(max_length=200, blank=True, null=True)
    JGDepartment = models.ForeignKey(
        JGDepartment, blank=True, null=True, on_delete=models.CASCADE)
    NothiCode = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.SectionName or ' '


class JGSubSection(models.Model):
    SubSectionName = models.CharField(max_length=200, blank=True, null=True)
    JGSection = models.ForeignKey(
        JGSection, blank=True, null=True, on_delete=models.CASCADE)
    NothiCode = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.SubSectionName or ' '


class File(models.Model):
    file_name = models.CharField(max_length=200, blank=True, null=True)
    file_number = models.CharField(max_length=200, blank=True, null=True)
    file_type = models.CharField(max_length=200, blank=True, null=True)
    file_class = models.CharField(max_length=10, blank=True, null=True, choices=dropdownChoices.ChoicesFileClass)
    file_section = models.ForeignKey(
        JGSection, blank=True, null=True, on_delete=models.CASCADE)
    FileCreationDate = models.DateTimeField(auto_now_add=False, auto_now=False)

    def __str__(self):
        return self.file_name or ' '