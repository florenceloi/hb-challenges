def calc(s):
    """Evaluate expression.

        ###########################################################################
        In this exercise, you'll build a "polish notation calculator".

        Polish notation is a different way to write an artithmetic expression.
        For example, instead of writing 1 + 2 * 3, as we would in normal
        ("infix") style, we could write it with the operators to the left of 
        their arguments. This expression would become + 1 * 2 3. You can read a
        polish notation expression backwards to see exactly what it does - in 
        this case, multiply 2 times 3, and add that result to 1.
        ###########################################################################

        >>> calc("+ 1 2")           # 1 + 2
        3

        >>> calc("* 2 + 1 2")       # 2 * (1 + 2)
        6

        >>> calc("+ 9 * 2 3")       # 9 + (2 * 3)
        15

        >>> calc("- 1 2")           # 1 - 2
        -1

        >>> calc("- 9 * 2 3")       # 9 - (2 * 3)
        3

        >>> calc("/ 6 - 4 2")       # 6 / (4 - 2)
        3
    """

    tokens = s.split(" ")

    operand2 = int(tokens.pop())

    while tokens:
        operand1 = int(tokens.pop())
        operator = tokens.pop()

        if operator == "+":
            operand2 = operand1 + operand2

        elif operator == "-":
            operand2 = operand1 - operand2

        elif operator == "*":
            operand2 = operand1 * operand2

        elif operator == "/":
            operand2 = operand1 / operand2

    return operand2


# ###############################################################################
# def check(king, queen):
#     """Given a chessboard with one K and one Q, see if the K can attack the Q.

#     This function is given coordinates for the king and queen on a chessboard.
#     These coordinates are given as a letter A-H for the columns and 1-8 for the
#     row, like "D6" and "B7":

#     ###########################################################################
#     Given a chessboard with one K and one Q, see if the Q can attack the K.

#     This function is given coordinates for the king and queen on a chessboard.
#     These coordinates are given as a letter A-H for the columns and 1-8 for the
#     row (see below for example):

#     Queens can move in any direction: horizontally, vertically, or diagonally,
#     as far as possible.

#     This function returns True if the king is in the line of attack of the queen.

#     For example, the first set of boards, Under Attack, show the king under attack.
#     ###########################################################################

#     >>> check("D6", "H6")
#     True

#     >>> check("E6", "E4")
#     True

#     >>> check("B7", "D5")
#     True

#     >>> check("A1", "H8")
#     True

#     >>> check("A8", "H1")
#     True

#     >>> check("D6", "H7")
#     False

#     >>> check("E6", "F4")
#     False
#     """


# ###############################################################################
# # Check Tree Balance

# class BinaryNode(object):
#     """Node in a binary tree."""

#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right

#     def is_balanced(self):
#         """Is the tree at this node balanced?"""


# ###############################################################################
# def coins(num_coins):
#     """Find change from combinations of `num_coins` of dimes and pennies.

#     This should return a set of the unique amounts of change possible.

#     ###########################################################################
#     You have an endless supply of dimes and pennies. How many different amounts
#     of total change can you make using exactly num_coins number coins?

#     For example, when num_coins = 3, you can create 4 different kinds of change:

#     3 cents from penny + penny + penny
#     12 cents dime + penny + penny
#     21 cents from dime + dime + penny
#     30 cents from dime + dime + dime
#     So, you should have a function that returns the set {3, 12, 21, 30} when
#     num_coins is 3.
#     ###########################################################################

#     >>> coins(1) == {1, 10}
#     True

#     >>> coins(2) == {2, 11, 20}
#     True

#     >>> coins(3) == {3, 12, 21, 30}
#     True

#     >>> coins(4) == {4, 13, 22, 31, 40}
#     True

#     >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
#     True
#     """


# ###############################################################################
# # Count Employees

# class Node(object):
#     """Node in a tree."""

