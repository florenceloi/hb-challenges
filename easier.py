def is_anagram_of_palindrome1(word):
    """Is the word an anagram of a palindrome?

    >>> is_anagram_of_palindrome1("a")
    True

    >>> is_anagram_of_palindrome1("ab")
    False

    >>> is_anagram_of_palindrome1("aab")
    True

    >>> is_anagram_of_palindrome1("arceace")
    True

    >>> is_anagram_of_palindrome1("arceaceb")
    False

    """

    if len(word) == 1:
        return True

    unique_chars = {w: 0 for w in word}

    for w in word:
        unique_chars[w] += 1

    one_counter = 0

    for count in unique_chars.values():
        if count != 2 and count != 1:
            return False
        elif count == 2:
            continue
        elif count == 1:
            one_counter += 1

    if one_counter > 1:
        return False
    else:
        return True


def is_anagram_of_palindrome2(word):
    """Is the word an anagram of a palindrome?

    >>> is_anagram_of_palindrome2("a")
    True

    >>> is_anagram_of_palindrome2("ab")
    False

    >>> is_anagram_of_palindrome2("aab")
    True

    >>> is_anagram_of_palindrome2("arceace")
    True

    >>> is_anagram_of_palindrome2("arceaceb")
    False

    """

    if len(word) == 1:
        return True

    unique_chars = {}

    for letter in word:
        count = unique_chars.get(letter, 0)
        unique_chars[letter] = count + 1

    one_counter = 0

    for count in unique_chars.values():
        if count != 2 and count != 1:
            return False
        elif count == 2:
            continue
        elif count == 1:
            one_counter += 1

    if one_counter > 1:
        return False
    else:
        return True


###############################################################################
def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31)
    4

    >>> max([binary_search(i) for i in range(1, 101)])
    7

    """

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    higher_than = 0
    lower_than = 101
    guess = None
    # import pdb; pdb.set_trace()
    while guess != val:
        num_guesses += 1
        guess = (lower_than - higher_than) / 2 + higher_than

        if val > guess:
            higher_than = guess

        elif val < guess:
            lower_than = guess

    return num_guesses


###############################################################################
def count_recursively(lst):
    """Return number of items in a list, using recursion.

    >>> count_recursively([])
    0

    >>> count_recursively([1, 2, 3])
    3

    """

    if not lst:
        return 0

    return 1 + count_recursively(lst[1:])


###############################################################################
def decode(s):
    """Decode a string.

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

    >>> decode("0h1ae2bcy")
    'hey'

    """
    word = ""

    for char in s:
        if char in "0123456789":
            new_char_index = s.index(char) + int(char) + 1
            word += s[new_char_index]

    return word


###############################################################################
def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8

    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8

    """

    seen = [False] * max_num

    for num in nums:
        seen[num - 1] = True

    return seen.index(False) + 1


