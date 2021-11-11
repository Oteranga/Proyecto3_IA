import math
import cluster as cl
from sklearn.neighbors import KDTree
import numpy as np

def distance(centroid,current_row):
    distance = 0
    for i in range(len(centroid)):
        distance += pow(centroid[i] - current_row[i], 2)
    return math.sqrt(distance)

def make_pairs(x_features):
    x_list = x_features.values.tolist()
    pairs = []
    for i in range(len(x_list)):
        new_object = cl.Pair(x_list[i], i)
        pairs.append(new_object)
    return pairs

def range_query(x_pairs, point, radius):
    new_pairs = []
    for set in x_pairs:
        new_pairs.append(set.data)
    new_arrays = np.array(new_pairs)
    tree = KDTree(new_arrays, leaf_size = 20)
    indices = tree.query_radius(np.array(point.data).reshape(1, -1), r = radius)
    neighbors = []
    for n in indices[0].tolist():
        new_object = cl.Pair(new_arrays[n], x_pairs[n].id)
        new_object.set_cluster(x_pairs[n].cluster)
        neighbors.append(new_object)
    return neighbors

def get_unique_values(values):
    list_of_unique_numbers = []
    unique_values = set(values)
    for value in unique_values:
        list_of_unique_numbers.append(value)
    return list_of_unique_numbers