from collections import deque

def path_finder(maze):
    maze = maze.split('\n')

    N = len(maze)
    start = (0, 0)
    end = (N - 1, N - 1)

    queue = deque([(start, 0)])

    visited = set()

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        current, steps = queue.popleft()
        x, y = current

        if current == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 'W' and (nx, ny) not in visited:
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))

    return False
