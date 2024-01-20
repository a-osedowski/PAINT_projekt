import sqlite3

conn = sqlite3.connect('kino_miasto.db')
cursor = conn.cursor()

try:
    cursor.execute('''
        CREATE TABLE kino (
            id INTEGER PRIMARY KEY,
            nazwa TEXT,
            adres TEXT
        )
    ''')
except Exception as e:
    pass

try:
    cursor.execute('''
        CREATE TABLE sala (
            id INTEGER PRIMARY KEY,
            kino_id INTEGER,
            numer TEXT,
            wielkosc TEXT,
            FOREIGN KEY (kino_id) REFERENCES kino(id)
        )
    ''')
except Exception as e:
    pass

try:
    cursor.execute('''
        CREATE TABLE seans (
            id INTEGER PRIMARY KEY,
            sala_id INTEGER,
            film_id INTEGER,
            data TEXT,
            godzina TEXT,
            FOREIGN KEY (sala_id) REFERENCES sala(id),
            FOREIGN KEY (film_id) REFERENCES film(id)
        )
    ''')
except Exception as e:
    pass

try:
    cursor.execute('''
        CREATE TABLE film (
            id INTEGER PRIMARY KEY,
            nazwa TEXT,
            kategoria TEXT,
            rezyser TEXT,
            nazwa_jpg TEXT
        )
    ''')
except Exception as e:
    pass

try:
    cursor.execute('''
        CREATE TABLE uzytkownik (
            id INTEGER PRIMARY KEY,
            login TEXT,
            haslo TEXT
        )
    ''')
except Exception as e:
    pass

try:
    cursor.execute('''
        CREATE TABLE rezerwacja (
            id INTEGER PRIMARY KEY,
            data TEXT,
            rzad TEXT,
            miejsce TEXT,
            uzytkownik_id INTEGER,
            seans_id INTEGER,
            FOREIGN KEY (uzytkownik_id) REFERENCES uzytkownik(id),
            FOREIGN KEY (seans_id) REFERENCES seans(id)
        )
    ''')
except Exception as e:
    pass


# 2 kina, rozne lokalizacje
kina = [
            (1, "Kino Miasto", "Warszawa ul. Fiołkowa 13"),
            (2, "Kino Miasto", "Warszawa ul. Różana 7")
]

try:
    cursor.executemany("INSERT INTO kino VALUES (?,?,?)", kina)
except Exception as e:
    pass

# kazde kino ma 2 sale
sale = [
            (1, 1, "1", "duza"),
            (2, 1, "2", "mala"),
            (3, 2, "1", "duza"),
            (4, 2, "2", "mala")
]

try:
    cursor.executemany("INSERT INTO sala VALUES (?,?,?,?)", sale)
except Exception as e:
    pass

