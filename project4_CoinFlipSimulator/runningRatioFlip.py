import random

print("\nWelcome to Running Ratio Flip! 🪙")

print("""
This program flips a coin multiple times and shows how the
ratio of heads/tails gets closer to 50/50 as the number of flips increases.
""")

numFlips=int(input("Please enter how many times you want to flip this coin 🪙  :  "))

heads=0
tails=0

interval=max(1, numFlips //10)
progress= input("To use default 10% interval of flips press enter. For customer interval press 'c': ")
if progress.lower()=="c":
    userInput=int(input("Enter your custom interval: "))
    interval=max(1,numFlips //userInput)

for i in range(numFlips+1):
    flip=random.choice(["Heads","Tails"])
    if flip=="Heads":
        heads+=1
    else:
        tails+=1

    if i% interval ==0:
        print("After ",i,"flips the results were: ")
        print("\n\t\t\t\t Heads: ", heads, f"({heads/numFlips:.2%})")
        print("\n\t\t\t\t Tails: ", tails, f"({tails/numFlips:.2%})")

if numFlips % interval != 0:
    print("=============================================================================")
    print("\nHere are the results after all flips have been completed:")
    print("\nAfter", numFlips ,"flips: ")
    print("\t\t\t Heads: ", heads, f"({heads/numFlips:.2%})")
    print("\n\t\t\t Tails: ", tails, f"({tails/numFlips:.2%})")