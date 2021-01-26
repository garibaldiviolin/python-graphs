def create_valid_path_graph():
    """The valid path from A to F is A-B-D-E-C-F."""
    return {
        "A": {"B": 2, "D": 4},
        "B": {"C": 9, "D": 1},
        "C": {"F": 6},
        "D": {"E": 5},
        "E": {"C": 3, "F": 10},
        "F": {}
    }


def create_invalid_path_graph():
    """Removes the edges that connects to F vertex."""
    valid_graph = create_valid_path_graph()
    del valid_graph["C"]["F"]
    del valid_graph["E"]["F"]
    return valid_graph
