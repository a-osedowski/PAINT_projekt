import datetime
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from Cinema.models import Film, Contact, Kino, Seans, Sala, Rezerwacja, Uzytkownik

def home(request):
    films = Film.objects.all()
    return render(request, 'index.html', {'films': films})

def cennik(request):
    return render(request, 'cennik.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        database = Contact.objects.create(imie_i_nazwisko=name, email=email, numer_telefonu=phone, temat=subject, tresc=message)
        database.save()
        return render(request, 'kontakt.html')
    else:
        return render(request, 'kontakt.html')

def details(request, pk):
    film = Film.objects.get(id=pk)
    seanse = Seans.objects.filter(film_id=pk).all()
    seanse_json = []
    for seans in seanse:
        sala = Sala.objects.get(id=seans.sala_id)
        kino = Kino.objects.get(id=sala.kino_id)
        data = {
            'seans_id': seans.id,
            'data': seans.data,
            'godzina': seans.godzina,
            'sala_numer': sala.numer,
            'sala_wielkosc': sala.wielkosc,
            'kino_nazwa': kino.nazwa,
            'kino_adres': kino.adres,
        }
        seanse_json.append(data)

    film_ret = {
        'id': film.id,
        'nazwa': film.nazwa,
        'kategoria1': film.kategoria1,
        'kategoria2': film.kategoria2,
        'premiera': film.premiera,
        'czas': film.czas,
        'produkcja': film.produkcja,
        'rezyser': film.rezyser,
        'obsada': film.obsada,
        'nazwa_jpg': film.nazwa_jpg,
        'seanse': seanse_json
    }

    return render(request, 'spoderman.html', {'film': film_ret})

def kup_bilet(request):
    kino = request.GET.get('kino')
    film = request.GET.get('film')
    film = Film.objects.get(id=film)
    seanse = Seans.objects.filter(film_id=film).all()
    seanse_json = []
    for seans in seanse:
        try:
            sala = Sala.objects.get(id=seans.sala_id, kino_id=kino)
            data = {
                'id': seans.id,
                'data': seans.data,
                'godzina': seans.godzina,
                'sala_numer': sala.numer,
                'sala_wielkosc': sala.wielkosc,
            }
            seanse_json.append(data)
        except:
            pass
    return render(request, 'seats.html', {'film': film, 'seanse': seanse_json})

def kup_bilet_sukces(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('fname')
        surname = request.POST.get('lname')
        email = request.POST.get('email')
        seans_id = request.POST.get('seans')
        user = Uzytkownik.objects.create(imie=name, nazwisko=surname, email=email)
        user.save()
        rez = Rezerwacja.objects.create(data=datetime.date, seans_id=seans_id, uzytkownik_id=user.id)
        rez.save()
        return HttpResponseRedirect(reverse('home'))