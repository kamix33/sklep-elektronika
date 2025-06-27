from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class Produkt(models.Model):
    kategorie = [
        ('elektronika', 'Elektronika'),
        ('gry', 'Gry'),
        ('rtv', 'RTV'),
    ]
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=8, decimal_places=2)
    kategoria = models.CharField(max_length=20, choices=kategorie)
    data_dodania = models.DateTimeField(auto_now_add=True)
    obrazek = models.ImageField(upload_to='produkty/', null=True, blank=True)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "produkt"
        verbose_name_plural = "produkty"
    
class Koszyk(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Koszyk {self.user.username}"
    
    class Meta:
        verbose_name = "koszyk"
        verbose_name_plural = "koszyki"
    

class PozycjaKoszyka(models.Model):
    koszyk = models.ForeignKey(Koszyk, on_delete=models.CASCADE, related_name='pozycje')
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    ilosc = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.ilosc} x {self.produkt.nazwa}"
    
    class Meta:
        verbose_name = "pozycja koszyka"
        verbose_name_plural = "pozycje koszyka"
    
class Zamowienie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_zamowienia = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, default='Nowe')

    def __str__(self):
        return f"Zamówienie #{self.id} - {self.user.username}"
    
    class Meta:
        verbose_name = "zamówienie"
        verbose_name_plural = "zamówienia"

class PozycjaZamowienia(models.Model):
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE, related_name='pozycje')
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    ilosc = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.ilosc} x {self.produkt.nazwa}"
    
    class Meta:
        verbose_name = "pozycja zamówienia"
        verbose_name_plural = "pozycje zamówienia"

