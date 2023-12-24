from string import ascii_letters, digits

user_names = input().split(", ")
allowed_chars = ascii_letters + digits + "-" + "_"

for user_name in user_names:
    if len(user_name) < 3 or len(user_name) > 16:
        continue

    contains_allowed_char = all([char in allowed_chars for char in user_name])

    if not contains_allowed_char:
        continue

    print(user_name)
