price_product = {}
quantity_product = {}

while True:
    line = input()
    if line == "buy":
        break

    args = line.split()
    product = args[0]
    price = float(args[1])
    quantity = int(args[2])

    if product in price_product:
        price_product[product] = price
        quantity_product[product] += quantity
    else:
        price_product[product] = price
        quantity_product[product] = quantity

for product in price_product:
    price = price_product[product]
    quantity = quantity_product[product]
    total_price = price * quantity

    print(f"{product} -> {total_price:.2f}")
