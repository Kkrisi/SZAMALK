
import random


#ctr+b-vel lehet sublime-ba py programot futtatni




#Írd ki, hogy melyik a legnagyobb szám a [100;100000] intervallumból, amelyiknek az utolsó számjegye nagyobb, mint az előtte lévő számjegyek összege.

'''
talaltam_lista=[]

for szam in range(100,117):
	szamjegy_osszeg=0

	for szamjegy in str(szam):
		szamjegy_osszeg+=int(szamjegy)

	szam_str=str(szam)
	if(int(szam_str[-1]) > (szamjegy_osszeg-int(szam_str[-1]))):
		talaltam_lista.append(szam)

print("Találtam lista:",talaltam_lista)
print("Sikeres")
'''













#Írd ki 100-tól kezdve a második 10 darab olyan számot, amelyiknek pontosan 7 osztója van (1-et és önmagát figyelmen kívül hagyva).


'''
for i in range(100,)


'''




















#Írd ki annak a sorozatnak a 15. elemét, amelyet úgy kapsz meg, hogy minden következő elemet az előző szám számjegyeinek kétszereséből állítod elő! (1, 2, 4, 8, 16, 212, 424, 848, 16816)

'''
szam=str(1)

for valtozo_szam in range(0,15):

	kesz_dupla=""
	for i in range(len(szam)):
		szamjegy=szam[i]

		ketszeres=int(szamjegy)*2
		kesz_dupla+=str(ketszeres)
	szam=kesz_dupla

print("15.elem:",szam)
print("Sikeres")
'''


























#Sorsolj ki egy 6 számjegyű számot. Add meg, hogy melyik prímszám van ehhez a legközelebb! Ha több ilyen van, írd ki mindet!

'''
sorsolt = random.randint(100000,999999)
print("Sorsolt szám:",sorsolt)

szamsor_szamjegyek=[]
primek=[]

tol=sorsolt-5
ig=sorsolt+6

for i in range(tol,ig):

	
	for oszto in range(2, int(i**0.5) + 1):
		if i % oszto == 0:
			print("Ez nem prím:",i)
		else:
			primek.append(i)
print(primek)
'''






































#Sorsolj ki egy 10 számjegyű számot. Írd ki a számon belüli prímszámokat! (pl: 1123456789 -> 2, 3, 5, 7, 11, 23, 67, 89, 1123, 4567, 23456789) A prímszámokat növekvő sorrendben add meg! Ugyanazt a számot ne írd ki kétszer! Ha nincs ilyen, akkor írd ki, hogy nincs ilyen szám!

'''
sorsolt_szam = random.randint(1000000000,9999999999)
#sorsolt_szam = 5464379409
print("Eredeti szám:",sorsolt_szam)


sorsolt_szam_str = str(sorsolt_szam)


prim_szamok_gyujto = []
prim_szamok = []

osszes_szamkombinacio = []





# Egy számjegyű tagoka a számból összegyüjtjük
for szamjegy in sorsolt_szam_str:
	osszes_szamkombinacio.append(szamjegy)



# Az összes több mint 1jegyű számot megkeressük pl 24 245 2469
i=2
# 2 számjegyűeket keresem ki a számból
for szamjegy in sorsolt_szam_str:
	szamjegy+=sorsolt_szam_str[:i]
	osszes_szamkombinacio.append(szamjegy[-2:])
	print("2 számjegyű:",szamjegy[-2:])


	# 3 számjegyűeket keresem ki a számból
	# Első számokat nem szabad belevenni, ezért van ez az intézkedés
	if(i>2):
		osszes_szamkombinacio.append(szamjegy[-3:])
		print("3 számjegyű:",szamjegy[-3:])

	# 4 számjegyűeket keresem ki a számból
	if(i>3):
		osszes_szamkombinacio.append(szamjegy[-4:])
		print("4 számjegyű:",szamjegy[-4:])

	# 5 számjegyűeket keresem ki a számból	
	if(i>4):
		osszes_szamkombinacio.append(szamjegy[-5:])
		print("5 számjegyű:",szamjegy[-5:])

	if(i>5):
		osszes_szamkombinacio.append(szamjegy[-6:])
		print("6 számjegyű:",szamjegy[-6:])

	if(i>6):
		osszes_szamkombinacio.append(szamjegy[-7:])
		print("7 számjegyű:",szamjegy[-7:])

	if(i>7):
		osszes_szamkombinacio.append(szamjegy[-8:])
		print("8 számjegyű:",szamjegy[-8:])

	if(i>8):
		osszes_szamkombinacio.append(szamjegy[-9:])
		print("9 számjegyű:",szamjegy[-9:])

	i+=1






# Prím számok keresése [az összes listán átfutunk(2es / 3ma számjegyek pl)]
for szamjegy in osszes_szamkombinacio:
	for i in range(2, int(int(szamjegy)**0.5) + 1):
		if(int(szamjegy) % i == 0):
			print("false:",szamjegy)
		elif(int(szamjegy)>1 and int(szamjegy) <=3):
			print("true:",szamjegy)
	print("true:",szamjegy)


	if(int(szamjegy)>1 and int(szamjegy) <=3):
		if(szamjegy not in prim_szamok_gyujto):
			prim_szamok_gyujto.append(szamjegy)







# Eltávolítjuk a prim_szamok_gyujto listából ami 2x van benne + ami nullaval kezdodik: pl '02'!!!!!!!!!!!!!!!!!!!!!!!
for szamjegy in prim_szamok_gyujto:
	if(szamjegy not in prim_szamok):
		if(szamjegy.startswith('0')):
			pass
		else:
			prim_szamok.append(int(szamjegy))



# Utolsó lépés, kíírás
if(prim_szamok==[]):
	print("Nincsenek benne prím számok")
else:
	prim_szamok.sort()
	print("Prím számok benne:",prim_szamok)

'''






























