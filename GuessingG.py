#Inez Fennelly 
# Guessing Game

# adapted from https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9

from random import randint

target = (randint(1, 100))
guess = 101

print("guess a number between 1 & 100")
while guess != target:
 guess = int(input("Please enter your guess: "))
 if guess == target:
    print("Well done! You are correct!")
 elif guess < target:
    print ("Too low")
 else: 
    print ("Too high")
