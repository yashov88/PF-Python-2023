from math import ceil

budget = float(input())
students = float(input())
price_of_flor = float(input())
price_of_eggs = float(input())
price_of_apron = float(input())

# student = flor, 10 eggs, apron
free_flor = students // 5

all_money = (price_of_apron * (students + ceil(students * 0.2))) + (price_of_eggs * 10) * students + price_of_flor * \
            (students - free_flor)

if budget > all_money:
    print(f"Items purchased for {all_money:.2f}$.")
else:
    print(f"{abs(budget - all_money):.2f}$ more needed.")