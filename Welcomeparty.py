print('wellcome')
guests = []
n = int(input('How many guests will be attending the party? '))
for i in range(n):
    a = input(f'Enter the name of guest {i + 1}: ')
    guests.append(a)
print(f'The final guest list is: {guests}')
while True:
    b = input('Do you want to remove any guests from the list? (yes/no): ')
    if b == ('yes'):
        c = input('Enter the name of the guest to remove: ')
        guests.remove(c)
        print(f'guest {c} has been removed from the list')
    else:
        break
print(f'The updated guest list is: {guests}')