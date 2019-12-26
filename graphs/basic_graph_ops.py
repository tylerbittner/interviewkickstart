######
# basic_graph_ops.py
######

from collections import deque


class Graph():

    def __init__(self, size):
        # Adjacency list is a list of lists
        self.adj_list = [[] for i in range(size)]

    def __repr__(self):
        return str(self.adj_list)

    def add_edge(self, start, end, undirected=True):
        self.adj_list[start].append(end)
        if undirected:
            self.adj_list[end].append(start)

    def has_eulearian_cycle(self):
        '''Return True if all vertices have even degree'''
        pass

    def has_eulearian_path(self):
        '''Return True if either 0 or 2 vertices have odd degree'''
        pass

    def bfs(self, start):
        '''
        Param start: int ID of vertex to start search at
        '''
        
        captured = [False] * len(self.adj_list)      # List of whether vertices have been "captured" yet (boolean)
        captured[start] = True
        visited = [False] * len(self.adj_list)       # List of visited vertices (boolean)
        visited[start] = True
        parent = [None] * len(self.adj_list)         # List of parents from which each vertex was reached (int)

        queue = deque()
        queue.append(start)

        while queue:
            curr_v = queue.popleft()
            captured[curr_v] = True
            for neighbor in self.adj_list[curr_v]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = curr_v
                    queue.append(neighbor)

        print(f'captured after bfs(): {captured}')
        print(f'visited after bfs(): {visited}')
        print(f'parent after bfs(): {parent}')


    # Practice BFS again
    def bfs_path(self, v):
        '''Return BFS path thru graph starting at v'''
        '''Time to code: 15:30'''
        visited = {}
        bfs_path = []
        q = deque()

        visited[v] = True
        q.append(v)

        while q:
            curr_v = q.popleft()
            bfs_path.append(curr_v)
            for u in self.adj_list[curr_v]:
                if u not in visited:
                    visited[u] = True
                    q.append(u)

        return bfs_path
        
    def dfs_path(self, v):
        visited = set()
        path = []

        visited.add(v)
        path.append(v)
        return self.dfs_path_rec(v, visited, path)

    def dfs_path_rec(self, v, visited, path):
        visited.add(v)
        for u in self.adj_list[v]:
            if u not in visited:
                visited.add(u)
                path.append(u)
                self.dfs_path_rec(u, visited, path)
        return path

    def find_all_components(self):
        pass


#---
# TEST CASES
#---

# Create test graph
#
#      [3]
#       |
# [0]--[1]--[4]
#  |    |  
#  |    |
# [2]--[5]--[6]
#
#
g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(1, 5)
g.add_edge(2, 5)
g.add_edge(5, 6)
print(f'graph: {g}')

print('*** Calling g.bfs()...')
g.bfs(0)

print('*** Calling g.bfs_path()...')
result = g.bfs_path(0)
print(f'bfs_path() result: {result}')
assert result == [0, 1, 2, 3, 4, 5, 6]

print('*** Calling g.dfs_path()...')
result = g.dfs_path(0)
print(f'dfs_path() result: {result}')
assert result == [0, 1, 3, 4, 5, 2, 6]
