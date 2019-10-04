from typing import List, Any

import pygame
pygame.init()
win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Hangman Game")


buttons = []
button_values = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
                 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't ', 21: 'u', 22: 'v', 23: 'w',
                 24: 'x', 25: 'y', 26: 'z'}
button_trigger = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


class Button(object):
    # a button class that eases up the button creation
    # takes color(hex values) x and y co-ordinates, width, height and the text
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    # for placing it on the screen
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        font = pygame.font.SysFont('arial', 15)
        text = font.render(self.text, 1, (0, 0, 0))
        win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    # tells us if the mouse pointer is over the element or not
    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False

    def update_color(self, color):
        # updates the color of the button
        self.color = color

    def update_text(self, text):
        # updates the text of the button
        self.text = text


posx = 80   # starting position of buttons
posy = 30
for i in range(1, 27):
    posx += 40
    if i == 14:
        posy += 50
        posx = 120
    buttons.append(Button((255, 255, 255), posx, posy, 30, 30, button_values[i]))  # setting up the buttons


def redraw_game_window():
    pygame.display.flip()
    for obj in buttons:
        obj.draw(win)


run = True

while run:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()  # gets the position of the mouse pointer
        if event.type == pygame.QUIT:
            run = False  # exits us out of the loop thus ending the game

        # hover functionality for the buttons
        for button in buttons:
            if button.is_over(pygame.mouse.get_pos()):
                if button_trigger[buttons.index(button)] == 0:
                    button.update_color((200, 2, 225))
            else:
                button.update_color((255, 255, 255))

        for button in buttons:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_over(pygame.mouse.get_pos()):
                    if button_trigger[buttons.index(button)] == 0:
                        print('you have pressed the button >> ', button_values[buttons.index(button)+1])
                        button_trigger[buttons.index(button)] = 1
    redraw_game_window()


pygame.quit()
