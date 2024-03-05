# You'll have to import Pandas with the following command

import pandas as pd

data = {"apples": [3, 2, 0, 1], "oranges": [0, 3, 7, 2]}

# we will be visualiging the data in a table format

purchases = pd.DataFrame(data)
# print(repr(purchases))

########################## CREATING OUR DATAFRAME ##########################

    # USE CASE `1`: Creating a DataFrame from a dictionary
# List of lists
data1 = [["tom", 25], ["krish", 30], ["nick", 26], ["juli", 22]]

# Create the pandas DataFrame
df = pd.DataFrame(data1, columns=["Name", "Age"])
# print(df)

    # USE CASE `2`: Creating a DataFrame with index Parameter ##########################
purchases = pd.DataFrame(data, index=["June", "Robert", "Lily", "David"])
print(purchases)

    # OUPUT
#         apples  oranges
# June         3        0
# Robert       2        3
# Lily         0        7
# David        1        2
