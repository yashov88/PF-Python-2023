def num_palindrome(numbers):

    if numbers == numbers[::-1]:
        return True
    else:
        return False


nums = [int(x) for x in input().split(", ")]
numbs = num_palindrome(nums)

print(numbs)
