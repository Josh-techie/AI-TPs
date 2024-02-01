# libraries
import pandas as pd
# connection au drive
from google.colab import drive
drive.mount("/content/drive", force_remount=True)
data = pd.read_csv('/content/drive/My Drive/market.csv')
# visualisation
data.head()
# description
data.describe()
df = data
# selection de la cible
y = df['Close']
# selection des caracteriqtique sans cible
x = df.drop(columns=['Date', 'Close', 'Total Trade Quantity', 'Turnover (Lacs)'])
# Separation de la base de données en training data and testing data
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.15)
print(train_x.shape )
print(test_x.shape)
print(train_y.shape)
print(test_y.shape)
# choix de modele
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
# training
regression.fit(train_x, train_y)
# metrique d'evaluation
from sklearn.metrics import mean_squared_error
print("regression coefficient",regression.coef_)
mse = mean_squared_error(test_y, predicted)
print("mean squared error: ", mse)
# testing
predicted=regression.predict(test_x)
# visualisation de quelques resultats de test
dfr=pd.DataFrame({'actual_close':test_y, 'Predicted_close':predicted})
dfr.head(10)
