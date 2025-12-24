m1,m2,m3,m4,m5 = map(int, input("Введіть маси вантажів через пробіл:").split())
M1,M2 = map(int, input("Введіть вантажопідйомність вантажівок через пробіл:").split())

suma = m1 + m2 + m3 + m4 + m5

cargos = [m1,m2,m3,m4,m5]

vasul = []
petro = []
if M1+M2 < suma:
    print("They can not do it!")
if M1 > suma and M2 > suma:
    print("They both can do it!")
if M1 > suma and M2 < suma:
    print("Vasyl can do it!")
if M1 < suma and M2 > suma:
    print("Petro can do it!")
if  M1 < suma and M2 < suma and M1+M2 >= suma:
    print("They need to work together!")

    counter = len(cargos) - 1
    while(True):
        if M1 - cargos[counter] >= 0:
            vasul.append(counter + 1)
            M1 = M1 - cargos[counter]
            counter = counter - 1
            if counter < 0:
                break
        if M2 - cargos[counter] >=0:
            petro.append(counter + 1)
            M2 = M2 - cargos[counter]
            counter = counter - 1
            if counter < 0:
                break

    print(f"Vasyl manages cargos: {vasul}")
    print(f"Petro manages cargos: {petro}")
        