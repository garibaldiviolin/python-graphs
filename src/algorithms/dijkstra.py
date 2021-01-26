def find_shortest_distance(distances, open_vertices):
    shortest_distance = None, float("inf")

    for vertex in open_vertices:
        if distances[vertex] < shortest_distance[1]:
            shortest_distance = vertex, distances[vertex]
    return shortest_distance[0]


def dijkstra_path(graph, start_vertex, end_vertex):
    shortest_path = []
    distances = {vertex: float("inf") for vertex in graph.keys()}
    distances[start_vertex] = 0

    open_vertices = {vertex for vertex in graph.keys()}

    while open_vertices:
        vertex = find_shortest_distance(distances, open_vertices)
        open_vertices.remove(vertex)
        shortest_path.append(vertex)
        if vertex == end_vertex:
            break

        for connected_vertex, distance in graph[vertex].items():
            new_distance = distances[vertex] + graph[vertex][connected_vertex]
            if new_distance < distances[connected_vertex]:
                distances[connected_vertex] = new_distance

    return shortest_path, distances[end_vertex]
