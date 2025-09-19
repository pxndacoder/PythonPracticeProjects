import random
print("\nWelcome to Multi Flip Counter! 🪙")
# --- Program Description ---
print("""
Coin Flip Simulator – Law of Large Numbers Demonstration 🪙

This program demonstrates the Law of Large Numbers (LLN) using coin flips.

1️⃣  What the Law of Large Numbers says:
   As the number of independent flips increases, the fraction of heads and tails
   will get closer and closer to the expected probability (50% each for a fair coin).

2️⃣  How fast it converges:
   - Small numbers of flips (10–20) can vary a lot (e.g., 7 heads, 3 tails).
   - Moderate numbers (100–500) start averaging out but still fluctuate.
   - Large numbers (1,000–10,000+) usually get very close to 50% heads/tails.

3️⃣  Why it never hits exactly 50%:
   Coin flips are random, so results can slightly differ each time.
   However, the percentage difference shrinks roughly proportional to 1/√n.

4️⃣  Rule of thumb:
   - 10–20 flips: very noisy
   - 100 flips: starts looking "kind of close"
   - 500–1,000 flips: visibly stabilizes around 50%
   - 10,000+ flips: extremely close to 50/50

Use this program to flip coins and observe how the results approach 50/50
as you increase the number of flips.
""")
numFlips=int(input("Please enter how many times you want to flip this coin 🪙  :  "))

heads=0
tails=0

for i in range(numFlips):
    flip=random.choice(["Heads","Tails"])
    if flip=="Heads":
        heads+=1
    else:
        tails+=1

print("\n After",numFlips, "flips the results were: ")
print("\n\t\t\t\t Heads: ", heads, f"({heads/numFlips:.2%})")
print("\n\t\t\t\t Tails: ", tails, f"({tails/numFlips:.2%})")