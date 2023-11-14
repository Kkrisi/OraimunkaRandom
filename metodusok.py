import math
import random


#[30,1000) --> 30 benne van, 1000 nincs benne
#math.floor(random.random()*(1001-30)+30)


# 1. generalj 5 veletlen szamot [1,90]
def OtVeletlen():
	i = 0
	while i != 5:
		szam = math.floor(random.random()*(90-1)+1)
		print(szam,end=";  ")
		i += 1






# 2. generalj 1.veletlen ketjegyuegesz szamot, dontse el hogy paros vagy nem
def Ketjegyu():
	szam = math.floor(random.random()*(99-10)+10)
	if szam % 2 == 0:
		eredmeny = "páros"
	else:
		eredmeny = "páratlan"
	print(f"A {szam} szám {eredmeny}")






# 3. generalj 15 db veletlen szamot [0,1] kozott, hany 1est generalt?
def TizeonVeletlen():
	i = 0
	szamlalo = 0
	while i != 15:
		szam = random.random()
		if szam == 1:
			szamlalo += 1
		print(szam)
		i += 1
	print(f"Ennyi 1-es volt: {szamlalo}")  # mindig 0 lesz a szamlalo








# 4. generalj egy veletlen szamo 1-10 kozott, szorozd meg 3mal, -15, /6, *2, -eredeti szám, egyenlo e az eredmeny 5tel?
#def HosszuFeladat():
def OsszevisszaFeladat():
	szam = szam = math.floor(random.random()*(10-1)+1)
	valtozott_szam = ((((szam*3)-15)/6)*2)-szam
	print(f"Eredeti: {szam}, valtozott szam {valtozott_szam}")
	if valtozott_szam == 5:
		print("Igen, a szám 5")
	else:
		kulonbseg = 5 - valtozott_szam
		print(f"Nem, a szám nem 5. (Különbség 5 és {valtozott_szam} között: {int(kulonbseg)})")






# 5. irj metodust, parameterben kapott szovegnek kiírja  hosszát
def HosszKiiras(kapott):
	print(len(kapott))

























