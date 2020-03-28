from django.db import models

# Create your models here.

class Data(models.Model):
	total_cases = models.CharField(max_length=300)
	new_cases = models.CharField(max_length=300)
	total_deaths = models.CharField(max_length=300)
	new_deaths = models.CharField(max_length=300)
	active_cases = models.CharField(max_length=300)
	total_recovered = models.CharField(max_length=300)
	serious_critical = models.CharField(max_length=300)

	def __str__(self):
		return self.title