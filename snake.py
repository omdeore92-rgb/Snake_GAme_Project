# snake.py
import pygame
from settings import CELL_SIZE, SNAKE_GREEN, SNAKE_HEAD

class Snake:
    def __init__(self, start_pos):
        self.body = [start_pos, (start_pos[0]-1, start_pos[1]), (start_pos[0]-2, start_pos[1])]
        self.direction = (1, 0)  # moving right initially

    def move(self, grow=False):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        if not grow:
            self.body.pop()
        return new_head

    def set_direction(self, new_dir):
        # Prevent direct reverse
        if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
            self.direction = new_dir

    def draw(self, screen):
        for i, seg in enumerate(self.body):
            color = SNAKE_HEAD if i == 0 else SNAKE_GREEN
            x, y = seg
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)
