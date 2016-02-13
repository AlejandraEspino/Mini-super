from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Cliente(models.Model):

	nombre = models.CharField(max_length=255)
	telefono= models.IntegerField(unique=True)
	direccion= models.TextField(max_length=255)
	foto= models.ImageField(blank=True)

	def __str__(self):
		return self.nombre
	class Meta:
		ordering = ('id' , )

	# def get_absolute_url(self):
	# 	return reverse('')
