from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("post here")	

def login(request):
	if request.method == "POST":
		email = request.POST.get('email','')
		passwd = request.POST.get('password','')
		return HttpResponse(email)

