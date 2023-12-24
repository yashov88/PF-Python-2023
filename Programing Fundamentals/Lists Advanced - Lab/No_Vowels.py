def remove_vowels_from_text(text):
    forbidden_letters = ['a', 'o', 'u', 'e', 'i']
    result = [char for char in text if char.lower() not in forbidden_letters]
    return "".join(result)


text = input()
print(remove_vowels_from_text(text))
# text = input()
# result = [char for char in text if char.lower() not in ['a', 'o', 'u', 'e', 'i']]
# # result = []
# # for char in text:
# #     if char.lower() not in ['a', 'o', 'u', 'e', 'i']:
# #         result.append(char)
#
# print("".join(result))
