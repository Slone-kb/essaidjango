from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from produits.models import Produits
from .forms import ProduitsForms

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
   liste_fruits = ['pomme', 'banane', 'orange']
   liste = [1, 2, 3]
   user = request.user
   title = "About Us"
   context = {
      'liste_fruits': liste_fruits,
      'liste': liste,
      'user': user,
      'title': 'about us',

      'html': '<center> <br> Hello, World! </center>',

   }
   return render(request, 'about.html', context)


def contact_views(request):
   return render(request, 'contact.html')
   
# 4. Afficher TOUS les produits (Liste)
def produits_liste_views(request):
    objects = Produits.objects.all()
    context = {
        'objects': objects
    }
    return render(request, 'produits/liste.html', context)


#pour le formulaire de creation d un produit
def produits_forms_views(request):
    form=ProduitsForms(request.POST or None)
    message=' '
   
    
    if request.method == 'POST':
        form = ProduitsForms(request.POST )
        if form.is_valid():
            form.save()
            message= "Produit créé avec succès"
    else:
        form = ProduitsForms()
    context={
                'message': message,
               ' form': form,
            }
    return render(request, 'produits/create.html', context)

# 5. Afficher UN SEUL produit (Détail par ID)
def produits_details_views(request, id):
    produits = get_object_or_404(Produits, id=id)
    
    context = {
        'produits': produits
    }
    return render(request, 'produits/details.html', context)