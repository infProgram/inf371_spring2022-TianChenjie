class Point:
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def copy(self):
        return Point(row=self.row, col=self.col)


import pygame
import random

pygame.init()
W = 800
H = 600

ROW = 30
COL = 40

size = (W, H)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

bg_color = (255, 225, 255)
snake_color = (200, 200, 200)


def gen_food():
    while 1:
        pos = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))

        is_coll = False

        if head.row == pos.row and head.col == pos.col:
            is_coll = True

        for snake in snakes:
            if snake.row == pos.row and snake.col == pos.col:
                is_coll = True
                break

        if not is_coll:
            break

    return pos


head = Point(row=int(ROW / 2), col=int(COL / 2))
head_color = (0, 128, 128)

snakes = [
    Point(row=head.row, col=head.col + 1),
    Point(row=head.row, col=head.col + 2),
    Point(row=head.row, col=head.col + 3),
]

food = gen_food()
food_color = (255, 255, 0)

direct = 'left'


def rect(point, color):
    cell_width = W / COL
    cell_height = H / ROW

    left = point.col * (W / COL)
    top = point.row * (H / ROW)

    pygame.draw.rect(
        window, color,
        (left, top, cell_width, cell_height)
    )
    pass


quit = True
clock = pygame.time.Clock()
while quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 273 or event.key == 119:
                if direct == 'left' or direct == 'right':
                    direct = 'up'
            elif event.key == 274 or event.key == 115:
                if direct == 'left' or direct == 'right':
                    direct = 'down'
            elif event.key == 276 or event.key == 97:
                if direct == 'up' or direct == 'down':
                    direct = 'left'
            elif event.key == 275 or event.key == 100:
                if direct == 'up' or direct == 'down':
                    direct = 'right'

    eat = (head.row == food.row and head.col == food.col)

    if eat:
        food = gen_food()

    snakes.insert(0, head.copy())

    if not eat:
        snakes.pop()

    if direct == 'left':
        head.col -= 1
    elif direct == 'right':
        head.col += 1
    elif direct == 'up':
        head.row -= 1
    elif direct == 'down':
        head.row += 1

    dead = False
    if head.col < 0 or head.row < 0 or head.col >= COL or head.row >= ROW:
        dead = True

    for snake in snakes:
        if head.col == snake.col and head.row == snake.row:
            deadW = True
            break

    if dead:
        print('You are dead')
        quit = False

    pygame.draw.rect(window, (255, 255, 255), (0, 0, W, H))

    for snake in snakes:
        rect(snake, snake_color)
    rect(head, head_color)
    rect(food, food_color)

    pygame.display.flip()

    clock.tick(10)
