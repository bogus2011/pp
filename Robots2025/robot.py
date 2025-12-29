n = int(input('n = '))
all_robots = input('robots = ')
t = int(input('t = '))

robots = []
counter = 0
for r in all_robots:
    robots.append([r,counter+1])
    print(robots)
    counter = counter+1

for step in range(t):
    print(step)
    for ro in robots:
        if ro[0] == 'R':
            ro[1] = ro[1] +1
        if ro[0] == 'L':
            ro[1] = ro[1] -1
    print(robots)

final = []

for i in range(n):
    r_in_cell = 0
    for ron in robots:
        if ron[1] == i+1:
            r_in_cell = r_in_cell +1
    final.append(r_in_cell)

print(final)
    