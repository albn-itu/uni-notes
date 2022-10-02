from random import randint

# util method
def mod_pow(base, exp, mod):
    res = 1
    while(exp > 0):
        if (exp % 2 == 1):
            res = (res * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return res

alpha = 666
p = 6661
k = 2227 # mod_pow(alpha, x, p)

def encrypt(m):
    r = randint(1, p-2)
    c1 = mod_pow(alpha, r, p)
    c2 = m * mod_pow(k, r, p)

    return (c1, c2)

def get_a():
    # Bruteforce
    for i in range(1, p-1): # Range is non inclusive, so instead of p-2 it's p-1 
        # If the calculation of the public key matches, we assume that must be the private key
        if mod_pow(alpha, i, p) == k:
            return i

def decrypt(c1, c2, a):
    m = c2 / mod_pow(c1, a, p)
    # Due to the fraction python assumes it to be a decimal, just remove the .0
    return round(m)

def modify(c2, x):
    return c2 * x

if __name__ == '__main__':
    c = encrypt(2000)
    print(c)

    a = get_a()
    print(a)

    decrypted = decrypt(c[0], c[1], a)
    print(decrypted)

    modified = modify(c[1], 3)
    print(modified)
    print(decrypt(c[0], modified, a))

