import random

def number_guessing_game():
    secret_number = random.randint(1, 20)  
    attempts = 0  
    max_attempts = 5 

    print("Select a number between 1 and 20. Try to guess it!")
    print(f"You have {max_attempts} attempts...")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess (1-20): "))

            if guess < 1 or guess > 20:
                print("Invalid input! Please enter a number between 1 and 20.")
                continue  
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the correct number {secret_number} in {attempts} attempts!")
                return  

        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 20.")
    
    print("You don't have enough attempts! The correct number was {secret_number}. Better luck next time!")

number_guessing_game()
