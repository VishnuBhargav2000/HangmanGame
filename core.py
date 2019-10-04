import pygame, random
pygame.init()
win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Hangman Game")


def load_words():
    print("Loading word list from file...")
    words_file = open('words.txt', 'r')
    line = words_file.readline()
    words = line.split()
    print("  ", len(words), "words loaded.")
    return words


def choose_word(wordslist):
    return random.choice(wordslist)


def word_guessed(sec_word, letters_guessed2):
    value = 0
    for char in sec_word:
        if char in letters_guessed2:
            value += 1
    return value == len(sec_word)


def letter_present(letter):
    global correct_letters_guessed
    if letter in secret_word:
        if letter not in correct_letters_guessed:
            correct_letters_guessed.append(letter)
    return letter in secret_word


def get_guessed_word(secret_word1):
    code = ''
    for char in secret_word1:
        if char in correct_letters_guessed:
            code += char
        else:
            code += "-"
    return code


def display_secret_word():
    posx = 10
    posy = 400
    for char in get_guessed_word(secret_word):
        posx += 40
        secret_word_buttons.append(Button((255, 255, 255), posx, posy, 30, 30, text=char))


correct_letters_guessed = []
wordlist = load_words()
secret_word = choose_word(wordlist)
print(secret_word)
buttons = []
button_values = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
                 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
                 24: 'x', 25: 'y', 26: 'z'}
secret_word_buttons = []


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
        self.guessed = False

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


def initialize_game():
    posx1 = 80   # starting position of buttons
    posy1 = 30
    # setting up the buttons
    for i in range(1, 27):
        posx1 += 40
        if i == 14:
            posy1 += 50
            posx1 = 120
        buttons.append(Button((255, 255, 255), posx1, posy1, 30, 30, button_values[i]))
    # setting up secret word text boxes


def redraw_game_window():
    pygame.display.flip()
    for obj in buttons:
        obj.draw(win)
    for but in secret_word_buttons:
        but.draw(win)
    tries_left_text = "tries  left : " + str(tries) + "  "
    tries_left_button.update_text(tries_left_text)
    tries_left_button.draw(win)


run = True
tries = 10
tries_left_button = Button((255, 255, 255), 10, 200, 100, 30, "tries  left : " + str(tries) + "  ")
initialize_game()
display_secret_word()


while run:
    while tries > 0:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # gets the position of the mouse pointer
            if event.type == pygame.QUIT:
                tries = -1
                run = False  # exits us out of the loop thus ending the game

            # hover functionality for the buttons
            for button in buttons:
                if button.is_over(pygame.mouse.get_pos()):
                    if not button.guessed:
                        button.update_color((200, 2, 225))
                else:
                    button.update_color((255, 255, 255))

            for button in buttons:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.is_over(pygame.mouse.get_pos()):
                        if not button.guessed:
                            letter_present(button_values[buttons.index(button)+1])
                            print(correct_letters_guessed)
                            print(get_guessed_word(secret_word))
                            display_secret_word()
                            if word_guessed(secret_word, correct_letters_guessed):
                                print("you have won the game")
                            if not letter_present(button_values[buttons.index(button)+1]):
                                tries -= 1
                            print(tries)
                            button.guessed = True
        redraw_game_window()
    run = False

pygame.quit()
