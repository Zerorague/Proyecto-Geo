import pygame
import math

pygame.init()

window_height = 500
window_width = 600
window = pygame.display.set_mode((window_height, window_width))

# the buttons for the shop MENU


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.over = False

    def draw(self, window, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(window, outline, (self.x-2,
                             self.y-2, self.width+4, self.height+4), 0)

        pygame.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                        self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def playSoundIfMouseIsOver(self, pos, sound):
        if self.isOver(pos):
            if not self.over:
                beepsound.play()
                self.over = True
        else:
            self.over = False


white = (255, 255, 255)
# the numbers for the calcaltor
s_1s = button((0, 255, 0), 40, 450, 30, 30, '1')
s_2s = button((0, 255, 0), 40, 400, 30, 30, '2')
s_3s = button((0, 255, 0), 40, 350, 30, 30, '3')
s_4s = button((0, 255, 0), 100, 450, 30, 30, '4')
s_5s = button((0, 255, 0), 100, 400, 30, 30, '5')
s_6s = button((0, 255, 0), 100, 350, 30, 30, '6')
s_7s = button((0, 255, 0), 150, 450, 30, 30, '7')
s_8s = button((0, 255, 0), 150, 400, 30, 30, '8')
s_9s = button((0, 255, 0), 150, 350, 30, 30, '9')
s_0s = button((0, 255, 0), 200, 450, 30, 30, '0')

numbers = [s_1s, s_2s, s_3s, s_4s, s_5s, s_6s, s_7s, s_8s, s_9s, s_0s]

# the symbols!
d_1s = button((0, 255, 0), 260, 450, 30, 30, '+')
d_2s = button((0, 255, 0), 260, 400, 30, 30, '-')
d_3s = button((0, 255, 0), 260, 350, 30, 30, 'x')
d_4s = button((0, 255, 0), 200, 400, 30, 30, '÷')
d_5s = button((0, 255, 0), 200, 350, 30, 30, '=')
d_6s = button((0, 255, 0), 260, 500, 30, 30, 'C')

symbols = [d_1s, d_2s, d_3s, d_4s, d_5s, d_6s]


# redraw window
def redraw(inputtap):
    # draw all the numbers
    for button in numbers:
        button.draw(window)

    # the symbols
    for button in symbols:
        button.draw(window)

    inputtap.draw(window)


def Symbols():
    global user_input
    global python_input
    global is_finished

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()

        try:
            if is_finished or user_input[-1] in ["+", "-", "x", "÷", "="]:
                # User shouldn't type two symbols continuously
                # User shouldn't input any symbols when game finished because there is no number
                return
        except IndexError:
            # User shouldn't input any symbols if there is no number
            return

        if d_1s.isOver(pos):
            print("+")
            user_input += "+"
            python_input += "+"

        if d_2s.isOver(pos):
            print("-")
            user_input += "-"
            python_input += "-"

        if d_3s.isOver(pos):
            print("x")
            user_input += "x"
            python_input += "*"

        if d_4s.isOver(pos):
            print("÷")
            user_input += "÷"
            python_input += "/"

        if d_5s.isOver(pos):
            print("=")
            result = eval(python_input)
            python_input = ""
            user_input += f"={result:.2f}"
            is_finished = True

        if d_6s.isOver(pos):
            print("C")
            python_input = ""
            user_input = ""


def MOUSEOVERnumbers():
    global user_input
    global python_input
    global is_finished

    if event.type == pygame.MOUSEBUTTONDOWN:
        if is_finished:
            user_input = ""
            python_input = ""
            is_finished = False
        pos = pygame.mouse.get_pos()
        if s_1s.isOver(pos):
            print("1")
            user_input += "1"
            python_input += "1"
        if s_2s.isOver(pos):
            print("2")
            user_input += "2"
            python_input += "2"
        if s_3s.isOver(pos):
            print("3")
            user_input += "3"
            python_input += "3"
        if s_4s.isOver(pos):
            print("4")
            user_input += "4"
            python_input += "4"
        if s_5s.isOver(pos):
            print("5")
            user_input += "5"
            python_input += "5"
        if s_6s.isOver(pos):
            print("6")
            user_input += "6"
            python_input += "6"
        if s_7s.isOver(pos):
            print("7")
            user_input += "7"
            python_input += "7"
        if s_8s.isOver(pos):
            print("8")
            user_input += "8"
            python_input += "8"
        if s_9s.isOver(pos):
            print("9")
            user_input += "9"
            python_input += "9"
        if s_0s.isOver(pos):
            print("0")
            user_input += "0"
            python_input += "0"


# the main loop
run = True
user_input = ""
python_input = ""
is_finished = True

while run:
    # input tap
    inputtap = button((253, 100, 32), 10, 280, 450, 50, f"{user_input}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        MOUSEOVERnumbers()

        Symbols()

    redraw(inputtap)
    pygame.display.update()

pygame.quit()
