days_and_rest = list(map(int, input("Введіть кількість днів та залишок через пробіл:").split()))

balance = days_and_rest[1]
init_days = days_and_rest[0]

print(days_and_rest)
days = []
days_to_rest = []
rest_collection = []

for inp in range(0,days_and_rest[0]):
    day = list(map(int, input(f"Введіть прибуток і витрати через пробіл в {inp+1}-й день:").split()))
    days.append(day)

print(days)
days.sort(key=lambda x:x[1], reverse=False)
print(days)

#let's cpnsidr zero working days
for day in days:
    if (balance - day[1] >= 0):
        balance = balance - day[1]
        days_to_rest.append(day)

print(f"For no working days there will be {len(days_to_rest)} to rest:")

rest_collection.append(len(days_to_rest))
         