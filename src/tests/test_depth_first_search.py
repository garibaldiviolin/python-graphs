from unittest import TestCase

from algorithms.depth_first_search import can_visit_all_nodes
from tests.fixtures import create_valid_path_graph, create_invalid_path_graph


class TestBreathFirstSearch(TestCase):
    def test_valid_path(self):
        graph = create_valid_path_graph()
        self.assertTrue(can_visit_all_nodes(graph, "A"))

    def test_invalid_path(self):
        graph = create_invalid_path_graph()
        self.assertFalse(can_visit_all_nodes(graph, "A"))

    def test_empty_graph(self):
        graph = {}
        self.assertFalse(can_visit_all_nodes(graph, "A"))
