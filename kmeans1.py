import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering

# Array of points
points = np.array([(2, 10), (2, 5), (8, 4), (5, 8), (7, 5), (6, 4), (1, 2), (4, 9)])

# K-means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans_labels = kmeans.fit_predict(points)

# DBSCAN
dbscan = DBSCAN(eps=2, min_samples=2)
dbscan_labels = dbscan.fit_predict(points)

# Agglomerative clustering
agglomerative = AgglomerativeClustering(n_clusters=3)
agglomerative_labels = agglomerative.fit_predict(points)

# Plotting
plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.scatter(points[:, 0], points[:, 1], c=kmeans_labels)
plt.title('K-means Clustering')

plt.subplot(132)
plt.scatter(points[:, 0], points[:, 1], c=dbscan_labels)
plt.title('DBSCAN Clustering')

plt.subplot(133)
plt.scatter(points[:, 0], points[:, 1], c=agglomerative_labels)
plt.title('Agglomerative Clustering')

plt.tight_layout()
plt.show()
