
import random

nyertes_szamok = []
szelveny_szamok = []
tipp_szamok = []

i=1
for szam in range(5):

	# Nyertes számok kiválasztása
	random_szam=random.randint(1,99)
	nyertes_szamok.append(random_szam)

	# Tippelt számok bekérése
	tipp=input(f"Kérlek add meg az {i}. tippelt számod: ")
	while not (tipp.isdigit() and int(tipp)>=0):
		print("Nem lehet 0 vagy azalatt és kötelező megadni egy számot!")
		print("--------------------------------------------------------")
		tipp=input(f"Kérlek add meg az {i}. tippelt számod: ")
	tipp_szamok.append(tipp)
	i+=1

# Töbdimenziós lista generálása (20x5)
for x in range(20):
	valtozo_lista = []
	for y in range(5):
		random_szam=random.randint(1,99)
		valtozo_lista.append(random_szam)
	szelveny_szamok.append(valtozo_lista)

# Eltalált számok keresése (5)
talalatok=0
for a in nyertes_szamok:
	for b in tipp_szamok:
		if(a==b):
			talalatok+=1
		else:
			pass

# Eltalált számok keresése (20x5)
talalatok_X=0
for lista in szelveny_szamok:
	for i in lista:
		for x in nyertes_szamok:
			if(i==x):
				talalatok_X+=1
			else:
				pass

print("Nyertes számok:",nyertes_szamok)
print("Tippelt számok:",tipp_szamok)
print("Találatok:",talalatok)
print("20x5-s listák találata:",talalatok_X)





