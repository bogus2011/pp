n = int(input(''))
x = int(input(''))
y = int(input(''))

def check_point(x,y,n):
    return not ((x)<=0) and not ((y)<=0) and not ((x)>n) and not ((y)>n)

def check_dublicates(h,e):
    dubliates=0
    for h_el in h:
        for e_el in e:
            if(h_el[0] == e_el[0] and h_el[1]==e_el[1]):
                dubliates = dubliates + 1
    return dubliates   

def horse (x,y,n):
    horse_pts = []
    if(check_point(x-1,y+2,n)):
        horse_pts.append([x-1,y+2])
    if(check_point(x+1,y+2,n)):
        horse_pts.append([x+1,y+2])
    if(check_point(x+2,y+1,n)):
        horse_pts.append([x+2,y+1])
    if(check_point(x+2,y-1,n)):
        horse_pts.append([x+2,y-1])
    if(check_point(x+1,y-2,n)):
        horse_pts.append([x+1,y-2])
    if(check_point(x-1,y-2,n)):
        horse_pts.append([x-1,y-2])
    if(check_point(x-2,y-1,n)):
        horse_pts.append([x-2,y-1])
    if(check_point(x-2,y+1,n)):
        horse_pts.append([x-2,y+1])
    return horse_pts

def elef_pts (x,y,n):
    elef_pts = []
    for i in range (1,n):
        if(check_point(x-i,y+i,n)):
            elef_pts.append([x-i,y+i])
    for i in range (1,n):
        if(check_point(x+i,y+i,n)):
            elef_pts.append([x+i,y+i])
    for i in range (1,n):
        if(check_point(x+i,y-i,n)):
            elef_pts.append([x+i,y-i])
    for i in range (1,n):
        if(check_point(x-i,y-i,n)):
            elef_pts.append([x-i,y-i])
    return elef_pts

h_points = horse(x,y,n)
e_points = elef_pts(x,y,n)
dublic = check_dublicates(h_points, e_points)

print(h_points)
print(e_points)

print(f"Можлива кількість ходів {len(h_points) + len(e_points) - dublic} )")
