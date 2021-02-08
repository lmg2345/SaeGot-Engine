import pygame
import os

#추상 카드 클래스----------------------------------------------------------------------------------------------------------
class Card:
    position = [0, 0]
    size = [0, 0]
    image = None
    image_clicked = None
    image_active = None
    active = False
    def __init__(self, card_size, card_image_path = None, card_cliked_image_path = None, card_active_image_path = None):
        # 버튼 크기 - [x,y], 버튼 이미지 - 경로
        self.position = [0, 0]
        self.size[0] = card_size[0]
        self.size[1] = card_size[1]
        self.center = None
        self.active = False
        module_path = os.path.dirname(__file__)
        if card_image_path == None:
            card_image_path = os.path.join(module_path, "./pic/default_card.png")
        if card_cliked_image_path == None:
            card_cliked_image_path = os.path.join(module_path, "./pic/default_card_clicked.png")
        if card_active_image_path == None:
            card_active_image_path = os.path.join(module_path, "./pic/default_card_active.png")

        self.image = pygame.image.load(card_image_path)
        self.image = pygame.transform.scale(self.image, [self.size[0], self.size[1]])
        self.image_clicked = pygame.image.load(card_cliked_image_path)
        self.image_clicked = pygame.transform.scale(self.image_clicked, [self.size[0], self.size[1]])
        self.image_active = pygame.image.load(card_active_image_path)
        self.image_active = pygame.transform.scale(self.image_active, [self.size[0], self.size[1]])

    # --위치 설정
    def set_position(self, position):
        self.position[0] = position[0]
        self.position[1] = position[1]
        self.center = self.image.get_rect()
        self.center.center = self.position

    # --액티브 설정
    def set_active(self, active):
        """
        액티브 설정

        :param active:  액티브 여부 - bool
        """
        self.active = active

    # --버튼 안에서 클릭 확인
    def get_clicked(self, mouse_position=None, mouse_click=None):
        """
        버튼 안에서 클릭 확인

        :param mouse_position:  마우스 위치 - (정수, 정수)
        :param mouse_click:     마우스 클릭 - [bool,bool,bool]
        :return:                버튼 안에서 클릭 여부 - bool
        """
        check1 = self.check_mouse_position(mouse_position)
        check2 = self.check_mouse_leftclicked(mouse_click)
        if check1 and check2:
            return True

        return False

    # --버튼 설정
    def show_button(self, screen, mouse_position=None, mouse_click=None):
        # 일반 상태
        screen.blit(self.image, self.center)

        check1 = self.active
        # 클릭 상태
        if self.get_clicked(mouse_position, mouse_click):
            screen.blit(self.image_clicked, self.center)
        # 액티브 상태
        if check1:
            screen.blit(self.image_active, self.center)

    #--마우스 위치 확인
    def check_mouse_position(self, mouse_position):
        if mouse_position != None:
            if self.position[0] - (self.size[0]) // 2 < mouse_position[0] < self.position[0] + (self.size[0]) // 2 \
                    and self.position[1] - (self.size[1]) // 2 < mouse_position[1] < self.position[1] + (self.size[1]) // 2:
                return True

        return False

    #--마우스 클릭 확인
    def check_mouse_leftclicked(self, mouse_click):
        if mouse_click != None:
            if mouse_click[0] == True:
                return True

        return False

# 숫자 카드 클래스---------------------------------------------------------------------------------------------------------
class Number_Card(Card):
    number = None
    def __init__(self, card_size, card_image_path=None, card_cliked_image_path=None, card_active_image_path=None):
        super().__init__(card_size, card_image_path, card_cliked_image_path, card_active_image_path)

    #--숫자 부여
    def set_number(self, number):
        """
        카드에 숫자 값 부여

        :param number: 숫자 - 실수
        """
        self.number = number

    #--숫자 확인
    def get_number(self):
        """
        카드의 숫자 값 확인
        
        :return:    숫자 - 실수
        """
        return self.number