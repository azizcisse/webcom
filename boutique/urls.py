from django.urls import path 
from boutique.views import index, details, verifier, confirm


urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', details, name="details"),
    path('verifier', verifier, name="verifier"),
    path('confirm', confirm, name="confirm"),
]

