'''David Tattersall, Mohamed Moussa'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



#Importing the data

data = pd.read_csv("bundesliga_player.csv")

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

print("-----Mode-----")
print(categorical_data.mode())


##4) Univariate graphical EDA
'''
#a) bins

sns.displot(numerical_data, x="age", binwidth=2)

sns.displot(numerical_data, x="height", binwidth=0.05)

sns.displot(numerical_data, x="price", binwidth=5)

sns.displot(numerical_data, x="max_price", binwidth=10)

sns.displot(numerical_data, x="shirt_nr", binwidth=2)

#b) conditioning

sns.displot(data, x="age", hue="position")

sns.displot(data, x="height", hue="position")

sns.displot(data, x="price", hue="position")

sns.displot(data, x="max_price", hue="position")

sns.displot(data, x="shirt_nr", hue="position")

#c) stacked histograms

sns.displot(data, x="age", hue="position", multiple="stack")

sns.displot(data, x="height", hue="position", multiple="stack")

sns.displot(data, x="price", hue="position", multiple="stack")

sns.displot(data, x="max_price", hue="position", multiple="stack")

sns.displot(data, x="shirt_nr", hue="position", multiple="stack")
'''
#d) dodge bars

sns.displot(data, x="price", hue="position", multiple="dodge", bins=3)

sns.displot(data, x="height", hue="position", multiple="dodge", binwidth= 0.05)









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