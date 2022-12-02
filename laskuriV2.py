import sys

class Tiedot:
    paivamaara = ""
    tuntikulutus = ""
    tunti = ""
    paiva = ""
    kuukausi = ""
    vuosi = ""

class Hinnat:
    paivamaara = ""
    tunti = ""
    tuntihinta = ""

class KulutusTulokset:
    vuosikulutus = 0
    kk1 = 0
    kk1hinta = 0 
    kk2 = 0
    kk2hinta = 0 
    kk3 = 0
    kk3hinta = 0 
    kk4 = 0
    kk4hinta = 0 
    kk5 = 0
    kk5hinta = 0 
    kk6 = 0
    kk6hinta = 0 
    kk7 = 0
    kk7hinta = 0 
    kk8 = 0
    kk8hinta = 0 
    kk9 = 0
    kk9hinta = 0 
    kk10 = 0
    kk10hinta = 0 
    kk11 = 0
    kk11hinta = 0 
    kk12 = 0
    kk12hinta = 0
    vuosihintaporssi = 0

def lueKulutusTiedosto(file):
    try:
        objektiLista = []
        kokoKulutus = 0
        tiedosto = open(file, 'r', encoding="utf-8")
        tiedosto.readline() # Lukee tyhjän rivin pois.
        while True:
            rivi = tiedosto.readline()
            if len(rivi) == 0:
                break
            lista = rivi.split(";")
            obj = Tiedot()
            obj.paivamaara = (lista[4].split("T"))[0]
            obj.tuntikulutus = lista[5].replace(",",".")
            obj.tunti = (lista[4].split("T"))[1][:-1]
            obj.paiva = ((lista[4].split("-"))[2]).split("T")[0]
            obj.kuukausi = (lista[4].split("-"))[1]
            obj.vuosi = (lista[4].split("-"))[0]
            objektiLista.append(obj)
            kokoKulutus += float(obj.tuntikulutus)
        return objektiLista

    except FileNotFoundError:
        print("Tiedostoa ei löytynyt. Lopetetaan.")
        sys.exit(0)
    except:
        print("Tiedoston lukemisessa virhe. Onko luettelo varmasti oikeassa muodossa?")
        sys.exit(0)

def lueHinnat(nimi):
    try:
        hintalista = []
        tiedosto = open(nimi, 'r', encoding="utf-8")
        tiedosto.readline() # Lukee tyhjän rivin pois.
        while True:
            rivi = tiedosto.readline()
            if len(rivi) == 0:
                break
            lista = rivi.split(";")
            objekti = Hinnat()
            objekti.paivamaara = (lista[0].split(" "))[0][1:]
            objekti.tunti = (lista[0].split(" "))[1][:-1]
            objekti.tuntihinta = (lista[1]).replace(",",".")
            hintalista.append(objekti)
        return hintalista
    except FileNotFoundError:
        print("Tiedoston lukemisessa virhe. Lopetetaan.")
        sys.exit(0)
    except:
        print("Tiedoston lukemisessa virhe. Onko luettelo varmasti oikeassa muodossa?")
        sys.exit(0)

