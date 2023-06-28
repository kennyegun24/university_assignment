# initialized list of items and gave them values as their prices
item_prices = {
    'ITEM1': 134,
    'ITEM2': 5321,
    'ITEM3': 32313
}

# Function to print the individual items. I decided to make this a global function so that it
# will get separated from the calculation logic and also to make code cleaner
# It takes the order prducts and price as parameters and prints it out
def print_products_price(product, price):
    print(f"{product:<30}", end=f"{str(price)}\n")

# Function to print the combined items bought by the customer and also to display
# the total price.
# It takes the order prducts and price as parameters and prints it out
def print_combos(product, price):
    print(f"Combo{product:<25}", end=f"{str(price)}\n")

# Function to print the contact
def print_contact():
    print('For delivey contact us on: +234 805 254 64789')

# Function to calculate each order. It takes a parameter which is an array
def calculate_purchase(params):
    check_num_of_item = len(params)
    total = 0

    print('Online Store')
    print('----------------------------------')
    print_products_price('Product', 'Price')
    print_products_price('ITEM1',item_prices['ITEM1'])
    print_products_price('ITEM2',item_prices['ITEM2'])
    print_products_price('ITEM3',item_prices['ITEM3'])

# This conditional statement is used to cheeck the length of the parameter passed
# to the function so different operations will be carried out if the conditions are met.
    if check_num_of_item == 1:
        total = item_prices[params[0]]

        # Here i passed the parameter to the print_combos and also the total, so it prints out the
        print_combos(f"({params[0]})", total)

    # This is an else if statement checking if the length of thr parameter is 2, if it is 2, it will then carry out the codes in the block
    elif check_num_of_item == 2:
        # This is checking the parameters being sent to the function
        if ('ITEM1' in params and 'ITEM2' in params) or ('ITEM1' in params and 'ITEM3' in params) or ('ITEM2' in params and 'ITEM3' in params):
            sum1 = item_prices[params[0]]
            sum2 = item_prices[params[1]]
            total = sum1 + sum2 * 0.9
            # The parameters and also the total values are being passed to the print_combos function
            print_combos(f"({params[0]} + {params[1]})", total)

    # This is an else if statement checking if the length of thr parameter is 3, if it is 2, it will then carry out the codes in the block
    elif check_num_of_item == 3:
        total = item_prices[params[0]] + item_prices[params[1]] + item_prices[params[2]] * 0.75
            # The parameters and also the total values are being passed to the print_combos function
        print_combos(f"({params[0]} + {params[1]} + {params[2]})", total)

    print('----------------------------------')
    # This is printing the contact after the calculations has been completed
    print_contact()


# Calling the function and passing different parameters
item1 = ['ITEM2']
calc1_price = calculate_purchase(item1)

# item2 = ['ITEM1',  'ITEM3']
# calc2_price = calculate_purchase(item2)

# item3 = ['ITEM1',  'ITEM2']
# calc3_price = calculate_purchase(item3)

item4 = ['ITEM2',  'ITEM3']
calc4_price = calculate_purchase(item4)

item5 = ['ITEM1',  'ITEM2', 'ITEM3']
calc5_price = calculate_purchase(item5)
