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

    def dbscan_algorithm(self):
        x_pairs = a.make_pairs(self.x_features,self.y_list)
        cluster = 0
        list_clusters = []
        for point in x_pairs:
            if point.cluster != -1 or self.already_in(point): #With label
                continue
            neighbors = a.range_query(x_pairs, self.y_list, point, self.r)
            if len(neighbors) < self.min_points: #Atypical values
                point.cluster = 0
                continue
            cluster += 1
            point.cluster = cluster
            if point in neighbors:
                neighbors.remove(point)
            new_cluster = self.update_cluster(neighbors,cluster,x_pairs)
            list_clusters.append(new_cluster)
        return self.list_clusters

    def update_cluster(self,neighbors,cluster,x_pairs):
        new_cluster = neighbors
        for val in neighbors:
            if val.cluster == 0:
                val.cluster = cluster
            elif val.cluster != -1 or self.already_in(val):
                continue
            new_neighbors = a.range_query(x_pairs, self.y_list, val, self.r)
            val.cluster = cluster
            if len(new_neighbors) < self.min_points:
                continue
            new_cluster = self.remove_repeated(new_cluster,new_neighbors)
        return new_cluster

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

    def already_in(self,point):
        for cluster in self.list_clusters:
            equal_arrays = False
            for val in cluster:
                comparison = point.data == val.data
                equal_arrays = comparison.all()
                if equal_arrays:
                    return True
            if not equal_arrays:
                continue
        return False
    
    def print_clusters(self):
        for cluster in self.list_clusters:
            print(len(cluster))
            for val in cluster:
                val.print_pair()