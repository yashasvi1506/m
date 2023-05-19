import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
iris = load_iris()
X = iris.data
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
kmeans_labels = kmeans.fit_predict(X_std)
agglo = AgglomerativeClustering(n_clusters=3)
agglo_labels = agglo.fit_predict(X_std)
dbscan = DBSCAN(eps=0.6, min_samples=3)
dbscan_labels = dbscan.fit_predict(X_std)
print("k-Means silhouette score:", silhouette_score(X_std, kmeans_labels))
print("Agglomerative silhouette score:", silhouette_score(X_std, agglo_labels))
print("DBSCAN silhouette score:", silhouette_score(X_std, dbscan_labels))
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))
ax1.scatter(X[:, 0], X[:, 1], c=kmeans_labels)
ax1.set_title("k-Means")
ax2.scatter(X[:, 0], X[:, 1], c=agglo_labels)
ax2.set_title("Agglomerative")
ax3.scatter(X[:, 0], X[:, 1], c=dbscan_labels)
ax3.set_title("DBSCAN")
plt.show()
