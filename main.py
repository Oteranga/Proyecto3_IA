import data as d
import kmeans as km
import dbscan as dbs
import gmm as g
import agglomerative as ag
from matplotlib import pyplot as plt

#full_data,x_features,y_values = d.parse_data()
full_data, x_features = d.parse_data()
#d.reduce_dim(full_data,2)
""" kmeans_obj = km.Kmeans(full_data,7)
cluster_groups = kmeans_obj.kmeans_algorithm()
kmeans_obj.print_clusters() """

dbscan_cluster = dbs.dbscan(x_features, 100, 40)
for val in dbscan_cluster:
    print(val)

""" plt.title("Hierarchical Clustering Dendrogram")
agglomerative_cluster = ag.agglomerativeClustering(x_features)
ag.plotDendogram(agglomerative_cluster, truncate_mode="level")
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show() """

print("Done")

