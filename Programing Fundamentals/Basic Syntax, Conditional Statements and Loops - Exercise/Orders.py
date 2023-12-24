number_of_orders = int(input())

total_price = 0
for _ in range(number_of_orders):
    price_capsule = float(input())
    days = int(input())
    capsule = int(input())

    if price_capsule < 0.01 or price_capsule > 100:
        continue

    if days < 1 or days > 31:
        continue

    if capsule < 1 or capsule > 2000:
        continue

    order_price = price_capsule * days * capsule
    total_price += order_price

    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total_price:.2f}")