import pygame
from Card import cards
from UI import system_interface

def main():
    Game = system_interface.Game_System()

    window_size = [1280, 720]
    window_screen = pygame.display.set_mode(window_size)
    window_screen.fill([0, 0, 200])
    clock = pygame.time.Clock()
    pygame.display.set_caption("Brain Card")

    card1 = cards.Number_Card([50, 100])

    while True:
        #마우스 인터페이스

        Game.set_event()
        Game.exit()
        mouse, click = Game.get_mouse_input()

        card1.set_position([200, 200])

        card1.show_button(window_screen, mouse, click)

        clock.tick(60)
        pygame.display.update()

if __name__ == '__main__':
    main()