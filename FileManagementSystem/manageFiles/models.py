from django.db import models

# Create your models here.


class File(models.Model):
	file_name = models.CharField(max_length=200)
	file_number = models.CharField(max_length=200)

	def __str__(self):
		return self.file_name + ' ' + self.file_number 