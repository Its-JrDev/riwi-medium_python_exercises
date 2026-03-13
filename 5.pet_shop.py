products = {
    1: ("Dog food bag (4kg)", 20000),
    2: ("Cat food bag (2kg)", 15000),
    3: ("Rabbit food bag (1kg)", 5000)
}

print("Welcome to J. Pets Store.")
print("\nWe currently offer the following products for pets:")

for key, (name, price) in products.items():
    print(f"{key}. {name}: ${price:,} pesos")

while True:
    pet_type = input("\nWhich type of pet are you buying for? (Dog, Cat, Rabbit): ").strip().lower()
    if pet_type == "dog":
        print("\nYou have selected products for dogs.")
        print(f'\nWe offer the following product for dogs: {products[1][0]} at ${products[1][1]:,} pesos.')
        break
    elif pet_type == "cat":
        print("\nYou have selected products for cats.")
        print(f'\nWe offer the following product for cats: {products[2][0]} at ${products[2][1]:,} pesos.')
        break
    elif pet_type == "rabbit":
        print("\nYou have selected products for rabbits.")
        print(f'\nWe offer the following product for rabbits: {products[3][0]} at ${products[3][1]:,} pesos.')
        break
    else:
        print("\nError: Invalid pet type. Please choose Dog, Cat, or Rabbit.")