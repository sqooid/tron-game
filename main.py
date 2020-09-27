# ! /usr/bin/env python

"""
main python file for tron game thing
"""

__author__ = "Lucas Liu"

import pygame
from entities import Rider, Border

pygame.init()

# Global variables
window_width = 1800
window_height = 980
win = pygame.display.set_mode((window_width, window_height))


# Draw function
def redraw():
    pygame.display.update()


# Making players
player1 = Rider(100, 200, (255, 255, 255), (255, 0, 255))
player2 = Rider(100, 440, (255, 255, 255), (0, 255, 255))
players = [player1, player2]

# Making (visual) boundary
boundary = Border(window_width, window_height, (255, 0, 0))
boundary.draw(win)

# Clock
clock = pygame.time.Clock()

# Input loop
run = True
while run:
    clock.tick(60)

    keys = pygame.key.get_pressed()

    # Un-drawing previous position
    for player in players:
        player.undraw(win)
        player.old_pos = (player.x + Rider.size // 2, player.y + Rider.size // 2)

    # Player control
    if keys[pygame.K_w] and player1.direction != "down":
        player1.direction = "up"
    elif keys[pygame.K_d] and player1.direction != "left":
        player1.direction = "right"
    elif keys[pygame.K_s] and player1.direction != "up":
        player1.direction = "down"
    elif keys[pygame.K_a] and player1.direction != "right":
        player1.direction = "left"
    if keys[pygame.K_SPACE] or player1.jumping:
        player1.jump()

    if keys[pygame.K_UP] and player2.direction != "down":
        player2.direction = "up"
    elif keys[pygame.K_RIGHT] and player2.direction != "left":
        player2.direction = "right"
    elif keys[pygame.K_DOWN] and player2.direction != "up":
        player2.direction = "down"
    elif keys[pygame.K_LEFT] and player2.direction != "right":
        player2.direction = "left"
    if keys[pygame.K_RCTRL] or player2.jumping:
        player2.jump()

    # Barrier creation
    for player in players:
        player.move()
        player.hitbox = pygame.Rect(player.x, player.y, player.width, player.height)
        if not player.jumping:
            player.add_barrier(win, player.old_pos, (player.x + Rider.size // 2, player.y + Rider.size // 2))

    # Checking collisions
    for player in players:
        # Checking wall collision
        if window_width - Rider.size <= player.x or player.x <= 0 or window_height - Rider.size <= player.y or player.y <= 0:
            player.alive = False
            run = False
        # Barrier collisions
        if not player.jumping:
            if player.hitbox.collidelist(Rider.common_barrier_list) < len(Rider.common_barrier_list) - 6:
                player.alive = False
                run = False

        player.draw_barriers(win)
        player.draw(win)

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redraw()

# End game
if player1.alive:
    print('Player 1 winner')
elif player2.alive:
    print('Player 2 winner')
else:
    print('You both losers')

pygame.quit()
