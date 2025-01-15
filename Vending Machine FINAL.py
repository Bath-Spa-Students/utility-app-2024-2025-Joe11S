print("""
Welcome to the vending machine.

""") #display title

#global variables are declared outside functions.

menu = {
    "Large Snacks (01 - 04)": {
        1 : {
            "Name" : "Doritos Cheese",
            "Price" : 8,
            "Stock" : 3
        },
        2 : {
            "Name" : "Doritos Spicy",
            "Price" : 8,
            "Stock" : 3
        },
        3 : {
            "Name" : "Cheetos Flamin' Hot",
            "Price" : 8,
            "Stock" : 3
        },
        4 : {
            "Name" : "Lays Salt",
            "Price" : 8,
            "Stock" : 3
        }
    },
    "Small Snacks (05 - 12)" : {
        5 : {
            "Name" : "Lays Spicy",
            "Price" : 3,
            "Stock" : 3
        },
        6 : {
            "Name" : "Lays Ketchup",
            "Price" : 3,
            "Stock" : 3
        },
        7 : {
            "Name" : "Maltesers",
            "Price" : 3,
            "Stock" : 3
        },
        8 : {
            "Name" : "Twix",
            "Price" : 3,
            "Stock" : 3
        },
        9 : {
            "Name" : "Snickers",
            "Price" : 3,
            "Stock" : 3
        },
        10 : {
            "Name" : "Toblerone",
            "Price" : 3,
            "Stock" : 3
        },
        11 : {
            "Name" : "Mars",
            "Price" : 3,
            "Stock" : 3
        },
        12 : {
            "Name" : "Bounty",
            "Price" : 3,
            "Stock" : 3
        }
    },
    "Bottles (13 - 17)" : {
        13 : {
            "Name" : "Masafi",
            "Price" : 1,
            "Stock" : 3
        },
        14 : {
            "Name" : "Masafi",
            "Price" : 1,
            "Stock" : 3
        },
        15 : {
            "Name" : "Masafi",
            "Price" : 1,
            "Stock" : 3
        },
        16 : {
            "Name" : "Pepsi",
            "Price" : 5,
            "Stock" : 3
        },
        17 : {
            "Name" : "Coca Cola",
            "Price" : 5,
            "Stock" : 3
        }
    },
    "Cans (18 - 25)" : {
        18 : {
            "Name" : "Coca Cola (Can)",
            "Price" : 3,
            "Stock" : 3
        },
        19 : {
            "Name" : "Pepsi (Can)",
            "Price" : 3,
            "Stock" : 3
        },
        20 : {
            "Name" : "Mountain Dew (Can)",
            "Price" : 3,
            "Stock" : 3
        },
        21 : {
            "Name" : "Fanta (Can)",
            "Price" : 3,
            "Stock" : 3
        },
        22 : {
            "Name" : "Sprite (Can)",
            "Price" : 3,
            "Stock" : 3
        },
        23 : {
            "Name" : "Pepsi (Can)",
            "Price" : 3,
            "Stock" : 3
        },
        24 : {
            "Name" : "Mango Rani Float (Can)",
            "Price" : 3,
            "Stock" : 3
        },
        25 : {
            "Name" : "Orange Rani Float (Can)",
            "Price" : 3,
            "Stock" : 3
        }
    }
}

purchase_history = [] #store purchase history of vending machine
cumulative_cost = 0 #store total profit throughout the life of the vending machine
user_ID = 0 #incremental. this variable defines the customer's ID.

admin_password = "123456" #change the value to change password.

def search_item_name(slot_no): #return item names
    if slot_no >= 1 and slot_no <5:
        return menu["Large Snacks (01 - 04)"][slot_no]["Name"]
    elif slot_no >= 5 and slot_no <13:
        return menu["Small Snacks (05 - 12)"][slot_no]["Name"]
    elif slot_no >= 13 and slot_no <18:
        return menu["Bottles (13 - 17)"][slot_no]["Name"]
    elif slot_no >= 18 and slot_no <26:
        return menu["Cans (18 - 25)"][slot_no]["Name"]

def search_item_cost(slot_no): #return item costs
    if slot_no >= 1 and slot_no <5:
        return menu["Large Snacks (01 - 04)"][slot_no]["Price"]
    elif slot_no >= 5 and slot_no <13:
        return menu["Small Snacks (05 - 12)"][slot_no]["Price"]
    elif slot_no >= 13 and slot_no <18:
        return menu["Bottles (13 - 17)"][slot_no]["Price"]
    elif slot_no >= 18 and slot_no <26:
        return menu["Cans (18 - 25)"][slot_no]["Price"]

