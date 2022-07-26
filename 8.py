from sklearn import datasets
import csv
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
wine = datasets.load_wine()
print ("Features: ", wine.feature_names)
wine_data=csv.reader("wine.csv")
print ("Labels: ", wine.target_names)
print (wine.data[0:5])
print (wine.target)
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3,random_state=109)
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("precison:",metrics.precision_score(y_test, y_pred,average="macro"))