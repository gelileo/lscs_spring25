# algorithms/bfs.py
# Approach: BFS begins at a source node and explores all its
# immediate neighbors first, then moves on to the neighbors
# of those nodes, effectively working level by level.
# A queue is typically used to keep track of nodes to visit next.
#

from collections import deque

def bfs(maze, start, goal):
    """
    Perform a Breadth-First Search on the maze.

    :param maze: 2D list (rows x cols) with 0 for open, 1 for wall
    :param start: (row, col) starting position
    :param goal: (row, col) goal position
    :return: A list of visited cells in order (for visualization)
             and the final path as a list of (row, col).
            If no path is found, return an empty list for the path.
    sample return:
    ([(0, 0), (0, 1), ...], [(0, 0), (0, 1), (1, 1), ...])
    where the first list is the order of visited cells and
    the second list is the path from start to goal.
    """
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    parent = dict()  # To reconstruct the path

    queue = deque([start])
    visited[start[0]][start[1]] = True

    order_visited = []  # For visualization or step counting

    while queue:
        current = queue.popleft()
        order_visited.append(current)

        if current == goal:
            # Reconstruct path after reaching the goal
            path = []
            # put your code here
            
            return order_visited, path

        r, c = current # Get current position
        # Explore neighbors (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # put your code here

    # If no path found
    return order_visited, []
