
def bfs(graph, start):
    """Breadth-first search algorithm.

    :param graph: Input graph represented as an adjacency list.
    :type graph: dict
    :param start: Starting node for BFS traversal.
    :type start: str
    :return: List of nodes in BFS order.
    :rtype: list
    """
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors = graph.get(node, [])
            queue.extend(neighbors)
    return visited
