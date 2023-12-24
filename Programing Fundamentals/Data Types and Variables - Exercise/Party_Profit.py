# Всеки ден печелите 50 монети, но също така харчите по 2 монети на спътник за храна.
# На всеки 3-ти (трети) ден организирате мотивационно парти, като харчите по 3 монети на спътник за питейна вода.
# На всеки 5-ти (пети) ден убивате чудовище-бос и печелите 20 монети на спътник.
# Но ако имате мотивационно парти в същия ден, харчите допълнителни 2 монети на спътник.
# На всеки 10-ти (десети) ден в началото на деня 2 (двама) от вашите спътници напускат,
# но на всеки 15-ти (петнадесети) ден 5 (пет) нови спътника се присъединяват в началото на деня.
group_size = int(input())
days = int(input())

coins = 0
for day in range(1, days+1):

    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size +=5
        coins -= 2 * group_size

    coins += 50 - 2 * group_size

    if day % 3 == 0:
        coins -= group_size * 3

    if day % 5 == 0:
        coins += 20 * group_size


print(f"{group_size} companions received {coins // group_size} coins each.")