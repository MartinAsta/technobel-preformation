'''
Help the book seller
Description
A bookseller has lots of books classified in 26 categories labeled A, B, C, ..., Z. Each book has a code of at least 3 characters. The 1st character of a code is a capital letter which defines the book category.

In the bookseller's stocklist each code is followed by a space and by a positive integer, which indicates the quantity of books of this code in stock.

Task
You will receive the bookseller's stocklist and a list of categories. Your task is to find the total number of books in the bookseller's stocklist, with the category codes in the list of categories. Note: the codes are in the same order in both lists.

Return the result as a string described in the example below, or as a list of pairs (Haskell/Clojure/Racket/Prolog).

If any of the input lists is empty, return an empty string, or an empty array/list (Clojure/Racket/Prolog).

Example
the bookseller's stocklist:
["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]

list of categories:
["A", "B", "C", "W"]

result:
(A : 20) - (B : 114) - (C : 50) - (W : 0)

Explanation:
category A: 20 books (ABART)
category B: 114 books = 25 (BKWRK) + 89 (BTSQZ)
category C: 50 books (CDXEF)
category W: 0 books
'''
def ex1(stocklist:list,categories:list) -> dict:
    res = {}
    for i in categories:
        res[i[0]] = 0
    for s in stocklist:
        book,count = s.split()
        count = int(count)
        category = book[0]
        if res.get(category) != None: 
            res[book[0]] += count
    return res

#print(ex1(["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"],["A", "B", "C", "W"]))

'''
Exercise: Deadfish Parser
Description
Create a parser to interpret and execute the Deadfish programming language.

Deadfish operates on a single integer value in memory, which is initially set to 0.

Commands
The language uses the following single-character commands:

i : Increment the value by 1
d : Decrement the value by 1
s : Square the value
o : Output the current value (add it to a result list)
All other characters should be ignored and have no effect.

Task
Write a function that:

Takes a string representing a Deadfish program as input
Processes each character one by one
Updates the value accordingly
Returns a list of all values produced by the o command
Output
Return a list (or array) of integers corresponding to each o command
If there are no o commands, return an empty list
Examples
Example 1
Input: "iiisdoso" Output: [8, 64]

Example 2
Input: "iiisdosodddddiso" Output: [8, 64, 3600]

Explanation (Example 1)
Start value = 0

i → 1 i → 2 i → 3 s → 9 d → 8 o → output 8 s → 64 o → output 64

Result:

[8, 64]
'''

def ex2(command:str) -> list:
    res = []
    val = 0
    for c in command:
        if c == "i":
            val += 1
        elif c == "d":
            val -= 1
        elif c == "s":
            val **= 2
        elif c == "o":
            res.append(val)
    return res

#print(ex2("iiisdosodddddiso"))

'''
Exercise: Find the Missing Term in an Arithmetic Progression
Description
An Arithmetic Progression (AP) is a sequence of numbers in which the difference between consecutive terms is constant.

You are given a list of numbers that are consecutive elements of an Arithmetic Progression. However, exactly one term is missing from the sequence.

The given list still follows the same order as the original sequence, but one value is missing somewhere in the middle.

Task
Write a function that:

Takes a list of integers as input
Finds and returns the missing number in the sequence
Constraints
The list will contain at least 3 numbers
The missing term will never be the first or the last element
The sequence always follows a valid arithmetic progression
Example
Input: [1, 3, 5, 9, 11] Output: 7

Explanation
The correct sequence should be:

1, 3, 5, 7, 9, 11

The common difference is +2, and the missing number is 7.
'''

def ex3(sequence:list) -> int:
    left = 0
    right = len(sequence) - 1
    mid = (left + right) // 2

    progression = min(abs(sequence[1] - sequence[0]),abs(sequence[right] - sequence[right - 1]))
    progression *= -1 if sequence[0] > sequence[right] else 1
    
    while left < right:
        if sequence[mid+1] != sequence[mid] + progression:
            return sequence[mid] + progression
        elif mid * progression + sequence[0] == sequence[mid]:
            left = mid
        else:
            right = mid
        mid = (left + right) // 2

#print(ex3([1, 4, 7, 10, 13, 16, 19, 22, 28]))

'''
Exercise: Sum of Pairs
Description
Given a list of integers and a target sum, find the first pair of numbers that add up to the given sum.

The pair must be selected by scanning the list from left to right.

Task
Write a function that:

Takes a list of integers
Takes a target sum value
Returns the first pair of numbers that add up to the target
Rules
The result must be a list (or array) containing exactly two numbers
The numbers must appear in the same order as in the original list
If multiple valid pairs exist, return the one whose second element has the smallest index
If no pair adds up to the target sum, return None (or equivalent)
Constraints
The input list may contain negative numbers
The input list may contain duplicate values
The list size can be very large, so your solution must be efficient
(Indice: Utiliser un set)

Examples
Example 1
Input: [11, 3, 7, 5], target = 10 Output: [3, 7]

Example 2
Input: [4, 3, 2, 3, 4], target = 6 Output: [4, 2]

Example 3
Input: [0, 0, -2, 3], target = 2 Output: None

Example 4
Input: [10, 5, 2, 3, 7, 5], target = 10 Output: [3, 7]
'''
def ex4(nums:list, target:int) -> list:
    seen = set()
    for n in nums:
        if target - n in seen:
            return [n, target-n]
        seen.add(n)

#print(ex4([11, 3, 7, 5],10))

'''Exercise: Sum of Parts
Description
Given a list of integers, consider all its "parts" obtained by successively removing elements from the beginning of the list.

For each part, compute the sum of its elements.

Task
Write a function that:

Takes a list of integers ls as input
Returns a list containing the sums of all parts of ls
Definition
The parts of a list are defined as follows:

The original list
The list without its first element
The list without its first two elements
...
The empty list
Output
Return a list of integers representing the sums of each part
The last element of the result must always be 0 (sum of the empty list)
Examples
Example 1
Input: [0, 1, 3, 6, 10] Output: [20, 20, 19, 16, 10, 0]

Example 2
Input: [1, 2, 3, 4, 5, 6] Output: [21, 20, 18, 15, 11, 6, 0]

Example 3
Input: [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358] Output: [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]

Notes
The input list may contain a large number of elements
Your solution should be efficient (avoid recalculating sums repeatedly)
'''
def ex5(input:list) -> list:
    total = 0
    res = [total]
    for i in range(len(input)-1,-1,-1):
        total += input[i]
        res.insert(0,total)
    return res

#print(ex5([1, 2, 3, 4, 5, 6]))

'''Bracket Matcher
Create a function BracketMatcher(str) that takes a string str as input and returns 1 if the parentheses in the string are correctly matched and properly nested. Otherwise, return 0.

Rules
A string is considered valid if: - Every opening parenthesis ( has a corresponding closing parenthesis ) - Parentheses are closed in the correct order

If the string contains no parentheses, return 1.

Examples
Input:
"(hello (world))"
Output:
1

Input:
"((hello (world))"
Output:
0

Input:
"(coder)(byte))"
Output:
0

Input:
"(c(oder)) b(yte)"
Output:
1
'''
def ex6() -> None:
    pass