from django.shortcuts import render, redirect, get_object_or_404
from .models import Produkt, Koszyk, PozycjaKoszyka, Zamowienie, PozycjaZamowienia
from .forms import RejestracjaForm, ZamowienieForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

def home(request):
    produkty = Produkt.objects.all()
    print(produkty)
    return render(request, 'home.html', {'produkty': produkty})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = LoginForm

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Niepoprawny login lub hasło.")
        return super().form_invalid(form)

from django.contrib import messages

def rejestracja(request):
    if request.method == 'POST':
        form = RejestracjaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Konto zostało utworzone. Możesz się teraz zalogować.')
            return redirect('login')
        else:
            for field, errs in form.errors.items():
                for err in errs:
                    label = form.fields[field].label if field in form.fields else ''
                    if label:
                        messages.error(request, f"{label}: {err}")
                    else:
                        messages.error(request, err)
    else:
        form = RejestracjaForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def dodaj_do_koszyka(request, produkt_id):
    produkt = get_object_or_404(Produkt, id=produkt_id)
    koszyk, created = Koszyk.objects.get_or_create(user=request.user)
    pozycja, created = PozycjaKoszyka.objects.get_or_create(koszyk=koszyk, produkt=produkt)
    if not created:
        pozycja.ilosc += 1
        pozycja.save()
    return redirect('koszyk')

@login_required
def koszyk_view(request):
    koszyk, created = Koszyk.objects.get_or_create(user=request.user)
    pozycje = koszyk.pozycje.all()
    for p in pozycje:
        p.wartosc = p.produkt.cena * p.ilosc
    suma = sum(p.wartosc for p in pozycje)
    return render(request, 'koszyk.html', {'pozycje': pozycje, 'suma': suma})


@login_required
def zloz_zamowienie(request):
    koszyk = Koszyk.objects.filter(user=request.user).first()
    if not koszyk or not koszyk.pozycje.exists():
        return redirect('home')

    zamowienie = Zamowienie.objects.create(user=request.user)
    for pozycja in koszyk.pozycje.all():
        PozycjaZamowienia.objects.create(
            zamowienie=zamowienie,
            produkt=pozycja.produkt,
            ilosc=pozycja.ilosc
        )
    koszyk.pozycje.all().delete()

    return render(request, 'potwierdzenie_zamowienia.html', {'zamowienie': zamowienie})

@login_required
def zamowienie(request):
    if request.method == 'POST':
        form = ZamowienieForm(request.POST)
        if form.is_valid():
            zam = Zamowienie.objects.create(
                user=request.user,
                data_zamowienia=timezone.now(),
                status='Nowe',
            )

            return render(request, 'potwierdzenie_zamowienia.html', {
                'numer_zamowienia': zam.id,
                'data_zamowienia': zam.data_zamowienia,
            })
    else:
        form = ZamowienieForm()

    return render(request, 'zamowienie.html', {'form': form})


def potwierdzenie_zamowienia(request):
    return render(request, 'potwierdzenie_zamowienia.html')

