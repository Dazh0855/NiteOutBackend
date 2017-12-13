from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django import forms
from api.forms import UsersForm
from api.models import Users
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	return HttpResponse("post here")	

@csrf_exempt
def login(request):
	if request.method == "POST":
		email = request.POST.get('email','')
		passwd = request.POST.get('password','')
		x = Users.objects.filter(user_name=email).exists()
		if x == True:
			y  = Users.objects.get(user_name = email)
			if y.user_password == passwd:
				return HttpResponse(0)
			else:
				return HttpResponse(2)
		else:
			user = Users.objects.create(user_name = email, user_password=passwd,)
			return HttpResponse(1)