#     def __init__(self, name, children=None):
#         self.name = name
#         self.children = children or []

#     def count_employees(self):
#         """Return a count of how many employees this person manages.

#         Return a count of how many people that manager manages. This should
#         include *everyone* under them, not just people who directly report to
#         them.
#         """

# ###############################################################################
def dec2bin(num):
    """Convert a decimal number to binary representation.

    >>> dec2bin(4)
    '100'

    >>> dec2bin(6)
    '110'
    """

    out = []
    place = 0

    # while loop just starting or dec num still larger than bin num
    while place == 0 or num >= 2 ** place:

        # if non-zero mod when dividing by increasing power of 2
        if num % 2 ** (place + 1):
            num -= 2 ** place
            out.append("1")

        else:
            out.append("0")

        place += 1

    return "".join(reversed(out))


def dec2bin2(num):
    """Convert a decimal number to binary representation.

    >>> dec2bin2(4)
    '100'

    >>> dec2bin2(6)
    '110'
    """

    out = ""

    num_bits = 1

    while 2 ** num_bits <= num:
        num_bits += 1

    for position in range(num_bits - 1, -1, -1):

        if 2 ** position <= num:
            num -= 2 ** position
            out += "1"

        else:
            out += "0"

    return out


# ###############################################################################
# # Friends

# class PersonNode(object):
#     """A node in a graph representing a person.

#     This is created with a name and, optionally, a list of adjacent nodes.
#     """

#     def __init__(self, name, adjacent=[]):
#         self.name = name
#         self.adjacent = set(adjacent)

#     def __repr__(self):
#         return "<PersonNode %s>" % self.name

# class FriendGraph(object):
#     """Graph to keep track of social connections."""

#     def __init__(self):
#         """Create an empty graph.

#         We keep a dictionary to map people's names -> nodes.
#         """

#         self.nodes = {}

#     def add_person(self, name):
#         """Add a person to our graph.

#             >>> f = FriendGraph()
#             >>> f.nodes
#             {}

#             >>> f.add_person("Dumbledore")
#             >>> f.nodes
#             {'Dumbledore': <PersonNode Dumbledore>}
#         """

#         if name not in self.nodes:
#             # Be careful not to just add them a second time -- otherwise,
#             # if we accidentally added someone twice, we'd clear our their list
#             # of friends!
#             self.nodes[name] = PersonNode(name)

#     def set_friends(self, name, friend_names):
#         """Set two people as friends.

#         This is reciprocal: so if Romeo is friends with Juliet, she's
#         friends with Romeo (our graph is "undirected").

#         >>> f = FriendGraph()
#         >>> f.add_person("Romeo")
#         >>> f.add_person("Juliet")
#         >>> f.set_friends("Romeo", ["Juliet"])

#         >>> f.nodes["Romeo"].adjacent
#         set([<PersonNode Juliet>])

#         >>> f.nodes["Juliet"].adjacent
#         set([<PersonNode Romeo>])
#         """

#         person = self.nodes[name]

#         for friend_name in friend_names:
#             friend = self.nodes[friend_name]

#             # Since adjacent is a set, we don't care if we're adding duplicates --
#             # it will only keep track of each relationship once. We do want to
#             # make sure that we're adding both directions for the relationship.
#             person.adjacent.add(friend)
#             friend.adjacent.add(person)

#     def are_connected(self, name1, name2):
#         """Is this name1 friends with name2?

#         >>> f = FriendGraph()
#         >>> f.add_person("Frodo")
#         >>> f.add_person("Sam")
#         >>> f.add_person("Gandalf")
#         >>> f.add_person("Merry")
#         >>> f.add_person("Pippin")
#         >>> f.add_person("Treebeard")
#         >>> f.add_person("Sauron")
#         >>> f.add_person("Dick Cheney")

