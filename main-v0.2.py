import sys
import time
import math
import sympy
import pygame

pygame.init()

# Physical Constant
g = 20 * 9.8

# Game Constant
FPS = 30
size = width, height = 800, 450
border = 25

# Color Constant
white = (255, 255, 255)
black = (0, 0, 0)

# Player Constant
player_width = 100
player_height = 100
speed = 3

# Graph Constant
axis_mark_length = 5
axis_mark_interval = 200


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Func:
    def __init__(self, formula, domain):
        self.formula = formula
        self.domain = domain
        self.points = []
        # Todo: calculate points based on the formula and domain.
        # The points attribute should be an array of Point object.

    def derivative(self):
        pass

    def integral(self):
        pass


class Player:
    def __init__(self, w, h, left, head):
        self.status = 'walk'
        self.width = w
        self.height = h
        self._left = left
        self._right = left + w
        self._head = head
        self._foot = head + h
        self.speed_y = g
        self.jump_timestamp = 0

    @property
    def head(self):
        return self._head

    @property
    def foot(self):
        return self._foot

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @head.setter
    def head(self, head):
        self._head = head
        self._foot = head + self.height

    @foot.setter
    def foot(self, foot):
        self._foot = foot
        self._head = foot - self.height

    def get_down(self):
        self.status = 'down'
        self.jump_timestamp = 0

    def jump_up(self):
        self.status = 'up'
        self.jump_timestamp = time.time()

    def go_walk(self):
        self.status = 'walk'
        self.jump_timestamp = 0
        self.foot = height/2


def real2screen(p):
    """
    Convert the real x coordinate in real plane to the x coordinate in our screen.
    The following graph shows how it works
     |--------------------------------------|---------|-----------------------------|
     0                                     400       500                           800 (screen coordinate)
     |                                                |                             |
     |                                     QAQ        |                             |
     |                                                |                             |
    400                                    800       900                           1200 (real coordinate)
     |--------------------------------------|---------|-----------------------------|
    Our player now at position 800 in the real plan, and he always lies on the center of our screen(x=400), if we want
    to check what's the corresponding screen x to position 900, it will be (900 - 800) + 400 = 500.

    Most of the calculation of drawing should be done in the real plane coordinates,
    and then use this function to accomplish the conversion.
    """
    return p - position + width//2


def get_screen_range(p):
    """
    Get current screen left and right border's real coordinate.
    """
    left_border = p - width//2
    right_border = p + width//2
    return left_border, right_border


def get_marks(p):
    """
    Get the x-axis marks' coordinate according to the current position p.
    """
    borders = left_border, right_border = get_screen_range(p)
    start_point, end_point = [math.ceil(border/axis_mark_interval) * axis_mark_interval for border in borders]
    marks = [mark for mark in range(start_point, end_point, axis_mark_interval)]
    return marks


def collision_detection(p, funs):
    """
    Todo:
    Detect if the player hit any functions in our graph.
    """
    return False


def func_generator(level):
    """
    Todo:
    Generator random Func object (according to the hard level)
    """
    pass


"""
Background Initialization
"""
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Axis Runner")
fpsClock = pygame.time.Clock()
funcs = []  # funcs is an array of Func object, which stores all of the function appeared on the screen
#  (or is going to appear), we use this array to draw the graph and show the formula.


"""
Player Parameter Initialization
"""
position = 0
player = Player(player_width, player_height, width/2 - player_width/2, height/2 - player_height)
player_img_src = pygame.image.load("player.jpg")
# player_img_down_src = pygame.image.load("player_down.jpg")
player_img = pygame.transform.scale(player_img_src, (player.width, player.height))
# player_img_down = pygame.transform.scale(player_img_down_src, (player.width, player.))
# player_rect = player.get_rect()

"""
Physical Parameter Initialization 
"""
t_max = 2*player.speed_y/g
h = lambda t: player.speed_y * t - 0.5 * g * t**2

while True:
    """Player Input Event detection"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player.status != 'up':
                    player.jump_up()
            if event.key == pygame.K_DOWN:
                if player.status != 'up':
                    player.get_down()

        if event.type == pygame.KEYUP:
            if player.status == 'down':
                player.go_walk()

    """
    Refresh
    """
    screen.fill(white)

    """
    Generate and draw the axis and x-axis marks.
    """
    if position < width/2:
        pygame.draw.line(screen, black, [width/2 - position, border], [width/2 - position, height-border])
    pygame.draw.line(screen, black, [0, height/2], [width, height/2])
    marks = get_marks(position)
    for mark in marks:
        pygame.draw.line(screen, black, [real2screen(mark), height/2 - axis_mark_length], [real2screen(mark), height/2])
        font = pygame.font.SysFont("Consolas", 20)
        text_surface = font.render(str(mark), True, black)
        screen.blit(text_surface, (real2screen(mark) - len(str(mark))*3, height/2 + axis_mark_length))

    """
    Todo: Generate and draw the player image(based on the attributes of player object).
    """
    if player.status == 'up':
        t = time.time() - player.jump_timestamp
        if t >= t_max:
            player.go_walk()
        else:
            player.foot = height/2 - h(t)

    player_rect = screen.blit(player_img, (player.left, player.head))

    """
    Todo: Generate(if necessary) and draw the functions.
    """

    """
    Todo: Collision Detection
    """
    collision_detection(position, [])

    """
    Todo: Failed Processor
    """

    """
    Todo: Background Event Checker
    """

    """
    Update and refresh
    """
    position += speed
    pygame.display.update()
    fpsClock.tick(FPS)
