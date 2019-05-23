
# Test if is assign the value or just a reference

a = [1, 2, 3]   # vytvoření seznamu
b = a           # tady se nový seznam nevytváří

# seznam vytvořený v prvním řádku má teď dvě jména: "a" a "b",
# ale stále pracujeme jenom s jedním seznamem

print(b)
a.append(4)
print(b)

# pokus dve mazani
cisla = [1, 2, 3, 4]
cisla[1:-1] = [0, 0, 0, 0, 0, 0]
print(cisla)
cisla[1:-1] = []
print(cisla)


cisla = [1, 2, 3, 4, 5, 6]
del cisla[-1]
print(cisla)
del cisla[3:5]
print(cisla)
del cisla

#operace se seznamy
melodie = ['C', 'E', 'G'] * 2 + ['E', 'E', 'D', 'E', 'F', 'D'] * 2 + ['E', 'D', 'C']
print(melodie)


#ukol
zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

def oprav_zaznamy(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        vysledek.append(jmeno.capitalize() + ' ' + prijmeni.capitalize())
    return vysledek

opravene_zaznamy = oprav_zaznamy(zaznamy)
print(opravene_zaznamy)

def vytvor_tabulku(velikost=11):
    seznam_radku = []
    for a in range(velikost):
        radek = []
        for b in range(velikost):
            radek.append(a * b)
        seznam_radku.append(radek)
    return seznam_radku

nasobilka = vytvor_tabulku()

print(nasobilka[2][3])  # dva krát tři
print(nasobilka[5][2])  # pět krát dva
print(nasobilka[8][7])  # osm krát sedm

# Vypsání celé tabulky
for radek in nasobilka:
    for cislo in radek:
        print(cislo, end=' ')
        print()