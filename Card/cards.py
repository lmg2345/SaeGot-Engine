import pygame
import os

#추상 카드 클래스----------------------------------------------------------------------------------------------------------
class Card:
    _position = [0, 0]
    _size = [0, 0]
    _image = None
    _image_clicked = None
    _image_active = None
    _active = False
    def __init__(self, card_size, card_image_path = None, card_cliked_image_path = None, card_active_image_path = None):
        """
        카드 생성
        
        :param card_size:               카드 크기 - [너비, 높이]
        :param card_image_path:         이미지 경로 - 문자열
        :param card_cliked_image_path:  클릭 이미지 경로 - 문자열
        :param card_active_image_path:  활성화 이미지 경로 - 문자열
        """
        # 버튼 크기 - [x,y], 버튼 이미지 - 경로
        self._position = [0, 0]
        self._size[0] = card_size[0]
        self._size[1] = card_size[1]
        self._center = None
        self._active = False
        module_path = os.path.dirname(__file__)
        if card_image_path == None:
            card_image_path = os.path.join(module_path, "./pic/default_card.png")
        if card_cliked_image_path == None:
            card_cliked_image_path = os.path.join(module_path, "./pic/default_card_clicked.png")
        if card_active_image_path == None:
            card_active_image_path = os.path.join(module_path, "./pic/default_card_active.png")

        self._image = pygame.image.load(card_image_path)
        self._image = pygame.transform.scale(self._image, [self._size[0], self._size[1]])
        self._image_clicked = pygame.image.load(card_cliked_image_path)
        self._image_clicked = pygame.transform.scale(self._image_clicked, [self._size[0], self._size[1]])
        self._image_active = pygame.image.load(card_active_image_path)
        self._image_active = pygame.transform.scale(self._image_active, [self._size[0], self._size[1]])

    # --위치 설정
    def set_position(self, position):
        """
        버튼 위치 설정

        :param position:    버튼 위치 - [x, y]
        """
        self._position[0] = position[0]
        self._position[1] = position[1]
        self._center = self._image.get_rect()
        self._center.center = self._position

    # --활성화 설정
    def set_active(self, active):
        """
        활성화 설정

        :param active:  활성화 여부 - bool
        """
        self._active = active

    # --버튼 안에서 클릭 확인
    def get_clicked(self, mouse_position=None, mouse_click=None):
        """
        버튼 안에서 클릭 확인

        :param mouse_position:  마우스 위치 - (x, y)
        :param mouse_click:     마우스 클릭 - [bool,bool,bool]
        :return:                버튼 안에서 클릭 여부 - bool
        """
        check1 = self._check_mouse_position(mouse_position)
        check2 = self._check_mouse_leftclicked(mouse_click)
        if check1 and check2:
            return True

        return False

    # --카드 그리기
    def show(self, screen, mouse_position=None, mouse_click=None):
        """
        화면에 카드 그리기

        :param screen:          pygame 화면 - Surface
        :param mouse_position:  마우스 위치 - (x, y)
        :param mouse_click:     마우스 클릭 - [bool,bool,bool]
        """
        # 일반 상태
        screen.blit(self._image, self._center)

        check1 = self._active
        # 클릭 상태
        if self.get_clicked(mouse_position, mouse_click):
            screen.blit(self._image_clicked, self._center)
        # 액티브 상태
        if check1:
            screen.blit(self._image_active, self._center)

    #--마우스 위치 확인
    def _check_mouse_position(self, mouse_position):
        """
        카드 영역 내 마우스 위치 여부 확인

        :param mouse_position:  마우스 위치 - (x, y)
        :return:                버튼 영역 내 마우스 위치 여부 - bool
        """
        if mouse_position != None:
            if self._position[0] - (self._size[0]) // 2 < mouse_position[0] < self._position[0] + (self._size[0]) // 2 \
                    and self._position[1] - (self._size[1]) // 2 < mouse_position[1] < self._position[1] + (self._size[1]) // 2:
                return True

        return False

    #--마우스 클릭 확인
    def _check_mouse_leftclicked(self, mouse_click):
        """
        마우스 클릭 여부 확인

        :param mouse_click:     마우스 클릭 - [bool,bool,bool]
        :return:                마우스 클릭 여부 - bool
        """
        if mouse_click != None:
            if mouse_click[0] == True:
                return True

        return False

# 숫자 카드 클래스---------------------------------------------------------------------------------------------------------
class Number_Card(Card):
    _number = None
    def __init__(self, card_size, card_image_path=None, card_cliked_image_path=None, card_active_image_path=None):
        super().__init__(card_size, card_image_path, card_cliked_image_path, card_active_image_path)

    #--숫자 부여
    def set_number(self, number):
        """
        카드에 숫자 값 부여

        :param number: 숫자 - 실수
        """
        self._number = number

    #--숫자 확인
    def get_number(self):
        """
        카드의 숫자 값 확인
        
        :return:    숫자 - 실수
        """
        return self._number