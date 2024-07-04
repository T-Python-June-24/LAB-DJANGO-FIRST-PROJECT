from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Defining a function which
# will receive request and
# perform task depending 
# upon function definition
def hello_geeks (request) :

	# This will return Hello Geeks
	# string as HttpResponse
	return HttpResponse("Hello Geeks")

def home(request):
    return render(request, 'home.html')

