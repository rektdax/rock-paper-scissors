# TODO
# 1. game: modify so you hare not repeating so many constants
# 2. use global where applicable: https://stackoverflow.com/questions/12665994/function-not-changing-global-variable
# 3. move 'user_input = input(">>>")' somewhere that it is only written 1-2 times (instead of 4)
import random

print("Welcome to the Rock, Paper, Scissors! Use the following commands to interact with the game.")
print("\t1. Play rock (rock)")
print("\t2. Play paper (paper)")
print("\t2. Play scissors (scissors)")
print("\t3. Show the score (show)")
print("\t4. Start over (clear)")
print("\t5. Exit the game (exit)")

user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]

user_input = input(">>>")

def game(u_score, c_score): 

	c_choice = random.choice(choices)
	u_choice = user_input

	if u_choice == c_choice:
		print("It's a tie!")
	elif u_choice == "scissors" and c_choice == "rock":
		c_score += 1
		print ("You lose!")
	elif u_choice == "scissors" and c_choice == "paper":
		u_score += 1
		print ("You win!")
	elif u_choice == "rock" and c_choice == "paper":
		c_score += 1
		print ("You lose!")
	elif u_choice == "rock" and c_choice == "scissors":
		u_score += 1
		print ("You win!")
	elif u_choice == "paper" and c_choice == "rock":
		u_score += 1
		print ("You win!")
	elif u_choice == "paper" and c_choice == "scissors":
		c_score += 1
		print ("You lose!")

	return u_score, c_score

def show(): 
	print("Score: " + str(user_score) + " - " + str(computer_score))

def clear(u_score, c_score):
	u_score = 0
	c_score = 0
	return u_score, c_score

while 'exit' not in user_input:
	if ('rock' in user_input) or ('paper' in user_input) or ('scissors' in user_input):
		user_score, computer_score = game(user_score, computer_score)
		show()
		user_input = input(">>>")
	elif 'show' in user_input:
		show()
		user_input = input(">>>")
	elif 'clear' in user_input:
		user_score, computer_score = clear(user_score, computer_score)
		show()
		user_input = input(">>>")
	else:
		print("Please enter a valid command.")
		user_input = input(">>>")