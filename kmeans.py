import random
import aux as a

class Kmeans:
    cluster_groups = dict()
    
    def __init__(self,data,k):
        self.data = data
        self.k = k
        self.rows = len(data)
        self.columns = len(data.columns)

    def kmeans_algorithm(self):
        random_indexes = [random.randint(0, self.rows-1) for i in range(self.k)]
        centroids = [self.data.iloc[i,0:self.columns-1].values.tolist() for i in random_indexes]
        diff_centroids = True
        for centroid in centroids:
            empty_list = []
            #self.cluster_groups[centroid] = empty_list
            self.cluster_groups.setdefault(centroid,[])
        self.assign_points_to_clusters(centroids)
        
        while diff_centroids:
            new_centroids = []
            for group in self.cluster_groups:
                new_centroid = []
                samples = self.cluster_groups[group]
                size = len(samples)
                for sample in samples:
                    new_centroid += a.distance(group,sample)
                new_centroid /= size
                new_centroids.append(new_centroid)
            if new_centroids != centroids:
                centroids = new_centroids
                self.assign_points_to_clusters(centroids)
            else:
                diff_centroids = False
        return self.cluster_groups
    
    def assign_points_to_clusters(self,centroids):
        for i in range(self.rows):
            row_list = self.data.iloc[i,:].values.tolist()
            distances = [a.distance(row_list,centroids[j].values.tolist()) for j in range(self.k)]
            min_value = min(distances)
            min_index = distances.index(min_value)
            self.cluster_groups[min_index].append(row_list)