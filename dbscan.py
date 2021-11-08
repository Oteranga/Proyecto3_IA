import aux as a

def dbscan(df, r, min_points):
    df = a.make_pairs(df)
    cluster = 1
    list_clusters = []
    for point in df:
        if point.cluster != 0: #With label
            continue
        neighbors = a.range_query(df, point, r)
        if len(neighbors) < min_points: #Atypical values
            point.cluster = 1
            continue
        cluster += 1
        point.cluster = cluster
        if point in neighbors:
            neighbors.remove(point)
        new_cluster = neighbors
        for val in neighbors:
            if val.cluster == 1:
                val.cluster = cluster
            elif val.cluster != 0:
                continue
            new_neighbors = a.range_query(df, val, r)
            val.cluster = cluster
            if len(new_neighbors) < min_points:
                continue
            new_cluster += new_neighbors
        list_clusters.append(new_cluster)
    return list_clusters
            
