bab = list(map(int, input("Введіть довжини сторін коробок через пробіл:").split()))

N = max(bab)

bab.remove(N)

plosh = 0

if N >= bab[0] + bab[1]:
    plosh = N * (N+max(bab))
else:
    plosh = N * (bab[0]+bab[1]+N)

print(plosh)

