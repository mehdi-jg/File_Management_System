# Generated by Django 4.0.4 on 2022-06-13 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageFiles', '0003_jgdepartment_jgdivision_jgsection_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file_department',
        ),
        migrations.RemoveField(
            model_name='file',
            name='file_division',
        ),
        migrations.AddField(
            model_name='file',
            name='file_class',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='file_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
