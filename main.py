########## Problems ##########

# 1. Write a recursive function to calculate the factorial of a number.
# Remember, factorial(n) = n * factorial(n-1), and factorial(0) = 1


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return (n * factorial(n - 1))

#print(factorial(1))
# big-O: T(n) = {3, n <= 0; n * T(n-1), n > 0}

# 2. Implement a recursive function to compute the nth Fibonacci number.
# The Fibonacci sequence is defined as: fib(n) = fib(n-1) + fib(n-2), with fib(0) = 0 and fib(1) = 1


def fibonacci(n: int) -> int:
    if (n == 1):
        return 0
    elif (n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(4))
# big-O: T(n) = {3, n <= 2; T(n-1) + T(n-2), n > 2}

# T(n) = T(n-1) + T(n-2) + 1

# fibonacci is increasing means that T(n-2) < T(n-1)

# T(n) = T(n-1) + T(n-2) + 1 < T(n-1) + T(n-1) + 1 = 2*T(n-1) + 1 = 2^n

# 3. Create a recursive function to calculate the sum of all numbers from 1 to n.

def sum_to_n(n: int) -> int:
    if (n == 1):
        return n
    else:   
        return n + sum_to_n(n-1)

#print(sum_to_n(4))
# big-O: T(n) = {3, n <= 1, n + T(n-1), n > 1}

# 4. Write a recursive function to reverse a string.

def reverse_string(s: str) -> str:
    if (len(s) == 0):
        return ''
    else:
        # we know this is a recursive call/step
        # what is argument of the recursive call?
        # the argument should get us closer to the base case
        return s[-1] + reverse_string(s[:-1])


#print(reverse_string("hello"))
# big-O: T(n) = {3, n = 0; 1 + T(n-1), n > 0)}

# 5. Implement a recursive binary search function.
# Assume the input list is sorted in ascending order.
# Return the index of the target element (or -1 if it is absent).

# binary_search(arr, target):
#     left, right = 0, len(arr)-1 
#     while left <= right:
#         mid = (left + right)/2
#         if (arr[mid] == target):
#             return mid
#         elif arr[mid] > target:
#             left = mid
#         else:
#             right = mid
#     return -1

def binary_search(arr: list, target: int):
    mid = len(arr)//2
    
    if (len(arr) == 0):
        return -float('inf')
    elif (arr[mid] == target):
        return mid
    elif(arr[mid] > target):
        return binary_search(arr[:mid], target)
    else:
        return (mid + 1) + binary_search(arr[mid+1:], target)

# T(0) = 3
# T(n) = 2 + T(n/2)
#
# For iterative version:
# T(n) = 3 * log2(n)

# n / 2^x = 1
# n = 2^x
# x = log2(n)

# 6. Create a recursive function to calculate the power of a number (x^n).


def power(x: float, n: int) -> float:
    if (n == 0):
        return 1
    else:
        return x * power(x, n-1)


#print(power(2, 3))
# big-O: T(n) = {3, n = 0; 1 + T(n-1), n > 0}


# 7. Implement a recursive function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
#
# The Euclidean algorithm for finding the GCD of two numbers a and b is based on the principle that
# the greatest common divisor of two numbers does not change if the smaller number is subtracted
# from the larger number. See if you can take it from there (what are the base cases?).


def gcd(a: int, b: int) -> int:
    if(a == b):
       return a
    elif (a < b):
       return gcd(a, b - a)
    else:
        return gcd(a - b, n)


# a - b = c         > a, b, and c are all integers
# da' - db' = c     > d is any divisor of a and b, so a' and b' are whole numbers'
# d(a' - b') = c    > reverse distribution
# a' - b' = c/d     > a' and b' are whole numbers, so c/d is a whole number. Therefore d divides c.

#print(gcd(19, 36))
# big-O: O(n)
# T(1) = 1
# T(n) = T(n-1) + 1

# 8. Write a recursive function to generate all possible permutations (ways of ordering the elements) of a string.


