#libraries
import pandas as pd
#connection au drive
from google.colab import drive
drive.mount("/content/drive", force_remount=True)
data = pd.read_csv('/content/drive/My Drive/heart.csv')
#visualiser les ligne de la base de données
data.head()
#Description de la base de données
data.describe()
df = data
#selection de la cible
y = df['target']
#selection des caractériqtiques sans cible
x = df.drop(columns=['target'])
#Separation de la base de données en training data and testing data
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.15)
print(train_x.shape )
print(test_x.shape)
print(train_y.shape)
print(test_y.shape)
#choix de modele
from sklearn.ensemble import RandomForestClassifier
classifier_rf = RandomForestClassifier()
#entrainement
classifier_rf.fit(train_x, train_y)
#evaluation
predictions = classifier_rf.predict(test_x)
#visualisation de quelque resultat
dfr=pd.DataFrame({'actual_etat':test_y, 'Predicted_disease':predictions})
dfr.head(10)
#evaluation metrique
#evaluation metrique
from sklearn.metrics import accuracy_score,confusion_matrix
print(accuracy_score(test_y, predictions))
confusion_matrix(test_y, predictions)
# 1 0
#1 TP FP
#0 FN TN
#accuracy = (TP+TN)/(TP+TN + FP + FN)
#sensitivity = TP/(TP+FN)
#specificty = TN/(TN+FP)
#PPV = TP / (TP+FP)
#NPV = TN / (TN+FN)