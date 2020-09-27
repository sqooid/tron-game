"""
python file for classes of entities
"""
import pygame


class Rider:
    movement_speed = 4
    jump_speed = 6
    size = 12
    common_barrier_list = []

    def __init__(self, x: int, y: int, colour: tuple, barrier_colour) -> None:
        self.x = x
        self.y = y
        self.old_pos = (x, y)
        self.width = Rider.size
        self.height = Rider.size
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.colour = colour
        self.direction = "right"
        self.jumping = False
        self.jump_timer = Rider.jump_speed
        self.barrier_colour = barrier_colour
        self.barrier_list = []
        self.alive = True

    def move(self):
        if self.direction == "up":
            self.y -= Rider.movement_speed
        elif self.direction == "right":
            self.x += Rider.movement_speed
        elif self.direction == "down":
            self.y += Rider.movement_speed
        else:
            self.x -= Rider.movement_speed

    def add_barrier(self, win, start: tuple, end: tuple) -> None:
        Rider.common_barrier_list.append(pygame.draw.line(win, self.barrier_colour, start, end))
        self.barrier_list.append(pygame.draw.line(win, self.barrier_colour, start, end))

    def draw_barriers(self, win):
        # for i in range(len(self.barrier_list) - 1, max(-1, len(self.barrier_list) - 10), -1):
        for i in range(len(self.barrier_list)):
            pygame.draw.rect(win, self.barrier_colour, self.barrier_list[i])

    def jump(self):
        if not self.jumping:
            self.jumping = True
        if self.jump_timer >= Rider.jump_speed * -1:
            self.y -= round(self.jump_timer * abs(self.jump_timer) * 0.2)
            self.jump_timer -= 1
        else:
            self.jump_timer = Rider.jump_speed
            self.jumping = False

    def draw(self, win) -> None:
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))

    def undraw(self, win) -> None:
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height))


class Border:
    def __init__(self, width: int, height: int, colour: tuple) -> None:
        self.width = width
        self.height = height
        self.colour = colour

        self.thickness = 1

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.thickness - 1, self.thickness - 1, self.width, self.height),
                         self.thickness)
