# list_example = ["apple", "banana", "cherry"]
# print("-".join(list_example))  # apple-banana-cherry
# print(list_example)     # ['apple', 'banana', 'cherry']

# some_text = "S o f t U n i"
# courses = some_text.split(" ") # сплитва по space
# print(courses)  # ['S', 'o', 'f', 't', 'U', 'n', 'i']

# list_of_numbers = [1, 3, 5, 7]
# print(list_of_numbers[-1])  # [0]
# print(list_of_numbers[-2])  # [1]
# print(list_of_numbers[-3])  # [2]
# print(list_of_numbers[-4])  # [3]

# meerkat = list()
#
# meerkat.append(input())
# meerkat.append(input())
# meerkat.append(input())
#
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
#
# print(meerkat)

# number = int(input())
# courses = list()
#
# for i in range(number):
#     courses.append(input())
#
# print(courses)

# animals = ["dog", "cat", "fish"]
# for element in animals:
#     print(element, end=" ")   #  cat dog fish

# zoo = ["dog", "cat", "fish"]
# for index in range(len(zoo)):
#     print(zoo[index], end=" ")
#     print(index)    # 0 1 2

# zoo = ["dog", "cat", "fish"]
# i = 0
# while i < len(zoo):
#     print(zoo[i], end=" ")
#     i += 1

# zoo = ["dog", "cat", "fish"]
# while zoo:
#     print(zoo[0], end=" ")
#     current_element = zoo[0]
#     zoo.remove(current_element)

# number = int(input())
#
# negatives = list()
# positives = list()
# sum_of_negatives = 0
#
# for i in range(number):
#     current = int(input())
#     if current >= 0:
#         positives.append(current)
#     else:
#         negatives.append(current)
#         sum_of_negatives += current
#
# print(positives)
# print(negatives)
# print(f"Count of positives: {len(positives)}")
# print(f"Sum of negatives: {sum_of_negatives}") # {sum(negatives)}

# courses = [1, 2, 3, 4, 5]
# if 3 in courses:
#     print("The number 3 is in the list")
#
# if 6 not in courses:
#     print("The number 6 is not in the list")

# number = int(input())
# search_word = input()
# strings = list()
# filtered = list()
#
# for i in range(number):
#     current_strings = input()
#     strings.append(current_strings)
#     if search_word in current_strings:
#         filtered.append(current_strings)
#
# print(strings)
# print(filtered)

# number = int(input())
# search_word = input()
#
# strings = []
# for i in range(number):
#     current_string = input()
#     strings.append(current_string)
# print(strings)
#
# for current_string in strings:
#     if search_word not in current_string:
#         strings.remove(current_string)
# print(strings)

# number = int(input())
# direct_command = ["even", "odd", "positive", "negative"]  # printAll
#
# positive = list()
# negative = list()
# even = list()
# odd = list()
#
# for i in range(number):
#     current = int(input())
#     if current % 2 == 0:
#         even.append(current)
#     else:
#         odd.append(current)
#     if current >= 0:
#         positive.append(current)
#     else:
#         negative.append(current)
#
# filtered_word = input()
#
# # if filtered_word == "even":
# #     print(even)
# # if filtered_word == "odd":
# #     print(odd)
# # if filtered_word == "positive":
# #     print(positive)
# # if filtered_word == "negative":
# #     print(negative)
# if filtered_word in direct_command:
#     print(eval(filtered_word))
# else:
#     print(f"Positive: {positive}")
#     print(f"Negative: {negative}")
#     print(f"Even: {even}")
#     print(f"Odd: {odd}")
#
# def say_hello(first_name):
#     print(f"Hello, {first_name}")
#
#
# name = input("Please enter your name: ")
#
# say_hello(name)
#
# def say_hello(first_name):
#     print(f"Hello, {first_name}")
#
#
# for i in range(1, 11):
#     say_hello(f"Test {i}")
#
# def say_hello(first_name, last_name):
#     print(f"Hello, {first_name} {last_name}!")
#
#
# first_name = input("Enter a firs name: ")
# last_name = input("Enter a last name: ")
#
# say_hello(first_name, last_name)
#
# def top():
#     print("This is the top")
#
#
# def middle():
#     print("This is the middle")
#
#
# def bottom():
#     print("This is the bottom")
#
#
# def print_whole():
#     top()
#     middle()
#     bottom()
#
#
# print_whole()
#
#
# my_list = [100, 200, 300]
# my_dict = {}
#
# for index, el in enumerate(my_list):
#     my_dict[index] = el
#
# print(my_dict)
# my_list = [100, 200, 300, 400]
# my_dict = {index: ("even" if index % 2 == 0 else "odd") for index, el in enumerate(my_list)}
#
# print(my_dict)