import random
import matplotlib.pyplot as plt

print("\nWelcome to Coin Flip Visualizer – Stage 2! 🪙📊")

# Ask user how many flips
num_flips = int(input("How many times do you want to flip the coin? "))

heads = 0
tails = 0

heads_ratios = []  # stores the % of heads after each flip
tails_ratios = []  # stores the % of tails after each flip

for i in range(1, num_flips + 1):
    flip = random.choice(["Heads", "Tails"])
    if flip == "Heads":
        heads += 1
    else:
        tails += 1

    # Calculate ratios
    heads_ratio = heads / i
    tails_ratio = tails / i

    heads_ratios.append(heads_ratio)
    tails_ratios.append(tails_ratio)

# Plot both ratios
plt.plot(range(1, num_flips + 1), heads_ratios, label="Heads %", color="blue")
plt.plot(range(1, num_flips + 1), tails_ratios, label="Tails %", color="green")
plt.axhline(0.5, color="red", linestyle="--", label="Expected 50%")  # expected value
plt.xlabel("Number of Flips")
plt.ylabel("Ratio")
plt.title("Coin Flip Simulation – Heads vs Tails")
plt.legend()
plt.show()
