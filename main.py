saldytuvas = {}



def remove_product():
    name = input('iveskite produkta: ')
    if name in saldytuvas.keys():
        if saldytuvas[name] > 1:
            istrinti = saldytuvas.get(name)
            saldytuvas[name] = istrinti - 1
        else:
            saldytuvas.pop(name)
        return 

def add_product(product_name, quantity=1):
    
    quantity = float(input("Įveskite kiekį: "))
    saldytuvas[product_name] = quantity
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
        
        
        
        

        add_product(name)

        

    elif choice == 2:
        
        print(saldytuvas)
        remove_product()
        print(saldytuvas)

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