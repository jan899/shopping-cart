# import all packages

from datetime import date
from datetime import datetime

# import dot-env and load the user name from the .env file 

import os
from dotenv import load_dotenv 

load_dotenv()

# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": "item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": "item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": "item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": "item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": "item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": "item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": "item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": "item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": "item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": "item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": "item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": "item"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": "item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": "item"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "item"},
    {"id":21, "name": "Bananas", "department": "grocery", "aisle": "fruit", "price": 0.79, "price_per": "pound"}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

price_by_pound = [p["id"] for p in products if p["price_per"] == "pound"]

# print(price_by_pound)

# TODO: write some Python code here to produce the desired output

# Explain to the user how to input identifiers

print("PLEASE INPUT ALL PRODUCT IDENTIFIERS ONE BY ONE. WHEN COMPLETE, PLEASE ENTER 'DONE'")
print("NOTE: IDENTIFIERS START AT 1")

# Get the user inputs and consolidate all of them into a list, until we're done
# use an infinite loop (while loop)

# empty lists for user products and amounts
user_products = []
# user_amounts = []

# loop through and populate the lists
while True:
    selected_id = input("Please input a product identifier: ")
    if selected_id.upper() == "DONE":
        break
    else:
        if int(selected_id) in price_by_pound:
            selected_amount = input("Please input an amount: ")
            user_products.append(
                {
                    "id":selected_id,
                    "amount":selected_amount,
                }
            )
            # user_products.append(int(selected_id))
            # user_amounts.append(int(selected_amount))
        else:
            user_products.append(
                {
                    "id":selected_id,
                    "amount":1,
                }
            )
            # user_products.append(int(selected_id))
            # user_amounts.append(int(1))
        # maybe display the selected product's name and price here/now

print("END OF USER INPUTS")
# print(user_products)
# print(user_amounts)

# Print the grocery store name & website

print("-------------------------------")
print("RECEIPT: FAST AND FURIOUS FOODS")
print("    www.f&ffamilyfoods.com")
print("-------------------------------")

#  The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM) 

now = datetime.now()
today = date.today()

current_time = now.strftime("%H:%M:%S")
print("CHECKOUT AT:", today, current_time)

# Set up empty list for consolidating prices

items_cost_list = []

# Perform product lookups to determine product's name and price

print("-------------------------------")
print("PRODUCTS PURCHASED:")
print("ITEM...UNITS...PRICE PER UNIT...TOTAL PRICE")
for s in user_products:
    matching_products = [p for p in products if p["id"] == int(s["id"])]
    for i in matching_products:
        print(">>>",i["name"],"...x",s["amount"],"...",to_usd(i["price"]),"...",to_usd(float(s["amount"])*float(i["price"])))
        items_cost_list.append(float(s["amount"])*float(i["price"]))
print("-------------------------------")

# Get total cost pre tax, sales tax, and total cost

subtotal = sum(items_cost_list)

# import sales taxt from the .env file

sales_tax = os.getenv("TAX_RATE", default=0.0875)

# sales_tax = 0.0875

print("SUBTOTAL =",to_usd(subtotal))
print("SALES TAX =",to_usd(subtotal*float(sales_tax)))
print("TOTAL =", to_usd(subtotal+subtotal*float(sales_tax)))

# Thank the user
print("-------------------------------")
print("SALUD, MI FAMILIA. COME AGAIN SOON")