def search_item_stock(slot_no): #return item stock
    if slot_no >= 1 and slot_no <5:
        return menu["Large Snacks (01 - 04)"][slot_no]["Stock"]
    elif slot_no >= 5 and slot_no <13:
        return menu["Small Snacks (05 - 12)"][slot_no]["Stock"]
    elif slot_no >= 13 and slot_no <18:
        return menu["Bottles (13 - 17)"][slot_no]["Stock"]
    elif slot_no >= 18 and slot_no <26:
        return menu["Cans (18 - 25)"][slot_no]["Stock"]

def purchase(): #perform purchases
    global user_balance
    global user_purchases
    global total_cost
    if user_balance >= final_cost:
        user_balance = user_balance - final_cost #deduct the item cost from user balance
        total_cost = total_cost + final_cost
        user_purchases = user_purchases + 1
        print("You have purchased", amount, item_name + "!")
        update_purchases(user_stock_input, amount)
        list()
    else:
        print("Purchase failed: Not enough change.")

def update_purchases(slot_no, amount): #update items after each purchase
    if slot_no >= 1 and slot_no <5:
        menu["Large Snacks (01 - 04)"][slot_no]["Stock"] = menu["Large Snacks (01 - 04)"][slot_no]["Stock"] - amount
    elif slot_no >= 5 and slot_no <13:
        menu["Small Snacks (05 - 12)"][slot_no]["Stock"] = menu["Small Snacks (05 - 12)"][slot_no]["Stock"] - amount
    elif slot_no >= 13 and slot_no <18:
        menu["Bottles (13 - 17)"][slot_no]["Stock"] = menu["Bottles (13 - 17)"][slot_no]["Stock"] - amount
    elif slot_no >= 18 and slot_no <26:
        menu["Cans (18 - 25)"][slot_no]["Stock"] = menu["Cans (18 - 25)"][slot_no]["Stock"] - amount

#these two functions compile two lists - the purchases and the purchase history.
def list():
    purchase_statement = str(user_purchases) + ": Item: " + item_name + ", Amount: " + str(amount) + ", Cost: " + str(final_cost) + " AED"
    purchase_list.append(purchase_statement)

def on_exit():
    global cumulative_cost
    history_prestatement = "Customer " + str(user_ID)
    cumulative_cost = cumulative_cost + total_cost
    purchase_history.append(history_prestatement)

    for l in purchase_list:
        purchase_history.append(l)
    
    history_poststatement = "Total Profit: " + str(total_cost)
    purchase_history.append(history_poststatement)

#The admin mode is a critical asset to the running of the vending machine, so it is password-protected.
def admin():
    
    def item_change(slot_no, new_item_name): #Change product name in the vending machine
        if slot_no >= 1 and slot_no <5:
            menu["Large Snacks (01 - 04)"][slot_no]["Name"] = new_item_name
        elif slot_no >= 5 and slot_no <13:
            menu["Small Snacks (05 - 12)"][slot_no]["Name"] = new_item_name
        elif slot_no >= 13 and slot_no <18:
            menu["Bottles (13 - 17)"][slot_no]["Name"] = new_item_name
        elif slot_no >= 18 and slot_no <26:
            menu["Cans (18 - 25)"][slot_no]["Name"] = new_item_name    
    
    def price_adjustment(slot_no, new_item_cost): #Adjust price in the vending machine.
        if slot_no >= 1 and slot_no <5:
            menu["Large Snacks (01 - 04)"][slot_no]["Price"] = new_item_cost
        elif slot_no >= 5 and slot_no <13:
            menu["Small Snacks (05 - 12)"][slot_no]["Price"] = new_item_cost
        elif slot_no >= 13 and slot_no <18:
            menu["Bottles (13 - 17)"][slot_no]["Price"] = new_item_cost
        elif slot_no >= 18 and slot_no <26:
            menu["Cans (18 - 25)"][slot_no]["Price"] = new_item_cost
    
    def restock(slot_no, restock_amount): #Restock items in the vending machine.
        if slot_no >= 1 and slot_no <5:
            menu["Large Snacks (01 - 04)"][slot_no]["Stock"] = menu["Large Snacks (01 - 04)"][slot_no]["Stock"] + restock_amount
        elif slot_no >= 5 and slot_no <13:
            menu["Small Snacks (05 - 12)"][slot_no]["Stock"] = menu["Small Snacks (05 - 12)"][slot_no]["Stock"] + restock_amount
        elif slot_no >= 13 and slot_no <18:
            menu["Bottles (13 - 17)"][slot_no]["Stock"] = menu["Bottles (13 - 17)"][slot_no]["Stock"] + restock_amount
        elif slot_no >= 18 and slot_no <26:
            menu["Cans (18 - 25)"][slot_no]["Stock"] = menu["Cans (18 - 25)"][slot_no]["Stock"] + restock_amount

    #driver code
    print("Enter your password: ") 
    p_input = input() #the admin is tasked to enter the password.
    if p_input == admin_password:
        print("Welcome to admin mode. Type item change to change item, price adjustment to adjust the price of each item, restock to restock items and purchase history to view purchases history. Press enter to exit admin mode.")
        admin_mode = input().lower() #input the mode

        if admin_mode == "item change": #Type item change to change the item names
            admin_stock_input = int(input("Enter the Slot Number to select item: ")) #search for item
            admin_item_name = search_item_name(admin_stock_input) #find item
            print(str(admin_stock_input) + ":", admin_item_name)
            print("Type your new item name.")

            new_item_name = input() #Type to change item name.

            item_change(admin_stock_input, new_item_name)
            print("Item name changed!")
            print(menu)


        elif admin_mode == "price adjustment": #Type price adjustment to change the item costs
            admin_stock_input = int(input("Enter the Slot Number to select item: ")) #search for item
            admin_item_name = search_item_name(admin_stock_input) #find item    
            admin_cost = search_item_cost(admin_stock_input) #find cost  
            print(str(admin_stock_input) + ":", admin_item_name + ". Cost:", admin_cost)
            print("Type your new item cost.")       

            new_item_cost = int(input()) #Type to change item cost.

            price_adjustment(admin_stock_input, new_item_cost)
            print("Item cost changed!")
            print(menu)

        elif admin_mode == "restock": #Type restock to restock items.
            admin_stock_input = int(input("Enter the Slot Number to select item: ")) #search for item
            admin_item_name = search_item_name(admin_stock_input) #find item    
            admin_stock = search_item_stock(admin_stock_input) #find cost  
            print(str(admin_stock_input) + ":", admin_item_name + ".", admin_stock, "Remaining.")
            print("Type the amount to restock.")       

            restock_amount = int(input()) #Type the amount to restock.

            restock(admin_stock_input, restock_amount)
            print("Item restocked!")
            print(menu)
        
        elif admin_mode == "purchase history": #Type purchase history to view purchase history.
            print(purchase_history)
            print("Total Cumulative Profit: ", cumulative_cost, "AED")
        
    else:
        print("Invalid Password!")

