saldytuvas = {}


def remove_product(name):
    if name in saldytuvas.keys():
     istrinti = saldytuvas.pop(name)
     liko = istrinti - 1
     return liko

def add_product(product_name, product_type, quantity=1):
    
    quantity = float(input("Įveskite kiekį: "))
    saldytuvas[product_name] = [quantity, product_type]
    print("Produktas sėkmingai pridėtas į šaldytuvą!\n")
    print(saldytuvas)

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
        