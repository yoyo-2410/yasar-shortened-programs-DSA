# Depth First Search Tree Traversal

def recursdfs(graph, s, path=None):
    if path is None:
        path = []
    if s not in path:
        path.append(s)
        if s not in graph:
            return path
        for neighbour in graph[s]:
            path = recursdfs(graph, neighbour, path)
    return path

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E", "F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

dfs = recursdfs(graph, "A")

print("\nDepth First Search Traversal\n")
print(dfs)
