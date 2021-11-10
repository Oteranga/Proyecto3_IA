import data as d
import kmeans as km
import dbscan as dbs
import gmm as g
import agglomerative as ag
from matplotlib import pyplot as plt

#full_data,x_features,y_values = d.parse_data()
full_data, x_features = d.parse_data()
#d.reduce_dim(full_data,2)

method_type = "dbscan"

if method_type == "kmeans":
    kmeans_obj = km.Kmeans(full_data,7)
    kmeans_obj.kmeans_algorithm()
    kmeans_obj.print_clusters()
elif method_type == "dbscan":
    dbscan_obj = dbs.DBSCAN(full_data, 90, 10)
    dbscan_obj.dbscan_algorithm()
    dbscan_obj.print_clusters()
elif method_type == "dendogram":
    plt.title("Hierarchical Clustering Dendrogram")
    agglomerative_cluster = ag.agglomerativeClustering(x_features)
    ag.plotDendogram(agglomerative_cluster, truncate_mode="level")
    plt.xlabel("Number of points in node (or index of point if no parenthesis).")
    plt.show()

print("Done")

