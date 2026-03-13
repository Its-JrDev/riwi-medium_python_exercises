clients = 5

count_vanilla = 0
count_chocolate = 0
count_strawberry = 0

def get_flavour():
    flavour = input("\nEnter ice cream flavour: ").strip().lower()
    if flavour == "vanilla":
        print('You chose vanilla flavour')
    elif flavour == "chocolate":
        print('You chose chocolate flavour')
    elif flavour == "strawberry":
        print('You chose strawberry flavour')
    else:
        print('Error: invalid flavour')
        return get_flavour()
    return flavour

for i in range(clients):
    print('----Ice Cream Shop Flavours----')
    print(f'Client {i + 1}')
    print('\nAvailable flavours: \nVanilla | Chocolate | Strawberry')
    flavour = get_flavour()
    
    if flavour == "vanilla":
        count_vanilla += 1
    elif flavour == "chocolate":  
        count_chocolate += 1
    elif flavour == "strawberry":
        count_strawberry += 1

print('\nTotal flavours chosen:')
print(f'Vanilla: {count_vanilla}')
print(f'Chocolate: {count_chocolate}')
print(f'Strawberry: {count_strawberry}')