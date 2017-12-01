from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("post here")	

def login(request):
	if request.method == "POST":
		x = request.POST.get('user_name','password')
		return x

