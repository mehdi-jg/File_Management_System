from django import forms
from .models import File, JGDepartment, JGDivision, JGSection

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
        labels = {
            'file_name': 'File Name',
            'file_number': 'File Number',
            'file_division': 'Select Division',
            'file_department': 'Select Department',
            'file_section': 'Select Section',
        }
    # For Showing text "Select" in designation dropdown list instead "----------"

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        
        self.fields['file_department'].queryset = JGDepartment.objects.none()

        if 'file_division' in self.data:
            try:
                file_division_id = int(self.data.get('file_division'))
                self.fields['file_department'].queryset = JGDepartment.objects.filter(JGDivision_id=file_division_id).order_by('NothiCode')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['file_department'].queryset = self.instance.file_division.file_department_set.order_by('NothiCode')

        
        self.fields["file_section"].queryset = JGSection.objects.none()
        if 'file_department' in self.data:
            try:
                file_department_id = int(self.data.get('file_department'))
                self.fields['file_section'].queryset = JGSection.objects.filter(JGDepartment_id=file_department_id).order_by('NothiCode')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['file_section'].queryset = self.instance.file_department.file_section_set.order_by('NothiCode')

