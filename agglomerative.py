from sklearn.cluster import AgglomerativeClustering
import numpy as np
from scipy.cluster.hierarchy import dendrogram

def agglomerativeClustering(df):
    df = df.values.tolist()
    dfArray = np.array(df)
    clustering = AgglomerativeClustering(distance_threshold=0, n_clusters=None).fit(dfArray)
    """ labels = clustering.labels_
    label = labels.tolist()
    finalClustering = list(dict.fromkeys(label))
    return finalClustering """
    return clustering

def plotDendogram(model, **kwargs):
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count
    linkage_matrix = np.column_stack([model.children_, model.distances_, counts]).astype(float)
    dendrogram(linkage_matrix, **kwargs)
