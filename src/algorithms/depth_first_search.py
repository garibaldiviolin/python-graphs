from queue import deque


def can_visit_all_nodes(graph, start_vertex):
    if not graph:
        return False

    vertices_to_visit = {
        vertex for vertex in graph.keys() if vertex != start_vertex
    }
    current_vertices = deque()
    current_vertices.append(start_vertex)

    while True:
        try:
            vertex = current_vertices.pop()
        except IndexError:
            break

        for connected_vertex in graph[vertex].keys():
            if connected_vertex not in vertices_to_visit:
                continue

            vertices_to_visit.remove(connected_vertex)
            current_vertices.append(connected_vertex)

    return len(vertices_to_visit) == 0
