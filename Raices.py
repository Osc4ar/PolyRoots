# coding=utf-8
from fractions import Fraction

def evaluate(px, root):
    res = 0
    i = 0
    for an in px:
        res += an * root ** i
        i += 1
    return res

def testRoots(px, proots):
    roots = []
    for root in proots:
        if evaluate(px, root) == 0:
            roots.append(root)
        if evaluate(px, -root) == 0:
            roots.append(-root)
    return roots

def abs(n):
    if n < 0:
        return -n
    return n

def getRoots(px):
    roots = []
    p = abs(px[0])
    q = abs(px[-1])
    for i in range(p, 0, -1):
        if p % i == 0:
            for j in range(q, 0, -1):
                if q % j == 0:
                    roots.append(Fraction(i, j))
    return testRoots(px, roots)

def main():
    n = int(input("Ingresa el grado del polinomio: \n -> "))
    px = [0] * (n + 1);
    for i in range(n, -1, -1):
        px[i] = int(input("Ingresa el termino x^" + str(i) + ":\n -> "))
    roots = getRoots(px)
    if len(roots) > 0:
        print("Las raices del polinomio son:")
        for r in roots:
            print("\t*)" + str(r))
    else:
        print("No se encontraron raices")

main()
