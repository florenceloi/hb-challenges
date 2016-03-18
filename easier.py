# def is_anagram_of_palindrome1(word):
#     """Is the word an anagram of a palindrome?

#     >>> is_anagram_of_palindrome1("a")
#     True

#     >>> is_anagram_of_palindrome1("ab")
#     False

#     >>> is_anagram_of_palindrome1("aab")
#     True

#     >>> is_anagram_of_palindrome1("arceace")
#     True

#     >>> is_anagram_of_palindrome1("arceaceb")
#     False

#     """

#     if len(word) == 1:
#         return True

#     unique_chars = {w: 0 for w in word}

#     for w in word:
#         unique_chars[w] += 1

#     one_counter = 0

#     for count in unique_chars.values():
#         if count != 2 and count != 1:
#             return False
#         elif count == 2:
#             continue
#         elif count == 1:
#             one_counter += 1

#     if one_counter > 1:
#         return False
#     else:
#         return True


# def is_anagram_of_palindrome2(word):
#     """Is the word an anagram of a palindrome?

#     >>> is_anagram_of_palindrome2("a")
#     True

#     >>> is_anagram_of_palindrome2("ab")
#     False

#     >>> is_anagram_of_palindrome2("aab")
#     True

#     >>> is_anagram_of_palindrome2("arceace")
#     True

#     >>> is_anagram_of_palindrome2("arceaceb")
#     False

#     """

#     if len(word) == 1:
#         return True

#     unique_chars = {}

#     for letter in word:
#         count = unique_chars.get(letter, 0)
#         unique_chars[letter] = count + 1

#     one_counter = 0

#     for count in unique_chars.values():
#         if count != 2 and count != 1:
#             return False
#         elif count == 2:
#             continue
#         elif count == 1:
#             one_counter += 1

#     if one_counter > 1:
#         return False
#     else:
#         return True


# def binary_search(val):
#     """Using binary search, find val in range 1-100. Return # of guesses.

#     >>> binary_search(50)
#     1

#     >>> binary_search(25)
#     2

#     >>> binary_search(75)
#     2

#     >>> binary_search(31)
#     4

#     >>> max([binary_search(i) for i in range(1, 101)])
#     7

#     """

#     assert 0 < val < 101, "Val must be between 1-100"

#     num_guesses = 0

#     higher_than = 0
#     lower_than = 101
#     guess = None
#     # import pdb; pdb.set_trace()
#     while guess != val:
#         num_guesses += 1
#         guess = (lower_than - higher_than) / 2 + higher_than

#         if val > guess:
#             higher_than = guess

#         elif val < guess:
#             lower_than = guess

#     return num_guesses


# def count_recursively(lst):
#     """Return number of items in a list, using recursion.

#     >>> count_recursively([])
#     0

#     >>> count_recursively([1, 2, 3])
#     3

#     """

#     if not lst:
#         return 0

#     return 1 + count_recursively(lst[1:])


# def decode(s):
#     """Decode a string.

#     >>> decode("0h")
#     'h'

#     >>> decode("2abh")
#     'h'

#     >>> decode("0h1ae2bcy")
#     'hey'

#     """
#     # import pdb; pdb.set_trace()
#     word = ""

#     for char in s:
#         if char in "0123456789":
#             new_char_index = s.index(char) + int(char) + 1
#             word += s[new_char_index]

#     return word


def missing_number_scan(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number_scan([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8
    """












































