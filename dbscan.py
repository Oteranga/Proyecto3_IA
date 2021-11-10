from matplotlib.pyplot import contour
import aux as a

class DBSCAN:
    list_clusters = []
    
    def __init__(self,df,r,min_points):
        self.df = df
        self.x_features = df.iloc[:,:-1]
        self.y_list = df.iloc[:,-1].values.tolist()
        self.r = r
        self.min_points = min_points
        self.x_pairs = a.make_pairs(self.x_features,self.y_list)

    def dbscan_algorithm(self):
        cluster = 0
        for point in self.x_pairs:
            if point.cluster != -1: #With label
                continue
            neighbors = a.range_query(self.x_pairs, self.y_list, point, self.r)
            if len(neighbors) < self.min_points: #Atypical values
                point.cluster = 0
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
            new_neighbors = a.range_query(self.x_pairs, self.y_list, val, self.r)
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
                val.print_pair()
        print(size)