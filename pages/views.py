from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_views(request):
   # return HttpResponse('<h1>Hello, World!</h1>') sans page html
   liste= [1,2,3,4,5]
   user=request.user
   context={
      'liste1' : liste,
   }
   if user.is_authenticated:
      context['user']=user.username
   else:
      context['user']= 'pas connect'

   return render(request,'home.html', context)

def about_views(request):
   return render(request, 'about.html')


def contact_views(request):
   return render(request, 'contact.html')
   


   
