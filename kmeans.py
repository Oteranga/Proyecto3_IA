import random
import aux as a

class Kmeans:
    cluster_groups = []
    
    def __init__(self,x_features,k):
        self.x_features = x_features
        self.k = k
        self.rows = len(self.x_features)

    def kmeans(self):
        random_indexes = [random.randint(0, self.rows-1) for i in range(self.k)]
        centroids_prev = [self.x_features.iloc[i,:].values.tolist() for i in random_indexes]
        centroids_next = []
        for i in range(self.k):
            self.cluster_groups[i] = []
        self.assign_points_to_clusters(centroids_prev)
        
        while centroids_prev!=centroids_next:
            new_centroid = []
            for i,group in enumerate(self.cluster_groups):
                samples = self.cluster_groups[group]
                size = len(samples)
                for j,sample in enumerate(samples):
                    new_centroid += a.distance(group,sample)
                new_centroid /= size
                centroids_next[i] = new_centroid
    
    def assign_points_to_clusters(self,centroids):
        for i in range(self.rows):
            row_list = self.x_features.iloc[i,:].values.tolist()
            distances = [a.distance(row_list,centroids[j].values.tolist()) for j in range(k)]
            min_value = min(distances)
            min_index = distances.index(min_value)
            self.cluster_groups[min_index].append(i)
