import math
import cluster as cl
from sklearn.neighbors import KDTree
import numpy as np

def distance(centroid,current_row):
    distance = 0
    for i in range(len(centroid)):
        distance += pow(centroid[i] - current_row[i], 2)
    return math.sqrt(distance)

def make_pairs(df):
    df = df.values.tolist()
    pairs = []
    for i in range(len(df)):
        newObject = cl.Pair(df[i])
        pairs.append(newObject)
    return pairs

def range_query(df, point, radius):
    new_df = []
    for set in df:
        new_df.append(set.data)
    new_arrays = np.array(new_df)
    tree = KDTree(new_arrays, leaf_size = 20)
    indices = tree.query_radius(np.array(point.data).reshape(1, -1), r = radius)
    neighbors = []
    for n in indices[0].tolist():
        newObject = cl.Pair(new_arrays[n])
        newObject.setCluster(df[n].cluster)
        neighbors.append(newObject)
    return neighbors

def get_unique_values(values):
    list_of_unique_numbers = []
    unique_values = set(values)
    for value in unique_values:
        list_of_unique_numbers.append(value)
    return list_of_unique_numbers