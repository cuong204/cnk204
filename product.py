name = input('Enter product name: ')
price = float (input('enter procducts price: '))
n_products = int(input('enter number of products: '))
total = price * n_products

print('+' + '-' * 20 + '+' + '-' * 10 + '-' * 10 + '+' + '-' * 10 + '+')
print(f'|{name:20}|{price:>10.2f}|{n_products:10}|{total:>10.2f}|')
print('+' + '-' * 20 + '+' + '-' * 10 + '+' + '-' * 10 + '+' + '-' * 10 + '+')