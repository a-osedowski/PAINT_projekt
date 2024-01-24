import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# 2 kina, rozne lokalizacje
kina = [
            (1, "Kino Fiołkowa", "Warszawa ul. Fiołkowa 13"),
            (2, "Kino Różana", "Warszawa ul. Różana 7")
]

try:
    cursor.executemany("INSERT INTO kino VALUES (?,?,?)", kina)
except Exception as e:
    pass

# kazde kino ma 2 sale
sale = [
            (1, "1", "duza", 1),
            (2, "1", "mala", 2),
            (3, "2", "duza", 1),
            (4, "2", "mala", 2)
]

try:
    cursor.executemany("INSERT INTO sala VALUES (?,?,?,?)", sale)
except Exception as e:
    pass

seanse = [
    (1, "22.01.2024", "14.00", 8, 1),
    (2, "22.01.2024", "17.00", 7, 1),
    (3, "22.01.2024", "20.00", 3, 1),

    (4, "22.01.2024", "14.00", 6, 2),
    (5, "22.01.2024", "17.00", 6, 2),
    (6, "22.01.2024", "20.00", 7, 2),

    (7, "22.01.2024", "14.00", 8, 3),
    (8, "22.01.2024", "17.00", 7, 3),
    (9, "22.01.2024", "20.00", 3, 3),

    (10, "22.01.2024", "14.00", 6, 4),
    (11, "22.01.2024", "17.00", 6, 4),
    (12, "22.01.2024", "20.00", 7, 4),

    (13, "23.01.2024", "14.00", 8, 1),
    (14, "23.01.2024", "17.00", 4, 1),
    (15, "23.01.2024", "20.00", 3, 1),

    (16, "23.01.2024", "14.00", 6, 2),
    (17, "23.01.2024", "17.00", 3, 2),
    (18, "23.01.2024", "20.00", 7, 2),

    (19, "23.01.2024", "14.00", 8, 3),
    (20, "23.01.2024", "17.00", 4, 3),
    (21, "23.01.2024", "20.00", 3, 3),

    (22, "23.01.2024", "14.00", 6, 4),
    (23, "23.01.2024", "17.00", 3, 4),
    (24, "23.01.2024", "20.00", 7, 4),

    (25, "24.01.2024", "14.00", 8, 1),
    (26, "24.01.2024", "17.00", 9, 1),
    (27, "24.01.2024", "20.00", 4, 1),

    (28, "24.01.2024", "14.00", 6, 2),
    (29, "24.01.2024", "17.00", 1, 2),
    (30, "24.01.2024", "20.00", 3, 2),

    (31, "24.01.2024", "14.00", 8, 3),
    (32, "24.01.2024", "17.00", 9, 3),
    (33, "24.01.2024", "20.00", 4, 3),

    (34, "24.01.2024", "14.00", 6, 4),
    (35, "24.01.2024", "17.00", 1, 4),
    (36, "24.01.2024", "20.00", 3, 4),

    (37, "25.01.2024", "14.00", 10, 1),
    (38, "25.01.2024", "17.00", 9, 1),
    (39, "25.01.2024", "20.00", 4, 1),

    (40, "25.01.2024", "14.00", 8, 2),
    (41, "25.01.2024", "17.00", 2, 2),
    (42, "25.01.2024", "20.00", 1, 2),

    (43, "25.01.2024", "14.00", 10, 3),
    (44, "25.01.2024", "17.00", 9, 3),
    (45, "25.01.2024", "20.00", 4, 3),

    (46, "25.01.2024", "14.00", 8, 4),
    (47, "25.01.2024", "17.00", 2, 4),
    (48, "25.01.2024", "20.00", 1, 4),

    (49, "26.01.2024", "14.00", 10, 1),
    (50, "26.01.2024", "17.00", 9, 1),
    (51, "26.01.2024", "20.00", 2, 1),

    (52, "26.01.2024", "14.00", 8, 2),
    (53, "26.01.2024", "17.00", 4, 2),
    (54, "26.01.2024", "20.00", 4, 2),

    (55, "26.01.2024", "14.00", 10, 3),
    (56, "26.01.2024", "17.00", 9, 3),
    (57, "26.01.2024", "20.00", 2, 3),

    (58, "26.01.2024", "14.00", 8, 4),
    (59, "26.01.2024", "17.00", 4, 4),
    (60, "26.01.2024", "20.00", 4, 4),

    (61, "27.01.2024", "14.00", 5, 1),
    (62, "27.01.2024", "17.00", 2, 1),
    (63, "27.01.2024", "20.00", 1, 1),

    (64, "27.01.2024", "14.00", 10, 2),
    (65, "27.01.2024", "17.00", 9, 2),
    (66, "27.01.2024", "20.00", 2, 2),
     ]
