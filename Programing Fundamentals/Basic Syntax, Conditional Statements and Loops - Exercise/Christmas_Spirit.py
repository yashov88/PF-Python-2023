# Decoration    Price/Piece Points/Shopping
# Ornament Set      2$          5
# Tree Skirt        5$          3
# Tree Garland      3$          10
# Tree Lights       15$         17
# • Every second day you buy Ornament Sets.
# • Every third day you buy Tree Skirts and Tree Garlands.
# • Every fifth day you buy Tree Lights.
# • Every tenth day your cat ruins all tree decorations, and you lose 20 points of the spirit:
# ◦ Because of that, you go shopping (for a second time during the day) to buy one piece of tree skirt,
#    garlands, and lights, but you do NOT earn additional spirit points for them.
# • Also, because of the cat - at the beginning of every eleventh day, you are forced to increase the quantity of
#    decorations needed to be bought each time you go shopping by 2.
# • If the last day is a tenth day, the cat demolishes even more and ruins the Christmas turkey, and you lose
#    an additional 30 points of spirit.
# • quantity - integer in the range [1…100]
# • days - integer in the range [1…100]
# • "Total cost: {budget}"
# • "Total spirit: {totalSpirit}"

quantity = int(input())
days_before_christmas = int(input())

ornament = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

spirit_points = 0
budget = 0

days = 0

while days_before_christmas != 0:
    days += 1
    if days % 11 == 0:
        quantity += 2
    if days % 2 == 0:
        budget += ornament * quantity
        spirit_points += 5
    if days % 3 == 0 and days % 5 == 0:
        budget += (tree_skirt + tree_garland + tree_lights) * quantity
        spirit_points += 60
    else:
        if days % 3 == 0:
            budget += (tree_skirt + tree_garland) * quantity
            spirit_points += 13
        if days % 5 == 0:
            budget += tree_lights * quantity
            spirit_points += 17
    if days % 10 == 0:
        spirit_points -= 20
        budget += tree_skirt + tree_garland + tree_lights
        if days_before_christmas == 1:
            spirit_points -= 30
    days_before_christmas -= 1

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit_points}")
