from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

datafile = "Coordenadas_Vacunacion_Risaralda_2.csv"

X = np.genfromtxt(
    datafile,
    delimiter=",",
    usecols=range(1, 3),
    skip_header=1
)

n_clusters=3

kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(X)
labels = kmeans.labels_
clusters = kmeans.cluster_centers_


# Plot init seeds along side sample data
plt.figure(1)
#colors = ['#4EACC5', '#FF9C34', '#4E9A06', 'm']
colors = ['#4EACC5', '#FF9C34', '#4E9A06']


for k, col in zip(range(n_clusters), colors):
    cluster_data = labels == k
    cluster_center = clusters[k]
    plt.scatter(X[cluster_data, 0], X[cluster_data, 1], c=col, marker='.')
    plt.scatter(cluster_center[0], cluster_center[1], c=col,marker='x', s=160)            

plt.title('KMeans')
plt.xticks([])
plt.yticks([])
plt.show()

