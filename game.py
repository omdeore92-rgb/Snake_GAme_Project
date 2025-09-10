# game.py
import pygame
from settings import WIDTH, HEIGHT, BLACK, WHITE, FPS
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake (Professional Version)")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 30)
        self.big_font = pygame.font.SysFont(None, 48)
        self.reset()

    def reset(self):
        start_x = WIDTH // (2 * 20)
        start_y = HEIGHT // (2 * 20)
        self.snake = Snake((start_x, start_y))
        self.food = Food(self.snake.body)
        self.score = 0
        self.game_over = False

    def update(self):
        if not self.game_over:
            new_head = self.snake.move()
            # Check wall collision
            if (new_head[0] < 0 or new_head[0] * 20 >= WIDTH or
                new_head[1] < 0 or new_head[1] * 20 >= HEIGHT):
                self.game_over = True

            # Check self collision
            elif new_head in self.snake.body[1:]:
                self.game_over = True

            # Check food
            elif new_head == self.food.position:
                self.score += 1
                self.snake.move(grow=True)  # grow snake
                self.food = Food(self.snake.body)

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)

        # HUD
        score_surf = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_surf, (10, 8))

        if self.game_over:
            over_surf = self.big_font.render("GAME OVER", True, WHITE)
            sub_surf = self.font.render("Press R to restart or Q/Esc to quit", True, WHITE)
            over_rect = over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
            sub_rect = sub_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
            self.screen.blit(over_surf, over_rect)
            self.screen.blit(sub_surf, sub_rect)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP: self.snake.set_direction((0, -1))
                    elif event.key == pygame.K_DOWN: self.snake.set_direction((0, 1))
                    elif event.key == pygame.K_LEFT: self.snake.set_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT: self.snake.set_direction((1, 0))
                    elif event.key == pygame.K_r: self.reset()
                    elif event.key in (pygame.K_q, pygame.K_ESCAPE): running = False

            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
