import random
options = ["rock", "paper", "scissors"]

class Game:
    # def __init__(self, move):
    #     self.move = move

    def win():
        print("you won! :) congrats!!")

    def lose():
        print("you lost! better luck next time :(")

    def tie():
        print("its a tie!")

    # def computer(self):
    #     print("computers choice: ")
    #     random_val = random.choice(options)
    #     print(random_val)

# run.computer()
while True:
    print("whats your move? rock, paper or scissors??")
    
    move = input("your move:  ")
    computer = random.choice(options)
    print("computer's move: " + computer)

    run = Game
    

    if move == computer:
        run.tie()
    elif move == "rock" and computer == "scissors":
        run.win()
    elif move == "rock" and computer == "paper":
        run.lose()
    elif move == "scissors" and computer == "rock":
        run.lose()
    elif move == "scissors" and computer == "paper":
        run.win()
    elif move == "paper" and computer == "scissors":
        run.lose()
    elif move == "paper" and computer == "rock":
        run.win()
    else:
        print("invalid input")
    