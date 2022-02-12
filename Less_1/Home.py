import pygame
from pygame.color import THECOLORS
import sys


def chek_color(txt):
    while True:
        try:
            color = str(input(txt))
            if color not in THECOLORS.keys():
                raise ValueError
            else:
                break
        except ValueError:
            print('! Неправильний колір !')
    return color


def chek_size(txt):
    while True:
        try:
            numb = float(input(txt))
            break
        except ValueError:
            print('! Ведіть число !')
    return numb


# --- Initialization ---
print('--- Ведіть Дані ---')
size = chek_size('Розмір :: ')
background = chek_color('Заді :: ')
color_bottom = chek_color('Основа :: ')
color_roof = chek_color('Дах :: ')

pygame.init()
screen = pygame.display.set_mode((size, size))
screen.fill(background)
# ----------------------


def draw():
    one_fourth_size = size / 4
    # --- Rect ---
    up_point_home = (one_fourth_size, one_fourth_size+(one_fourth_size/2))
    down_point_home = (one_fourth_size*2, one_fourth_size*2)
    bottom_home = pygame.Rect(up_point_home[0], up_point_home[1],
                              down_point_home[0], down_point_home[1])
    pygame.draw.rect(screen, color_bottom, bottom_home)
    # ------------

    # --- Triangle ---
    left_point_roof = (one_fourth_size/2, one_fourth_size+(one_fourth_size/2))
    right_point_roof = ((one_fourth_size*3)+one_fourth_size/2,
                        one_fourth_size+(one_fourth_size/2))
    up_point_roof = (one_fourth_size*2, one_fourth_size/2)
    roof = pygame.draw.polygon(screen, color_roof,
                               (left_point_roof, right_point_roof, up_point_roof))
    # ----------------
    pygame.display.flip()


def main():
    while True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw()


if __name__ == '__main__':
    main()
