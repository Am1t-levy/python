#1. 

age = int(input("enter your age: "))
if age >= 18:
    print("you can vote!")
elif age >= 16:
    print ("you cant vote")
else:
    print("you are a twat")      
 
2.

num = int (input ("enter any number to test whether it is odd or even: ")) 

if (num % 2) == 0:
    
    print ("the number is even")

else:

    print ("the number is odd")

3.

score = int(input("enter your score (0-100):"))

if 90 <= score <= 100:
    print("grade: A")
elif 80 <= score <= 89:
    print("grade B")
elif 70 <= score <= 79:
    print("grade C")
elif 60 <= score <= 69:
    print("grade D")
elif 0 <= score <= 60:
    print("grade F")

else:
    print("invalid score please insert a number between 0-100")

4.

num = float( input("enter any number: "))
if num > 0:
    print("positive number")
elif num == 0:
    print("zero")
else: 
    print("negative number")

5.

print("hello what is your age? ")

age = int(input("enter your age: "))

is_student = input("are you a student? (yes/no): ").strip().lower()

if age < 18 or is_student == "yes":
   print("you get a discount!!!")
else:
   print(" fuck off you dont get a discount!!!")

6.

for x in range(0,10):
   if x % 2 ==0:
     print(x)

7.

def calculate_sum() -> int:
    total = 0
    for num in range(1, 101):
        total += num
    return total 
print("the sum of numbers from 1 to 100 is:", calculate_sum()) 

8. 
number = int(input("enter a number: "))
print(f"multiplication table for {number}:")
for i in range (1,11):
       print(f"{number} * {i} = {number * i}" )

9. 
colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    print(x)

10.

i = 11
while i > 0:
  print(i)
  i -= 1
print("great success")

11.

import random

random_number = random.randint(1,10)
while True:
    guess = int(input("enter your guess: "))
    if guess < random_number:
        print("too low bro, try again.")
    elif guess > random_number:
        print("too high bro, try again")    
    else:
        print("congratulations! now initializing rm -r/ !!!")

12.

total_sum = 0
print("Enter numbers repeatedly. Enter a negative number to stop.")

while True:
   
  number = int(input("enter a number: "))
  if number < 0:
     print("negative number entered, bye bye.")
     break  
  else: 
    total_sum += number
print(f"the total of your all positive numbers: {total_sum}")

13.

def wtf():
    print("hello world")
wtf()

14.

def wtf(hello):
    print(hello + " amit")
wtf("hello")    
 
15.

number = int(input("enter a number: "))

def square(number):
    return number ** 2
result = square(number)
print(f"the square of {number} is {result}.")

16.

def factorial(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res
print(factorial(9)) 

17. 

def find_max(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i 
    return max
print("max is: "+str(find_max([1,5,6,3,0])))     


#18.
     





