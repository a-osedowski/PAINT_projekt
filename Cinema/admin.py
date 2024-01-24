from django.contrib import admin
from Cinema.models import Film, Kino, Uzytkownik, Rezerwacja, Sala, Seans
admin.site.register(Film)
admin.site.register(Kino)
admin.site.register(Uzytkownik)
admin.site.register(Rezerwacja)
admin.site.register(Seans)
admin.site.register(Sala)