import data as d
import kmeans as km
import dbscan as dbs
import gmm as g
import agglomerative as ag
from matplotlib import pyplot as plt

#full_data,x_features,y_values = d.parse_data()
full_data, x_features = d.parse_data()
#d.reduce_dim(full_data,2)


def test_dendogram():   
    plt.title("Hierarchical Clustering Dendrogram")
    agglomerative_cluster = ag.agglomerativeClustering(x_features)
    ag.plotDendogram(agglomerative_cluster, truncate_mode="level")
    plt.xlabel("Number of points in node (or index of point if no parenthesis).")
    plt.show()

def test_kmeans(num_tests):
    for i in range(num_tests):
        kmeans_obj = km.Kmeans(full_data,7)
        kmeans_obj.kmeans_algorithm()
        kmeans_obj.plot_clusters(i)

def test_dbscan(num_tests,radius,min_points):
    for i in range(num_tests):
        dbscan_obj = dbs.DBSCAN(full_data, radius, min_points)
        dbscan_obj.dbscan_algorithm()
        dbscan_obj.plot_clusters(i)

test_kmeans(4)
#test_dbscan(4,90,10)
print("Done")

