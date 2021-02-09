import pygame
import os


# 추상 버튼 클래스---------------------------------------------------------------------------------------------------------
class Rectangle_Center:
    _position = [0, 0]
    _size = [0, 0]
    _center = None
    _image = None
    _image_clicked = None
    _image_active = None
    _active = False
    def __init__(self, button_size, button_image_path = None, button_cliked_image_path = None, button_active_image_path = None):
        """
        버튼 생성
        
        :param button_size:                 버튼 크기 - [너비, 높이]
        :param button_image_path:           이미지 경로 - 문자열
        :param button_cliked_image_path:    클릭 이미지 경로 - 문자열
        :param button_active_image_path:    활성화 이미지 경로 - 문자열
        """
        # 버튼 크기 - [x,y], 버튼 이미지 - 경로
        self._position = [0, 0]
        self._size[0] = button_size[0]
        self._size[1] = button_size[1]
        self._center = None
        self._active = False
        module_path = os.path.dirname(__file__)
        if button_image_path == None:
            button_image_path = os.path.join(module_path, "./pic/default_button.png")
        if button_cliked_image_path == None:
            button_cliked_image_path = os.path.join(module_path, "./pic/default_button_clicked.png")
        if button_active_image_path == None:
            button_active_image_path = os.path.join(module_path, "./pic/default_button_active.png")

        self._image = pygame.image.load(button_image_path)
        self._image = pygame.transform.scale(self._image, [self._size[0], self._size[1]])
        self._image_clicked = pygame.image.load(button_cliked_image_path)
        self._image_clicked = pygame.transform.scale(self._image_clicked, [self._size[0], self._size[1]])
        self._image_active = pygame.image.load(button_active_image_path)
        self._image_active = pygame.transform.scale(self._image_active, [self._size[0], self._size[1]])

    #--위치 설정
    def set_position(self, position):
        """
        버튼 위치 설정

        :param position:    버튼 위치 - [x, y]
        """
        self._position[0] = position[0]
        self._position[1] = position[1]
        self._center = self._image.get_rect()
        self._center.center = self._position

    #--활성화 설정
    def set_active(self, active):
        """
        버튼 활성화 설정

        :param active:  활성화 여부 - bool
        """
        self._active = active
    
    #--버튼 안에서 클릭 확인
    def get_clicked(self, mouse_position = None, mouse_click = None):
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

    #--활성화 확인
    def get_active(self):
        """
        버튼 활성화 여부 확인

        :return:    활성화 여부 - bool
        """
        return self._active

    #--버튼 그리기
    def show(self, screen, mouse_position = None, mouse_click = None):
        """
        화면에 버튼 그리기

        :param screen:          pygame 화면 - Surface
        :param mouse_position:  마우스 위치 - (x, y)
        :param mouse_click:     마우스 클릭 - [bool,bool,bool]
        """
        #일반 상태
        screen.blit(self._image, self._center)

        check1 = self._active
        #클릭 상태
        if self.get_clicked(mouse_position, mouse_click):
            screen.blit(self._image_clicked, self._center)
        # 액티브 상태
        if check1:
            screen.blit(self._image_active, self._center)

    #--마우스 위치 확인
    def _check_mouse_position(self, mouse_position):
        """
        버튼 영역 내 마우스 위치 여부 확인

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


# 글자 버튼 클래스---------------------------------------------------------------------------------------------------------
class Text_Button(Rectangle_Center):
    _font = None
    _text_render = None
    _text = ""
    _text_center = None
    _text_color = [0,0,0]
    def __init__(self, button_size, text = "", text_size = 30, text_color = None, button_image_path = None,
                 button_cliked_image_path = None, button_active_image_path = None):
        """
        글자 버튼 클래스

        :param button_size:     버튼 크기 - [너비, 높이]
        :param text:            글자 - 문자열
        :param text_size:       글자 크기 - 정수 | 30
        :param text_color:      글자 색 - [r, g, b] | [0, 0, 0]
        :param button_image_path:    버튼 이미지 경로 - 문자열 | None
        """
        if text_color is None:
            text_color = [0,0,0]


        self._text_center = None
        super().__init__(button_size, button_image_path, button_cliked_image_path, button_active_image_path)
        self._font = pygame.font.Font(None, text_size)  # 폰트 설정
        self._text_color = text_color
        self._text = text
        self._text_render = self._font.render(self._text, True, self._text_color)  # 텍스트가 표시된 Surface 를 만듬

    #--위치 설정
    def set_position(self, position):
        """
        버튼 위치 설정

        :param position: 위치 - [x중앙, y중앙]
        """
        super().set_position(position)
        self._text_center = self._text_render.get_rect()
        self._text_center.center = self._position

    #--버튼 그리기
    def show(self, screen, mouse_position = None, mouse_click = None, text_pos_shift = None):
        """
        화면에 버튼 그리기

        :param screen:  pygame 화면 - Surface
        """
        super().show(screen, mouse_position, mouse_click)
        self._text_render = self._font.render(self._text, True, self._text_color)  # 텍스트가 표시된 Surface 를 만듬

        if text_pos_shift is None:
            screen.blit(self._text_render, self._text_center)
        else:
            text_pos = [0, 0]
            text_pos[0] = self._text_center[0] + text_pos_shift[0]
            text_pos[1] = self._text_center[1] + text_pos_shift[1]
            screen.blit(self._text_render, text_pos)

    # --글자 설정
    def set_text(self, text):
        """
        글자 설정
        
        :param text:    글자 - 문자열
        """
        #타입 변환
        if(str(type(text))!="<class 'str'>"):
            try:
                text = str(text)
            except:
                print("타입 변환 문제 발생")

        self._text = text