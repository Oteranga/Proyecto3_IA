import data as d
import kmeans as km
import dbscan as dbs
import gmm as g

#full_data,x_features,y_values = d.parse_data()
full_data, x_features = d.parse_data()
#reduce_dim(data)
""" kmeans_obj = km.Kmeans(full_data,7)
cluster_groups = kmeans_obj.kmeans_algorithm()
kmeans_obj.print_clusters() """

dbscan_cluster = dbs.dbscan(x_features, 70, 20)
for val in dbscan_cluster:
    print(val)

print("Done")

