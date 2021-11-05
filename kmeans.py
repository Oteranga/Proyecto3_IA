import random
import aux as a
import cluster as cl
import numpy as np
class Kmeans:
    cluster_groups = []
    
    def __init__(self,data,k):
        self.data = data
        self.k = k
        self.rows = len(data)
        self.columns = len(data.columns)

    def kmeans_algorithm(self):
        random_indexes = random.sample(range(self.rows), self.k)
        centroids = [self.data.iloc[i,:].values.tolist() for i in random_indexes]
        diff_centroids = True
        self.assign_centroids_to_clusters(centroids)
        self.assign_samples_to_clusters(centroids)
        
        while diff_centroids:
            new_centroids = []
            for i in range(self.k):
                new_centroid = []
                samples = self.cluster_groups[i].samples
                centroid = self.cluster_groups[i].centroid
                size = len(samples)
                for sample in samples:
                    if len(new_centroid)==0:
                        new_centroid = (a.distance(centroid,sample))
                    else:
                        new_centroid = np.add(new_centroid, a.distance(centroid,sample))
                new_centroid[:] = [x / size for x in new_centroid]
                new_centroids.append(new_centroid)
            
            if((len(new_centroids) == len(centroid)) 
            and (all(i in centroids for i in new_centroids))):
                centroids = new_centroids
                self.cluster_groups.clear()
                self.assign_centroids_to_clusters(centroids)
                self.assign_samples_to_clusters(centroids)
            else:
                diff_centroids = False
        return self.cluster_groups
    
    def assign_samples_to_clusters(self,centroids):
        for i in range(self.rows):
            row = self.data.iloc[i,:].values.tolist()
            distances = [a.distance(row,centroids[j]) for j in range(self.k)]
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