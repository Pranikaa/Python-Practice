import random

print("Welcome to the number guessing game")
number_to_guess = int(input("Guess the number from 1 - 6: "))
random_num = random.randint(1,6)

if number_to_guess == random_num:
    print("Congratulations, you have guess the correct number.")
else:
    print(f"Sorry, the correct number if {random_num}. Try Again!!!")
