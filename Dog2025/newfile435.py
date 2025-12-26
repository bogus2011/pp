from math import*

cupols = set()
res = set()

n,x1,y1,x2,y2 = map(int, input("Введіть кількість куполів, координати дога й бджіл  через пробіл:").split())

def doglen(x,y,cup):
    if pos >  x:
        ln = sqrt((cup-x)**2+y)
        return ln
    elif pos < x:
        ln = sqrt((x-cup)**2+y)
        return ln
    
def beelen(x,y,cup):
    if pos >  x:
        ln = sqrt((cup-x)**2+y)
        return ln
    elif pos < x:
        ln = sqrt((x-cup)**2+y)
        return ln

for i in range(0,n):
    pos,r = map(int, input("Введіть позицію центра та радіус купола через пробіл:").split())
    cupols.add((pos,r,i+1))
print(cupols)

for cup in cupols:
    dl = doglen(x1,y1,cup[0])
    bl = beelen(x2,y2,cup[0])
    if dl <= cup[1] and bl > cup[1]:
        res.add((cup[0],cup[1],'No',cup[2]))
    else:
        res.add((cup[0],cup[1],'Yes',cup[2]))
print(f'set of cupols in format(x,r,decision,num_of_cup)={res}')
    


    

    






