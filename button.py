import pygame



# 추상 버튼 클래스
class Rectangle_Center:
    position = [0, 0]
    size = [0, 0]
    center = None
    image = None
    image_clicked = None
    image_active = None
    active = False
    def __init__(self, button_size, button_image_path = None, button_cliked_image_path = None, button_active_image_path = None):
        # 버튼 크기 - [x,y], 버튼 이미지 - 경로
        self.position = [0, 0]
        self.size[0] = button_size[0]
        self.size[1] = button_size[1]
        self.center = None
        self.active = False

        if button_image_path == None:
            button_image_path = "pic/default_button.png"
        if button_cliked_image_path == None:
            button_cliked_image_path = "pic/default_button_clicked.png"
        if button_active_image_path == None:
            button_active_image_path = "pic/default_button_active.png"

        self.image = pygame.image.load(button_image_path)
        self.image = pygame.transform.scale(self.image, [self.size[0], self.size[1]])
        self.image_clicked = pygame.image.load(button_cliked_image_path)
        self.image_clicked = pygame.transform.scale(self.image_clicked, [self.size[0], self.size[1]])
        self.image_active = pygame.image.load(button_active_image_path)
        self.image_active = pygame.transform.scale(self.image_active, [self.size[0], self.size[1]])

    #--위치 설정
    def set_position(self, position):
        self.position[0] = position[0]
        self.position[1] = position[1]
        self.center = self.image.get_rect()
        self.center.center = self.position

    #--액티브 설정
    def set_active(self, active):
        """
        액티브 설정

        :param active:  액티브 여부 - bool
        """
        self.active = active
    
    #--버튼 안에서 클릭 확인
    def get_clicked(self, mouse_position = None, mouse_click = None):
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

    #--버튼 설정
    def show_button(self, screen, mouse_position = None, mouse_click = None):
        #일반 상태
        screen.blit(self.image, self.center)

        check1 = self.active
        #클릭 상태
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


# 글자 버튼 클래스
class Text_Button(Rectangle_Center):
    font = None
    text_render = None
    text = ""
    text_center = None
    text_color = [0,0,0]
    def __init__(self, button_size, text = "", text_size = 30, text_color = [0,0,0], button_image_path = None, \
                 button_cliked_image_path = None, button_active_image_path = None):
        """
        글자 버튼 클래스

        :param button_size:     버튼 크기 - [x,y]
        :param text:            글자 - 문자열
        :param text_size:       글자 크기 - 정수 | 30
        :param text_color:      글자 색 - [r, g, b] | [0, 0, 0]
        :param button_image_path:    버튼 이미지 경로 - 문자열 | None
        """
        self.text_center = None
        super().__init__(button_size, button_image_path, button_cliked_image_path, button_active_image_path)
        self.font = pygame.font.Font(None, text_size)  # 폰트 설정
        self.text_color = text_color
        self.text = text
        self.text_render = self.font.render(self.text, True, self.text_color)  # 텍스트가 표시된 Surface 를 만듬

    #--위치 설정
    def set_position(self, position):
        """
        버튼 위치 설정

        :param position: 위치 - [x중앙,y중앙]
        """
        super().set_position(position)
        self.text_center = self.text_render.get_rect()
        self.text_center.center = self.position

    #--버튼 설정
    def show_button(self, screen, mouse_position = None, mouse_click = None):
        """
        화면에 버튼 출력

        :param screen:  pygame 화면 - Surface
        """
        super().show_button(screen, mouse_position, mouse_click)
        self.text_render = self.font.render(self.text, True, self.text_color)  # 텍스트가 표시된 Surface 를 만듬
        screen.blit(self.text_render, self.text_center)

    # --글자 설정
    def set_text(self, text):
        """
        글자 설정
        
        :param text:    글자 - 문자열
        """
        self.text = text