#         >>> f.set_friends("Frodo", ["Sam", "Gandalf", "Merry", "Pippin"])
#         >>> f.set_friends("Sam", ["Merry", "Pippin", "Gandalf"])
#         >>> f.set_friends("Merry", ["Pippin", "Treebeard"])
#         >>> f.set_friends("Pippin", ["Treebeard"])
#         >>> f.set_friends("Sauron", ["Dick Cheney"])

#         >>> f.are_connected("Frodo", "Sam")
#         True

#         >>> f.are_connected("Sam", "Frodo")
#         True

#         >>> f.are_connected("Sam", "Treebeard")
#         True

#         >>> f.are_connected("Frodo", "Sauron")
#         False
#         """


# ###############################################################################
# def hex_convert(hex_in):
#     """Convert a hexadecimal string, like '1A', into it's decimal equivalent.

#     >>> hex_convert('6')
#     6

#     >>> hex_convert('1A')
#     26

#     >>> hex_convert('FFFF')
#     65535
#     """


# ###############################################################################
# def insertion_sort(alist):
#     """Given a list, sort it using insertion sort."""


###############################################################################
# Josephus Surviviors

class Node(object):
    """Doubly-linked node."""

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return "<Node prev=%s data=%s next=%s>" % (
            self.prev.data, self.data, self.next.data)

    @classmethod
    def make_list(cls, n):
        """Construct a circular doubly-linked list of n items. Returns head node.

            >>> node = Node.make_list(3)

            >>> node.data
            1

            >>> node.next.data
            2

            >>> node.next.next.next.data
            1

            >>> node.prev.data
            3

            >>> node.prev.prev.prev.data
            1
        """

        first = node = prev = cls(1)

        for i in range(2, n+1):
            node = Node(i, prev=prev)
            prev.next = node
            prev = node

        last = node

        first.prev = last
        last.next = first

        return first


def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor.

        >>> find_survivor(10, 3)
        4
    """

    node = Node.make_list(num_people)

    while node.next != node:

        for i in range(kill_every - 1):
            node = node.next

        node.prev.next = node.next
        node.next.prev = node.prev

        node = node.next

    return node.data


# ###############################################################################
# def largest_sum(nums):
#     """Find subsequence with largest sum.

#     >>> my_list = [1, 0, 3, -8, 4, -2, 3]

#     >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
#     [4, -2, 3]

#     >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
#     [4, -2, 3]

#     >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
#     [19]

#     >>> largest_sum([2, 2, -10, 1, 3, -20])
#     [2, 2]

#     >>> largest_sum([2, -2, 3, -1])
#     [3]

#     >>> largest_sum([-1, -2])
#     []
#     """


# ###############################################################################
# # Make Binary Search Tree

# # Use class BinaryNode defined on line 86

# def make_bst(nums):
#     """Given a list of sorted numbers, make a binary search tree.

#     Returns the root node of a new BST that is valid and balanced.
#     """


# ###############################################################################
# def merge_sort(lst):
#     """Divide and conquer: reduce to lists of 0-1 items, then recombine."""


# ###############################################################################
# def find_most_anagrams_from_wordlist(wordlist):
#     """Given a list of words, return the word with the most anagrams.

#     >>> all_words = [w.strip() for w in open('words.txt')]

#     >>> find_most_anagrams_from_wordlist(all_words)
#     'angor'
#     """


# ###############################################################################
# def num_word(num):
#     """Convert word to number.

#     >>> num_word(0)
#     'zero'

#     >>> num_word(2)
#     'two'

#     >>> num_word(-2)
#     'negative two'

#     >>> num_word(11)
#     'eleven'

#     >>> num_word(20)
#     'twenty'

#     >>> num_word(100)
#     'one hundred'

#     >>> num_word(121)
#     'one hundred twenty one'

#     >>> num_word(1256)
#     'one thousand two hundred fifty six'

#     >>> num_word(100001)
#     'one hundred thousand one'

#     >>> num_word(1000000)
#     'one million'

