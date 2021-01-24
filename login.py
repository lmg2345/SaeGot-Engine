import pygame
import sys
import button
import system_interface

from tkinter import *




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
    user_text = ''


    #id = 'test11111111111'
    ID_Button = button.Text_Button([200, 50], button_image_path="pic/button_text.png", button_active_image_path="pic/button_text_active.png")
    while True:
        #마우스 인터페이스
        mouse = pygame.mouse.get_pos()
        click = None

        Game.set_event()
        Game.exit()
        mouse, click = Game.get_mouse_input()
        if ID_Button.active:
            user_text = Game.get_key_input(user_text)
            ID_Button.set_text(user_text)

        ID_Button.set_position([200,200])

        if ID_Button.get_clicked(mouse, click):
            ID_Button.set_active(True)

        ID_Button.show_button(window_screen, mouse, click)
        clock.tick(30)
        pygame.display.update()

if __name__ == '__main__':
    main()
