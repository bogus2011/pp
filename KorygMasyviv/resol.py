import sys

n = int(input("Input n = "))
a = list(map(int, input("Input a[] separated with space: ").split()))

#n=5
#a = [1,-1,-2,3,6]
sorted_a = a.copy()

def try_sorting(mas):
    for i in range(1,len(mas)):
        print(mas[i])
        if mas[i] >= mas[i-1]:
            continue
        elif mas[i] * -1 > mas[i-1]:
            mas[i] = mas[i] * -1
        else:
            return False

def is_non_decreasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

if sorted_a[0] * -1 <= sorted_a[1]:
    sorted_a[0] = sorted_a[0] * -1
try_sorting(sorted_a)
if is_non_decreasing(sorted_a):
    print("YES")
    print(sorted_a)
    sys.exit()

sorted_a = a.copy()
if sorted_a[0] <= sorted_a[1] * -1:
    sorted_a[1] = sorted_a[1] * -1
try_sorting(sorted_a)
if is_non_decreasing(sorted_a):
    print("YES")
    print(sorted_a)
    sys.exit()

sorted_a = a.copy()
if sorted_a[0] * -1 <= sorted_a[1] * -1:
    sorted_a[0] = sorted_a[0] * -1
    sorted_a[1] = sorted_a[1] * -1
try_sorting(sorted_a)
if is_non_decreasing(sorted_a):
    print("YES")
    print(sorted_a)
    sys.exit()

sorted_a = a.copy()
try_sorting(sorted_a)
if is_non_decreasing(sorted_a):
    print("YES")
    print(sorted_a)
    sys.exit()

print("NO")
