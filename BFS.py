from collections import deque

def bfs_recursive(graph, queue):
    if not queue:
        return

    current_node = queue.popleft()
    print(current_node, end=' ')

    for neighbor in graph[current_node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    bfs_recursive(graph, queue)

def bfs(graph, start):
    visited.add(start)
    queue = deque([start])
    bfs_recursive(graph, queue)

if __name__ == "__main__":
    graph = {}

    # Taking user input for adding edges
    num_vertices = int(input("Enter the number of vertices: "))
    print("Enter edges in the format 'vertex1 vertex2'. Enter 'done' when finished:")

    for _ in range(num_vertices):
        vertex1, vertex2 = map(int, input().split())

        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []

        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

    visited = set()
    start_vertex = int(input("Enter the starting vertex for BFS: "))
    print("BFS Traversal:")
    bfs(graph, start_vertex)
