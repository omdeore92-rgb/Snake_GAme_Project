# settings.py

# Screen settings
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
FPS = 10  # base speed

# Colors (R,G,B)
BLACK = (0, 0, 0)
SNAKE_GREEN = (0, 180, 0)
SNAKE_HEAD = (0, 220, 0)
FOOD_RED = (200, 0, 0)
WHITE = (255, 255, 255)

# Derived (calculated)
COLUMNS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE
