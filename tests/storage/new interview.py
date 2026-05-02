# simple_digits = []
#
#
# for digit in range(20):
#     # if digit % 2 != 0:
#     #     simple_digits.append(digit)
#     is_prime_numer = True
#     for numer in simple_digits:
#         if digit % numer == 0:
#             is_prime_numer = False
#             break
#     if is_prime_numer==True:
#         simple_digits.append(digit)
# print(simple_digits)

# class A:
#     pass
#     def __new__(cls, *args, **kwargs):
#         pass
#
# print(dir(A))

# def positive_sum(arr):
#     positive_numbers = []
#
#     for number in arr:
#         if number == 0 or number > 0:
#             positive_numbers.append(number)
#             sum_arr = sum(positive_numbers)
#         if positive_numbers is not

# array_1 = [-1, -5, 8, 54]
# array_2 = [-1, -2, -3, -4, -5]
array_3 = [1,2,3,4,5]
array_4 = [1,-2,3,4,5]
array_5 = [-1,2,3,4,-5]

def positive_sum(arr):
    positive_numbers = []

    for number in arr:
        if number > 0:
            positive_numbers.append(number)
    if len(positive_numbers) > 0:
        return sum(positive_numbers)
    else:
        return 0

print(positive_sum(array_3))
print(positive_sum(array_4))
print(positive_sum(array_5))
