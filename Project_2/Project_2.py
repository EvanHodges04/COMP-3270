import os
import time
from collections import deque

def build_graph(edge_lines): # Builds the graph as an adjacency list.
    graph = {}
    for line in edge_lines:
        line = line.strip()
        tokens = line.split(',')
        node1 = tokens[0].strip()
        node2 = tokens[1].strip()
        
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        if node2 not in graph[node1]:
            graph[node1].append(node2)
        if node1 not in graph[node2]:
            graph[node2].append(node1)     
    return graph

def bfs(graph, start, target): # Performs BFS from the start node, terminating when the target node is visited.
    visited = set()
    queue = deque()
    visited_count = 0
    
    queue.append(start)
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        visited_count += 1
        
        if current == target:
            return visited_count
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)   
    return None

def dfs(graph, start, target): # Performs DFS from the start node, terminating when the target node is visited.
    visited = set()
    stack = []
    visited_count = 0
    
    stack.append(start)
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        visited_count += 1
        
        if current == target:
            return visited_count
        
        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                stack.append(neighbor)            
    return None

def main(): # Reads in test case file, builds graph, generates test pairs, measures and prints the BFS/DFS traversal metrics.
    
    file_path = os.path.join(os.path.dirname(__file__), "Data.txt")
    with open(file_path, 'r') as f:
        edge_lines = f.readlines()

    graph = build_graph(edge_lines)
    nodes = sorted(graph.keys(), key=lambda x: int(x.split('_')[1]))
    
    start_node = "N_0"    
    test_targets = [node for node in nodes if node != start_node]
    
    print("Node Pair\tBFS Distance\tBFS Time (ms)\tDFS Distance\tDFS Time (ms)")
    
    for target in test_targets:
        t0 = time.perf_counter()
        bfs_visited = bfs(graph, start_node, target)
        t1 = time.perf_counter()
        bfs_time = (t1 - t0) * 1000
        
        t2 = time.perf_counter()
        dfs_visited = dfs(graph, start_node, target)
        t3 = time.perf_counter()
        dfs_time = (t3 - t2) * 1000
        
        bfs_str = str(bfs_visited) if bfs_visited is not None else "-"
        dfs_str = str(dfs_visited) if dfs_visited is not None else "-"
        
        print(f"{start_node} -> {target}\t{bfs_str}\t\t{bfs_time:.4f}\t\t{dfs_str}\t\t{dfs_time:.4f}")
    input("Press enter to exit.")
main()