import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Rock Paper Scissors VS BigBobbyAI")
user_choice = input("Type 0 for Rock, 1 for Paper or 2 for Scissors\n").lower()
bots_choice = random.randint(0, 2)
if user_choice == "0" or user_choice == "rock":
    print(rock)
elif user_choice == "1" or user_choice == "paper":
    print(paper)
elif user_choice == "2" or user_choice == "scissors":
    print(scissors)
else:
    print("Invalid Input. Try Again :) ")
    exit()

print(f"BigBobbyAI Chose:")
if bots_choice == 0:
    print(rock)
elif bots_choice == 1:
    print(paper)
else:
    print(scissors)

if user_choice == "0" and bots_choice == 0:
    print("Its a Draw.")
if user_choice == "0" and bots_choice == 1:
    print("You lose :(")
if user_choice == "0" and bots_choice == 2:
    print("You win!")

if user_choice == "1" and bots_choice == 2:
    print("You lose :(")
if user_choice == "1" and bots_choice == 1:
    print("Its a Draw.")
if user_choice == "1" and bots_choice == 0:
    print("You win!")

if user_choice == "2" and bots_choice == 0:
    print("You lose :(")
if user_choice == "2" and bots_choice == 1:
    print("You win!")
if user_choice == "2" and bots_choice == 2:
    print("Its a Draw.")

if user_choice == "rock" and bots_choice == 0:
    print("Its a Draw.")
if user_choice == "rock" and bots_choice == 1:
    print("You lose :(")
if user_choice == "rock" and bots_choice == 2:
    print("You win!")

if user_choice == "paper" and bots_choice == 2:
    print("You lose :(")
if user_choice == "paper" and bots_choice == 1:
    print("Its a Draw.")
if user_choice == "paper" and bots_choice == 0:
    print("You win!")

if user_choice == "scissors" and bots_choice == 0:
    print("You lose :(")
if user_choice == "scissors" and bots_choice == 1:
    print("You win!")
if user_choice == "scissors" and bots_choice == 2:
    print("Its a Draw.")

print("Thank you for playing!")