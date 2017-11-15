from django.db import models

class Users(models.Model):
	user_name = models.CharField(max_length=20)
	user_information = models.CharField(max_length=255)
	user_password = models.CharField(max_length=30)
	user_id = models.AutoField(primary_key=True)
class Events(models.Model):
	title  = models.CharField(max_length=255)
	description = models.Charfield(max_length=255)
	start_time = models.DateField
	stop_time = models.DateField
	price = models.IntegerField
	location = Field.default