def analysoi(objektiLista, hinnasto):
    x = input("Minkä vuoden kulutustiedot haluat analysoida: ")
    tulokset = []
    tulos = KulutusTulokset()
    for i in range(0, len(objektiLista)):
        obj = objektiLista[i]
        if obj.vuosi == x:
            tulos.vuosikulutus += float(obj.tuntikulutus)
            if obj.kuukausi == "01":
                tulos.kk1 += float(obj.tuntikulutus)
            elif obj.kuukausi == "02":
                tulos.kk2 += float(obj.tuntikulutus)
            elif obj.kuukausi == "03":
                tulos.kk3 += float(obj.tuntikulutus)
            elif obj.kuukausi == "04":
                tulos.kk4 += float(obj.tuntikulutus)
            elif obj.kuukausi == "05":
                tulos.kk5 += float(obj.tuntikulutus)
            elif obj.kuukausi == "06":
                tulos.kk6 += float(obj.tuntikulutus)
            elif obj.kuukausi == "07":
                tulos.kk7 += float(obj.tuntikulutus)
            elif obj.kuukausi == "08":
                tulos.kk8 += float(obj.tuntikulutus)
            elif obj.kuukausi == "09":
                tulos.kk9 += float(obj.tuntikulutus)
            elif obj.kuukausi == "10":
                tulos.kk10 += float(obj.tuntikulutus)
            elif obj.kuukausi == "11":
                tulos.kk11 += float(obj.tuntikulutus)
            elif obj.kuukausi == "12":
                tulos.kk12 += float(obj.tuntikulutus)
            for j in range(0, len(hinnasto)):
                hintaobj = hinnasto[j]
                if obj.paivamaara == hintaobj.paivamaara and obj.tunti == hintaobj.tunti:
                    tulos.vuosihintaporssi += float(hintaobj.tuntihinta) * float(obj.tuntikulutus)
                    if obj.kuukausi == "01":
                        tulos.kk1hinta += float(hintaobj.tuntihinta) * float(obj.tuntikulutus)
                    elif obj.kuukausi == "02":
                        tulos.kk2hinta += float(hintaobj.tuntihinta) * float(obj.tuntikulutus)
                    elif obj.kuukausi == "03":
                        tulos.kk3hinta += float(hintaobj.tuntihinta) * float(obj.tuntikulutus)
                    elif obj.kuukausi == "04":
                        tulos.kk4hinta += float(hintaobj.tuntihinta) * float(obj.tuntikulutus)
                    elif obj.kuukausi == "05":
                        tulos.kk5hinta += float(hintaobj.tuntihinta) * float(obj.tuntikulutus)
                    elif obj.kuukausi == "06":
                        tulos.kk6hinta += float(hintaobj.tuntihinta) * float(obj.tuntikulutus)
                    elif obj.kuukausi == "07":
                        tulos.kk7hinta += float(hintaobj.tuntihinta) * float(obj.tuntikulutus)
                    elif obj.kuukausi == "08":
                        tulos.kk8hinta += float(hintaobj.tuntihinta) * float(obj.tuntikulutus)
                    elif obj.kuukausi == "09":
                        tulos.kk9hinta += float(hintaobj.tuntihinta) * float(obj.tuntikulutus)
                    elif obj.kuukausi == "10":
                        tulos.kk10hinta += float(hintaobj.tuntihinta) * float(obj.tuntikulutus)
                    elif obj.kuukausi == "11":
                        tulos.kk11hinta += float(hintaobj.tuntihinta) * float(obj.tuntikulutus)
                    elif obj.kuukausi == "12":
                        tulos.kk12hinta += float(hintaobj.tuntihinta) * float(obj.tuntikulutus)
    tulokset.append(tulos)
    return tulokset

