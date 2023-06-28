# import turtle

def print_circum(radius):
    circumference=2 * 3.14159 * radius
    print(f"The circumference of the radius is {circumference}")

print_circum(300)
print_circum(140)
print_circum(20)


item_prices = {
    'ITEM1': 134,
    'ITEM2': 5321,
    'ITEM3': 32313
}

def calculate_purchase(params):
    check_num_of_item = len(params)
    total = 0

    def print_products_price(product, price):
        print(f"{product:<30}", end=price)

    def print_combos(product, price):
        print(f"Combo{product:<25}", end=f"{str(price)}\n")

    def print_contact():
        print('For delivey contact us on +234 805 254 64789')

    print('Online Store')
    print('----------------------------------')
    print_products_price('Product', 'Price \n')

    if check_num_of_item == 1:
        total = item_prices[params[0]]
        print_combos(f"({params[0]})", item_prices[params[0]])

    elif check_num_of_item == 2:
        if ('ITEM1' in params and 'ITEM2' in params) or ('ITEM1' in params and 'ITEM3' in params) or ('ITEM2' in params and 'ITEM3' in params):
            sum1 = item_prices[params[0]]
            sum2 = item_prices[params[1]]
            total = sum1 + sum2 * 0.9
            print_combos(f"({params[0]} + {params[1]})", item_prices[params[0]])

    elif check_num_of_item == 3:
        total = item_prices[params[0]] + item_prices[params[1]] + item_prices[params[2]] * 0.75
        print_combos(f"({params[0]} + {params[1]})", total)

    print('----------------------------------')
    print_contact()
    return total

# item1 = ['ITEM2']
# calc1_price = calculate_purchase(item1)

# item2 = ['ITEM1',  'ITEM3']
# calc2_price = calculate_purchase(item2)

# item3 = ['ITEM1',  'ITEM2']
# calc3_price = calculate_purchase(item3)

# item4 = ['ITEM2',  'ITEM3']
# calc4_price = calculate_purchase(item4)

item5 = ['ITEM1',  'ITEM2', 'ITEM3']
calc5_price = calculate_purchase(item5)
