import json
import logging


#logeris
def create_logger(logger_name, log_file):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

mano_logeris = create_logger("mano_logeris", 'logeris.log')





# Užduotis - funkijų išnaudojimas basic projekte
with open('saldytuvas.json', 'r+', encoding='utf-8') as data:
    saldytuvas = json.load(data)
    mano_logeris.info("loaded saldytuvas.json")

receptai = {}

def remove_product(name, quantity=1):
    if name in saldytuvas.keys():
        if saldytuvas[name][0] > quantity:
         saldytuvas[name][0] -= quantity
        else:
         saldytuvas.pop(name)
        
        with open("saldytuvas.json", "w", encoding="utf-8") as json_file:
            json.dump(saldytuvas, json_file)
            mano_logeris.info(f"removed from saldytuvas.json, {name}")

def add_product(product_name, unit='kg', quantity=1):
    # quantity = float(input("Įveskite kiekį: "))
    # unit = input("unit: ")
    if unit == "kg":
        quantity *= 1  # convert kg to g

    if product_name in saldytuvas: 
     saldytuvas[product_name][0] += quantity

    else:
     saldytuvas[product_name] = [quantity, unit]

    with open("saldytuvas.json", "w", encoding="utf-8") as json_file:
            json.dump(saldytuvas, json_file)
            mano_logeris.info(f"added to saldytuvas.json, {name}")

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

def ar_iseina(saldytuvas):
    ivestas_receptas = str(input("Iveskite recepta formatu - Ingridientas : kiekis: "))
    porcijos = int(input("Iveskite porciju kieki: "))
    produktu_sarasas = ivestas_receptas.split(",")
    receptas = {}
    pirkiniu_sarasas = {}
    for produktas in produktu_sarasas:
        # receptas{produktas}
        pavadinimas, kiekis = produktas.split(":")
        pavadinimas = pavadinimas.strip()
        receptas[pavadinimas] = float(kiekis)
    if pavadinimas in saldytuvas:
        for ingridiantas, kiekis in receptas.items():
            if ingridiantas in saldytuvas:
                if saldytuvas[ingridiantas][0] < kiekis * porcijos:
                    pirkiniu_sarasas[ingridiantas] = (kiekis * porcijos)
                else:
                    print(f"{ingridiantas} = {kiekis * porcijos} Užtenka pagaminti {porcijos}")
                    #saldytuvas[ingridiantas][0] -= kiekis * porcijos
                    remove_product(ingridiantas, (kiekis * porcijos))  
        print(f"Pirkinius sarašas: {pirkiniu_sarasas}")    
    else:
        print(f"{pavadinimas} Nėra šaldytuve. Trūksta {float(kiekis)}")
            
while True:
    print("""
    1- prideti produkta
    2- isimti produkta
    3- apziureti produktus saldytuve
    4- ar iseina

    0- iseiti
    
    """)
    try:
        choice = int(input("pasirinkite funkcija: "))
    except Exception as e:
            mano_logeris.info(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
            print(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
            pass
    else:
        if choice == 1:
            try:
                name = input("produkto pavadinimas: ")
                unit = input("unit: ")
                quantity = float(input("Įveskite kiekį: "))
                add_product(name, unit, quantity)
            except Exception as e:
                mano_logeris.info(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
                print(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
                pass

        elif choice == 2:
            try:
                name = input("iveskite produkto pavadinima: ")
                remove_product(name)
            except Exception as e:
                mano_logeris.info(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
                print(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
                pass
            else:
                print(saldytuvas)
            

        elif choice == 3:
            try:
                view_product()
                total_mass()
            except Exception as e:
                mano_logeris.info(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
                print(f"Klaida: {e.__class__.__name__}, {e.with_traceback(None)}")
                pass


        elif choice == 4:
            ar_iseina(saldytuvas)

        elif choice == 0:
            print("Viso gero")
            mano_logeris.info('Exit')
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