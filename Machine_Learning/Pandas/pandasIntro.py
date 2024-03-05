# You'll have to import Pandas with the following command

import pandas as pd

data = {"apples": [3, 2, 0, 1], "oranges": [0, 3, 7, 2]}

# we will be visualiging the data in a table format

purchases = pd.DataFrame(data)
print(purchases)
