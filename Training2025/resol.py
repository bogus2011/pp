k = int(input("Введіть кількість солдат:"))
finish = list(map(int, input("Введіть порядок, у якому солдати фінішівали:").split()))
start = list(range(1,k+1))
z = len(finish)

print(f"Z = {z}")

sachku = []
print(f"Солдати стартували у правильному порядку: {start}")
print(f"Солдати фінішували у такому порядку: {finish}")

for i in range(1,z):
    if (i+1) < finish[i]:
        sachku.append(finish[i])
print(f"Sachku: {sachku}")
print(f"Кількість сачків {len(sachku)}")