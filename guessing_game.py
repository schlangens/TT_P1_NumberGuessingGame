"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
Scott Schlangen - V1 - 08/31/2021
--------------------------------
"""

import random

def start_game():
    answer = random.randint(1,10)
    attempt_limit = 10
    attempts = 0
    # for troubleshooting print(answer)
    name = input("What is your name? ")
    print("---------------------------------------------------------------------------------------------")
    print("Welcome to the number guessing game! {} Guess a number between 1 - 10  ".format(name))
    while attempts < attempt_limit:
      try:
          guess_text = input("What is your best guess? ")
          guess_text = int(guess_text)
          attempts += 1
      except ValueError as err:
              print("is not a valid number 1-10".format(err))
              continue
      else:
          if answer == guess_text:
            print(f"You guess the right number! it was {guess_text}. It took you {attempts} attempt(s) to guess the right number!")
            break
          if guess_text < answer:
              print("It's higher.")
          elif guess_text > answer:
              print("It's lower")
    print("---------------------------------------------------------------------------------------------")    
    print(f"Bye {name}, you're done after those {attempts} attempts")

start_game()