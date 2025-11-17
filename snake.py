import tkinter as tk
import random

# Grid and cell sizes
GRID_SIZE = 20
CELL_SIZE = 25
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

# Game colors
BG_COLOR = "black"
SNAKE_COLOR = "green"
APPLE_COLOR = "red"

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game - Tkinter Version")

        self.canvas = tk.Canvas(root, width=WINDOW_SIZE, height=WINDOW_SIZE, bg=BG_COLOR)
        self.canvas.pack()

        # Score label
        self.score = 0
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 16))
        self.score_label.pack()

        # Initial snake
        self.snake = [(10, 10), (9, 10), (8, 10)]  # Starting position
        self.direction = "RIGHT"

        # Place the first apple
        self.apple = self.spawn_apple()

        # Keyboard controls
        self.root.bind("<Up>", lambda e: self.change_direction("UP"))
        self.root.bind("<Down>", lambda e: self.change_direction("DOWN"))
        self.root.bind("<Left>", lambda e: self.change_direction("LEFT"))
        self.root.bind("<Right>", lambda e: self.change_direction("RIGHT"))

        # Start game loop
        self.game_running = True
        self.game_loop()

    def spawn_apple(self):
        while True:
            pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            if pos not in self.snake:
                return pos

    def change_direction(self, new_dir):
        opposite = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if opposite[new_dir] != self.direction:
            self.direction = new_dir

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == "UP":
            head_y -= 1
        elif self.direction == "DOWN":
            head_y += 1
        elif self.direction == "LEFT":
            head_x -= 1
        elif self.direction == "RIGHT":
            head_x += 1

        new_head = (head_x, head_y)

        # Check for collisions
        if (
            head_x < 0 or head_x >= GRID_SIZE or
            head_y < 0 or head_y >= GRID_SIZE or
            new_head in self.snake
        ):
            self.game_running = False
            self.canvas.create_text(WINDOW_SIZE//2, WINDOW_SIZE//2, text="GAME OVER", fill="red", font=("Arial", 30))
            return

        self.snake.insert(0, new_head)

        # Check if apple eaten
        if new_head == self.apple:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.apple = self.spawn_apple()
        else:
            self.snake.pop()  # Remove tail if not eating apple

    def draw(self):
        self.canvas.delete("all")

        # Draw apple
        x, y = self.apple
        self.canvas.create_rectangle(
            x*CELL_SIZE, y*CELL_SIZE,
            (x+1)*CELL_SIZE, (y+1)*CELL_SIZE,
            fill=APPLE_COLOR
        )

        # Draw snake
        for x, y in self.snake:
            self.canvas.create_rectangle(
                x*CELL_SIZE, y*CELL_SIZE,
                (x+1)*CELL_SIZE, (y+1)*CELL_SIZE,
                fill=SNAKE_COLOR
            )

    def game_loop(self):
        if self.game_running:
            self.move_snake()
            self.draw()
            self.root.after(150, self.game_loop)  # Update every 150ms

# Run the game
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