def tulostaTulokset(tulokset):
    x = input("Laske kiinteällä hinnalla? k/e: ")
    if x == "k":
        a = input("Syötä kiinteä hinta käyttäen pistettä (snt/kWh): ")
        print()
        print("Tammikuu kulutus: " + str(round((tulokset[0].kk1), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk1) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk1hinta / 100), 2)) + "€")
        print("Helmikuu kulutus: " + str(round((tulokset[0].kk2), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk2) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk2hinta / 100), 2)) + "€")
        print("Maaliskuu kulutus: " + str(round((tulokset[0].kk3), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk3) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk3hinta / 100), 2)) + "€")
        print("Huhtikuu kulutus: " + str(round((tulokset[0].kk4), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk4) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk4hinta / 100), 2)) + "€")
        print("Toukokuu kulutus: " + str(round((tulokset[0].kk5), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk5) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk5hinta / 100), 2)) + "€")
        print("Kesäkuu kulutus: " + str(round((tulokset[0].kk6), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk6) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk6hinta / 100), 2)) + "€")
        print("Heinäkuu kulutus: " + str(round((tulokset[0].kk7), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk7) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk7hinta / 100), 2)) + "€")
        print("Elokuu kulutus: " + str(round((tulokset[0].kk8), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk8) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk8hinta / 100), 2)) + "€")
        print("Syyskuu kulutus: " + str(round((tulokset[0].kk9), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk9) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk9hinta / 100), 2)) + "€")
        print("Lokakuu kulutus: " + str(round((tulokset[0].kk10), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk10) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk10hinta / 100), 2)) + "€")
        print("Marrakuu kulutus: " + str(round((tulokset[0].kk11), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk11) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk11hinta / 100), 2)) + "€")
        print("Joulukuu kulutus: " + str(round((tulokset[0].kk12), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk12) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk12hinta / 100), 2)) + "€\n")
        print("Kokonaiskulutus: " + str(round((tulokset[0].vuosikulutus), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].vuosikulutus) * float(a)) / 100), 2)) + "€, ja pörssisähköllä: " + str(round((tulokset[0].vuosihintaporssi / 100), 2)) + "€")
        print()
    else:
        print("\nKokonaiskulutus: " + str(round((tulokset[0].vuosikulutus), 2)) + "kWh, pörssisähköllä: " + str(round((tulokset[0].vuosihintaporssi / 100), 2)) + "€\n")
        print("Tammikuun kulutus: " + str(round((tulokset[0].kk1), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk1hinta / 100), 2)) + "€")
        print("Helmikuu kulutus: " + str(round((tulokset[0].kk2), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk2hinta / 100), 2)) + "€")
        print("Maaliskuu kulutus: " + str(round((tulokset[0].kk3), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk3hinta / 100), 2)) + "€")
        print("Huhtikuu kulutus: " + str(round((tulokset[0].kk4), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk4hinta / 100), 2)) + "€")
        print("Toukokuu kulutus: " + str(round((tulokset[0].kk5), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk5hinta / 100), 2)) + "€")
        print("Kesäkuu kulutus: " + str(round((tulokset[0].kk6), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk6hinta / 100), 2)) + "€")
        print("Heinäkuu kulutus: " + str(round((tulokset[0].kk7), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk7hinta / 100), 2)) + "€")
        print("Elokuu kulutus: " + str(round((tulokset[0].kk8), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk8hinta / 100), 2)) + "€")
        print("Syyskuu kulutus: " + str(round((tulokset[0].kk9), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk9hinta / 100), 2)) + "€")
        print("Lokakuu kulutus: " + str(round((tulokset[0].kk10), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk10hinta / 100), 2)) + "€")
        print("Marrakuus kulutus: " + str(round((tulokset[0].kk11), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk11hinta / 100), 2)) + "€")
        print("Joulukuu kulutus: " + str(round((tulokset[0].kk12), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk12hinta / 100), 2)) + "€")
        print()
    return None