#Sorsolj ki egy 10 számjegyű számot. Melyik az a legnagyobb legalább kétjegyű szám ezen belül, amelyiknek a számjegyei növekvő sorrendben állnak? (pl: 1234345673 -> 34567) Ha nincs ilyen, akkor írd ki, hogy nincs ilyen szám!

'''
#sorsolt_szam = random.randint(1000000000,9999999999)
sorsolt_szam=73459678
print("Eredeti szám:",sorsolt_szam)

sorsolt_str = str(sorsolt_szam)

szamjegy_lista=[]


for i in sorsolt_str:
	szamjegy_lista.append(int(i))

print(szamjegy_lista)


talalt_szam_lista=[]


for i in szamjegy_lista:
	print("Számjegy(i):",i)
	for x in range(1,6):
		print("-------------------")


		if int(i)+1==int(szamjegy_lista[x]):
			print("i+1==",int(i)+1,"Kövi:",int(szamjegy_lista[x]))

			if i not in talalt_szam_lista:
				print(i," nincs benne még a ",talalt_szam_lista," listában")
				print(i,"csatolva a listához")
				talalt_szam_lista.append(i)
				print("lista: ",talalt_szam_lista)


			if int(szamjegy_lista[x]) not in talalt_szam_lista:
				talalt_szam_lista.append(szamjegy_lista[x])

print("Számjegylista::",talalt_szam_lista)
	'''	

















'''
	jelenlegi_szamjegy = int(sorsolt_str[i])
	kovetkezo_szamjegy = int(sorsolt_str[i+1])

	print(sorsolt_str[i-5])
	if jelenlegi_szamjegy == kovetkezo_szamjegy-1:
		talaltam_szam += str(jelenlegi_szamjegy)+str(kovetkezo_szamjegy)
		print("talaltam_szam:",talaltam_szam)
		if kovetkezo_szamjegy == int(sorsolt_str[i+2]):
			talaltam_szam += sorsolt_str[i+2]
	talaltam_lista.append(talaltam_szam)
'''











'''
	if (elso_szamjegy+1 == masodik_szamjegy):
		talalt_szam = str(elso_szamjegy)+str(masodik_szamjegy)
		talaltam_lista.append(talalt_szam)
print(talaltam_lista)
'''






























#Sorsolj ki egy 10 számjegyű számot. Írd ki azokat a számjegyeket, amelyek nem fordulnak elő a számban! Ha nincs ilyen, írd ki, hogy nincs hiányzó számjegy!


'''
sorsolt_szam = random.randint(1000000000,9999999999)
print("Eredeti szám:",sorsolt_szam)


alap_szamok = [0,1,2,3,4,5,6,7,8,9]
hianyzo_szamok = []

sorsolt_szam_str = str(sorsolt_szam)



for szamjegy in sorsolt_szam_str:
	if(int(szamjegy) in alap_szamok):
		alap_szamok.remove(int(szamjegy))
	else:
		pass


print("Számjegyek amik nem szerepelnek benne:",alap_szamok)
print("Sikeres")

'''


























#Sorsolj ki egy 10 számjegyű számot. Írd ki azokat a 3 számjegyű számokat, amelyek az eredeti számjegyekből összerakhatóak úgy, hogy a számjegyeik növekvő sorrenden állnak. Ugyanazt a számot ne írd ki kétszer! Ha nincsenek ilyenek, akkor írd ki, hogy nincsenek ilyen számok!

'''
sorsolt = random.randint(1000000000,9999999999)
print("Sorsolt szám:",sorsolt)
sorsolt_str = str(sorsolt)
nyertesek_lista = []


for i in range(len(sorsolt_str) - 2):

	elso_szamjegy = int(sorsolt_str[i])
	masodik_szamjegy = int(sorsolt_str[i + 1])
	harmadik_szamjegy = int(sorsolt_str[i + 2])


	if (elso_szamjegy+1 == masodik_szamjegy and masodik_szamjegy+1 == harmadik_szamjegy):
		talalt_szam = str(elso_szamjegy)+str(masodik_szamjegy)+str(harmadik_szamjegy)
		nyertesek_lista.append(talalt_szam)


print("Nyertesek:", nyertesek_lista)
print("Sikeres")
'''




























#Sorsolj ki egy 5 számjegyű számot. Írd ki, hogy van-e olyan számjegye, amelyik nagyobb a többi számjegy összegénél! Ha van ilyen, írd ki melyik az! Ha nincs ilyen, írd ki, hogy nincs ilyen számjegy!

'''
sorsolt = random.randint(10000,99999)
print("Sorsolt szám:",sorsolt)
print("-----------------------")

osszeg=0

nyertes_str = str(sorsolt)
szamjegy_lista=[]

for szamjegy in nyertes_str:
	szamjegy_lista.append(szamjegy)
	osszeg+=int(szamjegy)
print("Összeg:",osszeg)

szamjegy_lista.sort()



legnagyobb=""

for szam in szamjegy_lista:
	if(int(szam)>osszeg-int(szam)):
		legnagyobb=szam

if(legnagyobb==""):
	print("Nincs olyan számjegy ami nagyobb lenne a többi számjegy összegénél")
else:
	print("Találtunk:",legnagyobb)

print("Sikeres")
'''





