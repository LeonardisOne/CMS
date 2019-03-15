from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Assistance(models.Model):
	number = models.CharField(
		max_length=8)
	name = models.CharField(
		max_length=50)

	def __str__(self):
		return self.name

class Incident(models.Model):
	Fire = 'FIR'
	Haze = 'HAZ'
	Cat_on_tree = 'CAT'
	Tsunami = 'TSU'

	INCIDENT_TYPE_CHOICES = (
		(Fire,'Fire'),
		(Haze, 'Haze'),
		(Cat_on_tree, 'Cat on a tree'),
		(Tsunami, 'Tsunami'),
	)

	submitter = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		null=True)

	caller = models.CharField(
		max_length=50,
		default='Anonymous')

	incident_type = models.CharField(
		max_length=3,
		choices=INCIDENT_TYPE_CHOICES,
		)

	incident_date = models.DateTimeField('date incident happens',
											auto_now_add=True)

	assistance_type = models.ForeignKey(
		Assistance,
		on_delete=models.CASCADE)

	severity = models.IntegerField(default=1,
		choices=(
			(1,'1'),
			(2,'2'),
			(3,'3'),
			(4,'4'),
			(5,'5'),
			))

	location = models.TextField(default ='Singapore')

	is_closed = models.BooleanField(default=False)

	incident_closed_date = models.DateTimeField(null=True)

	def __str__(self):
		if self.is_closed:
			return "Case closed"
		else:
			return "Case not closed"

	class Meta:
		ordering = ["-incident_date"]
