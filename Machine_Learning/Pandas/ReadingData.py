# by now it should be automatic to import the libraries you'll need

import pandas as pd

#################### READING DATA FROM CSV FILE ####################

data = pd.read_csv("data.csv")  # yeah as simple as that 😀

# but wait how do I know if the data was read correctly?
# let's print the first 5 rows of the data
# print(data.head())

# if you run the code you can see it's all good.

# hold up you have to suffer bro, before you learn! 😂
# if you take a look at the data you'll see that the csv file is well structured and formatted
# but what if the file is not well formatted, for examples instead of using `,` we used `;`

# Well I got you covered, you can use the `sep` parameter to specify the delimiter

data1 = pd.read_csv("data1.csv", sep=";")
# here to print and this time we'll print the first 10 rows\
# just getting acquainted with head() method
# print(data1.head(6))
# or print the whole thing
# print(data1)

# #################### READING DATA FROM JSON FILE ####################

data2 = pd.read_json("data.json")
print(data2)