saldytuvas = {}


def remove_product():
    pass

def add_product(product_name, product_type, quantity=1):
    product_name = input("Įveskite produkto pavadinimą: ")
    quantity = float(input("Įveskite kiekį: "))
    saldytuvas[product_name] = quantity
    print("Produktas sėkmingai pridėtas į šaldytuvą!\n")

def view_product():
    pass


while True:
    print("""
    1- prideti produkta
    2- isimti produkta
    3- apziureti produktus saldytuve

    0- iseiti
    
    """)
    choice = int(input("pasirinkite funkcija: "))

    if choice == 1:
        name = input("produkto pavadinimas: ")
        tipas = input("ar produktas yra skaiciuojamas litrais ?: ")
        kiekis = int(input("kiekis idedamas i saldytuva: "))
        
        
        if tipas.lower() == "taip":
            tipas = True
        else:
            tipas = False

        add_product(name, tipas)

        

    elif choice == 2:
        pass

    elif choice == 3:
        pass

    elif choice == 0:
        print("Viso gero")
        break
    else:
        print('invalid Choice')
        
    saldytuvas = {"morkos" : 3, "burokai" : 2, "bananai" : 5, "bulves:" : 7, "pienas" : 1, "apelsinai" : 2}
        for morkos, 3 in saldytuvas.items():
        print(morkos, 3)