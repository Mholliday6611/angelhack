from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Subscribers(models.Model):
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50, blank=True)

	def __unicode__(self):
		return self.first_name