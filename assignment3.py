
item_prices = {
    'ITEM1': 134,
    'ITEM2': 5321,
    'ITEM3': 32313
}


def print_products_price(product, price):
    print(f"{product:<30}", end=f"{str(price)}\n")

def print_combos(product, price):
    print(f"Combo{product:<25}", end=f"{str(price)}\n")

def print_contact():
    print('For delivey contact us on: +234 805 254 64789')

def calculate_purchase(params):
    check_num_of_item = len(params)
    total = 0

    print('Online Store')
    print('----------------------------------')
    print_products_price('Product', 'Price')
    print_products_price('ITEM1',item_prices['ITEM1'])
    print_products_price('ITEM2',item_prices['ITEM2'])
    print_products_price('ITEM3',item_prices['ITEM3'])

    if check_num_of_item == 1:
        total = item_prices[params[0]]
        print_combos(f"({params[0]})", total)

    elif check_num_of_item == 2:
        if ('ITEM1' in params and 'ITEM2' in params) or ('ITEM1' in params and 'ITEM3' in params) or ('ITEM2' in params and 'ITEM3' in params):
            sum1 = item_prices[params[0]]
            sum2 = item_prices[params[1]]
            total = sum1 + sum2 * 0.9
            print_combos(f"({params[0]} + {params[1]})", total)

    elif check_num_of_item == 3:
        total = item_prices[params[0]] + item_prices[params[1]] + item_prices[params[2]] * 0.75
        print_combos(f"({params[0]} + {params[1]} + {params[2]})", total)

    print('----------------------------------')
    print_contact()
    return total

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
