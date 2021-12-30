#
# Author: Papi Diagne
#

from math import log10,floor
def next_different_int(n):
    if n<9:
        return n+1
    num_digits = floor(log10(n))+1
    first_digit = (n//10**(num_digits-1))
    str_num = str(n)

    while str(first_digit) in str_num and first_digit<9:
        first_digit+=1

    if str(first_digit) in str(str_num):
        next_power = 1
        while str(next_power) in str_num and next_power<n//10**(num_digits-1):
            next_power+=1
        if str(next_power) in str_num:
            return("Impossible") # Our number contains all possible digits
        second_digit = 0
        while str(second_digit) in str_num and second_digit<9:
            second_digit+=1
        if str(second_digit) in str_num:
            return "Impossible"
        output = str(next_power*10+second_digit)
    else:
        output = str(first_digit)

    # [1,num_digits[ other digits
    for i in range(1,num_digits):
        j = 0
        while str(j) in str_num and j<9:
            j+=1
        output+=str(j)
    for i in output:
        if i in str_num:
            return "Impossible"

    return int(output)

print(next_different_int(12)) #Output: 30