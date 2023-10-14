

# KadarKristof --- FeketeOvesFeladatok --- Titkositas


# Kiolvassuk a fájl tartalmát, ékezetekre figyelve
szoveg=open("szöveg.txt","r",encoding="utf-8").read()
print("Eredeti szöveg:",szoveg)


# Az abc-t kisbetűssé kell formázni hogy tudjuk használni később
ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ,.:?!"
ABC=ABC.lower()
ABC=list(ABC)

titkosABC="XYZABCDEFGHIJKLMNOPQRSTUVW,.:?!"
titkosABC=list(titkosABC)

# A titkosítás folyamat "szíve"
titkosSzoveg=""
for i in szoveg:
    aktBetu = i.strip()   # A beolvasott szöveget betűkre felosztjuk

    if (aktBetu in ABC):
        poz = ABC.index(aktBetu) + 1    # Megkeresi az adott betűt hogy hol van az ABC változóban és annak az indexét adja neki +1-t
        titkosBetu = titkosABC[poz - 1]     # A "poz" számmal megkeressünk egy bizonyos indexű/sorszámú betűt a titkos ABC-ben
        titkosSzoveg+=titkosBetu  # A kapott titkosBetuk-et összerakjuk a titkoSzoveg változóba egy szövegként
    elif(aktBetu==""):     # "Space"-k miatt
        titkosBetu=" "
        titkosSzoveg+=titkosBetu
    else:
        titkosBetu="#"    # Ékezetes betűk miatt
        titkosSzoveg+=titkosBetu


# Végül kiírjuk a titkosított szöveget és elmentjük azt egy új fájlba
print("Titkosított szöveg: ", titkosSzoveg)
file = open('TitkosítottSzöveg.txt', 'w')
file.write(titkosSzoveg)

