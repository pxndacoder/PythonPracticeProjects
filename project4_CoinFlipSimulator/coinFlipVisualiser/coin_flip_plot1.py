import random
import matplotlib.pyplot as plt

print("\nWelcome to Coin Flip Visualizer! 🪙📊")

# Ask user how many flips
num_flips = int(input("How many times do you want to flip the coin? "))

heads = 0 #stores the percentage of heads after each flip 
ratios=[] #stores the percentage of heads after each flip 

for i in range(1, num_flips + 1):
    flip = random.choice(["Heads", "Tails"])
    if flip == "Heads":
        heads += 1

    ratio= heads/i
    ratios.append(ratio)

    # Plot
plt.plot(range(1, num_flips + 1), ratios, label="Heads %") #x-axis, y-axis, label
plt.axhline(0.5, color="red", linestyle="--", label="Expected 50%") #draws a horizontal line at 0.5 aka the expected value of heads
plt.xlabel("Number of Flips") #x-axis label
plt.ylabel("Heads Ratio")# y-axis label
plt.title("Law of Large Numbers – Coin Flip Simulation") #Title of plot
plt.legend() #shows the legend using the labels provided
"""In plotting (like with matplotlib), a legend is a small box or area on the graph that explains what each line, marker, or color represents."""
plt.show() #displays the plot in a seperate window 