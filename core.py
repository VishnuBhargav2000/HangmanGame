import pygame
import vocab

pygame.init()

win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Hangman Game")
hangman_images = [pygame.image.load("assets/10 level/0.jpg"), pygame.image.load("assets/10 level/1.jpg"), pygame.image.load("assets/10 level/2.jpg"), pygame.image.load("assets/10 level/3.jpg"), pygame.image.load("assets/10 level/4.jpg"), pygame.image.load("assets/10 level/5.jpg"),
                pygame.image.load("assets/10 level/6.jpg"), pygame.image.load("assets/10 level/7.jpg"), pygame.image.load("assets/10 level/8.jpg"), pygame.image.load("assets/10 level/9.jpg"), pygame.image.load("assets/10 level/10.jpg"), pygame.image.load("assets/10 level/won.jpg")]


def word_guessed(sec_word, letters_guessed2):
    value = 0
    for char in sec_word:
        if char in letters_guessed2:
            value += 1
    return value == len(sec_word)


def display_secret_word(secret_word1):
    posx = 10
    posy = 250
    code = ''
    # setting up secret word text boxes
    for char in secret_word1:
        if char in correct_letters_guessed:
            code += char
        else:
            code += "-"
    for char in code:
        secret_word_buttons.append(Button((255, 255, 255), posx, posy, 30, 30, text=char))
        posx += 40


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
    pygame.draw.rect(win, (0, 0, 0), [10, 250, 330, 30])
    posx = 80   # starting position of buttons
    posy = 30
    global image, tries, secret_word, category, letter_buttons, secret_word_buttons, correct_letters_guessed
    letter_buttons = []
    # setting up the buttons
    for i in range(1, 27):
        posx += 40
        if i == 14:
            posy += 50
            posx = 120
        letter_buttons.append(Button((255, 255, 255), posx, posy, 30, 30, button_values[i]))
    image = hangman_images[0]
    secret_word, category = vocab.choose_word()
    print(secret_word)
    tries = 10
    secret_word_buttons = []
    correct_letters_guessed = []
    display_secret_word(secret_word)
    category_button.update_text("category : " + category)


def redraw_game_window():
    pygame.display.flip()
    for obj in letter_buttons:
        if obj.guessed:
            pass
        else:
            obj.draw(win)
    for but in secret_word_buttons:
        but.draw(win)
    tries_left_text = "tries  left : " + str(tries) + "  "
    tries_left_button.update_text(tries_left_text)
    tries_left_button.draw(win)
    category_button.draw(win)
    win.blit(image, (450, 150))


def end_game():
    pygame.quit()


# assigning each image to tries value so that right image can be displayed.
hangman_image_loader = {10: 0, 9: 1, 8: 2, 7: 3, 6: 4, 5: 5, 4: 6, 3: 7, 2: 8, 1: 9, 0: 10, 11: 11}
button_values = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
                 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
                 24: 'x', 25: 'y', 26: 'z'}
# list, when  filled up will contain all the buttons used for giving inputs
letter_buttons = []
# list, when  filled up will contain all the buttons used for showing the output
secret_word_buttons = []
# list that stores the letters guessed by the user that do exist in the word
correct_letters_guessed = []

# run == True >> game runs;     run == False >> game doesnt run
run = True

# based upon the difficulty the tries or guesses left is stored
tries = 10

# choosing a random category and a word from that category from that category
secret_word, category = vocab.choose_word()

# button initialisation
tries_left_button = Button((255, 255, 255), 10, 200, 200, 30, "tries  left : " + str(tries) + "  ")
category_button = Button((255, 255, 255), 10, 150, 200, 30, "category : " + category)

# starting the game
initialize_game()

display_secret_word(secret_word)


while run:
    # we need to end the game if the tries or the guesses of the player deplete
    while 11 > tries > 0:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # gets the position of the mouse pointer
            if event.type == pygame.QUIT:
                end_game()

            # hover functionality for the buttons
            for button in letter_buttons:
                if button.is_over(pygame.mouse.get_pos()):
                    if not button.guessed:
                        button.update_color((200, 2, 225))
                else:
                    button.update_color((255, 255, 255))

            for button in letter_buttons:
                if button.is_over(pygame.mouse.get_pos()):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if not button.guessed:
                            letter = button_values[letter_buttons.index(button)+1]

                            if letter in secret_word and letter not in correct_letters_guessed:
                                correct_letters_guessed.append(letter)
                            display_secret_word(secret_word)

                            if letter not in secret_word:
                                tries -= 1

                            if word_guessed(secret_word, correct_letters_guessed):
                                tries = 11
                                # exits us out of the loop thus ending the game

                            button.guessed = True
                            image = hangman_images[hangman_image_loader[tries]]
        redraw_game_window()

    redraw_game_window()    # for showing the winning image
    pygame.time.wait(5000)
    initialize_game()


pygame.quit()   # quits the game
