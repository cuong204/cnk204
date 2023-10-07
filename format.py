message = 'Hello python'
print('|' + message + '|')
print(f'|{message:50}|')
print(f'|{message:>50}|')
print(f'|{message:<50}|')
print(f'|{message:^50}|')

n = 100
print(f'|{n:100}|')
print(f'|{n:>100}|')
print(f'|{n:<100}|')
print(f'|{n:^100}|')

PI = 3456789.3456789
print(f'|{PI:100}|')
print(f'|{PI:>100.5f}|')
print(f'|{PI:<100.5f}|')
print(f'|{PI:^100.5f}|')