def calculate_order(product, quantity):
    resul = 0
    if product == "water":
        resul = quantity * 1.00
    elif product == "coffee":
        resul = quantity * 1.50
    elif product == "coke":
        resul = quantity * 1.40
    elif product == "snacks":
        resul = quantity * 2

    return resul


product_buy = input()
requested_quantity = int(input())
res = calculate_order(product_buy, requested_quantity)
print(f"{res:.2f}")
