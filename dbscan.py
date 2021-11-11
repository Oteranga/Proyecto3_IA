from matplotlib.pyplot import contour
import aux as a
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import collections
class DBSCAN:
    list_clusters = []
    
    def __init__(self,df,r,min_points):
        self.df = df
        self.x_features = df.iloc[:,:-1]
        self.y_list = df.iloc[:,-1].values.tolist()
        self.r = r
        self.min_points = min_points
        self.x_pairs = a.make_pairs(self.x_features)
        self.column_names = a.get_unique_values(df.iloc[:,-1].values.tolist())

    def dbscan_algorithm(self):
        cluster = 0
        pos = 0
        while pos!=len(self.x_pairs)-1:
        #for point in self.x_pairs:
            point = self.x_pairs[pos]
            if point.cluster != -1: #With label
                continue
            neighbors = a.range_query(self.x_pairs, point, self.r)
            if len(neighbors) < self.min_points: #Atypical values
                point.cluster = 0
                pos += 1
                continue
            cluster += 1
            point.cluster = cluster
            new_cluster = self.update_cluster(neighbors,cluster)
            self.remove_classified(new_cluster)
            self.list_clusters.append(new_cluster)
        return self.list_clusters

    def update_cluster(self,neighbors,cluster):
        new_cluster = neighbors
        for val in neighbors:
            if val.cluster == 0:
                val.cluster = cluster
            elif val.cluster != -1:
                continue
            new_neighbors = a.range_query(self.x_pairs, val, self.r)
            val.cluster = cluster
            if len(new_neighbors) < self.min_points:
                continue
            new_cluster = self.remove_repeated(new_cluster,new_neighbors)
        return new_cluster
    
    def remove_classified(self,new_cluster):
        for val in new_cluster:
            if val in self.x_pairs:
                self.x_pairs.remove(val)

    def remove_repeated(self,main_list,temp_list):
        new_list = main_list.copy()
        for val in temp_list:
            equal_arrays = False
            for val2 in new_list:
                list1 = val.data
                list2 = val2.data
                comparison = list1 == list2
                equal_arrays = comparison.all()
                if equal_arrays:
                    break
            if not equal_arrays:
                new_list.append(val)
        return new_list
    
    def print_clusters(self):
        size = 0
        for i,cluster in enumerate(self.list_clusters):
            print("Cluster "+str(i+1))
            size += len(cluster)
            for val in cluster:
                val.print_pair(self.y_list)
        print(size)
    
    def plot_clusters(self,num_name):
        num_clusters = len(self.list_clusters)
        temp = np.zeros((num_clusters, len(self.column_names)))
        dfs = pd.DataFrame(temp,columns=self.column_names)
        for i in range(num_clusters):
            counter = self.get_frequency(self.list_clusters[i])
            for tissue in counter:
                dfs.at[i,tissue] = counter[tissue]
        dfs.plot.bar(rot=0)
        plt.savefig("plots/plot_dbscan"+str(num_name))
    
    def get_frequency(self,samples):
        tissues = []
        for sample in samples:
            tissues.append(self.y_list[sample.id])
        counter = collections.Counter(tissues)
        return counter