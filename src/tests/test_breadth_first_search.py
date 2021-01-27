from unittest import TestCase

from algorithms.breadth_first_search import breadth_first_search_path
from tests.fixtures import create_valid_path_graph, create_invalid_path_graph


class TestBreathFirstSearch(TestCase):
    def test_valid_path(self):
        graph = create_valid_path_graph()
        expected_path = ["A", "B", "C"]
        self.assertEqual(
            breadth_first_search_path(graph, "A", "C"),
            expected_path
        )

    def test_invalid_path(self):
        graph = create_invalid_path_graph()
        expected_path = []
        self.assertEqual(
            breadth_first_search_path(graph, "A", "F"),
            expected_path
        )

    def test_empty_graph(self):
        graph = {}
        expected_path = []
        self.assertEqual(
            breadth_first_search_path(graph, "A", "F"),
            expected_path
        )
