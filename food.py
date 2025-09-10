# food.py
import pygame, random
from settings import CELL_SIZE, COLUMNS, ROWS, FOOD_RED

class Food:
    def __init__(self, snake_body):
        self.position = self.random_position(snake_body)

    def random_position(self, snake_body):
        while True:
            pos = (random.randint(0, COLUMNS - 1), random.randint(0, ROWS - 1))
            if pos not in snake_body:
                return pos

    def draw(self, screen):
        x, y = self.position
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, FOOD_RED, rect)
