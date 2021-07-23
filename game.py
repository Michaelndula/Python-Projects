from random import randint

#list of play options

t = ["Rock", "Paper", "Scissors"]

#assign a random play to comp

computer = t[randint("0,2")]

#set player to false

player = False

while not player:
    #set player to True
    player = input("Rock","Paper","Scissors?")
    if player == computer:
        print("You Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose!",computer,"Covers",player)
        else:
         print("You Win!",player,"Smashes",computer)

    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose!",computer,"Cut",player)
        else:
            print("You Win!",player,"Covers",computer) 

    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose!",computer,"Smashes",player)
        else:
            print("You Win!",player,"Cut",computer) 

    else:
            print("That's not a valid play. Check Your spelling!!")

            #player was set to True, But we want it to be False so the loop continues
player = False
computer = t[randint(0,2)]