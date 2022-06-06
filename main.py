import random
# Rock Paper Scissors

print("\nROCK PAPER SCISSORS\n\n")
print("This is a simple game you play with the computer.\n")
print("It involves you Choosing between Rock(R), Paper(P), or Scissors(S).")
print("Then your answer is compared with the choice of the computer to determine the winner.\n\n")

is_running = True

# List for the choices in the game and their names
game_option = ["R", "P", "S"]
option_names = ["Rock", "Paper", "Scissors"]

# Define the function that decides the winner
def decider():

    if(cpu == "Rock" and player == "Paper"):
        print("Player(" + player + ") : CPU(" + cpu + ")\n")
        print("Result: Player Wins!!!")

    elif(cpu == "Rock" and player == "Scissors"):
        print("Player(" + player + ") : CPU(" + cpu + ")\n")
        print("Result: CPU Wins!!!")

    elif(cpu == "Paper" and player == "Scissors"):
        print("Player(" + player + ") : CPU(" + cpu + ")\n")
        print("Result: Player Wins!!!")

    elif(cpu == "Paper" and player == "Rock"):
        print("Player(" + player + ") : CPU(" + cpu + ")\n")
        print("Result: CPU Wins!!!")

    elif(cpu == "Scissors" and player == "Rock"):
        print("Player(" + player + ") : CPU(" + cpu + ")\n")
        print("Result: Player Wins!!!")

    elif(cpu == "Scissors" and player == "Paper"):
        print("Player(" + player + ") : CPU(" + cpu + ")\n")
        print("Result: CPU Wins!!!")
    
    return 0

# Keeps the program running
while(is_running):
    # Randomly generate CPU choice
    cpu = random.choice(option_names)
    my_choice = input("Input either R, P or S, for Rock Paper or Scissors, respectively\n")
    
    # Gets users choice and captures any error
    try:
        player = option_names[game_option.index(my_choice)]
    except ValueError:
        print("Try again")
        continue

    # 
    if (cpu != player):
        decider()
    
        # Asks the user to either go again or quit
     
        go_on = input("Do you want to play again?: Y/N\n")
        if (go_on == "Y"):
            continue
        elif (go_on == "N"):
            print("Thanks for playing. See you soon")
            is_running = False
        else:
            print("Wrong input. Good bye")
            is_running = False

    else:
        print("Player(" + player + ") : CPU(" + cpu + ")\n")
        print("Result: It's a tie")
