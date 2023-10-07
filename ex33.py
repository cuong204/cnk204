def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
            return False
        
    return True

for k in range(100):
    if is_prime(k):
        print(k, end=" ")

n = int(input('Enter n: '))
print_primes(n, 10) 