
from django.db import models
from django.urls import reverse


class Kino(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    nazwa = models.CharField(max_length=150, db_column='nazwa')
    adres = models.CharField(max_length=150, db_column='adres')

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        db_table = 'kino'
        managed = True

class Sala(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE, db_column='kino_id')
    numer = models.CharField(max_length=150, db_column='numer')
    wielkosc = models.CharField(max_length=150, db_column='wielkosc')


    def __str__(self):
        return self.kino

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        db_table = 'sala'
        managed = True


class Film(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    nazwa = models.CharField(max_length=150, db_column='nazwa')
    kategoria1 = models.CharField(max_length=150, db_column='kategoria1')
    kategoria2 = models.CharField(max_length=150, db_column='kategoria2')
    premiera = models.CharField(max_length=255, db_column='premiera')
    czas = models.CharField(max_length=255, db_column='czas')
    produkcja = models.CharField(max_length=255, db_column='produkcja')
    rezyser = models.CharField(max_length=255, db_column='rezyser')
    obsada = models.TextField(max_length=255, db_column='obsada')
    nazwa_jpg = models.CharField(max_length=150, db_column='nazwa_jpg')

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        db_table = 'film'
        managed = True

class Seans(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, db_column='sala_id')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, db_column='film_id')
    data = models.CharField(max_length=150, db_column='data')
    godzina = models.CharField(max_length=150, db_column='godzina')

    def __str__(self):
        return self.sala

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        db_table = 'seans'
        managed = True

class Uzytkownik(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    imie = models.CharField(max_length=150, db_column='imie')
    nazwisko = models.CharField(max_length=150, db_column='nazwisko')
    email = models.CharField(max_length=150, db_column='email')

    def __str__(self):
        return self.login

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        db_table = 'uzytkownik'
        managed = True

class Rezerwacja(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    data = models.CharField(max_length=150, db_column='data')
    rzad = models.CharField(max_length=150, db_column='rzad')
    miejsce = models.CharField(max_length=150, db_column='miejsce')
    uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE, db_column='uzytkownik_id')
    seans = models.ForeignKey(Seans, on_delete=models.CASCADE, db_column='seans_id')

    def __str__(self):
        return self.rezerwacja

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        db_table = 'rezerwacja'
        managed = True

from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    imie_i_nazwisko = models.CharField(max_length=255)
    email = models.EmailField()
    numer_telefonu = models.CharField(max_length=20)
    temat = models.CharField(max_length=255)
    tresc = models.CharField(max_length=400)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        db_table = 'contact'
        managed = True

