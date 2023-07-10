from django.shortcuts import redirect, render
from .models import Product, Commande
from django.core.paginator import Paginator


def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
        
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    
    return render(request, 'boutique/index.html', {'product_object':product_object})


def details(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'boutique/details.html', {'product':product_object})


def verifier(request):
    if request.method == "POST":
        items = request.POST.get('items')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        total = request.POST.get('total')
        com = Commande(items=items, nom=nom, email=email, adresse=adresse, ville=ville, pays=pays, zipcode=zipcode, total=total)
        com.save()
        return redirect('confirm')
        
    return render(request, 'boutique/verifier.html')


def confirm(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'boutique/confirm.html', {'name':nom})