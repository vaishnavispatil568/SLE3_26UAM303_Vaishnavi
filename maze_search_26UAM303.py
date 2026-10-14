from collections import deque

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

class MazeProblem:
    def __init__(self, maze, start, goal):
        self.maze = maze
        self.start = start
        self.goal = goal

    def bfs_search(self):
        queue = deque([Node(self.start)])
        visited = {self.start}
        while queue:
            current = queue.popleft()
            if current.state == self.goal:
                return self.reconstruct_path(current)
            for next_state in self.get_successors(current.state):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(Node(next_state, current))
        return None

    def dfs_search(self):
        stack = [Node(self.start)]
        visited = set()
        while stack:
            current = stack.pop()
            if current.state == self.goal:
                return self.reconstruct_path(current)
            if current.state not in visited:
                visited.add(current.state)
                for next_state in self.get_successors(current.state):
                    if next_state not in visited:
                        stack.append(Node(next_state, current))
        return None

    def get_successors(self, state):
        # Return valid neighboring positions (Up, Down, Left, Right)
        pass

    def reconstruct_path(self, node):
        path = []
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1]
                  
