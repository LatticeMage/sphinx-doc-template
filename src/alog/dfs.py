
def dfs(graph, start, visited=None):
    """Depth-first search algorithm.

    :param graph: Input graph represented as an adjacency list.
    :type graph: dict
    :param start: Starting node for DFS traversal.
    :type start: str
    :param visited: List of already visited nodes.
    :type visited: list, optional
    :return: List of nodes in DFS order.
    :rtype: list
    """
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
