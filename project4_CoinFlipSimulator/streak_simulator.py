import random 

print("\nWelcome to Streak Simulator! 🪙")

numFlips = int(input("Enter how many times you want to flip the coin: "))

currentStreak = 0
longestHeads = 0
longestTails = 0
last_flip = None

for i in range(numFlips):
    flip = random.choice(["Heads","Tails"])
    
    if flip == last_flip:
        currentStreak += 1
    else:
        currentStreak = 1  # reset streak
    
    # update longest streaks
    if flip == "Heads":
        longestHeads = max(longestHeads, currentStreak)
    else:
        longestTails = max(longestTails, currentStreak)

    # Print ongoing streak
    print(f"Flip {i+1}: {flip} (Current streak: {currentStreak})")

    last_flip = flip

# Final results
print("\nFinal Results 🪙")
print("Longest Heads streak:", longestHeads)
print("Longest Tails streak:", longestTails)