def kirjoita(tulokset):
    tiedosto = open("tulokset.txt", 'w', encoding="utf-8")
    x = input("Laske kiinteällä hinnalla? k/e: ")
    if x == "k":
        a = input("Syötä kiinteä hinta käyttäen pistettä (snt/kWh): ")
        tiedosto.write("Kiinteä hinta: " + str(a) + "snt/kWh\n\n")
        tiedosto.write("Tammikuu kulutus: " + str(round((tulokset[0].kk1), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk1) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk1hinta / 100), 2)) + "€\n")
        tiedosto.write("Helmikuu kulutus: " + str(round((tulokset[0].kk2), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk2) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk2hinta / 100), 2)) + "€\n")
        tiedosto.write("Maaliskuu kulutus: " + str(round((tulokset[0].kk3), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk3) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk3hinta / 100), 2)) + "€\n")
        tiedosto.write("Huhtikuu kulutus: " + str(round((tulokset[0].kk4), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk4) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk4hinta / 100), 2)) + "€\n")
        tiedosto.write("Toukokuu kulutus: " + str(round((tulokset[0].kk5), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk5) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk5hinta / 100), 2)) + "€\n")
        tiedosto.write("Kesäkuu kulutus: " + str(round((tulokset[0].kk6), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk6) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk6hinta / 100), 2)) + "€\n")
        tiedosto.write("Heinäkuu kulutus: " + str(round((tulokset[0].kk7), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk7) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk7hinta / 100), 2)) + "€\n")
        tiedosto.write("Elokuu kulutus: " + str(round((tulokset[0].kk8), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk8) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk8hinta / 100), 2)) + "€\n")
        tiedosto.write("Syyskuu kulutus: " + str(round((tulokset[0].kk9), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk9) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk9hinta / 100), 2)) + "€\n")
        tiedosto.write("Lokakuu kulutus: " + str(round((tulokset[0].kk10), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk10) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk10hinta / 100), 2)) + "€\n")
        tiedosto.write("Marrakuu kulutus: " + str(round((tulokset[0].kk11), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk11) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk11hinta / 100), 2)) + "€\n")
        tiedosto.write("Joulukuu kulutus: " + str(round((tulokset[0].kk12), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].kk12) * float(a)) / 100), 2)) + "€, pörssisähköllä: " + str(round((tulokset[0].kk12hinta / 100), 2)) + "€\n\n")
        tiedosto.write("Kokonaiskulutus: " + str(round((tulokset[0].vuosikulutus), 2)) + "kWh, kiinteällä sopimuksella: " + str(round((((tulokset[0].vuosikulutus) * float(a)) / 100), 2)) + "€, ja pörssisähköllä: " + str(round((tulokset[0].vuosihintaporssi / 100), 2)) + "€\n")
        tiedosto.close()
    else:
        tiedosto.write("\nKokonaiskulutus: " + str(round((tulokset[0].vuosikulutus), 2)) + "kWh, pörssisähköllä: " + str(round((tulokset[0].vuosihintaporssi / 100), 2)) + "€\n")
        tiedosto.write("Tammikuun kulutus: " + str(round((tulokset[0].kk1), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk1hinta / 100), 2)) + "€\n")
        tiedosto.write("Helmikuu kulutus: " + str(round((tulokset[0].kk2), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk2hinta / 100), 2)) + "€\n")
        tiedosto.write("Maaliskuu kulutus: " + str(round((tulokset[0].kk3), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk3hinta / 100), 2)) + "€\n")
        tiedosto.write("Huhtikuu kulutus: " + str(round((tulokset[0].kk4), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk4hinta / 100), 2)) + "€\n")
        tiedosto.write("Toukokuu kulutus: " + str(round((tulokset[0].kk5), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk5hinta / 100), 2)) + "€\n")
        tiedosto.write("Kesäkuu kulutus: " + str(round((tulokset[0].kk6), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk6hinta / 100), 2)) + "€\n")
        tiedosto.write("Heinäkuu kulutus: " + str(round((tulokset[0].kk7), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk7hinta / 100), 2)) + "€\n")
        tiedosto.write("Elokuu kulutus: " + str(round((tulokset[0].kk8), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk8hinta / 100), 2)) + "€\n")
        tiedosto.write("Syyskuu kulutus: " + str(round((tulokset[0].kk9), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk9hinta / 100), 2)) + "€\n")
        tiedosto.write("Lokakuu kulutus: " + str(round((tulokset[0].kk10), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk10hinta / 100), 2)) + "€\n")
        tiedosto.write("Marrakuus kulutus: " + str(round((tulokset[0].kk11), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk11hinta / 100), 2)) + "€\n")
        tiedosto.write("Joulukuu kulutus: " + str(round((tulokset[0].kk12), 2)) + "kWh" + ", pörssisähköllä: " + str(round((tulokset[0].kk12hinta / 100), 2)) + "€\n\n")
        tiedosto.close()


def ohjelma():
    x = input("Syötä kulutustiedoston nimi (sisältäen tiedostopäätteen .csv): ")
    y = input("Syötä hintatiedoston nimi (sisältäen tiedostopäätteen .csv): ")
    objektiLista = lueKulutusTiedosto(x)
    hinnasto = lueHinnat(y)
    tulokset = analysoi(objektiLista, hinnasto)
    tulostaTulokset(tulokset)
    z = input("Haluatko kirjoittaa tulokset tekstitiedostoon? k/e: ")
    if z == 'k':
        kirjoita(tulokset)
    print("Kiitos ohjelman käytöstä.")

    return None

ohjelma()