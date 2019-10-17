import pygame
import vocab

pygame.init()

win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Hangman Game")
hangman_images = {"lose": pygame.image.load("assets/lose.png"), "won": pygame.image.load("assets/won.png"),
                  "correct": pygame.image.load("assets/correct.png"), "wrong": pygame.image.load("assets/wrong.png"),
                  "idle": pygame.image.load("assets/idle.png")}
bg = pygame.image.load("assets/bg.png")


def word_guessed(sec_word, letters_guessed2):
    value = 0
    for char in sec_word:
        if char in letters_guessed2:
            value += 1
    return value == len(sec_word)


def display_secret_word(secret_word1):
    posx = 20
    posy = 250
    code = ''
    # setting up secret word text boxes
    for char in secret_word1:
        if char in correct_letters_guessed:
            code += char
        else:
            code += "-"
    for char in code:
        secret_word_buttons.append(Button((179, 220, 216), posx, posy, 25, 30, text=char))
        posx += 35


# noinspection PyShadowingNames
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
    win.blit(bg, (0, 0))
    global image, tries, secret_word, category, letter_buttons, secret_word_buttons, score, correct_letters_guessed
    letter_buttons = []

    # setting up the buttons
    posx = 70   # starting position of buttons
    posy = 40
    for i in range(1, 27):
        posx += 40
        if i == 14:
            posy += 60
            posx = 110
        letter_buttons.append(Button((255, 255, 255), posx, posy, 30, 30, button_values[i]))

    # choosing a random category and a word from that category from that category
    secret_word, category = vocab.choose_word()
    print(secret_word)

    # based upon the difficulty the tries or guesses left is stored
    if difficulty == "hard":
        tries = 7
    else:
        tries = 10

    # resetting the image to welcome image
    image = hangman_images["idle"]

    # resetting the correct letters guessed and secret word buttons that will be displayed on the screen
    secret_word_buttons = []
    correct_letters_guessed = []

    # resetting the text displayed on the game window
    display_secret_word(secret_word)
    category_button.update_text("category : " + category)
    welcome_player.update_text("welcome, " + str(name))

    if len(secret_word) > 5:
        score = 100
    else:
        score = 0


def redraw_game_window():
    pygame.display.flip()   # updates the display

    for obj in letter_buttons:  # displays the letter buttons on the screen
        if obj.guessed:
            pass    # if the letter is already guessed , it will not be displayed
        else:
            obj.draw(win)

    for but in secret_word_buttons:
        but.draw(win)   # to display the secret word on the screen

    pygame.draw.rect(win, (255, 255, 255), [400, 150, 300, 300])
    tries_left_button.update_text("tries  left : " + str(tries) + "  ")
    if tries != -1:
        tries_left_button.draw(win)
    category_button.draw(win)
    win.blit(image, (400, 150))
    welcome_player.draw(win)


def end_game():
    # quits the game
    pygame.quit()


# noinspection PyShadowingNames
def start_menu():
    global start, name, difficulty
    posx = 80
    posy = 170
    for i in range(1, 27):
        posx += 40
        if i == 14:
            posy += 50
            posx = 120
        letter_buttons.append(Button((255, 255, 255), posx, posy, 30, 30, button_values[i]))
    done = Button((179, 220, 216), posx-120, posy+156, 60, 30, "DONE")
    easy = Button((179, 220, 216), 350, posy + 105, 60, 30, "Easy")
    hard = Button((179, 220, 216), 450, posy + 105, 60, 30, "Hard")
    display_name = Button((255, 255, 255), posx-400, posy+60, 200, 30, " player name : ")
    bg = pygame.image.load("assets/start_screen.png")

    def redraw_window():
        pygame.display.flip()
        win.blit(bg, (0, 0))
        for obj in letter_buttons:
            if obj.guessed:
                pass
            else:
                obj.draw(win)
        done.draw(win)
        easy.draw(win)
        hard.draw(win)
        display_name.update_text(" player name : " + str(name))
        display_name.draw(win)

    while True:     # main loop

        # quits thw game wen close is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()

            # button mechanics for difficulty done buttons
            if done.is_over(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return
            if easy.is_over(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = "easy"
            if hard.is_over(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = "hard"

            # hover functionality for those buttons
            if easy.is_over(pygame.mouse.get_pos()):
                easy.update_color((200, 240, 240))
            else:
                easy.update_color((179, 220, 216))

            if hard.is_over(pygame.mouse.get_pos()):
                hard.update_color((200, 240, 240))
            else:
                hard.update_color((179, 220, 216))

            if done.is_over(pygame.mouse.get_pos()):
                done.update_color((200, 240, 240))
            else:
                done.update_color((179, 220, 216))

            # hover functionality for letter buttons
            for button in letter_buttons:
                if button.is_over(pygame.mouse.get_pos()):
                    if not button.guessed:
                        button.update_color((179, 220, 216))
                else:
                    button.update_color((255, 255, 255))

            # mechanism of letter buttons
            for button in letter_buttons:
                if button.is_over(pygame.mouse.get_pos()):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        letter = button_values[letter_buttons.index(button)+1]
                        name += letter
            redraw_window()


# assigning each image to tries value so that right image can be displayed.
button_values = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
                 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
                 24: 'x', 25: 'y', 26: 'z'}

# list, when  filled up will contain all the buttons used for giving inputs
letter_buttons = []

# list, when  filled up will contain all the buttons used for showing the output
secret_word_buttons = []

# list that stores the letters guessed by the user that do exist in the word
correct_letters_guessed = []

run, start = True, True
name, difficulty, tries = "", "", 0
secret_word, category = "", ""
score = 0

# these are not actually buttons i have used objects of button class to display variables (text) on screen
# because, it makes it a lot simpler and more productive
tries_left_button = Button((255, 255, 255), 20, 350, 200, 30, "tries  left : " + str(tries) + "  ")
category_button = Button((255, 255, 255), 20, 150, 200, 30, "category : " + category)
welcome_player = Button((255, 255, 255), 20, 300, 200, 30, "welcome, " + name)


start_menu()
initialize_game()


while run:
    # we need to end the game if the tries or the guesses of the player deplete
    while tries >= 0:
        if tries == 0:
            # player has depleted all of his tries.
            image = hangman_images["lose"]
            redraw_game_window()
            break

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # gets the position of the mouse pointer
            if event.type == pygame.QUIT:
                end_game()

            # hover functionality for the buttons
            for button in letter_buttons:
                if button.is_over(pygame.mouse.get_pos()):
                    if not button.guessed:
                        button.update_color((179, 220, 216))
                else:
                    button.update_color((255, 255, 255))

            for button in letter_buttons:
                if button.is_over(pygame.mouse.get_pos()):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if not button.guessed:
                            letter = button_values[letter_buttons.index(button)+1]
                            # registering click of the button

                            if letter in secret_word and letter not in correct_letters_guessed:     # correct guess
                                correct_letters_guessed.append(letter)
                                image = hangman_images["correct"]

                                # increasing the score of the player after every correct guess
                                if difficulty == "easy":
                                    score += 70
                                else:
                                    score += 100

                            display_secret_word(secret_word)  # updating the secret word on screen

                            if letter not in secret_word:       # wrong guess
                                tries -= 1
                                image = hangman_images["wrong"]

                            if word_guessed(secret_word, correct_letters_guessed):
                                tries = -1      # exits us out of the loop thus ending the game
                                image = hangman_images["won"]
                                score += 250

                            button.guessed = True
        redraw_game_window()

    redraw_game_window()    # for showing the winning image
    pygame.time.wait(3000)
    print(score)
    initialize_game()

