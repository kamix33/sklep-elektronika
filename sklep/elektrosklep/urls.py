from django.urls import path
from .views import CustomLoginView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.rejestracja, name='rejestracja'),
    path('dodaj_do_koszyka/<int:produkt_id>/', views.dodaj_do_koszyka, name='dodaj_do_koszyka'),
    path('koszyk/', views.koszyk_view, name='koszyk'),
    path('zloz_zamowienie/', views.zloz_zamowienie, name='zloz_zamowienie'),
    path('zamowienie/', views.zamowienie, name='zamowienie'),
    path('potwierdzenie_zamowienia/', views.potwierdzenie_zamowienia, name='potwierdzenie_zamowienia'),
]
