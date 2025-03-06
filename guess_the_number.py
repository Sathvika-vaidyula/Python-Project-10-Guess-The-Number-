import random
logo = r""" 
 ________                       ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/                  \/     \/          \/            \/    \/     \/       
"""
print(logo)
print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

choose = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if choose == "easy":
    attempts = 10
elif choose == "hard":
    attempts = 5
else:
    print("Invalid difficulty level. Please choose 'easy' or 'hard'.")
    exit()

print(f"You have {attempts} attempts to guess the number.")
number_to_guess = random.randint(1, 100)

while attempts > 0:
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    attempts -= 1

    if guess < number_to_guess:
        print("Too low.")
    elif guess > number_to_guess:
        print("Too high.")
    else:
        print(f"You got it! The number is {guess}.")
        break
    
    print(f"You have {attempts} attempts remaining.")

if attempts == 0:
    print(f"Sorry, you ran out of attempts. The number was {number_to_guess}.")
