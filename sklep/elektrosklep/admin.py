from django.contrib import admin
from .models import Produkt, Koszyk, PozycjaKoszyka, Zamowienie, PozycjaZamowienia

admin.site.register(Produkt)
admin.site.register(Koszyk)
admin.site.register(PozycjaKoszyka)
admin.site.register(Zamowienie)
admin.site.register(PozycjaZamowienia)