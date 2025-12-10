# primes_small.py
def is_prime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True

print([x for x in range(2,51) if is_prime(x)])
