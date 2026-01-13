a,b,c,d,n,x,y = map(int, input("Введіть довжини сторін коробок через пробіл:").split())

yab = a + b
gru = b + c

for i in range(0,n):
    if x <= yab and y <= gru:
        cando = "Yes"
        yab -= x
        gru -= y
    else:
        cando = 'No'
        break
print(cando)