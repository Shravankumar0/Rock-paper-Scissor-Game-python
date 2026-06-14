"""
   Workflow of project
   1: Input form user(Rock, Paper, Scissor)
   2: Computer choice (Computer will choose randamaly not conditionally)
   3: Result print
   
   Cases:
   A- Rock
   Rock - Rock = Tie
   Rock - Paper = Paper Win
   Rock - Scissor = Scissor Win
   
   B- Paper
   Paper - Paper = Tie
   Paper - Rock = Paper win
   Paper - Scissor = Scissor win
   
   C- Scissor
   Scissor - Scissor = Tie
   Scissor - Rock = Rock win
   Scissor - Paper = Scissor Win 
"""

import random
item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"User Choice : {user_choice}, computer Choice : {comp_choice}")

if user_choice == comp_choice:
    print("Both Chooses same : = Match Tie")
    
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper cover Rock : Computer win")
    else:
        print("Rock Smeshes Scissor  = You win ")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cut paper : Computer win")
    else:
        print("paper cover Rock  = You win ")
            
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cut paper :You win")
    else:
        print("Rock smashes Scissor = Computer win ")
        