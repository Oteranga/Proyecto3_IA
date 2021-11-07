import random

from seaborn.palettes import color_palette
import aux as a
import cluster as cl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class Kmeans:
    cluster_groups = []
    
    def __init__(self,data,k):
        self.data = data
        self.column_names = a.get_unique_values(data.iloc[:,-1].values.tolist())
        self.k = k
        self.rows = len(data)
        self.columns = len(data.columns)

    def kmeans_algorithm(self):
        random_indexes = random.sample(range(self.rows), self.k)
        centroids = [self.data.iloc[i,:-1].values.tolist() for i in random_indexes]
        diff_centroids = True
        self.assign_centroids_to_clusters(centroids)
        self.assign_samples_to_clusters(centroids)
        
        while diff_centroids:
            new_centroids = self.set_new_centroids()
            if((len(new_centroids) == len(centroids)) 
            and (all(i in centroids for i in new_centroids))):
                centroids = new_centroids
                self.cluster_groups.clear()
                self.assign_centroids_to_clusters(centroids)
                self.assign_samples_to_clusters(centroids)
            else:
                diff_centroids = False
        return self.cluster_groups
    
    def set_new_centroids(self):
        new_centroids = []
        for i in range(self.k):
            new_centroid = []
            samples = self.cluster_groups[i].samples
            size = len(samples)
            for sample in samples:
                if len(new_centroid)==0:
                    new_centroid = sample[:-1].copy()
                else:
                    temp = [sample[x] + new_centroid[x] for x in range(len(new_centroid))]
                    new_centroid = temp.copy()
            temp_centroid = [x / size for x in new_centroid]
            new_centroids.append(temp_centroid)
        return new_centroids
    
    def assign_samples_to_clusters(self,centroids):
        for i in range(self.rows):
            row = self.data.iloc[i,:].values.tolist()
            distances = [a.distance(row[:-1],centroids[j]) for j in range(self.k)]
            min_value = min(distances)
            min_index = distances.index(min_value)
            self.cluster_groups[min_index].add_sample(row)
    
    def assign_centroids_to_clusters(self,centroids):
        for centroid in centroids:
            new_cluster = cl.Cluster(centroid)
            self.cluster_groups.append(new_cluster)
    
    def print_clusters(self):
        for i in range(self.k):
            print("Cluster",i,":")
            self.cluster_groups[i].print_samples()
    
    def plot_clusters(self):
        temp = np.zeros((self.k, len(self.column_names)))
        dfs = pd.DataFrame(temp,columns=self.column_names)
        for i in range(self.k):
            counter = self.cluster_groups[i].get_frequency()
            for tissue in counter:
                dfs.at[i,tissue] = counter[tissue]
        dfs.plot.bar(rot=0)
        plt.show()