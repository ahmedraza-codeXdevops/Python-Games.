import tkinter as tk
import random

WIDTH = 600
HEIGHT = 400
CELL = 20

snake = [(100, 100), (80, 100), (60, 100)]
direction = "Right"
food = None
score = 0
game_over = False

root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 16))
score_label.pack()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()


def create_food():
    global food

    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)

        if (x, y) not in snake:
            food = (x, y)
            break


def draw():
    canvas.delete("all")

    if food:
        x, y = food
        canvas.create_oval(
            x, y, x + CELL, y + CELL,
            fill="red"
        )

    for i, (x, y) in enumerate(snake):
        if i == 0:
            canvas.create_rectangle(
                x, y, x + CELL, y + CELL,
                fill="lime"
            )
        else:
            canvas.create_rectangle(
                x, y, x + CELL, y + CELL,
                fill="green"
            )


def change_direction(new_direction):
    global direction

    opposite = {
        "Up": "Down",
        "Down": "Up",
        "Left": "Right",
        "Right": "Left"
    }

    if new_direction != opposite[direction]:
        direction = new_direction


def move():
    global snake, score, game_over

    if game_over:
        return

    head_x, head_y = snake[0]

    if direction == "Up":
        head_y -= CELL
    elif direction == "Down":
        head_y += CELL
    elif direction == "Left":
        head_x -= CELL
    elif direction == "Right":
        head_x += CELL

    new_head = (head_x, head_y)

    if (
        head_x < 0 or
        head_x >= WIDTH or
        head_y < 0 or
        head_y >= HEIGHT or
        new_head in snake
    ):
        end_game()
        return

    snake.insert(0, new_head)

    if new_head == food:
        score += 10
        score_label.config(text=f"Score: {score}")
        create_food()
    else:
        snake.pop()

    draw()
    root.after(100, move)


def end_game():
    global game_over

    game_over = True

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2,
        text="GAME OVER",
        fill="red",
        font=("Arial", 35, "bold")
    )

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 + 50,
        text=f"Score: {score}",
        fill="white",
        font=("Arial", 20)
    )


def restart():
    global snake, direction, score, game_over

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = "Right"
    score = 0
    game_over = False

    score_label.config(text="Score: 0")
    create_food()
    draw()
    move()


root.bind("<Up>", lambda event: change_direction("Up"))
root.bind("<Down>", lambda event: change_direction("Down"))
root.bind("<Left>", lambda event: change_direction("Left"))
root.bind("<Right>", lambda event: change_direction("Right"))

restart_button = tk.Button(
    root,
    text="Restart",
    command=restart,
    font=("Arial", 12)
)

restart_button.pack(pady=5)

create_food()
draw()
move()

root.mainloop()