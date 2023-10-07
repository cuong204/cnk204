products = {'computer': 1000, 'ram': 200, 'keyboard': 100, 'mouse': 50}
#write a program to manage products wotj following feature:
#1. add a new product (ask for name and price, check name is not in the dictionary)
#2. delete a procduct( aks for name and check name is in the dictionary)
#3. edit a product(ask for name, check name is in the dictionary, ask for new price)
#4. Search a product( akse for name, check nam is in the dictionary, print price
#5. print all product

def product_management(products):
    while running:
        print_menu()
        choice = int(input("enter your choice: "))
        if choice ==1:
            Add_new_product(products)
        elif choice == 2:
            edit_products(products)
        elif choice == 3:
            delete_products(products)
        elif choice == 4:
            search_products(products)
        elif choice == 5:
            print_all(products)
        elif choice == 6:
            running = False
        else:
            print("Invalid choice. Please try again")

def print_menu():
    print("1. Add a product")
    print("2. Edit a product")
    print("3. Delete a product")
    print("4. Search product")
    print("5. Search product")
    print("6. Print all")

def add_product(products):
    product = input('enter new product: ')
    if product not in products:
        price_product = int(input('enter price of product: '))
        products[product] = price_product
    print(products)

def delete_product(products):
    product = input('enter product want to delete: ')
    if product in products:
        del products[product]
    print(products)

def edit_product(products):
    product = input('enter product exist: ')
    if product in products:
        price_product = int(input('enter price of product: '))
        products[product] = price_product
        print(products)

def search_product(products):
    product = input('enter product: ')
    if product in products:
        print(f'{product} found in product, price: {products[product]}')
    else:
        print(f'{product} found in products')

def print_all(products):
    for product in products:
        print(f'{product:20}:{products[product]:20}')
    