# Lesson 4: Interactive Mode

## Objectives
- Enable users to navigate the maze manually.
- Learn how to handle keyboard inputs in Pygame.
- Record visited Path and # of steps navigated

## Lecture

In this lecture, we will:
1. Explore the concept of interactive mode in a maze-solving application.
2. Learn how to handle keyboard inputs in Pygame to navigate the maze.
3. Understand how to track the player's position and update the maze dynamically.

### Key Topics:
- Pygame event handling for keyboard inputs.
- Updating the player's position based on valid moves.
- Visualizing the player's path in the maze.

### Sample Code Segments

#### Pygame Event Handling for Keyboard Inputs
```python
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            print("Up arrow pressed")
        elif event.key == pygame.K_DOWN:
            print("Down arrow pressed")
        elif event.key == pygame.K_LEFT:
            print("Left arrow pressed")
        elif event.key == pygame.K_RIGHT:
            print("Right arrow pressed")
```

#### Updating the Player's Position Based on Valid Moves
```python
player_pos = [1, 1]  # Starting position
maze = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
]

new_pos = [player_pos[0] - 1, player_pos[1]]  # Move up
if maze[new_pos[0]][new_pos[1]] == 0:  # Check if the new position is valid
    player_pos = new_pos
    print("Player moved to", player_pos)
else:
    print("Invalid move")
```

#### Visualizing the Player's Path in the Maze
```python
visited = []
player_pos = [1, 1]
visited.append(tuple(player_pos))

# Draw visited cells
for cell in visited:
    rect = pygame.Rect(cell[1] * CELL_SIZE, cell[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, (0, 255, 0), rect)  # Green for visited cells

pygame.display.flip()
```

## Homework #1

- Add a feature to highlight the player's path.

## Homework #2: Add a Step Counter Feature

### Objective
Enhance the maze application by adding a step counter feature that tracks the number of steps the user takes while navigating the maze. The step count should be displayed within the user's current cell in the maze visualization.

### Instructions

1. **Understand the Existing Code**

2. **Identify Where to Add the Step Counter**
   - Locate the section of the code where the player's position is updated based on keyboard inputs (refer to the "Updating the Player's Position Based on Valid Moves" section in the lecture).
   - Plan to increment a step counter variable each time the player makes a valid move.

3. **Implement the Step Counter**
   - Initialize a variable `step_count = 0` at the start of the game to track the number of steps.
   - Inside the logic that updates the player's position, increment `step_count` by 1 whenever the player makes a valid move.

4. **Update the Maze Visualization**
   - Modify the visualization logic to display the step count in the user's current cell.
   - Use the `pygame.font.Font` class to render the step count as text. For example:
     ```python
     font = pygame.font.Font(None, 36)  # Create a font object
     text = font.render(str(step_count), True, (255, 255, 255))  # Render the step count as white text
     screen.blit(text, (player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE))  # Draw the text in the player's cell
     ```

5. **Test Your Implementation**
   - Run the maze application and navigate through the maze using the arrow keys.
   - Verify that the step count increments correctly and is displayed in the user's current cell.
   - Ensure the step count resets to 0 when the game restarts.

### Python Concepts and Libraries to Understand
- **Variables and Incrementing**: Understand how to declare and update variables.
- **Pygame Basics**: Familiarize yourself with `pygame.font.Font` for rendering text and `screen.blit` for drawing on the screen.
- **Event Handling**: Review how keyboard inputs are processed in Pygame.

### Potential Challenges and Hints
- **Text Overlap**: If the step count text overlaps with other visual elements, clear the cell before drawing the text.
  - Hint: Use `pygame.draw.rect` to redraw the cell background before displaying the step count.
- **Off-by-One Errors**: Ensure the step count increments only on valid moves.
  - Hint: Add debug print statements to verify when and where the step count is updated.
- **Font Size and Positioning**: Adjust the font size and text position to ensure the step count is clearly visible.

Good luck, and have fun enhancing your maze application!


# Lesson 5: Understanding Maze-Solving Algorithms

## Objectives
- Learn the basics of maze-solving algorithms like BFS and DFS.
- Implement a simple BFS algorithm to find a path in a grid.

## Lecture

In this lecture, we will:
1. Understand what the Breadth-First Search (BFS) algorithm is and why it is useful.
2. Learn how BFS explores a maze step by step to find the shortest path.
3. See how BFS keeps track of visited cells and reconstructs the path.
4. Introduce the concept of a queue and how it is used in BFS.

### Key Concepts/Topics

#### What is BFS?
BFS is like exploring a maze level by level. Imagine you are standing at the start of a maze, and you want to find the shortest way to the end. BFS helps you do this by checking all possible paths one step at a time.

#### How BFS Works
1. Start at the beginning of the maze.
2. Look at all the neighboring cells you can move to.
3. Move to each neighbor one by one, but don’t visit the same cell twice.
4. Keep doing this until you reach the end of the maze.

#### Why BFS Finds the Shortest Path
BFS explores all possible paths step by step, so the first time it reaches the end, it has found the shortest way there.

#### Introducing the Queue
A queue is a data structure that works like a line of people waiting for something. The first person in line is the first to be served. This is called "First In, First Out" (FIFO).

**Code Example: Using a Queue**
```python
from collections import deque

# Create a queue
queue = deque()

# Add items to the queue
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue after adding items:", list(queue))

# Remove items from the queue
first_item = queue.popleft()
print("Removed:", first_item)
print("Queue after removing an item:", list(queue))
```

#### Initializing the BFS Algorithm
```python
from collections import deque

# Initialize the BFS queue and visited set
queue = deque([start])
visited = set()
visited.add(start)
parent = {start: None}
```

#### Exploring Neighbors in BFS
```python
# Explore neighbors
for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    nr, nc = current[0] + dr, current[1] + dc
    neighbor = (nr, nc)

    if (
        0 <= nr < len(maze)
        and 0 <= nc < len(maze[0])
        and maze[nr][nc] == 0  # Check if the cell is a path
        and neighbor not in visited
    ):
        queue.append(neighbor)
        visited.add(neighbor)
        parent[neighbor] = current
```

#### Reconstructing the Path
```python
# Reconstruct the path from end to start
path = []
current = end
while current:
    path.append(current)
    current = parent[current]
path.reverse()  # Reverse the path to get it from start to end
print("Path:", path)
```

## Homework
- There's a new file under `algorithms/bfs.py`
- It contains incomplete implementation, look for places with "# put your code here"
- Try complete the code
- call this func in main.py and print out the path.