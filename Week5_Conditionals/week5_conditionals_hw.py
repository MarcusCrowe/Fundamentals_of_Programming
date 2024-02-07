
# Q1
digit = int(input("Enter a number 0 to 9: "))

#Each index number matches its element in the list
num_list = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

#Checks if the user input is valid, and either prints the correct response, or says invalid
if digit >= 0 and digit <= 9:
    print(num_list[digit])
else:
    print('Invalid number!')


# Q2
# Rock
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

#Importing random to use for the computer choice
import random
player_choice = input("Would you like to play rock, paper or scissors?: ")

#If the users input isn't valid, it says that and exits the program.
if player_choice != 'rock' and player_choice != 'paper' and player_choice != 'scissors':
    print(f"You picked '{player_choice}', invalid choice!")
    exit()

#Chooses computer's number
random_number = round(random.random(), 2)
#Globalizing computer_choice variable
computer_choice = ''

#Chooses computer's move (lines 61-68)
if random_number >= 0 and random_number < 1/3:
    computer_choice = 'rock'

elif random_number >= 1/3 and random_number < 2/3:
    computer_choice = 'paper'

else:
    computer_choice = 'scissors'

#Globalizing result variable
result = ''

#Logic for rock paper scissors game (lines 74-93)
#if player and computer have same move, it is a tie
if player_choice == computer_choice:
    result = 'Tie'

#logic if player's choice is rock
elif player_choice == 'rock':
    if computer_choice == 'paper':
        result = 'You lose!'
    else:
        result = 'You win!'

#logic if player's choice is paper
elif player_choice == 'paper':
    if computer_choice == 'rock':
        result = 'You win!'
    else:
        result = 'You lose!'

#logic if player's choice is scissors
elif player_choice == 'scissors':
    if computer_choice == 'rock':
        result = 'You lose!'
    else:
        result = 'You win!'

#Final print/return statement for after the game
print(f'You picked {player_choice}. Computer picked {computer_choice}. {result}')

# Q3
year = int(input("Pick a year!: "))

#if year is divisble by 4 and not divisible by 100, it is a leap year
#   if not divisible by 4, it is not a leap year
#if year is divisible by 4 and 100, but not 400, it is not a leap year
#   if it is, it is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('It is a leap year!')
        else:
            print("It is not a leap year!")
    else:
        print('It is a leap year!')
else:
    print("It is not a leap year!")

# Q4
print("Welcome to Treasure Island. Your mission is to find the treasure.")
#reusing same variable to reduce clutter (choice)
choice = input("left or right?: ")
#if move is left, continue, if else, game over
if choice == 'left':
    choice = input("swim or wait?: ")
    #if choice is wait, continue, if else, game over
    if choice == 'wait':
        choice = input("Which door - red, blue, or yellow?: ")
        #if choice is red, game over
        if choice == 'red':
            print('Burned by fire. Game Over.')
        #if choice is blue, game over
        elif choice == 'blue':
            print('Eaten by beasts. Game Over.')
        #if choice is yellow, you win
        elif choice == 'yellow':
            print('You win!')
        #if choice is anything else, invalid choice, game over
        else:
            print('Invalid choice. Game Over.')
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
