'''
### Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method

result = []
for number in range(2000, 3201):
    if number % 7 == 0 and number % 5 != 0:
        result.append(str(number))
print(",".join(result))
    
'''

'''
### Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

number = int(input('enter a number:'))

def factorial(n):
    if n == 0 or n ==1:
        return 1 
    else:
        return n*factorial(n-1)
result = factorial(number)
print (result)
'''

'''
### Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

n=int(input("enter a number: "))

result_dict = {}

for i in range(1,n+1):
    result_dict[i] = i*i

print(result_dict)
'''

'''

### Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple


input_seuquence = (input("enter the desired sequence: "))

number_list = input_seuquence.split(',')
number_tuple = tuple(number_list)

print(number_list)
print(number_tuple)
'''

'''
### Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters


class StringManipulator:
    def _init_(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

# Test function
def testStringManipulator():
    manipulator = StringManipulator()
    manipulator.getString()
    manipulator.printString()

# Testing the class
testStringManipulator()

'''

'''
### Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24


import math

# Fixed values of C and H
C = 50
H = 30

# Taking input from the user
input_sequence = input("Enter , sep values of D: ")

# Splitting the input sequence into a list
values_of_D = input_sequence.split(',')

# Initializing an empty list to store the results
result = []

# Calculating Q for each value of D using a for loop
for D in values_of_D:
    Q = int(math.sqrt((2 * C * int(D)) / H))
    result.append(Q)

# Printing the output
print(','.join(map(str, result)))
'''
'''
### Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1,., X-1; j=0,1,..Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.


# Taking input from the user
input_str = input("Enter two digits X, Y (comma-separated): ")

# Extracting X and Y from the input
X, Y = map(int, input_str.split(','))

# Initializing an empty 2-dimensional array
result_array = []

# Using nested for loops to generate the array
for i in range(X):
    row = []
    for j in range(Y):
        row.append(i * j)
    result_array.append(row)

# Printing the output
print(result_array)
'''
'''

### Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

# Taking input from the user
input_sequence = input("Enter a comma-separated sequence of words: ")

# Splitting the input into a list of words
words_list = input_sequence.split(',')

# Sorting the words alphabetically
sorted_words = sorted(words_list)

# Printing the output
print(','.join(sorted_words))
'''

'''
### Question 9
Level 2

Question:

Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT


# Taking input from the user
input_lines = []

while True:
    line = input("Enter a line : ")
    if not line:
        break
    input_lines.append(line)

# Capitalizing all characters in each line using a for loop
capitalized_lines = []
for line in input_lines:
    capitalized_lines.append(line.upper())

# Printing the output
for capitalized_line in capitalized_lines:
    print(capitalized_line)
'''

'''
### Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.

# Taking input from the user
input_sequence = input("Enter a sequence of whitespace-separated words: ")

# Splitting the input into a list of words
words_list = input_sequence.split()

# Removing duplicates using a set and sorting alphanumerically
unique_sorted_words = sorted(set(words_list))

# Printing the output
print(' '.join(unique_sorted_words))

'''

'''
### Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

# Taking input from the user
input_sequence = input("Enter a sequence of comma-separated 4-digit binary numbers: ")

# Splitting the input into a list of binary numbers
binary_numbers = input_sequence.split(',')

# Checking for divisibility by 5 and creating a list of valid numbers
divisible_by_5 = [num for num in binary_numbers if int(num, 2) % 5 == 0]

# Printing the output
print(','.join(divisible_by_5))
'''

'''
### Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.


result = []

for num in range(1000, 3001):
    if all(int(digit) % 2 == 0 for digit in str(num)):
        result.append(str(num))

print(','.join(result))
'''

