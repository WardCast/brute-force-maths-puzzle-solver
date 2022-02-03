from itertools import permutations
from sys import exit

centre_number = 15
digits = [1, 2, 3, 4, 5, 6, 7, 8]

def top_is_correct(digits_perm):
    if digits_perm[0] + digits_perm[1] + digits_perm[2] == centre_number:
        return True
    else:
        return False

def right_is_correct(digits_perm):
    if digits_perm[2] + digits_perm[4] + digits_perm[7] == centre_number:
        return True
    else:
        return False

def bottom_is_correct(digits_perm):
    if digits_perm[7] + digits_perm[6] + digits_perm[5] == centre_number:
        return True
    else:
        return False

def left_is_correct(digits_perm):
    if digits_perm[5] + digits_perm[3] + digits_perm[0] == centre_number:
        return True
    else:
        return False

def is_correct(digits_perm):
    condition1 = top_is_correct(digits_perm)
    condition2 = right_is_correct(digits_perm)
    condition3 = bottom_is_correct(digits_perm)
    condition4 = left_is_correct(digits_perm)

    if condition1 and condition2 and condition3 and condition4:
        print(digits_perm)
        exit()
    

for i, perm in enumerate(permutations(digits, 8)):
    print(i)
    is_correct(perm)
    

