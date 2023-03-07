# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb
import math

def lesser_of_two_evens(a, b):
    if (a % 2 == 0 and b % 2 == 0):
        return min(a, b)
    else:
        return max(a, b)


# print(lesser_of_two_evens(2, 4))
# print(lesser_of_two_evens(2, 5))

def animal_crackers(text):
    split_word = text.split(" ")
    if split_word[0][0] == split_word[1][0]:
        return True
    else:
        return False

# print(animal_crackers("Levelheaded Llama"))
# print(animal_crackers('Crazy Kangaroo'))


def makes_twenty(n1, n2):
    return 20 == n1 or 20 == n2 or 20 == n1 + n2

# print(makes_twenty(20,10))
# print(makes_twenty(12,8))
# print(makes_twenty(2,3))


def old_macdonald(name):
    capitalized = []
    for index, letter in enumerate(name):
        if index == 0 or index == 3:
            capitalized.append(name[index].upper())
        else:
            capitalized.append(letter)
    return ''.join(capitalized)

#alternate soln.
# def old_macdonald(name):
#     if len(name) > 3:
#         return name[:3].capitalize() + name[3:].capitalize()
#     else:
#         return 'Name is too short!'

# print(old_macdonald('macdonald'))


def master_yoda(text):
    reversed_word = text.split(" ")
    reversed_word.reverse()
    return ' '.join(reversed_word)


# print(master_yoda("I am home"))
# print(master_yoda('We are ready'))

def almost_there(n):
    return (n <= 110 and n >= 90) or (n <= 210 and n >= 190)

# print(almost_there(90))
# print(almost_there(104))
# print(almost_there(150))
# print(almost_there(209))


def has_33(nums):
    compare_num = nums[0]
    for number_index in range(1, len(nums)):
        if compare_num == nums[number_index] and nums[number_index] == 3:
            return True
        else:
            compare_num = nums[number_index]
    return False

# print("Has 33")
# print(has_33([1, 3, 3]))#true
# print(has_33([1, 3, 1, 3]))#false
# print(has_33([3, 1, 3]))#false
# print(has_33([3, 1, 3, 1, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]))#true


def paper_doll(text):
    return ''.join(list(map(lambda letter: letter * 3, text)))

# print(paper_doll('hello'))


def summer_69(arr):
    sum = 0
    ignoring = False
    for number in arr:
        if (number == 6 and not ignoring):
            ignoring = True
            continue
        elif (number == 9 and ignoring):
            ignoring = False
            continue
        if not ignoring:
            sum += number
    return sum

# print(summer_69([4, 5, 6, 7, 8, 9]))#9
# print(summer_69([2, 1, 6, 9, 11]))#14
# print(summer_69([1, 3, 5]))#9


def spy_game(nums):
    spy_number = []
    for number in nums:
        if number == 0 or number == 7:
            spy_number.append(f"{number}")
    if (''.join(spy_number) == '007'):
        return True
    else:
        return False

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

def vol(rad):
    return round(((4/3)*(math.pi)*(rad*rad*rad)), 4)

# print(vol(2))

def unique_list(lst):
    unique_items = set()
    for number in lst:
        unique_items.add(number)
    return list(unique_items)

# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))