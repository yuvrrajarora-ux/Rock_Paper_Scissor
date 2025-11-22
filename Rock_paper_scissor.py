import random

'''
1 for Rock
-1 for Paper
0 for Scissor
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (r for Rock, p for Paper, s for Scissor): ")

youdict = {"r": 1, "p": -1, "s": 0}
reversedict = {1: "Rock", -1: "Paper", 0: "Scissor"}

# Safe input handling
you = youdict.get(youstr)
if you is None:
    print("Invalid choice!")
    exit()

print(f"You chose {reversedict[you]} | Computer chose {reversedict[computer]}")

if computer == you:
    print("It's a Draw 😐")

else:
    if (computer == -1 and you == 1):   # Paper vs Rock
        print("You lose! 😭") 
    
    elif (computer == 1 and you == -1): # Rock vs Paper
        print("You Win! 🙂")

    elif (computer == 0 and you == 1):  # Scissor vs Rock
        print("You Win! 🙂")

    elif (computer == 1 and you == 0):  # Rock vs Scissor
        print("You lose! 😭")

    elif (computer == -1 and you == 0): # Paper vs Scissor
        print("You Win! 🙂")

    elif (computer == 0 and you == -1): # Scissor vs Paper
        print("You lose! 😭")

    else:
        print("Something Went Wrong")
