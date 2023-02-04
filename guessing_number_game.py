from logo import logo
import random 
from replit import clear

#creating a "number" list of 100 numbers
number_list = []
for number in range(1,101):
    number_list.append(number)
#makes the computer choice a random number from the number_list
computer_choice = random.choice(number_list)

def attempts_handler(difficulty):
    """ This function keep track of the attempts of the user based on the difficulty parameter """

    is_game_over = False
    attempts = 0

    if difficulty == 'easy':
        attempts = 10
    if difficulty == 'hard':
        attempts = 5

    while not is_game_over:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        #attempts decreasing cicle
        while guess != int(computer_choice):
            #decreasing the attempts 
            attempts -= 1
            if attempts == 0:
                is_game_over = True
                return print("You don't have attempts left. You lose.")
            else:
                if guess < computer_choice:
                    print("Too low")
                    print("Guess again")
                else:
                    print("Too high")
                    print("Guess again")
                print(f"You have {attempts} attempts remaining to guess the number.")
                guess = int(input("Make a guess: "))
        #ending the game by setting the is_game_over_flag on true and returning the result
        if guess == computer_choice:
            is_game_over = True
            return print(f"You guessed the right number {computer_choice}. You win!")

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 0 and 100.")

    #debug
    #print('[COMPUTER_CHOICE]',computer_choice)

    #handling the difficulty level input if is diferent from easy or hard
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
    while difficulty_level != 'easy' and difficulty_level != 'hard':
        print("You've entered an invalid value. Please try again.")
        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

    attempts_handler(difficulty=difficulty_level)

play_game()

while input("Do you want play again ? Type 'yes' or 'no'\n") == 'yes':
    clear()
    play_game()
