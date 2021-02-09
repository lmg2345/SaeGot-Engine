import pygame
import sys
from UI import button
from UI import system_interface





def main():
    Game = system_interface.Game_System()

    #window_screen = Tk()
    #window_screen.title("test")
    #window_screen.geometry("1280x720")
    window_size = [1280, 720]
    window_screen = pygame.display.set_mode(window_size)
    window_screen.fill([0, 0, 200])
    clock = pygame.time.Clock()
    pygame.display.set_caption("Brain Card")
    ID_text = ''
    PW_text = ''


    #id = 'test11111111111'
    ID_Button = button.Text_Button([200, 50], button_image_path="pic/button_text.png",
                                   button_active_image_path="pic/button_text_active.png")
    PW_Button = button.Text_Button([200, 50], button_image_path="pic/button_text.png",
                                   button_active_image_path="pic/button_text_active.png")

    while True:
        #마우스 인터페이스
        mouse = pygame.mouse.get_pos()
        click = None

        Game.set_event()
        Game.exit()
        mouse, click = Game.get_mouse_input()
        if ID_Button.get_active():
            ID_text = Game.get_key_input(ID_text)
            ID_Button.set_text(ID_text)

        if PW_Button.get_active():
            PW_text = Game.get_key_input(PW_text)
            PW_Button.set_text(PW_text)

        ID_Button.set_position([200, 200])
        PW_Button.set_position([200, 400])

        if ID_Button.get_clicked(mouse, click):
            PW_Button.set_active(False)
            ID_Button.set_active(True)

        if PW_Button.get_clicked(mouse, click):
            ID_Button.set_active(False)
            PW_Button.set_active(True)

        ID_Button.show(window_screen, mouse, click)
        PW_Button.show(window_screen, mouse, click)


        clock.tick(60)
        pygame.display.update()

if __name__ == '__main__':
    main()
