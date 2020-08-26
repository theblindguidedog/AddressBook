from django.db import models

class Address(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	phone = models.CharField(max_length=15)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=100)
	postcode = models.CharField(max_length=10)
	comments = models.CharField(max_length=2000)

	def __str__(self):
		return self.name


