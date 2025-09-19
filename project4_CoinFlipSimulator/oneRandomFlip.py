#project inspired by the Law of Large Numbers
import random 
print("This program flips a coin with sides Heads or Tails every time the enter key is pressed")

while True:
    user_input=input("Press 'enter' to flip the coin 🪙  or type 'q' and press enter to quit: ")
    
    if user_input.lower()=="q":
        print("Thanks for playing! Goodbye 🪙")
        break
    flip=random.choice(["Heads", "Tails"])
    print("The coin landed on: ",flip)