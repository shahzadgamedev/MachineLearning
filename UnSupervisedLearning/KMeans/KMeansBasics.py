import numpy as np
import matplotlib.pyplot as plt
from InteractiveGraph import InteractiveGraph

plot_objects = []


def perform_k_means_clustering(graph, input_data, max_interation, ax, change_color):
    # number of data points
    m = input_data.shape[0]
    color_list = []
    if m < 2:
        print("Number of data points must be at least 2")
        return

    distCentroid1 = np.zeros(m)
    distCentroid2 = np.zeros(m)
    # defined two centroids
    centroid1 = input_data[0]
    centroid2 = input_data[1]

    for i in range(max_interation):
        points_centroid1 = []
        points_centroid2 = []
        color_list.clear()
        for d in range(m):
            distCentroid1[d] = distance(centroid1, input_data[d])
            distCentroid2[d] = distance(centroid2, input_data[d])
            if distCentroid1[d] < distCentroid2[d]:
                points_centroid1.append(input_data[d])
                color_list.append('red')
            else:
                points_centroid2.append(input_data[d])
                color_list.append('blue')
        centroid1 = np.mean(points_centroid1, axis=0)
        centroid2 = np.mean(points_centroid2, axis=0)
        print(f"Iteration {i + 1}:")
        print(f"Centroid 1: {centroid1}")
        print(f"Centroid 2: {centroid2}")
        change_color(color_list)
        graph.show_centroid(centroid1, centroid2)


def distance(centroid, data_point):
    return np.sqrt(np.sum((centroid - data_point) ** 2))


interactive_graph = InteractiveGraph(perform_k_means_clustering)
