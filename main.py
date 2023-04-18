saldytuvas = {}


def remove_product():
    pass

def add_product():
    product_name = input("Įveskite produkto pavadinimą: ")
    quantity = float(input("Įveskite kiekį: "))
    saldytuvas[product_name] = quantity
    print("Produktas sėkmingai pridėtas į šaldytuvą!\n")

def view_product():
    pass
