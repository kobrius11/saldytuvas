saldytuvas = {}

def remove_product():
    name = input('Įveskite produkto pavadinimą: ')

    if name in saldytuvas.keys():
        if saldytuvas[name][0] > 1:
            saldytuvas[name][0] -= 1
        else:
            saldytuvas.pop(name)

def add_product(product_name):
    quantity = float(input("Įveskite kiekį: "))
    unit = input("vienetai: ")

    if unit == "kg":
        quantity *= 1000  # convert kg to g

    if product_name in saldytuvas: 
        saldytuvas[product_name] += [quantity, unit]
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
            total_kg += value[0] / 1000  # convert g to kg
        elif value[1] == 'l':
            total_l += value[0]
        else:
            total_vienetas += value[0]

    print("Bendra produktų masė: {:.2f} kg ir {:.2f} l, {} vienetai".format(total_kg, total_l, total_vienetas))

while True:
    print("""
    1 - Pridėti produktą
    2 - Išimti produktą
    3 - Apžiūrėti produktus šaldytuve

    0 - Išeiti
    """)

    choice = int(input("Pasirinkite funkciją: "))

    if choice == 1:
        name = input("Produkto pavadinimas: ")
        add_product(name)

    elif choice == 2:
        print(saldytuvas)
        remove_product()
        print(saldytuvas)

    elif choice == 3:
        view_product()
        total_mass()

    elif choice == 0:
        print("Viso gero")
        break

    else:
        print('Neteisingas pasirinkimas.')
