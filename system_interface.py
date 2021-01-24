import pygame
import sys


class Game_System:
    events = None
    mouse_position = None
    def __init__(self):
        pygame.init()
        self.events = None
        self.mouse_position = None

    #--이벤트 설정
    def set_event(self):
        """
        이벤트 설정 반드시 선행되어야함
        """
        self.events = pygame.event.get()

    #--종료
    def exit(self):
        """
        게임 종료 시 시스템 종료
        """
        # 종료
        for event in self.events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    #--마우스 정보
    def get_mouse_input(self):
        """
        현재 마우스 위치와 마우스 클릭 정보를 받아옴

        :return:    마우스 위치 - (정수, 정수), 마우스 클릭 - [bool,bool,bool]
        """
        # 마우스 위치
        mouse_click = [False, False, False]
        for event in self.events:
            # 마우스 위치
            if event.type == pygame.MOUSEMOTION:
                self.mouse_position = event.pos

            # 마우스 클릭(현재 왼쪽:1, 가운데:2, 오른쪽만:3 동시는 아직 없음, 클릭 누르고 있는것 적용안됨)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click[0] = True
                if event.button == 2:
                    mouse_click[1] = True
                if event.button == 3:
                    mouse_click[2] = True
            else:
                mouse_click[0] = False
                mouse_click[1] = False
                mouse_click[2] = False

        return self.mouse_position, mouse_click

    #--키보드 값 입력
    def get_key_input(self, text=""):
        """
        키보드 입력 값을 받아옴
        text값이 있을 때는 text에 입력된 값을 추가하여 return,
        text값이 없을 때는 입력된 값만 return

        :param text:    글자 - 문자열 | ""
        :return:
        """
        for event in self.events:
            # 키보드 인터페이스
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = text[:-1]
                else:
                    text += event.unicode

        return text