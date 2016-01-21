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


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    text = text.lower()
    candidate_palindromes = find_pairs(text)
    print candidate_palindromes
    for candidate in candidate_palindromes:
        first = candidate[0]
        last = candidate[1] + 1
        t = text[first:last]
        if find_palindromes(t):
            return first, last
    return None


def find_pairs(text):
    pairs = []
    #reverse = text[::-1]
    for i, a in enumerate(text):
        for j, b in reversed(list(enumerate(text))):
            print j, b
            if i != j and text[i] == b:
                pairs.append([i, j])

    return pairs


def find_palindromes(text):
    reverse = text[::-1]
    return text == reverse


def test():
    l = longest_subpalindrome_slice
    #assert l('racecar') == (0, 7)
    #assert l('Racecar') == (0, 7)
    assert l('RacecarX') == (0, 7)
    assert l('Race carr') == (7, 9)
    assert l('') == (0, 0)
    assert l('something rac e car going') == (8, 21)
    assert l('xxxxx') == (0, 5)
    assert l('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
