import pygame
from UI import button
from UI import system_interface


def main():
    Game = system_interface.Game_System()
    window_size = [1280, 720]
    window_screen = pygame.display.set_mode(window_size)
    window_screen.fill([0, 0, 200])
    clock = pygame.time.Clock()

    while True:
        Game.set_event()
        Game.exit()
        mouse, click = Game.get_mouse_input()


        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()