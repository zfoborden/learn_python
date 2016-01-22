# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

import math
import copy


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    text = text.lower()
    candidate_palindromes = find_pairs(text)
    find_palindromes(candidate_palindromes)

    return None


def find_pairs(text):
    pairs = []
    odd = False if len(text) % 2 == 0 else int(math.ceil((float(len(text))) / 2))
    for i, a in enumerate(text):
        for j, b in reversed(list(enumerate(text))):
            if ((odd != 0 and i == odd and j == odd) or i != j) and text[i] == b:
                pairs.append([i, j])

    return pairs


def find_palindromes(candidates):
    found = False
    length = len(candidates)
    for i, a in enumerate(candidates):
        print a
        for j, b in enumerate(reversed(candidates)):
            if a == b:
                newKey = copy.copy(j)
                expected = [a[0], b[1] - 1]
                for c in candidates[i:j]:
                    if candidates[i + 1] == candidates[j - 1]:
                        pass
            else:
                pass

    return found


def test():
    l = longest_subpalindrome_slice
    #assert l('racecar') == (0, 7)
    #assert l('Racecar') == (0, 7)
    #assert l('RacecarX') == (0, 7)
    #assert l('Race carr') == (7, 9)
    #assert l('') == (0, 0)
    assert l('something rac e car going') == (8, 21)
    assert l('xxxxx') == (0, 5)
    assert l('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
