# Define game constants
WIDTH = 40
HEIGHT = 20
SNAKE_SYMBOL = "@"
FOOD_SYMBOL = "$"

def generate_snake():
  # Starting position and length
  return [(WIDTH // 2, HEIGHT // 2), (WIDTH // 2 - 1, HEIGHT // 2)]

def generate_food(snake):
  # Ensure food doesn't spawn on the snake
  import random
  food_x = random.randint(1, WIDTH - 2)
  food_y = random.randint(1, HEIGHT - 2)
  while (food_x, food_y) in snake:
    food_x = random.randint(1, WIDTH - 2)
    food_y = random.randint(1, HEIGHT - 2)
  return food_x, food_y

def print_board(snake, food):
  # Clear the console (optional)
  print("\033c")  # This might not work on all terminals

  for y in range(HEIGHT):
    for x in range(WIDTH):
      if (x, y) in snake:
        print(SNAKE_SYMBOL, end="")
      elif (x, y) == food:
        print(FOOD_SYMBOL, end="")
      else:
        print(" ", end="")
    print()

def get_direction():
  # Get user input for direction (limited options here)
  direction = input("Enter direction (w, a, s, d): ")
  if direction.lower() in ["w", "a", "s", "d"]:
    return direction
  else:
    print("Invalid direction!")
    return get_direction()

def game_loop():
  snake = generate_snake()
  food_x, food_y = generate_food(snake)
  x_dir, y_dir = 1, 0  # Initial movement direction

  while True:
    # Print the board
    print_board(snake, (food_x, food_y))

    # Get user input and update direction
    new_dir = get_direction()
    if new_dir == "w" and y_dir != 1:  # Prevent backtracking
      x_dir, y_dir = 0, -1
    elif new_dir == "s" and y_dir != -1:
      x_dir, y_dir = 0, 1
    elif new_dir == "a" and x_dir != 1:
      x_dir, y_dir = -1, 0
    elif new_dir == "d" and x_dir != -1:
      x_dir, y_dir = 1, 0

    # Update snake position (check for collisions)
    new_head = (snake[0][0] + x_dir, snake[0][1] + y_dir)
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake[1:]:
      print("Game Over!")
      break

    snake.insert(0, new_head)  # Add new head

    # Check for food collision
    if new_head == (food_x, food_y):
      food_x, food_y = generate_food(snake)  # Generate new food
    else:
      snake.pop()  # Remove tail if not eating

game_loop()