#     >>> num_word(-1234567890)  
#     'negative one billion two hundred thirty four million
#     five hundred sixty seven thousand eight hundred ninety'

#     >>> num_word(999999999999)  
#     'nine hundred ninety nine billion nine hundred ninety nine million
#     nine hundred ninety nine thousand nine hundred ninety nine'
#     """


# ###############################################################################
# def one_away(w1, w2):
#     """Given two strings, are they, at most, one edit away?

#     >>> one_away("make", "fake")
#     True

#     >>> one_away("task", "take")
#     False

#     >>> one_away("ask", "asks")
#     True

#     >>> one_away("asks", "ask")
#     True
#     """


# ###############################################################################
# def rev(s):
#     """Reverse word-order in string, preserving spaces.

#     >>> rev("")
#     ''

#     >>> rev("hello")
#     'hello'

#     >>> rev("hello world")
#     'world hello'

#     >>> rev(" hello  world   ")
#     '   world  hello '
#     """


# ###############################################################################
# def to_roman(num):
#     """Converts positive integers to Roman numeral equivalent using Old-school style.

#     >>> to_roman(5)
#     'V'

#     >>> to_roman(267)
#     'CCLXVII'

#     >>> to_roman(99)
#     'LXXXXVIIII'
#     """

#     if num != int(num) or num > 4999 or num < 1:
#         raise ValueError("Cannot convert")


# ###############################################################################
# # SQL Managers


# ###############################################################################
# def time_word(time):
#     """Convert time to text.

#     >>> time_word("00:00")
#     'midnight'

#     >>> time_word("12:00")
#     'noon'

#     >>> time_word("01:00")
#     "one o'clock am"

#     >>> time_word("06:01")
#     'six oh one am'

#     >>> time_word("06:10")
#     'six ten am'

#     >>> time_word("06:18")
#     'six eighteen am'

#     >>> time_word("06:30")
#     'six thirty am'

#     >>> time_word("10:34")
#     'ten thirty four am'

#     >>> time_word("00:12")
#     'twelve twelve am'

#     >>> time_word("12:09")
#     'twelve oh nine pm'

#     >>> time_word("23:23")
#     'eleven twenty three pm'
#     """


# ###############################################################################
# # Tree Cousins

# class Node(object):
#     """Doubly-linked node in a tree.

#         >>> na = Node("na")
#         >>> nb1 = Node("nb1")
#         >>> nb2 = Node("nb2")

#         >>> nb1.set_parent(na)
#         >>> nb2.set_parent(na)

#         >>> na.children
#         [<Node nb1>, <Node nb2>]

#         >>> nb1.parent
#         <Node na>
#     """

#     parent = None

#     def __init__(self, data):
#         self.children = []
#         self.data = data

#     def __repr__(self):
#         return "<Node %s>" % self.data

#     def set_parent(self, parent):
#         """Set parent of this node.

#         Also sets the children of the parent to include this node.
#         """

#         self.parent = parent
#         parent.children.append(self)

#     def cousins(self):
#         """Find nodes on the same level as this node.

#         >>> b.cousins() == {c, d}
#         True

#         >>> c.cousins() == {b, d}
#         True

#         >>> e.cousins() == {f, g, h, i, j}
#         True

#         >>> k.cousins() == {l}
#         True

#         >>> a.cousins() == set()   # empty set
#         True
#         """


# ###############################################################################
# def zero_matrix(matrix):
#     """Given an NxM matrix, for cells=0, set their row and column to zeroes.

#     >>> zero_matrix([
#     ...    ['A', 'B', 'C', 'D'],
#     ...    ['E', 'F',  0 , 'H'],
#     ...    ['I', 'J', 'K', 'L']
#     ...    ])
#     [['A', 'B', 0, 'D'], [0, 0, 0, 0], ['I', 'J', 0, 'L']]
#     """


###############################################################################
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
