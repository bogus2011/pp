n,m,k = map(int, input("Введіть параметри кімнати і к-сть прямокутників через пробіл:").split())
andrii_pos = [0,0]
prev_point_x = 0
prev_point_y = 0

prams = set()

def chek_whether_point_belongs_to_any_rectangle(x,y):
    for p in prams:
        if x>=p[0] and x<=p[2] and y>=p[1] and y<= p[3]:
            return True
        
def return_by_x():
    while True:
        andrii_pos[0] = andrii_pos[0] - 0.5
        print(andrii_pos)
        if not chek_whether_point_belongs_to_any_rectangle(andrii_pos[0],andrii_pos[1]+0.5):
            andrii_pos[1] = andrii_pos[1] + 0.5

            #this is needed to overcome return due to prev point check
            if not chek_whether_point_belongs_to_any_rectangle(andrii_pos[0],andrii_pos[1]+0.5):
                andrii_pos[1] = andrii_pos[1] + 0.5

            print(andrii_pos)
            break
    
def return_by_y():
        while True:
            andrii_pos[1] = andrii_pos[1] - 0.5
            print(andrii_pos)
            if not chek_whether_point_belongs_to_any_rectangle(andrii_pos[0]+0.5,andrii_pos[1]):
                andrii_pos[0] = andrii_pos[0] + 0.5

                #this is needed to overcome return due to prev point check
                if not chek_whether_point_belongs_to_any_rectangle(andrii_pos[0]+0.5,andrii_pos[1]):
                    andrii_pos[0] = andrii_pos[0] + 0.5
                
                print(andrii_pos)
                break

for i in range(0,k):
    x1,y1,x2,y2 = map(int, input("Введіть довжини сторін коробок через пробіл:").split())
    prams.add((x1,y1,x2,y2))

while andrii_pos[0]+0.5 < n or andrii_pos[1]+0.5 < m: #move point forward
    if andrii_pos[0]+0.5 != n:
        if not chek_whether_point_belongs_to_any_rectangle(andrii_pos[0]+0.5,andrii_pos[1]): #skip move by x if there is a rectangle ahead
            andrii_pos[0] = andrii_pos[0] + 0.5
            print(andrii_pos)

    if andrii_pos[1]+0.5 != m:
        if not chek_whether_point_belongs_to_any_rectangle(andrii_pos[0],andrii_pos[1]+0.5): #skip move by y if there is a rectangle ahead
            andrii_pos[1] = andrii_pos[1] + 0.5
            print(andrii_pos)

    if prev_point_x == andrii_pos[0] and prev_point_y == andrii_pos[1] and andrii_pos[0] + 0.5 == n: # check if we need to return by x
        return_by_x()
    
    if prev_point_x == andrii_pos[0] and prev_point_y == andrii_pos[1] and andrii_pos[1] + 0.5 == m: # check if we need to return by y
        return_by_y()

    prev_point_x = andrii_pos[0]
    prev_point_y = andrii_pos[1]

    if andrii_pos[0] + 0.5 == n and andrii_pos[1] + 0.5 == m:
        print("YES")
        break