try:
    cursor.executemany("INSERT INTO seans VALUES (?,?,?,?,?)", seanse)
except Exception as e:
    pass

filmy = [
            (1, "Aquaman",                                  "Akcja",        "Sci-Fi",       "19 grudnia 2018",      "2 godz. 23 min.",  "USA, Australia",               "James Wan",                        "Jason Momoa, Amber Heard, Willem Dafoe",                           "aqua.jpg"),
            (2, "Igrzyska Śmierci: Ballada ptaków i węży",  "Akcja",        "Sci-Fi",       "17 listopada 2023",    "2 godz. 37 min.",  "USA",                          "Francis Lawrence",                 "Tom Blyth, Rachel Zegler, Viola Davis",                            "ballada.jpg"),
            (3, "Barbie",                                   "Dramat",       "Komedia",      "21 lipca 2023",        "1 godz. 54 min.",  "USA, Kanada",                  "Greta Gerwig",                     "Margot Robbie, Ryan Gosling, America Ferrera",                     "barbie.jpg"),
            (4, "Oppenheimer",                              "Biograficzny", "Dramat",       "21 lipca 2023",        "3 godz.",          "USA, Wielka Brytania",         "Christopher Nolan",                "Cillian Murphy, Emily Blunt, Matt Damon",                          "oppenheimer.jpg"),
            (5, "Spider-Man: Poprzez multiwersum",          "Animacja",     "Akcja",        "2 czerwca 2023",       "2 godz. 20 min.",  "USA",                          "Joaquim Dos Santos, Kemp Powers",  "Shameik Moore, Hailee Steinfeld, Brian Tyree Henry",               "spider-man.jpg"),
            (6, "Świąteczna niespodzianka",                 "Familijny",    "Świąteczny",   "9 grudnia 2022",       "1 godz. 18 min.",  "Norwegia",                     "Andrea Eckerbom",                  "Marte Klerck-Nilssen, John F. Brungot, Lene Kongsvik Johansen",    "swieta.jpg"),
            (7, "Szybcy i wściekli 10",                     "Akcja",        " ",            "19 maja 2023",         "2 godz. 21 min.",  "USA, Chiny, Japonia",          "Louis Leterrier",                  "Vin Diesel, Michelle Rodriguez, Jason Momoa",                      "szybcy.jpg"),
            (8, "Trolle 3",                                 "Animacja",     "Familijny",    "1 grudnia 2023",       "1 godz. 31 min.",  "USA",                          "Walt Dohrn",                       "Anna Kendrick, Justin Timberlake, Camila Cabello",                 "trolle.jpg"),
            (9, "Wonka",                                    "Fantasy",      "Komedia",      "14 grudnia 2023",      "1 godz. 53 min.",  "USA, Kanada, Wielka Brytania", "Paul King",                        "Timothée Chalamet, Calah Lane, Keegan-Michael Key",                "wonka.jpg"),
            (10, "Między nami żywiołami",                   "Animacja",     "Przygodowy",   "14 lipca 2023",        "1 godz. 41 min.",  "USA",                          "Peter Sohn",                       "Leah Lewis, Mamoudou Athie, Ronnie Del Carmen",                    "zywioly.jpg")
]

try:
    cursor.executemany("INSERT INTO film VALUES (?,?,?,?,?,?,?,?,?,?)", filmy)
except Exception as e:
    pass

uzytkownicy = [
            (1, "user", "tajnehaslo1")
]

try:
    cursor.executemany("INSERT INTO uzytkownik VALUES (?,?,?)", uzytkownicy)
except Exception as e:
    pass

# sprawdzenie
"""
cursor.execute("SELECT * FROM kino")
print(cursor.fetchall())
cursor.execute("SELECT * FROM sala")
print(cursor.fetchall())
cursor.execute("SELECT * FROM seans")
print(cursor.fetchall())
cursor.execute("SELECT * FROM film")
print(cursor.fetchall())
cursor.execute("SELECT * FROM uzytkownik")
print(cursor.fetchall())
"""

conn.commit()
conn.close()