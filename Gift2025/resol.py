m,n,k= map(int, input("Введіть кількість днів та залишок через пробіл:").split())

count_recipients = 0

m1 = m
n1 = n

if k-1 <= m and m-(k-1) < n-(k-1) :
    n1 -= 1
    count_recipients = m + 1

if k-1 <= n and n-(k-1) < m-(k-1):
    m1 -= 1
    count_recipients = n + 1

print(count_recipients)
print(f"max shmat for advok {m1*n1}")