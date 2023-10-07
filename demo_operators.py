a = int(input('enter a: '))
b = int(input('enter b: '))

print('a % b =', a % b)
print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a //b =', a // b)
print('a % b', a % b)
print('a ** b =', a ** b)

price = int(input('enter price: '))
discount = int(input('enter discount: '))

print('price % discount', price % discount)
initial_balance = float (input(' Enter initial balance: '))
interest_rate = int(input('enter interest rate: '))
years = int(input('enter number of year: '))

# A = P(1 + r/100)^n
final_balance = initial_balance * (1 + interest_rate / 100) ** years
print('Final blance:', final_balance)