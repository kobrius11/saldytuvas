# Užduotis - funkijų išnaudojimas basic projekte
saldytuvas = {'spageciai': [1, "kg"], 'pomidoru padazas': [1, "kg"], 'suris': [1, "kg"]}
receptai = {
    "Spageciai su suriu": {'spageciai': 1, 'pomidoru padazas': 1, 'suris': 1}, \
    "sumustinis": {"batonas": 1, "sviestas": 1, "suris": 1}, \
    'blynai': {'kiausinis': 2,'pienas' : 0.5 , 'miltai': 1}
}

def remove_product(name, quantity=1):
    

    if name in saldytuvas.keys():
        if saldytuvas[name][0] > quantity:
            saldytuvas[name][0] -= quantity

        else:
            saldytuvas.pop(name)
        return

def add_product(product_name, unit='kg', quantity=1):
    # quantity = float(input("Įveskite kiekį: "))
    # unit = input("unit: ")
    if unit == "kg":
        quantity *= 1  # convert kg to g

    if product_name in saldytuvas: 
        saldytuvas[product_name][0] += quantity

    else:
        saldytuvas[product_name] = [quantity, unit]

    print("Produktas sėkmingai pridėtas į šaldytuvą!\n")
    print(saldytuvas)

def view_product():

    for key, value in saldytuvas.items():
        print(key, value)

def total_mass():
    total_kg = 0
    total_l = 0
    total_vienetas = 0

    for value in saldytuvas.values():

        if value[1] == 'kg':
            total_kg += value[0]

        elif value[1] == 'l':
            total_l += value[0]

        else:
            total_vienetas += value[0]

    print("Bendra produktų masė: {:.2f} kg ir {:.2f} l, {} vienetai".format(total_kg/1, total_l, total_vienetas))

def ar_iseina():
    for count, key in enumerate(receptai.keys()):
        print(f'Nr: {count} - {key}')
    print('\n')
    x = int(input("kuri nr norite gaminti?: "))
    pasirinkimas = list(receptai)[x]
    print("\n")

    for key, val in receptai[pasirinkimas].items():

            if key in saldytuvas and val <= saldytuvas[key][0]:
                kartai = saldytuvas[key][0] / val
                print(f'sito produkto {key} uztenka, pagaminti {pasirinkimas} recepta, {kartai} kartu\n')

            else:
                kartai = 0
                print(f'sito produkto {key} neuztenka, pagaminti {pasirinkimas} recepta\n')
        
    choice = input(f"ar norite gaminti, patiekala? {pasirinkimas}: ")

    if choice.lower() == "taip" and kartai > 0:

            for key, val in receptai[pasirinkimas].items():
                remove_product(key, val)
                #saldytuvas[key][0] -= val
            add_product(pasirinkimas, unit="porcija", quantity=1)

    else:
        print('\nnegalima pagaminti produkto :(')

            
        




            
while True:
    print("""
    1- prideti produkta
    2- isimti produkta
    3- apziureti produktus saldytuve
    4- ar iseina

    0- iseiti
    
    """)
    choice = int(input("pasirinkite funkcija: "))

    if choice == 1:
        name = input("produkto pavadinimas: ")
        unit = input("unit: ")
        quantity = float(input("Įveskite kiekį: "))
        add_product(name, unit, quantity)

    elif choice == 2:
        name = input("iveskite produkto pavadinima: ")
        print(saldytuvas)
        remove_product(name)
        print(saldytuvas)

    elif choice == 3:
        view_product()
        total_mass()

    elif choice == 4:
        ar_iseina()

    elif choice == 0:
        print("Viso gero")
        break

    else:
        print('')
        
# galiu paaiškinti, ką reiškia kai kurių kodinio pavyzdžio eilučių kodas:

# Eilutėje 1 yra sukurtas žodynas (dictionary) "saldytuvas", kuriame saugoma informacija apie produktų kiekius ir vienetus.
# Eilutėje 2 yra sukurtas žodynas "receptai", kuriame saugoma informacija apie receptus ir reikalingus produktų kiekius.
# Eilutėje 5 pradedama "remove_product()" funkcija, skirta ištrinti produktą iš saldytuvo.
# Eilutėje 15 pradedama "add_product()" funkcija, skirta pridėti produktą į saldytuvą.
# Eilutėje 23 pradedama "view_product()" funkcija, skirta peržiūrėti produktus, esančius saldytuve.
# Eilutėje 34 pradedama "total_mass()" funkcija, skirta apskaičiuoti bendrą produktų masę, esančią saldytuve.
# Eilutėje 43 pradedama "ar_iseina()" funkcija, skirta patikrinti, ar galima pagaminti pasirinktą receptą iš produktų, esančių saldytuve.
# Eilutėje 50-61 yra meniu, kuriame vartotojas gali pasirinkti, kokią funkciją vykdyti.
# Eilutėje 63 programa baigiasi.