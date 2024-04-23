import sys
import pygame

from src.Player.player import Player, render_player


# Init Pygame
pygame.init()

# Windows settings
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE INVASION")


player = Player()

# Setting the FPS limit
FPS = 60
clock = pygame.time.Clock()


# Main gaming loop
def main():
    run = True
    while run:
        #
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_LEFT:
                    player.move_left_flag = True
                elif events.key == pygame.K_RIGHT:
                    player.move_right_flag = True
            elif events.type == pygame.KEYUP:
                if events.key == pygame.K_LEFT:
                    player.move_left_flag = False
                elif events.key == pygame.K_RIGHT:
                    player.move_right_flag = False

        # Updating the player's position depending on the flags
        if player.move_left_flag:
            player.move_left()
        elif player.move_right_flag:
            player.move_right()

        win.fill('black')
        render_player(win, player)
        pygame.display.flip()

        # FPS Limit
        clock.tick(FPS)


if __name__ == '__main__':
    main()