seanse = [
            (1, 1, 8, "22.01.2024", "14.00"),
            (2, 1, 7, "22.01.2024", "17.00"),
            (3, 1, 3, "22.01.2024", "20.00"),
            (4, 2, 6, "22.01.2024", "14.00"),
            (5, 2, 6, "22.01.2024", "17.00"),
            (6, 2, 7, "22.01.2024", "20.00"),
            (7, 3, 8, "22.01.2024", "14.00"),
            (8, 3, 7, "22.01.2024", "17.00"),
            (9, 3, 3, "22.01.2024", "20.00"),
            (10, 4, 6, "22.01.2024", "14.00"),
            (11, 4, 6, "22.01.2024", "17.00"),
            (12, 4, 7, "22.01.2024", "20.00"),

            (13, 1, 8, "23.01.2024", "14.00"),
            (14, 1, 4, "23.01.2024", "17.00"),
            (15, 1, 3, "23.01.2024", "20.00"),
            (16, 2, 6, "23.01.2024", "14.00"),
            (17, 2, 3, "23.01.2024", "17.00"),
            (18, 2, 7, "23.01.2024", "20.00"),
            (19, 3, 8, "23.01.2024", "14.00"),
            (20, 3, 4, "23.01.2024", "17.00"),
            (21, 3, 3, "23.01.2024", "20.00"),
            (22, 4, 6, "23.01.2024", "14.00"),
            (23, 4, 3, "23.01.2024", "17.00"),
            (24, 4, 7, "23.01.2024", "20.00"),

            (25, 1, 8, "24.01.2024", "14.00"),
            (26, 1, 9, "24.01.2024", "17.00"),
            (27, 1, 4, "24.01.2024", "20.00"),
            (28, 2, 6, "24.01.2024", "14.00"),
            (29, 2, 1, "24.01.2024", "17.00"),
            (30, 2, 3, "24.01.2024", "20.00"),
            (31, 3, 8, "24.01.2024", "14.00"),
            (32, 3, 9, "24.01.2024", "17.00"),
            (33, 3, 4, "24.01.2024", "20.00"),
            (34, 4, 6, "24.01.2024", "14.00"),
            (35, 4, 1, "24.01.2024", "17.00"),
            (36, 4, 3, "24.01.2024", "20.00"),

            (37, 1, 10, "25.01.2024", "14.00"),
            (38, 1, 9, "25.01.2024", "17.00"),
            (39, 1, 4, "25.01.2024", "20.00"),
            (40, 2, 8, "25.01.2024", "14.00"),
            (41, 2, 2, "25.01.2024", "17.00"),
            (42, 2, 1, "25.01.2024", "20.00"),
            (43, 3, 10, "25.01.2024", "14.00"),
            (44, 3, 9, "25.01.2024", "17.00"),
            (45, 3, 4, "25.01.2024", "20.00"),
            (46, 4, 8, "25.01.2024", "14.00"),
            (47, 4, 2, "25.01.2024", "17.00"),
            (48, 4, 1, "25.01.2024", "20.00"),

            (49, 1, 10, "26.01.2024", "14.00"),
            (50, 1, 9, "26.01.2024", "17.00"),
            (51, 1, 2, "26.01.2024", "20.00"),
            (52, 2, 8, "26.01.2024", "14.00"),
            (53, 2, 4, "26.01.2024", "17.00"),
            (54, 2, 4, "26.01.2024", "20.00"),
            (55, 3, 10, "26.01.2024", "14.00"),
            (56, 3, 9, "26.01.2024", "17.00"),
            (57, 3, 2, "26.01.2024", "20.00"),
            (58, 4, 8, "26.01.2024", "14.00"),
            (59, 4, 4, "26.01.2024", "17.00"),
            (60, 4, 4, "26.01.2024", "20.00"),

            (61, 1, 5, "27.01.2024", "14.00"),
            (62, 1, 2, "27.01.2024", "17.00"),
            (63, 1, 1, "27.01.2024", "20.00"),
            (64, 2, 10, "27.01.2024", "14.00"),
            (65, 2, 9, "27.01.2024", "17.00"),
            (66, 2, 2, "27.01.2024", "20.00"),
            (67, 3, 5, "27.01.2024", "14.00"),
            (68, 3, 2, "27.01.2024", "17.00"),
            (69, 3, 1, "27.01.2024", "20.00"),
            (70, 4, 10, "27.01.2024", "14.00"),
            (71, 4, 9, "27.01.2024", "17.00"),
            (72, 4, 2, "27.01.2024", "20.00"),

            (73, 1, 5, "28.01.2024", "14.00"),
            (74, 1, 5, "28.01.2024", "17.00"),
            (75, 1, 1, "28.01.2024", "20.00"),
            (76, 2, 10, "28.01.2024", "14.00"),
            (77, 2, 9, "28.01.2024", "17.00"),
            (78, 2, 2, "28.01.2024", "20.00"),
            (79, 3, 5, "28.01.2024", "14.00"),
            (80, 3, 5, "28.01.2024", "17.00"),
            (81, 3, 1, "28.01.2024", "20.00"),
            (82, 4, 10, "28.01.2024", "14.00"),
            (83, 4, 9, "28.01.2024", "17.00"),
            (84, 4, 2, "28.01.2024", "20.00")
]
try:
    cursor.executemany("INSERT INTO seans VALUES (?,?,?,?,?)", seanse)
except Exception as e:
    pass

filmy = [
            (1, "Aquaman", "Akcja", "James Wan", "aqua.jpg"),
            (2, "Igrzyska Śmierci: Ballada ptaków i węży", "Akcja", "Francis Lawrence", "ballada.jpg"),
            (3, "Barbie", "Komedia", "Greta Gerwig", "barbie.jpg"),
            (4, "Oppenheimer", "Biograficzny", "Christopher Nolan", "oppenheimer.jpg"),
            (5, "Spider-Man: Poprzez multiwersum", "Animacja", "Joaquim Dos Santos & Kemp Powers", "spider-man.jpg"),
            (6, "Świąteczna niespodzianka", "Familijny", "Andrea Eckerbom", "swieta.jpg"),
            (7, "Szybcy i wściekli 10", "Akcja", "Louis Leterrier", "szybcy.jpg"),
            (8, "Trolle 3", "Animacja", "Walt Dohrn", "trolle.jpg"),
            (9, "Wonka", "Fantasy", "Paul King", "wonka.jpg"),
            (10, "Między nami żywiołami", "Animacja", "Peter Sohn", "zywioly.jpg")
]

try:
    cursor.executemany("INSERT INTO film VALUES (?,?,?,?,?)", filmy)
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
