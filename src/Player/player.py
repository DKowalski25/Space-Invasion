import pygame

WIDTH, HEIGHT = 800, 600


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 64, 24)
        self.rect.center = (400, HEIGHT - 24)
        self.speed = 3
        self.move_left_flag = False
        self.move_right_flag = False

        # Rectangle for the cannon
        self.gun_rect = pygame.Rect(0, 0, 20, 30)
        self.gun_rect.center = (400, HEIGHT - 30)
        self.gun_speed = 3

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.speed
            self.gun_rect.x -= self.speed

    def move_right(self):
        if self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.gun_rect.x += self.speed


# Color
WHITE, BLACK = (255, 255, 255), (0, 0, 0)


def render_player(screen, player):
    # Draw the main body of the player
    pygame.draw.rect(screen, WHITE, player.rect)

    # Drawing the cannon
    pygame.draw.rect(screen, WHITE, player.gun_rect)

