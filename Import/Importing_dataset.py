import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#age, height = np.loadtxt("bundesliga_player.csv", delimiter=",", max_rows=1, unpack=True, usecols=(3,4), skiprows=1)

data = pd.read_csv("bundesliga_player.csv")


ages = np.array(data["age"])
market_values = np.array(data["price"])
height = np.array(data["height"])


plt.bar(ages,  market_values, color = "red")

plt.title("Relationship between ages of Bundesliga players and Market Values")
plt.xlabel("Age")
plt.ylabel("Market Value")

plt.show()

plt.bar(height, market_values)

plt.title("Relationship between heights of Bundesliga players and Market Values")
plt.xlabel("Height")
plt.ylabel("Market Value")

plt.show()