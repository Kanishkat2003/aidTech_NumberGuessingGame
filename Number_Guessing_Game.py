import random
import time

def clear_screen():
    # Clear the console screen (works in Windows and Unix-based systems)
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def guess_the_number():
    clear_screen()
    print("*********************************************************")
    print("             Welcome to the Number Guessing Game!")
    print("*********************************************************")
    name = input("What's your name? ")
    print(f"Hello, {name}! I'm thinking of a number between 1 and 100.")
    
    while True:
        secret_number = random.randint(1, 100)
        attempts = 0
        
        while attempts < 10:
            try:
                guess = int(input("Take a guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            attempts += 1
            if guess == secret_number:
                print("\nCongratulations, you guessed the number!")
                print(f"The secret number was {secret_number}. You did it in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        
        if attempts >= 10:
            print(f"\nSorry, you've run out of attempts. The secret number was {secret_number}.")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Goodbye.")
            time.sleep(1)  # Pause for a moment before exiting to make it more user-friendly
            clear_screen()
            break

if __name__ == "__main__":
    guess_the_number()

