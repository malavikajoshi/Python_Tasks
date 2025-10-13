# 1. Number Guessing Game: Write a script that generates a random number and allows a user to guess it, providing "higher" or "lower" 
# feedback until they guess correctly. 
import random

print("Welcome to the Number Guessing Game!")
number_to_guess = random.randint(1, 100)

attempts = 0
guess = 0

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it right in {attempts} attempts.")

#2. List Iteration: Create a list of numbers. Write a for loop to print each number and its square.
list_one=[1,34,54,23,4,3,8,9,22]
for i in list_one:
    print(f"{i},its square is {i**2}")


# 3.FizzBuzz: Write a program that prints the numbers from 1 to 100. For multiples of
# three, print "Fizz" instead of the number. For multiples of five, print "Buzz". For
# numbers which are multiples of both three and five, print "FizzBuzz".
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0 or i%5==0:
        if i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
    else:
        print(i)