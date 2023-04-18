
saldytuvas = {"morkos": 3, "burokai": 2, "bananai": 5, "bulves": 7, "pienas": 1, "apelsinai": 2}


def remove_product():
    name = input('Įveskite produkto pavadinimą: ')
    if name in saldytuvas.keys():
        ###
        if saldytuvas[name].get("quantity") > 1:
            ###
            istrinti = saldytuvas.get(name).get("quantity")
            saldytuvas[name] = istrinti - 1
        else:
            saldytuvas.pop(name)
        return


def add_product(product_name, unit):
    quantity = float(input("Įveskite kiekį: "))
    if unit == "kg":
        quantity *= 1  # convert kg to g
    if product_name in saldytuvas:
        saldytuvas[product_name] += quantity
    else:
        saldytuvas[product_name] = {"quantity": quantity, "Type": product_type}
    print("Produktas sėkmingai pridėtas į šaldytuvą!\n")
    print(saldytuvas)

def view_product():
    for key, value in saldytuvas.items():
        print(key, value)

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
    print("Bendra produktų masė: {:.2f} kg ir {:.2f} l".format(total_kg/1000, total_l))

while True:
    print("""
    1- pridėti produktą
    2- išimti produktą
    3- apžiūrėti produktus šaldytuve
    4- peržiūrėti bendrą produktų masę

    0- išeiti

    """)
    choice = int(input("Pasirinkite funkciją: "))

    if choice == 1:
        name = input("Produkto pavadinimas: ")
        unit = input("Produkto matavimo vienetai (kg/l): ")
        add_product(name, unit)

    elif choice == 2:
        print(saldytuvas)
        remove_product()
        print(saldytuvas)

    elif choice == 3:
        view_product()

    elif choice == 4:
        total_mass()

    elif choice == 0:
        print("Viso gero")
        break
    else:
        print('Neteisingas pasirinkimas')
