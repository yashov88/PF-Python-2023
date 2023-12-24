budget = float(input())

flour_price = float(input())
egg_price = flour_price * 0.75
milk_price = (flour_price * 1.25) * 0.25
loaf_price = flour_price + egg_price + milk_price

loafs_counter = 0
colored_eggs_counter = 0
while loaf_price <= budget:
    loafs_counter += 1
    budget -= loaf_price
    colored_eggs_counter += 3

    if loafs_counter % 3 == 0:
        colored_eggs_counter -= loafs_counter - 2

print(f"You made {loafs_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")

