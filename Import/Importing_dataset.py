import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing the data

data = pd.read_csv("bundesliga_player.csv")

ages = np.array(data["age"])
market_values = np.array(data["price"])
height = np.array(data["height"])
max_value = np.array(data["max_price"])
position = np.array(data["position"])


#C
#This graph shows the relationship between Bundesliga players ages and their values
#It can tell us at what age Bundesliga players are most valuable (around 19-25years)
#It can also tell us how the market values change as age goes up (it goes up until the 20s, then goes down as the player gets older)
#Lastly, it tells us that older players see a decline in their values, even when they once had a high maximum market value

plt.bar(ages, market_values, color="red")
plt.scatter(ages, max_value, color="blue")

plt.title("Relationship between Player Age and Market Values in the Bundesliga")
plt.xlabel("Age (years)")
plt.ylabel("Market Value (Million euros)")
plt.legend(["Max Value", "Market Value"])
plt.show()

#D
#This bar chart shows the relationship between player position and their market values
#Goalkeepers have the lowest market values (around 37million euros)
#Defenders have the second lowest market values (around 75million euros)
#Midfielders have the highest market values with (around 120 million euros)
#It shows that market values are influenced by the player position

plt.bar(position, market_values)
plt.title("Position vs Market Value")
plt.xlabel("Position")
plt.ylabel("Market Value (Million euros)")
plt.grid()
plt.show()

#E
#These subplots show how physical traits and market values are influenced from a players position
#It shows that goalkeepers, while they are taller, their market values are lower
#On the other hand, midfielders and attackers are shorter on average, but they have higher market values 
#In other words, player position influences height and market value, but height have no connection with market value

plt.subplot(1,2,1)
plt.scatter(position, height)
plt.title("Position vs Height")
plt.xlabel("Position")
plt.ylabel("Market Value (Million euros)")

plt.subplot(1,2,2)
plt.scatter(position, market_values)
plt.title("Position vs Market Values")
plt.xlabel("Position")
plt.ylabel("Market Value (Million euros")

#used plt.tightlayout to make the words not stuck to eachother
plt.tight_layout()
plt.show()

#F
#This scatter plot shows the relationship between heights of players and their corresponding market values
#It can tell us whether heights have an influence on market value (doesn't seem so)
#It can also tell us if the most valuable players are tall or short or average (no correlation between height and market value)
#Lastly, it can tell us if very small or very tall players have their market values negatively influenced by their height (extreme heights correlates with lower market values)

plt.scatter(height, market_values)
plt.xlabel("Height (m)")
plt.ylabel("Market Value (Million euros)")
plt.title("Relationship Between the Height and Market Values of Bundesliga Players")
plt.show()

#G
#This bar chart shows the relationship between Bundesliga player ages and their corresponding market values
#From the chart, we can see that players around 18-20 years old have the highest market values out of all bundesliga players
#From ages 21-27 years old, players have relatively similar market values (not much fluctuation)
#After around 29 years old, Bundesliga players value plummets down and they lose their market values

plt.bar(ages,  market_values, color = "red")
plt.title("Relationship between ages of Bundesliga players and Market Values")
plt.xlabel("Age")
plt.ylabel("Market Value (Million euros)")

plt.show()