def missing_number2(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number2([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8

    >>> missing_number2([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8

    """

    nums.sort()

    counter = 1

    while counter != max_num:
        if nums[counter - 1] != counter:
            return counter
        counter += 1


def missing_number3(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number3([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8

    >>> missing_number3([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8

    """

    expected_sum = (max_num + 1) * (max_num / 2)

    return expected_sum - sum(nums)


###############################################################################
def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'

    >>> pig_latin('porcupine are cute')
    'orcupinepay areyay utecay'

    >>> pig_latin('give me an apple')
    'ivegay emay anyay appleyay'
    """

    words = phrase.split(" ")

    pl_list = []

    for word in words:
        if word[0] in "aeiou":
            new_word = word + "yay"
        else:
            new_word = word[1:] + word[0] + "ay"
        pl_list.append(new_word)

    return " ".join(pl_list)


###############################################################################
def is_prime(num):
    """Is num a prime number?

    num will always be a positive integer.

    >>> is_prime(0)
    False

    >>> is_prime(1)
    False

    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False

    >>> is_prime(7)
    True

    >>> is_prime(25)
    False

    """

    assert num >= 0, "Num should be a positive integer!"

    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    n = 3

    while n * n <= num:

        if num % n == 0:
            return False

        n += 2

    return True


def primes(count):
    """Return count number of prime numbers, starting at 2.

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

    """

    primes = []

    if count >= 1:
        primes.append(2)

    n = 3

    while len(primes) < count:

        if is_prime(n):
            primes.append(n)

        n += 2

    return primes


###############################################################################
def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place.

    >>> print_digits(1)
    1

    >>> print_digits(314)
    4
    1
    3

    >>> print_digits(12)
    2
    1

    """

    while num:
        print num % 10

        num = num / 10


###############################################################################
def print_recursively(lst):
    """Print items in the list, using recursion.

    >>> print_recursively([1, 2, 3])
    1
    2
    3

    """

    if lst:
        print lst[0]

        print_recursively(lst[1:])


###############################################################################
def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

    >>> lst = ["hey", "there", "you"]

    >>> recursive_index("hey", lst)
    0

    >>> recursive_index("you", lst)
    2

    >>> recursive_index("porcupine", lst) is None
    True

    """

    def _recursive_index(needle, haystack, start_at):

        if start_at == len(haystack):
            return None

        if haystack[start_at] == needle:
            return start_at

        return _recursive_index(needle, haystack, start_at + 1)

    return _recursive_index(needle, haystack, 0)


# ###############################################################################
# class Node(object):
#     """Class in a linked list."""

#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

#     def as_string(self):
#         """Represent data for this node and its successors as a string.

#         >>> Node(3).as_string()
#         '3'

#         >>> Node(3, Node(2, Node(1))).as_string()
#         '321'
#         """

#         out = []
#         n = self

#         while n:
#             out.append(str(n.data))
#             n = n.next

#         return "".join(out)


# def remove_node(node):
#     """Given a node in a linked list, remove it.

#     Remove this node from a linked list. Note that we do not have access to
#     any other nodes of the linked list, like the head or the tail.

#     Does not return anything; changes list in place.
#     """

#     if not node.next:
#         raise ValueError("Cannot remove tail node")

#     node.data = node.next.data
#     node.next = node.next.next


# def reverse_linked_list(head):
#     """Given LL head node, return head node of new, reversed linked list.

#     >>> ll = Node(1, Node(2, Node(3)))
#     >>> reverse_linked_list(ll).as_string()
#     '321'
#     """

#     out_head = None
#     n = head

#     while n:
#         out_head = Node(n.data, out_head)
#         n = n.next

#     return out_head


###############################################################################
class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    """Linked list."""

    def __init__(self, head=None):
        self.head = head

    def as_string(self):
        """Represent data for this list as a string.

        >>> LinkedList(Node(3)).as_string()
        '3'

        >>> LinkedList(Node(3, Node(2, Node(1)))).as_string()
        '321'

        """

        out = []
        n = self.head

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


def reverse_linked_list_in_place(lst):
    """Given linked list, reverse the nodes in this linked list in place.

    >>> ll = LinkedList(Node(1, Node(2, Node(3))))

    >>> reverse_linked_list_in_place(ll)

    >>> ll.as_string()
    '321'

    """

    prev = None
    curr = lst.head

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    lst.head = prev


###############################################################################
def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list.

    >>> lst = [1, 2, 3, 4, 6, 8]

    >>> show_evens(lst)
    [1, 3, 4, 5]

    """

    out = []

    for i, num in enumerate(nums):
        if num % 2 == 0:
            out.append(i)

    return out


###############################################################################
def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().

    >>> a = [1, 3, 5, 7]
    >>> b = [2, 6, 8, 10]

    >>> sort_ab(a, b)
    [1, 2, 3, 5, 6, 7, 8, 10]

    """

    out = []

    while a and b:
        if a[0] < b[0]:
            num = a.pop(0)
        else:
            num = b.pop(0)
        out.append(num)

    while a or b:
        if a:
            out.extend(a)
            a = None
        else:
            out.extend(b)
            b = None

    return out


###############################################################################
def split(astring, splitter):
    """Split astring by splitter and return list of splits.

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

    """

    out = []
    index = 0

    while index <= len(astring):

        curr_index = index
        index = astring.find(splitter, index)

        if index != -1:
            out.append(astring[curr_index:index])
            index += len(splitter)

        else:
            out.append(astring[curr_index:])
            break

    return out


###############################################################################
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
