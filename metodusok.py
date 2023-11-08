
import random


def veletlen():
	i = 0
	while i < 10:
		szam = random.random()
		print(szam)
		i+=1








# 1. generalj 5 veletlen szamot [1,90]
def OtVeletlen():
	i = 0
	while i != 5:
		szam = random.randint(1,90)
		print(szam,end=";  ")
		i += 1






# 2. generalj 1.veletlen ketjegyuegesz szamot, dontse el hogy paros vagy nem
def Ketjegyu():
	szam = random.randint(10,99)
	if szam % 2 == 0:
		eredmeny = "páros"
	else:
		eredmeny = "páratlan"
	print(f"A {szam} szám {eredmeny}")






# 3. generalj 15 db veletlen szamot [0,1] kozott, hany 1est generalt?
def TizeonVeletlen():
	i = 0
	while i != 15:









# 4. generalj egy veletlen szamo 1-10 kozott, szorozd meg 3mal, -15, /6, *2, -eredeti szám, egyenlo e az eredmeny 5tel?
#def HosszuFeladat():
def OsszevisszaFeladat():
	szam = random.randint(2,9) 
	valtozott_szam = ((((szam*3)-15)/6)*2)-szam
	print(f"Eredeti: {szam}, valtozott szam {valtozott_szam}")
	if valtozott_szam == 5:
		print("Igen, a szám 5")
	else:
		print("Nem, a szám nem 5")






# 5. irj metodust, parameterben kapott szovegnek kiírja  hosszát
def HosszKiiras(kapott):
	print(len(kapott))






















