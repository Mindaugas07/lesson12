# squares = {i: i * i for i in range(10) if i != 5}
# print(squares)

# squares = {i: i * i for i in range(10) if i % 2}
# print(squares)

# values = ["a", "b", "c"]
# for count, value in enumerate(values):
#     print(count, value)

# my_tuple = (1, 2, 3)
# num1, num2, num3 = my_tuple
# print(my_tuple)

# values = ["a", "b", "c"]
# for value in enumerate(values):
#     # print(value)
#     count, value = value

    # print (f"aflkj {count} fdsa {value}")

# def even_items(numbers: list):
#     return {i + 1 : v for i, v in enumerate(numbers, start=1) if not i % 2}

# seq = list(range(1, 11))

# print(even_items(seq))

# def even_items(numbers: list):
#     new_list = []
#     for i, v in enumerate(numbers, start=1):
#         if not i % 2:
#             new_list.append(v)
#     return new_list

# seq = list(range(1, 145))
# print(even_items(seq))

# 3
# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# words_with_e = [word for word in text.split(" ") if "e" in word]
# print(len(words_with_e))


# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# words_with_e = [word for word in text.split() if len(word) > 5]
# print(len(words_with_e))

# 5
# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# letter_dict = {}
# for letter in text:
#     if letter.isalpha():
#         letter_dict[letter] = letter_dict.get(letter, 0) + 1
# print(letter_dict)


# 6
# import math

# def is_perfect_square(number):

#     if number != 0 and (math.sqrt(number)) * (math.sqrt(number)) == number:
#         print("Perfect square")
#     else:
#         print("Not perfect square")

# is_perfect_square(4)

# def common(a, b, c):
#     for item_a in a:
#         for item_b in b:
#             for item_c in c:


        
    

# print(common([1,2,2,3],[5,3,2,2],[7,3,2,2]))