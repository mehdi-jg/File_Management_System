# Generated by Django 4.0.5 on 2022-06-19 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageFiles', '0005_file_filecreationdate_alter_file_file_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='FileCreationDate',
            field=models.DateTimeField(),
        ),
    ]
