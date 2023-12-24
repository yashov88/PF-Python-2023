def is_valid_length(password):
    return 6 <= len(password) <= 10


def contains_alpha_numeric_chars(password):
    return password.isalnum()


def contains_at_least_two_digits(password):
    digit_count = 0
    for ch in password:
        if ch.isdigit():
            digit_count += 1

    return digit_count >= 2


input_password = input()
isValid = True

if not is_valid_length(input_password):
    isValid = False
    print("Password must be between 6 and 10 characters")

if not contains_alpha_numeric_chars(input_password):
    isValid = False
    print("Password must consist only of letters and digits")

if not contains_at_least_two_digits(input_password):
    isValid = False
    print("Password must have at least 2 digits")

if isValid:
    print("Password is valid")
