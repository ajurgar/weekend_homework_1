def get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]

def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]

def add_or_remove_cash(total_petshop, cash):
    total_petshop["admin"]["total_cash"] += cash

def get_pets_sold(pets):
    return pets["admin"]["pets_sold"]

def increase_pets_sold(pets, pets_sold):
    pets["admin"]["pets_sold"] = pets_sold
    return pets

def get_stock_count(pets_stock):
    return len(pets_stock["pets"])

def get_pets_by_breed(pets, breed):
    total_pets = []
    for pet in pets["pets"]:
        if pet["breed"] == breed:

            total_pets.append(pet)
    return total_pets

def find_pet_by_name(pets, name):
    for pet in pets["pets"]:
        if pet["name"] == name:
            return pet

# for every individual pet in the list of pets
# the pet_name (that we dropped "Arthur") and so we are askin the function

def find_pet_by_name(pets, name):
    for pet in pets["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(list,pet_name):
    for individualpet in list["pets"]:
        if individualpet["name"] == pet_name:
            return list["pets"].remove(individualpet)


def add_pet_to_stock(shop_count, pet_name):
    shop_count['pets'].append(pet_name)

def get_customer_cash(name):
    return name["cash"]

def remove_customer_cash(total_left, cash):
   total_left["cash"] -= cash

def get_customer_pet_count(pet_count):
    return len(pet_count["pets"])
   

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)