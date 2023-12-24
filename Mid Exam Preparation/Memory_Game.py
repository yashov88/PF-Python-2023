def is_range_idx(idx, cards_count):
    if 0 <= idx < len(cards_count):
        return True
    return False


def is_valid_idx(idx1, idx2, count_cards):
    if is_range_idx(idx1, count_cards) and is_range_idx(idx2, count_cards) and idx1 != idx2:
        return True
    return False


cards = input().split()

command = input()
n_moves = 0

while command != "end":
    n_moves += 1
    index1, index2 = [int(el) for el in command.split()]
    if is_valid_idx(index1, index2, cards):
        if cards[index1] == cards[index2]:
            element = cards[index1]
            cards.pop(index1)
            cards.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print("Try again!")
    else:
        element_to_add = f"-{n_moves}a"
        index = len(cards) // 2
        cards.insert(index, element_to_add)
        cards.insert(index, element_to_add)
        print("Invalid input! Adding additional elements to the board")

    if not cards:
        print(f"You have won in {n_moves} turns!")
        exit(0)
    command = input()

print(f"Sorry you lose :(")
print(*cards, sep=" ")
