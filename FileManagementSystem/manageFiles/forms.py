from django import forms
from .models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
        labels = {
            'file_name': 'File Name',
            'file_number': 'File Number',
            'file_division': 'Division',
            'file_department': 'Department',
            'file_section': 'Section',
        }
    # For Showing text "Select" in designation dropdown list instead "----------"

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields["file_division"].empty_label = "Select a Division"
        self.fields["file_department"].empty_label = "Select a Department"
        self.fields["file_section"].empty_label = "Select a Section"