def permutations(s: str) -> list[str]: # "abc" ->  ["cab", "acb", "abc", "cba", "bca", "bac"]
    if (len(s) == 0):
        return [""]
    else:
        char = s[0] # "c"
        small_perms = permutations(s[1:]) # "ab" ->  ["ab", "ba"]
        # "ab" -> "cab", "acb", "abc"
        # "ba" -> "cba", "bca", "bac"
        big_perms = []
        for i in range(len(s)):
            for perm in small_perms:
                big_perms.append(perm[:i] + char + perm[i:])

        return big_perms


s = "my string"
new_s = s[:2] + " new" + s[2:]
#print(s)
#print(new_s)

# permutations of abcd
#
#                a            b                 c
#     ab         ac      ad    ba     bc          ca    cb
#  abc  abd    acb  acd        acb  acd   bac     bca        cab    cba  
# abcd  abdc  acbd  acdb  adbc  adcb    

# 'obvious' ways of reducing inputs
# list (base is empty list): pop/remove the first or last element
# integer (base is 0 or 1): subtract one, divide by 2
# string (base is empty string): remove the first or last character

# permutations("abc") -> ["cab", "acb", "abc", "cba", "bca", "bac"]
# permutations("ab") -> ["ab", "ba"]

#permutations("ab"))
#print(len(permutations("abcdef")))
# big-O: 
# T(0) = 3
# T(n) = 3 + (n * n!)(4) + 1

# T(n) ~ 1! + 2! + 3! + ... + n!

# T(n) = 1 + T(n-1) + 1 + n*(n-1)!*3 = T(n-1) + 2 + 3*n!

# O(n*n!)

# 9. Create a recursive function to solve the Tower of Hanoi puzzle.
# The function should print the steps to move n disks from source to destination using an auxiliary peg.
#
# The Tower of Hanoi is a classic problem in computer science and mathematics:
# - There are three pegs (usually labeled A, B, and C) and n disks of different sizes.
# - Initially, all disks are stacked on the source peg (A) in order of decreasing size, with the largest at the bottom.
# - The goal is to move all disks to the destination peg (C) while following these rules:
#   1. Only one disk can be moved at a time.
#   2. Each move consists of taking the upper disk from one stack and placing it on top of another stack or an empty peg.
#   3. No larger disk may be placed on top of a smaller disk.
#
# This problem is tricky, don't spend too much time attempting it along.


def tower_of_hanoi(n: int, start: str, end: str, aux: str) -> None:
    if (n == 1):
        return print(f"move {start} to {end}")
    else:
        tower_of_hanoi(n-1, start, aux, end)
        tower_of_hanoi(1, start, end, aux)
        tower_of_hanoi(n-1, aux, end, start)

#tower_of_hanoi(3, "A", "C", "B")

# big - O: T(0) = 3
# T(1) = 1
# T(n) = T(n-1) + T(1) + T(n-1) = 2*T(n-1) + 1

# 10. Implement a recursive function to check if a given string is a palindrome.

def is_palindrome(s: str) -> bool:
    if (len(s) == 0 or len(s) == 1):
        return True
    elif (s[0] != s[-1]):
        return False
    else:
        return is_palindrome(s[1:-1])

#print(is_palindrome("cac"))
# big-O: T(0) = {5}
# T(0) = 1
# T(n) = T(n-2) + 1

def substrings(s) -> list[str]: # we need ["", "b", "c", "bc", "a", "ab", "ac", "abc"]

    if (len(s) == 0):
        return ['']
    else:
        char = s[0]
        all_str = []

        rec_result = substrings(s[1:]) # we get ["", "b", "c", "bc"]

        for str in rec_result:
            all_str.extend([str, char + str])
            
        return all_str
        
print(substrings("abcde")) 

# Recursion Diagram:

# Function Calls:
# > "abc"
#    > "bc"
#        > "c"
#            > ""

# Function Returns:
#            > ['']
#        > ['', 'c']
#    > ['', 'b', 'c', 'bc']
# > ['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']


# "abc" -> ["", "b", "c", "bc", "a", "ab", "ac", "abc"]
# "bc"  -> ["", "b", "c", "bc"]

# abc
# 000
# 100
# 
