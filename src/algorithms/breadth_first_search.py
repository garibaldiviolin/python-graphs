from queue import Queue


def get_shortest_path(paths, start_vertex, end_vertex):
    shortest_path = [end_vertex]

    current_vertex = end_vertex
    while current_vertex != start_vertex:
        current_vertex = paths[current_vertex]
        shortest_path.insert(0, current_vertex)

    return shortest_path


def breadth_first_search_path(graph, start_vertex, end_vertex):
    if not graph:
        return []

    paths = {}
    visited_vertices = set()
    vertices = Queue()
    vertices.put(start_vertex)

    while vertices.empty() is False:
        vertex = vertices.get()

        for connected_vertex in graph[vertex].keys():
            if connected_vertex in visited_vertices:
                continue

            visited_vertices.add(connected_vertex)
            paths[connected_vertex] = vertex
            vertices.put(connected_vertex)
            if connected_vertex == end_vertex:
                return get_shortest_path(paths, start_vertex, end_vertex)

    return []
