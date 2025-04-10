# Ice cream shop Application
# Author: Hamza Yusuf

# our menu items
flavors = ["vanilla", "carmel", "cookies n cream", "strawberry", "mint chocolate", "chocolate"]
toppings = ["cherries", "syrup", "whipping cream"]
cones = ["cake cone", "sugar cone", "waffle cone"]
prices = {"scoop": 2.50, "toppings": 0.50}

# display menu
def display_menu():
    print("\n=== Welcome to the ice cream shop! ===")
    print("\nAvailable Flavors:")
    for flavor in flavors:
        print(f" - {flavor}")
    
    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f" - {topping}")
    
    print("\nAvailable Cone Types:")
    for cone in cones:
        print(f" - {cone}")

    print("\nPrices")
    print(f"Scoops: ${prices['scoop']:.2f} each")
    print(f"Toppings: ${prices['toppings']:.2f} each")  

# search for a flavor to check if we have it in stock
def search_flavor():
    favorite_flavor = input("\nEnter the flavor you're looking for: ").lower()
    if favorite_flavor in [f.lower() for f in flavors]:
        print(f"{favorite_flavor.title()} is available!")
    else:
        print(f"Sorry, {favorite_flavor.title()} is not available.")

# get flavors
def get_flavors():
    chosen_flavors = []
    while True:
        try:
            num_scoops = int(input("\nHow many scoops would you like? (1-3): "))
            if 1 <= num_scoops <= 3:  
                break
            print("Please choose between 1 and 3 scoops.")
        except ValueError:
            print("Please enter a valid number.")
    
    print("\nFor each scoop, enter the flavor you like:")
    for i in range(num_scoops):
        while True:
            flavor = input(f"Scoop {i+1}: ").lower()
            if flavor in [f.lower() for f in flavors]:
                chosen_flavors.append(flavor)
                break
            print("Sorry, that flavor is not available.")
    
    return num_scoops, chosen_flavors

# get cone
def get_cone():
    while True:
        cone = input("\nEnter your cone type (cake cone, sugar cone, or waffle cone): ").lower()
        if cone in [c.lower() for c in cones]:
            return cone
        print("Sorry, that cone type is not currently available. Please enter a valid cone type.")

# get toppings
def get_toppings():
    chosen_toppings = []
    while True:
        topping = input("\nEnter a topping (or type 'done' if finished): ").lower()
        if topping == "done":
            break
        if topping in [t.lower() for t in toppings]:
            chosen_toppings.append(topping)
            print(f"Added {topping}")
        else:
            print("Sorry, that topping isn't available.")
    return chosen_toppings  

# calculate total and discount if the total is over 10
def calculate_total(num_scoops, num_toppings):
    scoops_cost = num_scoops * prices["scoop"]
    topping_cost = num_toppings * prices["toppings"]
    subtotal = scoops_cost + topping_cost

    discount = 0
    if subtotal > 10:
        discount = subtotal * 0.10

    total = subtotal - discount
    return total, discount

# print receipt, made sure the order was correct in order for it to work had syntax problems
def print_receipt(num_scoops, chosen_flavors, chosen_toppings, cone_choice, total, discount):
    print("\n=== Your ice cream order ===")
    for i in range(num_scoops):
        print(f"Scoop{i+1}: {chosen_flavors[i].title()}")

    print(f"\nCone: {cone_choice.title()}")

    if chosen_toppings:
        print("\nToppings")
        for topping in chosen_toppings:
            print(f"- {topping.title()}")

    if discount > 0:
        print(f"\nDiscount applied: -${discount:.2f}")

    print(f"\nTotal: ${total:.2f}")

    with open("daily_orders.txt", "a") as file:
        file.write(f"\nOrder: {num_scoops} scoops, Cone: {cone_choice.title()} - Total: ${total:.2f}")


# main
def main():
    display_menu()
    search_flavor()
    num_scoops, chosen_flavors = get_flavors()
    chosen_toppings = get_toppings()
    cone_choice = get_cone()
    total, discount = calculate_total(num_scoops, len(chosen_toppings)) # list of toppings 
    print_receipt(num_scoops, chosen_flavors, chosen_toppings, cone_choice, total, discount)
# make sure order was correct here
if __name__ == "__main__":
    main()
