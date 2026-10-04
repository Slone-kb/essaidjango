from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_views(request):
   # return HttpResponse('<h1>Hello, World!</h1>') sans page html
   return render(request,'home.html')

def about_views(request):
   return render(request, 'about.html')


def contact_views(request):
   return render(request, 'contact.html')
   


   
