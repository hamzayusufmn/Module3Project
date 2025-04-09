# Ice cream shop Application
# Author: Hamza Yusuf

# our menu items
flavors = {"vanilla", "carmel", "cookies n cream", "strawberry","mint chocolate",  "chocolate"}
toppings = {"cherries", "syrup", "whipping cream"}
cones =  ["cake cone", "sugar cone", "waffle cone"]
prices = {"scoop": 2.50, "toppings": 0.50}  

# Function to display menu
def display_menu():
    """Shows available flavors and toppings to the customer"""
    print("\n=== Welcome to the ice cream shop! ===")
    print("\nAvailable Flavors:")
    for flavor in flavors:
        print(f" - {flavor}")
    
    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f" - {topping}")
    
    # Display prices
    print("\nPrices")
    print(f"Scoops: ${prices['scoop']:.2f} each")
    print(f"Toppings: ${prices['toppings']:.2f} each")  




def search_flavor():
    # this allows for user to look for flacor 
    favorite_flavor = input("\nEnter the flavor you're looking for: ").lower()
    if fav in [f.lower() for f in flavors]:
        print(f"{fav.title()} is available!")
    else:
        print(f"Sorry, {fav.title()} is not available.")


# Function to get flavors
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
            if flavor in flavors:
                chosen_flavors.append(flavor)
                break
            print("Sorry, that flavor is not available.")
    
    return num_scoops, chosen_flavors
def get_cone():
    
    while True:
        cone = input("\nEnter your cone type (cake cone, sugar cone, or waffle cone): ").lower()
        if cone in [c.lower() for c in cones]:
            return cone
        print("Sorry, that cone type is not available. Please enter a valid cone type.")



# Function to get toppings
def get_toppings():
    chosen_toppings = []
    while True:
        topping = input("\nEnter a topping (or type 'done' if finished): ").lower()
        if topping == "done":
            break
        if topping in toppings:
            chosen_toppings.append(topping)
            print(f"Added {topping}")
        else:
            print("Sorry, that topping isn't available.")
    return chosen_toppings  
# loop that asks user for topping and if they dont want they enter done also err handling for users who put in other items, wont accept untill they add correct topping

def calculate_total(num_scoops, num_toppings):
    scoops_cost = num_scoops * prices["scoop"]
    topping_cost = num_toppings * prices["toppings"]
    return scoops_cost + topping_cost
    discount = 0
    if subtotal > 10:
        discount = subtotal * 0.10
    total = subtotal - discount
    return total, discount

def print_receipt(num_scoops, chosen_flavors, chosen_toppings):
    print("\n=== Your ice cream order ===")
    for i in range(num_scoops):
        print(f"Scoop{i+1}: {chosen_flavors[i].title()}")
    
    if chosen_toppings:
        print("\nToppings")
        for topping in chosen_toppings:
            print(f"- {topping.title()}")
    
    total = calculate_total(num_scoops, len(chosen_toppings))
    print(f"\nTotal: ${total:.2f}")
    
    with open("daily_orders.txt", "a") as file:
        file.write(f"\nOrder: {num_scoops} scoops - ${total:.2f}")
        
# Main function
def main():
    display_menu()
    num_scoops, chosen_flavors = get_flavors()
    chosen_toppings = get_toppings()
    
    
    # display the receipts
    print_receipt(num_scoops, chosen_flavors, chosen_toppings)

if __name__ == "__main__":
    main()
