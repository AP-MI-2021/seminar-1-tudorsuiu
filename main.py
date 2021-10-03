def minimum(x, y, z):
    '''
    determina minimul a 3 numere
    :param x: nr. intreg
    :param y: nr. intreg
    :param z: nr. intreg
    :return: minimul dintre x, y si z
    '''
    if x <= y and x <= z:
        return x
    elif y <= x and y <= z:
        return y
    else:
        return z

assert minimum(4, 5, 2) == 2
assert minimum(0, 1, 0) == 0
assert minimum(1, 1, 1) == 1
assert minimum(40, 13, 27) == 13
assert minimum(309, 625, 984) == 309

def isPrime(x):
    '''
    determina daca numarul este prim 
    :param x: nr. intreg
    :return: True daca numarul este prim si False in caz contrar
    '''
    if x < 2:
        return False
    for d in range(2, x // 2 + 1):
        if x % d == 0:
            return False
    return True

assert isPrime(-1) == False
assert isPrime(0) == False
assert isPrime(1) == False
assert isPrime(2) == True
assert isPrime(3) == True
assert isPrime(4) == False


def oglindit(x):
    '''
    determina oglinditul numarului
    :param x: nr. intreg
    :return: oglinditul numarului
    '''
    y = 0
    while x != 0:
        y = y * 10 + x % 10
        x = x // 10
    return y

assert oglindit(0) == 0
assert oglindit(91) == 19
assert oglindit(544) == 445
assert oglindit(8331) == 1338

shouldRun = True

while shouldRun:
    print("1.Determinati minimul a 3 numere")
    print("2.Determinati daca un numar este prim")
    print("3.Determinati, pentru n numere, daca acestea sunt prime")
    print("4.Determinati palindromul unui numar")
    print("x.Iesire")
    optiune = input("Selectati optiunea: ")
    if optiune == "1":
        x = int(input("Dati primul numar: "))
        y = int(input("Dati al doilea numar: "))
        z = int(input("Dati al treilea numar: "))
        print(minimum(x, y, z))

    elif optiune == "2":
        x = int(input("Dati numarul: "))
        print(isPrime(x))

    elif optiune == "3":
        n = int(input("Cate numere urmeaza a fi citite?: "))
        for i in range(n):
            x = int(input("Dati numarul: "))
            print(isPrime(x))

    elif optiune == "4":
        x = int(input("Dati numarul: "))
        print(oglindit(x))

    elif optiune == "x":
        shouldRun = False

    else:
        print("Optiune gresita! Reincercati!")

