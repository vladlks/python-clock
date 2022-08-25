import pygame
from datetime import datetime
import math

RES = WIDTH, HEIGHT = 1200, 800
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50
radius_list = {'sec': RADIUS - 10, 'min': RADIUS - 55, 'hour': RADIUS - 100, 'digit': RADIUS - 30}
RADIUS_ARK = RADIUS + 8

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))

font = pygame.font.SysFont('Verdana', 60)

def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    for digit, pos in clock60.items():
        radius = 20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2
        pygame.draw.circle(surface, pygame.Color('gainsboro'), get_clock_pos(clock60, digit, 'digit'), radius, 7)
    pygame.draw.line(surface, pygame.Color('yellow'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, hour, 'hour'), 15)
    pygame.draw.line(surface, pygame.Color('grey'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 7)
    pygame.draw.line(surface, pygame.Color('blue'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, second, 'sec'), 4)
    pygame.draw.circle(surface, pygame.Color('white'), (H_WIDTH, H_HEIGHT), 8)
    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('forestgreen'), pygame.Color('orange'))
    surface.blit(time_render, (0, 0))
    sec_angle = -math.radians(clock60[t.second]) + math.pi / 2
    pygame.draw.arc(surface, pygame.Color('silver'),
                    (H_WIDTH - RADIUS_ARK, H_HEIGHT - RADIUS_ARK, 2 * RADIUS_ARK, 2 * RADIUS_ARK),
                    math.pi / 2, sec_angle, 8)

    pygame.display.flip()
    clock.tick(20)