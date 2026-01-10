# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to 
# represent a snake, water, or a gun.
#  
# The gun beats the snake, 
# the water beats the gun, and 
# the snake beats the water. 
# Write a python program to create a Snake Water Gun game in Python using if-else statements.
import random
opt=["snake","water","gun"]
a=(input("Choose ->(1)SNAKE (2)WATER (3)GUN:"))
x=(random.choice(opt))

win=(f"YOU WON!\n\nYOU CHOSE:{a} AND COMPUTER CHOSE:{x}")
lose=(f"YOU LOSE!\n\nYOU CHOSE:{a} AND COMPUTER CHOSE:{x}")
your_score=0
comp_score=0
if a not in opt:
    print("INVALID CHOICE")
elif a == x:
    print(f"Both Chose:{(a)} It Results In A Draw")
elif a=="gun" and x=="snake":# The gun beats the snake, 
    print(win)
elif a=="water" and x=="gun":# the water beats the gun
    print(win)
elif a=="snake" and x=="water":# the snake beats the water. 
    print(win)
else:
    print(lose)
    