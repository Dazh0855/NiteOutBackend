from django.test import TestCase
from django.db import models
# Create your tests here.

class TestModels(TestCase):
	def SetUp(self):
		Users.objects.create(user_name="name", user_info="info", user_password="password", user_id=2)
		Events.objects.create(title="title",price = "price")
	def test_database(self):
		name = Users.objects.get(user_name="name")
		password = Users.objects.get(user_password="password")
		info = Users.objects.get(user_info="info")
		title = Events.objects.get(title="title")
		price = Events.objects.get(price="price")
		self.assertEqual(name,"name")
		self.assertEqual(password,"password")
		self.assertEqual(info,"info")
		self.assertEqual(user_id,2)
	
		
