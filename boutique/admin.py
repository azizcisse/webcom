from django.contrib import admin
from .models import Category, Product, Commande

admin.site.site_header = "AFRICOM"
admin.site.site_title = "AFRICOM BOUTIQUE EN LIGNE"
admin.site.index_title = "GERE PAR AZIZ"



class AdminCategorie(admin.ModelAdmin):
     list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title',)
    list_editable = ('price', 'category',)

class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'adresse', 'ville', 'pays', 'total', 'date_commande')
    
    
    
admin.site.register(Product, AdminProduct),
admin.site.register(Category, AdminCategorie),
admin.site.register(Commande, AdminCommande),