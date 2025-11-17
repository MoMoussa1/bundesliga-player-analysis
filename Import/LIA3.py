'''David Tattersall, Mohamed Moussa'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Importing the data

data = pd.read_csv("bundesliga_player (1).csv")


##2) Preliminary steps

#Initial data inspection


# a)
head = data.head()
print(head) #Print the first 5 rows

print(data.shape) #Prints the dimensions of the dataset (rows, columns) (515,17)

data.info() #Shows the columns which have data that are not empty (non-null), also shows the type of each data (float,int)
# missing values:
# 286 full_name
# 5 place_of_birth
# 5 price
# 5 max_price
# 9 foot
# 34 contract_expires
# 27 player_agent
# 322 outfitter

# c)


#Filled numeric columns with median for some prices and max prices since it was only 5 that were missing for both, and the median represents the data relatively well
data["price"] = data["price"].fillna(data["price"].median())
data["max_price"] = data["max_price"].fillna(data["max_price"].median())


#Did not drop because we wouldve lost a lot of data. Instead, just replaced with NA so that we can still use other data from the same row
data["outfitter"] = data["outfitter"].fillna("NA")
data["player_agent"] = data["player_agent"].fillna("NA")
data["foot"] = data["foot"].fillna("NA")
data["full_name"] = data["full_name"].fillna("NA")
data["place_of_birth"] = data["place_of_birth"].fillna("NA")


# a)
dataset_description = data.describe()
print(dataset_description) #Shows mean, std, statistical summary


# b)


duplicates = data.duplicated()


count_duplicates = duplicates.value_counts()
print(count_duplicates) # no duplicates


##3) Univariate non-graphical EDA


#Manipulating Numerical Data


numerical_data = data[["age", "height", "price", "max_price", "shirt_nr"]]


print("-----Mean-----")
print(numerical_data.mean())


print("-----Median-----")
print(numerical_data.median())


print("-----Mode-----")
print(numerical_data.mode())


print("-----Standard Deviation-----")
print(numerical_data.std())


print("-----Variance-----")
print(numerical_data.var())


print("-----Skew-----")
print(numerical_data.skew())


print("-----Kurtosis-----")
print(numerical_data.kurtosis())


print("-----Quartiles-----")
print(numerical_data.quantile([0.25,0.5, 0.75]))


# Manipulating Categorical Data


categorical_data = data[["name", "full_name", "nationality", "place_of_birth", "position", "foot", "club", "contract_expires", "joined_club", "player_agent", "outfitter"]]


# Frequency Counts


name_frequency = data["name"].value_counts()
print("----Name Frequencies----")
print(name_frequency)


full_name = data["full_name"].value_counts()
print("----Full Name Frequencies----")
print(full_name)


nationality = data["nationality"].value_counts()
print("----Nationality Frequencies----")
print(nationality)


place_of_birth = data["place_of_birth"].value_counts()
print("----Place of Birth Frequencies----")
print(place_of_birth)


position = data["position"].value_counts()
print("----Position Frequencies----")
print(position)


foot = data["foot"].value_counts()
print("----Preferred foot Frequencies----")
print(foot)


club = data["club"].value_counts()
print("----Club Frequencies----")
print(club)


contract_expires = data["contract_expires"].value_counts()
print("----Contract Expires Frequencies----")
print(contract_expires)


joined_club = data["joined_club"].value_counts()
print("----Date Joined Club Frequencies----")
print(joined_club)


player_agent = data["player_agent"].value_counts()
print("----Player Agent Frequencies----")
print(player_agent)


outfitter = data["outfitter"].value_counts()
print("----Outfitter Frequencies----")
print(outfitter)


# Proportion


name_prop = name_frequency/515
print("----Name Proportion----")
print(name_prop)


full_name_prop = full_name/515
print("----Full Name Proportion----")
print(full_name_prop)


nationality_prop = nationality/515
print("----Nationality Proportion----")
print(nationality_prop)


place_of_birth_prop = place_of_birth/515
print("----Place of Birth Proportion----")
print(place_of_birth_prop)


position_prop = position/515
print("----Position Proportion----")
print(position_prop)


foot_prop = foot/515
print("----Preferred Foot Proportion----")
print(foot_prop)


club_prop = club/515
print("----Club Proportion----")
print(club_prop)


contract_expires_prop = contract_expires/515
print("----Date of Contract Expiration Proportion----")
print(contract_expires_prop)


player_agent_prop = player_agent/515
print("----Player agent Proportion----")
print(player_agent_prop)


outfitter_prop = outfitter/515
print("----Outfitter Proportion----")
print(outfitter_prop)


# Modes


#Name: none
#Full_name: none
#Nationality: German
#Place of Birth: Berlin
#Position: Defender
#Foot: right
#Club: TSG Hoffenheim, Augsburg, Schalke 04
#Contract expires: 2025-06-30
#player_agent: ROOF
#Outfitter: Adidas




# Number of unique categories


unique = categorical_data.nunique()
print("----Unique Values----")
print(unique)




##4) Univariate graphical EDA


#I.a) bins


sns.displot(numerical_data, x="age", binwidth=2)


sns.displot(numerical_data, x="height", binwidth=0.05)


sns.displot(numerical_data, x="price", binwidth=5)


sns.displot(numerical_data, x="max_price", binwidth=10)


sns.displot(numerical_data, x="shirt_nr", binwidth=2)


#I.b) conditioning


sns.displot(data, x="age", hue="position")


sns.displot(data, x="height", hue="position")


sns.displot(data, x="price", hue="position")


sns.displot(data, x="max_price", hue="position")


sns.displot(data, x="shirt_nr", hue="position")


#I.c) stacked histograms


sns.displot(data, x="age", hue="position", multiple="stack")


sns.displot(data, x="height", hue="position", multiple="stack")


sns.displot(data, x="price", hue="position", multiple="stack")


sns.displot(data, x="max_price", hue="position", multiple="stack")


sns.displot(data, x="shirt_nr", hue="position", multiple="stack")


#I.d) dodge bars


sns.displot(data, x="height", hue="position", multiple="dodge", bins=3)


sns.displot(data, x="age", hue="position", multiple="dodge", bins=3)


sns.displot(data, x="price", hue="position", multiple="dodge", binwidth=20)


sns.displot(data, x="max_price", hue="position", multiple="dodge", binwidth=20)


sns.displot(data, x="shirt_nr", hue="position", multiple="dodge", binwidth=15)


#I.e) Normalized histogram statistics


sns.displot(data, x="height", hue="club", stat="density", common_norm=False)


sns.displot(data, x="age", hue="club", stat="density", common_norm=False)


sns.displot(data, x="price", hue="club", stat="density", common_norm=False)


sns.displot(data, x="max_price", hue="club", stat="density", common_norm=False)


sns.displot(data, x="shirt_nr", hue="club", stat="density", common_norm=False)


#I.f) Kernel density estimations


sns.displot(data, x="height", kind="kde", bw_adjust=0.5)


sns.displot(data, x="age", kind="kde", bw_adjust=0.30)


sns.displot(data, x="price", kind="kde", bw_adjust=0.5)


sns.displot(data, x="max_price", kind="kde", bw_adjust=0.5)


sns.displot(data, x="shirt_nr", kind="kde", bw_adjust=0.5)


#I.g) Empirical cumulative distribution


sns.displot(data, x="height", hue="position", kind="ecdf")


sns.displot(data, x="age", hue="position", kind="ecdf")


sns.displot(data, x="price", hue="position", kind="ecdf")


sns.displot(data, x="max_price", hue="position", kind="ecdf")


sns.displot(data, x="shirt_nr", hue="position", kind="ecdf")


#II.a) Distribution of the variables


#height: normally distributed (slight skew but negligible)
#age: normally distributed (slight skew but negligible)
#price: skewed
#max_price: skewed
#shirt_nr: bimodal


#II.b) Outliers


#height: No significant outliers
#age: No significant outliers
#price: Yes, there are many outliers (for example some players cost 120M, 110M etc.. disturbing the mean)
#max_price: Yes, same thing, many outliers
#shirt_nr: NO significant outliers


#II.c) Central Tendency and Dispersion


#height: the median height for a player is 1.85m tall. The data is not spread out much with a standard deviation of 6cm, so player heights find themselves close to the median
#age: the median age for a player is 25 years old, with a moderate spread (s.d of 4.70years).
#price: the median price for a player is very low (3.5M euros), the deviation is very high (14.59M euros), indicating big dispersion in the data
#max_price: the median max value for players in the bundeslifa is 7M euros, with a very high dispersion in the data (s.d = 18.58M euros), same pattern as price
#shirt_nr: the median shirt number is 20, with a high standard deviation of 12.41, indicating dispersion in the data


#II.d) Direction of Skewness


#height: normally distributed (slight skew to the right but negligible)
#age: normally distributed (slight skew to the left but negligible)
#price: skewed to the right
#max_price: skewed to the right
#shirt_nr: bimodal


#II.e) Range with highest frequency


#height: 1.82m to 1.90m are most common, 1.65m to 1.73m and 1.95m to 2.00m are the least frequent
#age: 23yrs to 27yrs are most common, 17-20yrs and 35-40yrs are least frequent
#price: 0-10M euros are most common, 40-120M euros are least frequent
#max_price: 0-20M euros are most common, 20-150M euros are least frequent
#shirt_nr: 1-10 and 20-29 are most common, 35-50 are least frequent


##5 Multivariate non-graphical EDA


position_foot = pd.crosstab(data["position"], data["foot"], normalize = "index")
print(position_foot)


#From this, we can see that goalkeepers are predominantly right footed, this is due to the historical preference of goalkeepers being right-footed, however we can still see that goalkeepers that are two-footed are prioritised due to modern changes in the sport (distribution)
#We can also see that defenders have the highest left foot percent of any group (38.3%), this shows that teams need left footed and right footed defenders equally to start the play from the defense into the attack on both sides
#In the midfield, right-footed players are mostly favoured.
#In attack, left footed players are marginally favoured (18%) to provide a different way of attacking the opponent (wingers etc.)


club_outfitter = pd.crosstab(data["club"], data["outfitter"], normalize = "index")
print(club_outfitter)


#In the biggest clubs such as Bayern Munich and Borussia Dortmund Adidas, Nike, and Puma prevail over other player sponsors
#In Bayern Munich, the most common sponsor in their players is adidas with 40.7% of players wearing adidas, this shows the historic partnership between the club and the outfitter
#However, in Borussia Dortmund, there is a more balanced distribution of sponsors with 20% of the players wearing Nike, 16.7% of players wearing Adidas, and 13.3% wearing Puma
#The club with the highest amount of players wearing Puma is Borussia Monchengladbach


club_nationality = pd.crosstab(data["club"], data["nationality"], normalize = 'index')
print(club_nationality)


#In the top clubs like Bayern Munich, Bourssia Dortmund, and Leipzig, there is less of a focus on German players
#Instead, these clubs set their focus on international talents to win them more trophies
#For instance, Bayern and Leipzig both have around 22% of their players as German, which is low considering that they are German teams
#In Dortmund, the focus is more on Scandinavian (6.7%) and English players
#In Leipzig the focus is more on French and African talent
#In Borussia Monchengladbach, one of the smaller teams in Germany, the focus is more on German players with 44.4% of players being German


data["club_position"] = data["club"] + " " + data["position"]
three_way_table = pd.crosstab(data["club_position"], data["foot"])
print(three_way_table)


#Right-footed players dominate across all clubs and position
#However, attackers show the highest proportion of left-footed players. This shows that clubs value left-footed attackers like wingers for crossing,etc.
#One club that stands out is TSG Hoffenheim. In fact, they have a huge amount of left-footed midfielders, maybe it shows that they have a certain strategy when recruiting.
#6.1
#a)
sns.relplot(data, x="age", y="price", col="foot")  

#b)
sns.relplot(data, x="age", y="price", hue="position", size="height", col="foot")

#c)
sns.relplot(data, x="age", y="price", kind="line")
#it makes sense to use age and price because they are both continuous,
#and there is a clear relationship between the two.
#market value goes up around the age of 20 and continues
#increasing until about the age of 28 where it starts going down.
#which makes sense because 28 is considered the prime age for athletes

#d)
sns.barplot(data, x="position", y="price", ci="sd")

#e)
sns.lmplot(data, x="height", y="price")


#6.2 
#a)
sns.catplot(data, x="foot", y="price", kind="strip", jitter=True)

#b)
sns.catplot(data, x="position", y="height", kind="strip", jitter=False)

#c)
sns.catplot(data, x="outfitter", y="price", hue="foot", kind="swarm")
plt.tight_layout()


#d)
sns.catplot(data, x="position", y="height", hue="foot", kind="box")
plt.show()

#e)
sns.boxenplot(data, x="position", y="height")
plt.show()

#f)
sns.violinplot(data, x="position", y="age", hue="foot", bw_adjust=0.5)
plt.show()

#g)
g=sns.catplot(data, x="position", y="height", bw_adjust=0.5, kind="violin", inner=None)
sns.swarmplot(data, x="position", y="height", color="k", size=3, ax=g.ax)
plt.show()

#h)
sns.barplot(data, x="position", y="price", hue="foot", ci=97)
plt.show()

#i)
sns.pointplot(data, x="position", y="price", hue="foot", ci=90, linestyles="--")
plt.show()

#j)
sns.countplot(data, x="position")
plt.show()

#6.3
#a)
sns.histplot(data, x="height", y="price", bins=30, cmap="plasma", cbar=True)

#b)
sns.displot(data, x="shirt_nr", y="price", kind="kde", fill=True, thresh=0.05, levels=15)  

#c) 
sns.displot(data, x="shirt_nr", y="price", hue="foot", kind="kde", fill=True)