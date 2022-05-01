import unittest
from recursive import shortestpath
from recursive import recursive_floyd_warshall


class TestFloydAlgo(unittest.TestCase):

    # Test Shortestpath function
    def test_shortestpath(self):
        INF = 9999
        graph = [[0, 5, INF, 10],
                 [INF, 0, 3, INF],
                 [INF, INF, 0, 1],
                 [INF, INF, INF, 0]
                 ]
        self.assertEqual(shortestpath(2, 3, 0, graph), 1)

    # Test recursive_floyd_warshall function
    def test_recursive_floyd_warshall(self):
        INF = 9999
        graph = [[0, 5, INF, 10],
                 [INF, 0, 3, INF],
                 [INF, INF, 0, 1],
                 [INF, INF, INF, 0]
                 ]
        output = [[0, 5, 8, 9],
                  [INF, 0, 3, 4],
                  [INF, INF, 0, 1],
                  [INF, INF, INF, 0]
                  ]
        self.assertEqual(recursive_floyd_warshall(graph), output)