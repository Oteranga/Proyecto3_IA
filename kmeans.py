import random
import aux as a

def kmeans(x_features,k):
    rows = len(x_features)
    groups = {}
    random_indexes = [random.randint(0, rows-1) for i in range(k)]
    centroids_prev = [x_features.iloc[i,:] for i in random_indexes]
    centroids_next = []
    for i in range(k):
        groups[i] = []
    
    while centroids_prev!=centroids_next:
        for i in range(rows):
            row_list = x_features.iloc[i,:].values.tolist()
            distances = [a.distance(row_list,centroids_prev[j].values.tolist()) for j in range(k)]
            min_value = min(distances)
            min_index = distances.index(min_value)
            groups[min_index].append(i)
