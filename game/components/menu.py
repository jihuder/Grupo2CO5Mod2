import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 50)
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw (self, screen ):
        screen.blit(self.text, self.text_rect)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def update_message(self, message):
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def draw_score(self, game, color = (255, 255, 255), coord_x = SCREEN_WIDTH - 50, coord_y = 25):
        font = pygame.font.Font(FONT_STYLE, 16)
        text = font.render(f'score: {game.score}', True, color)
        text_rect = text.get_rect()
        text_rect.center = ((coord_x, coord_y))
        game.screen.blit(text, text_rect)

    def draw_deaths(self, game, coord_x = SCREEN_WIDTH - 50, coord_y = 25):
        font = pygame.font.Font(FONT_STYLE, 16)
        text = font.render(f'score: {game.score}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = ((coord_x, coord_y))
        game.screen.blit(text, text_rect)