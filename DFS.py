def dfs(graph, vertex, visited):
    visited[vertex] = True
    print(vertex, end=' ')

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def main():
    graph = {}

    # Taking user input for adding edges
    num_vertices = int(input("Enter the number of vertices: "))
    print("Enter edges in the format 'vertex1 vertex2': ")

    for _ in range(num_vertices):
        vertex1, vertex2 = map(int, input().split())

        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []

        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

    # Initializing visited array
    visited = {vertex: False for vertex in graph}

    # Starting DFS from vertex 1
    start_vertex = int(input("Enter the starting vertex for DFS: "))
    print("DFS Traversal:")
    dfs(graph, start_vertex, visited)

if __name__ == "__main__":
    main()
