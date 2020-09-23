# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# Approach 1: Use a map/dict to store the counts of each character. Use this approach if the chars in the str are wildly varying, .i.e string contains all chars in the unicode spectrum
# Approach 2: Use an array of fixed length to store counts. Use this approach if the string contains only small set of chars (All lower or all upper or just a mix of upper and lower case)
# Approach 3: Since we cannot use any additional data structures in the second part of the question, Use the bits of an integer to flag occurance of a char 

import collections 

def is_unique_1(s):
    counts_dict = collections.Counter(s)
    for chars in counts_dict:
        if counts_dict[chars] > 1:
            return False
    return True

def is_unique_2(s):
    counts = [0] * 26
    for chars in s:
        index = ord(chars)-ord('a')
        if counts[index] > 0:
            return False
        counts[index] += 1
    return True

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# There are much more elegant ways to do this. Find them before you post this
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def is_unique_3(s):
    counts = 0
    def flip_bit(bit_to_flip, counts):
        flipper = 1
        mask = 1 << bit_to_flip
        if mask & counts > 0:
            return -1
        flipper = flipper << bit_to_flip
        counts = counts + flipper
        return counts
        
    for chars in s:
        index = ord(chars) - ord('a')
        res = flip_bit(index, counts)
        if res < 0:
            return False
        else:
            counts = res
    return True

functions = [is_unique_1, is_unique_2, is_unique_3]
for f in functions:
    print(f("hello"))
    print(f("helo"))
    print(f(""))