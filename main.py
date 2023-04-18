
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


def add_product(product_name, unit):
    quantity = float(input("Įveskite kiekį: "))
    if product_name in saldytuvas: 
        saldytuvas[product_name] += quantity
    else:
        saldytuvas[product_name] = quantity
    print("Produktas sėkmingai pridėtas į šaldytuvą!\n")
    print(saldytuvas)

def view_product():
    for key, value in saldytuvas.items():
        print( key, value)


def total_mass():
    total_kg = 0
    total_l = 0
    for key, value in saldytuvas.items():
        if key in ["morkos", "burokai", "bulves"]:
            total_kg += value
        elif key in ["pienas"]:
            total_l += value
        elif key in ["bananai", "apelsinai"]:
            total_kg += value * 0.5  # assuming an average weight of 0.5 kg per fruit
    print("Bendra produktų masė: {:.2f} kg ir {:.2f} l".format(total_kg/1, total_l))


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
        view_product()

    elif choice == 0:
        print("Viso gero")
        break
    else:
        print('invalid Choice')
        