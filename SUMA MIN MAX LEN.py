lista = [10,4,5,7,2,3,6,13]
legkisebb = lista[0]
legnagyobb = lista[0]
def mini(lista):
        legkisebb = lista[0]
        for szam in lista:
            if szam < legkisebb:
                legkisebb = szam
        return legkisebb
    
    

lista = [10,4,5,7,2,3,6,13]
legkisebb = lista[0]

def maxi(lista):
        legnagyobb = lista[0]
        for szam in lista:
            if szam > legnagyobb:
                legnagyobb = szam
        return legnagyobb


def suma(lista):
    osszeg = 0
    for szam in lista:
        osszeg = osszeg + szam
    return osszeg


def leni(lista):
    db = 0
    for szam in lista:
        db += 1
    return db

def atlag(lista):
    return suma(lista) / leni(lista)



    