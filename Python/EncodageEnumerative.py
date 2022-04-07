"""
Exercice 15 du TD cryptographie basée sur les codes

Encodage en mots de poids constants

SABIR ILYASS.

"""

def factorielle(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact

def arrangements(n,k):
    if (k > n):
        return 0
    else:
        arrangement = 1
        for i in range(n-k+1, n+1):
            arrangement *= i
        return arrangement

def binomial(i,j):
    return arrangements(i,j) // factorielle(j)

def inverse_binomial(x,j):
    i = 0
    while (binomial(i,j) <= x):
        i = i + 1
    return (i - 1)

def phi(n,t,x):
    if (x < 0 or x >= binomial(n, t)):
        return None
    else:
        result, j = 0, t
        while (j > 0):
            ij = inverse_binomial(x, j)
            result += 2 ** ij
            x -= binomial(ij, j)
            j -= 1
        return result

def decimal_to_binary(n):
    s = ""
    while(n >= 1):
        s = str(n % 2) + s
        n = n // 2
    return s
def inverse_phi(n, t, e):
    binary_of_e = decimal_to_binary(e)
    length = len(binary_of_e)
    index, result = 1, 0
    for i in range(length - 1, -1, -1):
        value = int(binary_of_e[i])
        if (value):
            result += binomial(length - 1 - i, index)
            index += 1

    return result

# pour remplir le tableau
reponse = []
for n in range(5,9):
    if (n == 7 or n == 8):
        for t in range(2, 6):
            L = []
            for m in range(14):
                L.append(phi(n, t, m))
            reponse.append(L)
    else:
        for t in range(2, 5):
            L = []
            for m in range(14):
                L.append(phi(n, t, m))
            reponse.append(L)

for i in range(len(reponse)):
    print(reponse[i])
