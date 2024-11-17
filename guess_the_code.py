# Code 1:
for i in range(1, 10):
    if i % 2 == 0:
        print(i * i)
# Question:
# What will this code print, and what does it do?
# print the square root of the even numbers, 4,16,36,64.


# Code 2:
word = "hello"
new_word = word[1:] + word[0]
print(new_word)
# Question:
# What does this code output, and what is it doing to the string?
# elloh, prints all the letters expect the first and then adds the first.


# Code 3:
numbers = [1, 2, 3, 4, 5]
squared_numbers = [n ** 2 for n in numbers if n % 2 == 1]
print(squared_numbers)
# Question:
# What will be the output of this code, and what is the purpose of the list comprehension?
# prints the square root of the odd numbers 


# Code 4:
fruits = {"apple": 3, "banana": 5, "cherry": 2}
total = 0
for fruit in fruits:
  total += fruits[fruit]
print(total)
# Question:
# What will this code print, and what is it calculating?
# prints the sum values of the keys.


# Code 5:
text = "Python"
result = ""
for char in text:
    result = char + result
print(result)
# Question:
# What will this code print, and what does it do to the string text?
# prints the reversed text.


# Code 6:
set_a = {1, 2, 3}
set_b = {2, 3, 4}
result = set_a.symmetric_difference(set_b)
print(result)
# Question:
# What does this code output, and what does the symmetric_difference method do?
# prints a new set with elements in either the set or other but not both.


# Code 7:
def greet(name="stranger"):
  print(f"Hello, {name}!")
greet()
greet("Alice")
# Question:
# What will this code print, and what is the purpose of the name="stranger" part in the function
# definition?
# first prints the given value "stranger" and then prints the function with a new value for name(Alice)


# Code 8:
sentence = "This is a simple sentence."
count = sentence.count("s")
print(count)
# Question:
# What does this code output, and what is it counting?
# prints how many times the letter 's' appears in the sentence.


# Code 9:
x = 10
y = 5
z = x > y and y < 0 or x < 0
print(z)
# Question:
# What will this code print, and how does the expression in z evaluate?
# prints false because none of the operators are correct, the expression in z evaluates as false due to the syntax of the "and" , "or" in the sentence. 


# Code 10:
n = 1
while n < 10:
    print(n)
    n += 3
# Question:
# What will be the output of this code, and how does the while loop control the flow?
# prints the given number (1) and every iteration adds 3 to the result as long as the result is lower than 10.


# Code 11:
values = (1, 2, 3)
a, b, c = values
print(a + b + c)
# Question:
# What will this code print, and what is happening with a, b, c = values?
# prints 6, which is the sum of (1,2,3), we defind a=1, b=2, c=3 therefore it prints all there values combined.


# Code 12:
data = [10, 20, 30, 40, 50]
print(data[-3])
# Question:
# What will this code output, and what is the purpose of -3 in the list indexing?
# prints the third number in the list counting in reverse starting from -5.


# Code 13:
info = {"name": "Alice", "age": 25}
info["age"] = 26
print(info)
# Question:
# What will this code print, and what does the line info["age"] = 26 do?
# prints "name: alice , age: 26", we changed the value of the age in the second line from 25 to 26.

# Code 14:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [row[1] for row in matrix]
print(result)
# Question:
# What will this code output, and what is the purpose of the list comprehension?
# prints [2,5,8] row[1] iterates every second index in each row and the result being a row that composed from those indexes.  