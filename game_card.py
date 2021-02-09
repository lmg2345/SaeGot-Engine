import pygame
from Card import card
from UI import system_interface
from UI import button
from User.card_user import Card_User

def main():
    Game = system_interface.Game_System()

    window_width = 1280
    window_height = 720
    window_size = [window_width, window_height]
    window_screen = pygame.display.set_mode(window_size)
    window_screen.fill([150, 230, 220])
    clock = pygame.time.Clock()
    pygame.display.set_caption("Brain Card")


    Player_1 = Card_User([10, 10, 10])
    Player_2 = Card_User([10, 10, 10])

    Life_Button_width = 150
    Life_button_height = 150

    Player_1__Life = {}
    for i in range(3):
        Player_1__Life[i] = button.Text_Button([Life_Button_width, Life_button_height])

    for i, life in Player_1__Life.items():
        life.set_text(Player_1.get_life(i))

    Player_2__Life = {}
    for i in range(3):
        Player_2__Life[i] = button.Text_Button([Life_Button_width, Life_button_height])

    for i, life in Player_2__Life.items():
        life.set_text(Player_2.get_life(i))


    Card_width = 50
    Card_height = 100

    Card_1 = card.Number_Card([Card_width, Card_height])

    while True:
        #마우스 인터페이스

        Game.set_event()
        Game.exit()
        mouse, click = Game.get_mouse_input()

        Card_1.set_position([200, 200])
        for i, life in Player_1__Life.items():
            life.set_position([(i+1)*window_width//4, 4*window_height//6])
        for i, life in Player_2__Life.items():
            life.set_position([(i+1)*window_width//4, 2*window_height//6])

        window_screen.fill([150, 230, 220])
        Card_1.show(window_screen, mouse, click)
        for _, life in Player_1__Life.items():
            life.show(window_screen, text_pos_shift = [0, -Life_button_height//2])
        for _, life in Player_2__Life.items():
            life.show(window_screen, text_pos_shift = [0, -Life_button_height//2])

        clock.tick(60)
        pygame.display.update()

if __name__ == '__main__':
    main()