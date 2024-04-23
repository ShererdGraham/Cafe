# Create menu list to store menu items
menu = ["Tea", "Juice", "Fried Egg", "Bacon", "Toast"]

# Create dictionaries to store amount and cost of each item
stock = {"Tea": 4, 
         "Juice": 6,
         "Fried Egg": 2, 
         "Bacon": 3, 
         "Toast": 5
        }
price = {"Tea": 2, 
         "Juice": 3,
         "Fried Egg": 2, 
         "Bacon": 3,
         "Toast": 1
        }

print(
'''Welcome to the Coding Cafe
Here's our menu\n''')


while(True):
    
    total_stock_value = 0
    # Loop through menu to get number and cost of each item and print each one
    for item in menu:       
        print(f"{item}: £{price[item]}... only {stock[item]} left!")
        
        # Create total stock value by summing the multiple the amount of each item and its price
        total_stock_value += stock[item] * price[item]

    # Print the total value of the stock
    print(f"\nAnd if you want to buy it all, it'll be £{total_stock_value}!")


    item_picked = input("What item would you like? Type done when your order is finished\n")        
    cost_of_order = 0
    for item in menu:    
        if item == item_picked:
            cost_of_order += price[item]
            stock[item] -= 1
    if item_picked == "done":
        break

    print(f"That will be £{cost_of_order}\n")