'''
### Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3


# Taking input from the user
sentence = input("Enter a sentence: ")

# Initializing counters for letters and digits
letters_count = 0
digits_count = 0

# Calculating the number of letters and digits
for char in sentence:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1

# Printing the output
print("LETTERS", letters_count)
print("DIGITS", digits_count)

'''
'''

### Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9


# Taking input from the user
sentence = input("Enter a sentence: ")

# Initializing counters for uppercase and lowercase letters
uppercase_count = 0
lowercase_count = 0

# Calculating the number of uppercase and lowercase letters
for char in sentence:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

# Printing the output
print("UPPERCASE", uppercase_count)

print("lowercase", lowercase_count)
'''
'''
### Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.


# Taking input from the user
digit = input("Enter a single digit: ")

# Calculating the value of a + aa + aaa + aaaa
result = int(digit) + int(digit * 2) + int(digit * 3) + int(digit * 4)

# Printing the output
print(result)
'''
'''
### Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.



# Taking input from the user
input_numbers = input("Enter a sequence of comma-separated numbers: ")

# Splitting the input into a list of numbers
numbers_list = [int(num) for num in input_numbers.split(',')]

# Using a list comprehension to square each odd number
squared_odd_numbers = [num**2 for num in numbers_list if num % 2 != 0]

# Printing the output
print(','.join(map(str, squared_odd_numbers)))

'''
'''
### Question 18
Level 3

Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:


import re

# Taking input from the user
passwords_input = input("Enter a sequence of comma-separated passwords: ")

# Splitting the input into a list of passwords
passwords_list = passwords_input.split(',')

# Checking the validity of each password
valid_passwords = []

for password in passwords_list:
    if (
        6 <= len(password) <= 12
        and re.search("[a-z]", password)
        and re.search("[0-9]", password)
        and re.search("[A-Z]", password)
        and re.search("[$#@]", password)
    ):
        valid_passwords.append(password)

# Printing the output
print(','.join(valid_passwords))
'''
'''
### Question 19
Level 3

Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use itemgetter to enable multiple sort keys.


from operator import itemgetter

# Taking input from the user
tuples_input = input("Enter tuples (name, age, height) separated by commas: ")

# Splitting the input into a list of tuples
tuples_list = [tuple(data.split(',')) for data in tuples_input.split(';')]

# Sorting the tuples based on multiple criteria
sorted_tuples = sorted(tuples_list, key=itemgetter(0, 1, 2))

# Printing the output
print(sorted_tuples)
'''
'''
### Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield


class DivisibleBySevenGenerator:
    def _init_(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        for num in range(self.n + 1):
            if num % 7 == 0:
                yield num

# Taking input for the range
n = int(input("Enter the range (n): "))

# Creating an instance of the class
divisible_by_seven_gen = DivisibleBySevenGenerator(n)

# Using the generator to iterate numbers divisible by 7
for num in divisible_by_seven_gen.generate_divisible_by_seven():
    print(num)
'''   

'''
### Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input.


# Taking input from the user
input_text = input("Enter a sentence: ")

# Splitting the input into words and creating a dictionary to store frequencies
word_frequency = {}

# Counting the frequency of each word
for word in input_text.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1

# Sorting the dictionary keys alphanumerically
sorted_keys = sorted(word_frequency.keys())

# Printing the output
for key in sorted_keys:
    print(f"{key}:{word_frequency[key]}")
'''

'''
### Question 23
level 1

Question:
Write a method which can calculate square value of number

Hints:
Using the ** operator


def calculate_square(number):
    return number ** 2

# Example usage
result = calculate_square(5)
print(result)

'''
'''
### Question 25
Level 1

Question:
Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define a instance parameter, need add it in __init__ method
You can init a object with construct parameter or set the value later

class MyClass:
    # Class parameter
    class_param = "Class Parameter"

    def _init_(self, instance_param):
        # Instance parameter
        self.instance_param = instance_param

# Creating an instance of the class
obj = MyClass("Instance Parameter")

# Accessing class parameter
print("Class Parameter:", MyClass.class_param)

# Accessing instance parameter
print("Instance Parameter:", obj.instance_param)
'''

