import random

'''
1 for Stone
-1 for Paper
0 for Scissor
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (st for Stone, p for Paper, sr for Scissor): ")

youdict = {"st": 1, "p": -1, "sr": 0}
reversedict = {1: "Stone", -1: "Paper", 0: "Scissor"}

# Safe input handling
you = youdict.get(youstr)
if you is None:
    print("Invalid choice!")
    exit()


# convert your input
you = youdict.get(youstr)

if you is None:
    print("Invalid input! 😢")
else:
    print(f"You chose {reversedict[you]} | Computer chose {reversedict[computer]}")

    if computer == you:
        print("It's a Draw 😐")

    elif (computer == 1 and you == -1) or \
         (computer == -1 and you == 0) or \
         (computer == 0 and you == 1):
        print("You Win! 🙂")

    else:
        print("You Lose! ☹️")