#By default, after pressing enter, the vending machine is in customer (user) mode, which is in the main vending machine file.

#driver code
for i in range(4294967296):

    #mode selection
    print("Press enter to run as customer or type exit to leave the vending machine. Type admin if you own the vending machine.")
    mode = input().lower()
    if mode == "exit": #if exit is typed in, the loop is broken and vending machine is exited.
        break
    #admin block
    elif mode == "admin": #if admin is typed in, admin mode begins
        admin()

    #using vending machine as customer is the default mode
    else:
        for j in range(4294967296):
            print("Press enter to confirm the next user. Type exit to exit to menu.")
            user_cancel = input().lower()
            
            #exit loop block
            if user_cancel == "exit": #If cancel is typed in, the loop is broken.
                break

            #continue from here            
            else:
                purchase_list = [] #clear purchase list per customer
                total_cost = 0 #clear total cost per customer
                user_purchases = 0 #clear user purchases per customer
                user_balance = float(input("Deposit your cash here: ")) #ask user to deposit cash                
                for purchase_iteration in range(4294967296):
                    print("Your change is", user_balance, "AED")
                    print("Press enter to proceed with your next purchase. Type finish to finish usage, release change and switch to next user.")
                    user_confirm = input().lower()
                    
                    #exit loop block
                    if user_confirm == "finish": #If done is typed in, the loop is broken.
                        user_ID = user_ID + 1 #increment user ID by 1 after each loop.
                        print("Thank you for using our vending machine. Your items purchased: ",  purchase_list, " Total cost is", total_cost, "AED, with a change of", user_balance, "AED.")
                        on_exit() #append to user history on exit
                        break
                    
                    #continue from here
                    print(menu) #display menu
                    user_stock_input = int(input("Enter the Slot Number to select item: ")) #search for item
                    item_name = search_item_name(user_stock_input) #find item
                    base_cost = search_item_cost(user_stock_input) #find cost
                    item_stock = search_item_stock(user_stock_input) #find stock
                    amount = int(input("Enter the amount of items to purchase: ")) #enter user amount
                    
                    final_cost =  base_cost * amount #display final cost
                    print("Do you want to purchase", str(amount), str(item_name), "worth", str(final_cost), "AED?", item_stock, "remaining. Press enter to purchase. Type cancel to cancel purchase.")
                    confirmation = input().lower()
                    
                    #type cancel to cancel purchase
                    if confirmation == "cancel":
                        print("Purchase cancelled.")
                    
                    else:
                        if item_stock > 0: #check for items in stock
                            if amount <= item_stock: #check if there are enough items in stock
                                purchase()
                            else: #if the amount is greater than the amount of stock, it purchases all
                                amount = item_stock
                                final_cost =  base_cost * amount
                                purchase()      
                        else:
                            print("Purchase failed: The item is currently out of stock.")
            j = 0 #this ensures infinite looping
    i = 0 #this ensures infinite looping