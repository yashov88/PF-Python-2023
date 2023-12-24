# is_Found = False
#
# while True:
#     num_one = int(input())
#     num_two = int(input())
#
#     for i in range(num_two, num_one, - 1):
#         if i % num_one == 0:
#             is_Found = True
#             print(i)
#             exit()

divisor = int(input())
max_num = int(input())

result = 0
for num in range(1, max_num + 1):
    if num % divisor == 0:
        result = num

print(result)
