from unittest import TestCase

from algorithms.dijkstra import dijkstra_path
from tests.fixtures import create_valid_path_graph, create_invalid_path_graph


class TestDijkstra(TestCase):
    def test_valid_path(self):
        graph = create_valid_path_graph()
        expected_path = (["A", "B", "D", "E", "C", "F"], 17)
        self.assertEqual(dijkstra_path(graph, "A", "F"), expected_path)

    def test_invalid_path(self):
        graph = create_invalid_path_graph()
        expected_path = ([], 0)
        self.assertEqual(dijkstra_path(graph, "A", "F"), expected_path)
