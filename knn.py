import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
data = pd.read_csv('knndata.csv')
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
accuracy = knn.score(X_test, y_test)
print("Accuracy:", accuracy)
new_data = [[6.0, 2.7], [5.2, 2.8], [5.6, 2.7],[4.9, 2.5]]
predictions = knn.predict(new_data)
print(predictions)
