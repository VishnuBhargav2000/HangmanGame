import pygame
import vocab
import mysql.connector
import socket

#  DRIVER CODE 3 #######################################
pygame.init()
win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Hangman Game")
hangman_images = {"lose": pygame.image.load("assets/lose.png"), "won": pygame.image.load("assets/won.png"),
                  "correct": pygame.image.load("assets/correct.png"), "wrong": pygame.image.load("assets/wrong.png"),
                  "idle": pygame.image.load("assets/idle.png")}
bg = pygame.image.load("assets/bg.png")


def is_internet_connected():
    # returns the availability of active internet connection
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("www.google.com", 80))
        print("Connected")
        return True
    except OSError:
        print("not connected")
        pass
    return False
# DRIVER CODE 3 END ############################################


# DATABASE   ###################################################
if is_internet_connected():

    mydb = mysql.connector.connect(
        host="remotemysql.com",
        user="NON1wuL7Sf",
        passwd="kEFFpgWwFZ",
        database="NON1wuL7Sf")
    mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE users(NAME varchar(255), score int);") bvcd3s2``
# mycursor.execute("drop TABLE users;")
# DATABASE END   ###############################################


# DRIVER CODE 3   ##############################################
def reset_positions():
    # resets the positions of the buttons so that they can be re-purposed
    easy.x = 350
    hard.x = 450
    easy.y = 325
    hard.y = 325
    save_and_exit.y = 400
# DRIVER CODE 3 END   ##########################################


# DRIVER CODE 2 ################################################
def word_guessed(sec_word, letters_guessed2):
    value = 0
    for char in sec_word:
        if char in letters_guessed2:
            value += 1
    return value == len(sec_word)
# DRIVER CODE 2 END ############################################


# DRIVER CODE 1 ################################################
def display_secret_word(secret_word1):
    posx = 20
    posy = 260
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
# DRIVER CODE 1 END  ###########################################


# GUI ##########################################################
# noinspection PyShadowingNames
class Button(object):
    # a button class that eases up the button creation
    # takes color(hex values) x and y co-ordinates, width, height and the text
    def __init__(self, color, x, y, width, height, text='', font=0):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.guessed = False
        self.font = font

    # for placing it on the screen
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.font == 0:
            font = pygame.font.SysFont('arial', 15)
        else:
            font = pygame.font.SysFont('font.tff', 30)

        if self.font == 0:
            text = font.render(self.text, 1, (0, 0, 0))
        else:
            text = font.render(self.text, 1, (100, 100, 100))

        win.blit(text,
                 (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        # tells us if the mouse pointer is over the element or not
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
# GUI END ######################################################


# DRIVER CODE 1 ################################################
def initialize_game():
    win.blit(bg, (0, 0))
    global image, tries, secret_word, category, letter_buttons, secret_word_buttons, score, correct_letters_guessed, temp_Score
    letter_buttons = []
    reset_positions()

    # setting up the buttons
    posx = 70  # starting position of buttons
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

    temp_Score = 0

    # resetting the image to welcome image
    image = hangman_images["idle"]

    # resetting the correct letters guessed and secret word buttons that will be displayed on the screen
    secret_word_buttons = []
    correct_letters_guessed = []

    # resetting the text displayed on the game window
    display_secret_word(secret_word)
    category_button.update_text(category)
    welcome_player.update_text("welcome, "+str(name))
# DRIVER CODE 1 END ############################################


# GUI  #########################################################
def redraw_game_window():
    # puts the content on the screen.
    pygame.display.flip()  # updates the display
    for obj in letter_buttons:  # displays the letter buttons on the screen
        if obj.guessed:
            pass  # if the letter is already guessed , it will not be displayed
        else:
            obj.draw(win)

    for but in secret_word_buttons:
        but.draw(win)  # to display the secret word on the screen

    pygame.draw.rect(win, (255, 255, 255), [400, 150, 300, 300])

    tries_left_button.update_text(str(tries) + " tries ")
    if tries != -1:
        tries_left_button.draw(win)

    category_button.draw(win)
    win.blit(image, (400, 155))
    welcome_player.draw(win)
# GUI END ######################################################


# DRIVER CODE 1 ################################################
def close_game():
    # quits the game
    pygame.quit()
# DRIVER CODE 1 END ############################################


# DRIVER CODE 1  + GUI #########################################
def end_round():
    """
    opens up a window that shows the word and their score and takes user input on
    whether they wish to continue or not
    :return: null
    """
    global difficulty

    def change_pos():
        # as the buttons are re-purposed, location needs to be changed to fit to the new screen
        easy.x = 200
        hard.x = 350
        easy.y = 170
        hard.y = 170
        save_and_exit.y = 420

    def redraw_win():
        # displays the content on the screen
        change_pos()
        hard.draw(win)
        easy.draw(win)
        save_and_exit.draw(win)
        pygame.display.flip()
        win.blit(background, (0, 0))
        if word_guessed(secret_word, correct_letters_guessed):
            char = hangman_images["won"]
        else:
            char = hangman_images["lose"]
        win.blit(char, (400, 150))
        display_score.draw(win)
        display_word.draw(win)

    def save_n_exit():
        global name, score
        if is_internet_connected():  # if internet is connected the data will be stored in the database
            sql = "INSERT INTO users(NAME, score) VALUES (%s, %s)"
            val = (name, score)
            mycursor.execute(sql, val)
            mydb.commit()
            close_game()    # exits out of the game
        else:
            close_game()    # exits out of the game

    display_score = Button((179, 220, 216), 200, 290, 50, 30, str(score))
    display_word = Button((179, 220, 216), 220, 235, 150, 30, str(secret_word))
    background = pygame.image.load("assets/end_screen.png")

    while True:
        for events in pygame.event.get():
            position = pygame.mouse.get_pos()

            if save_and_exit.is_over(position):
                if events.type == pygame.MOUSEBUTTONDOWN:
                    save_n_exit()

            if easy.is_over(position):
                if events.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = "easy"
                    return

            if hard.is_over(position):
                if events.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = "hard"
                    return

            # hover functionality for those buttons
            if easy.is_over(position):
                easy.update_color((200, 240, 240))
            else:
                easy.update_color((179, 220, 216))

            if save_and_exit.is_over(position):
                save_and_exit.update_color((200, 240, 240))
            else:
                save_and_exit.update_color((179, 220, 216))

            if hard.is_over(position):
                hard.update_color((200, 240, 240))
            else:
                hard.update_color((179, 220, 216))
            redraw_win()


# noinspection PyShadowingNames
def start_menu():

    if is_internet_connected():
        internet_status.update_text("ONLINE")   # updates the text on the screen.
    else:
        internet_status.update_text("OFFLINE")  # updates the text on the screen.

    global start, name, difficulty
    posx = 80
    posy = 170
    for i in range(1, 27):
        posx += 40
        if i == 14:
            posy += 50
            posx = 120
        letter_buttons.append(Button((255, 255, 255), posx, posy, 30, 30, button_values[i]))    # letter buttons
    bg = pygame.image.load("assets/start_screen.png")

    def redraw_window():
        # displays the content on the screen.
        pygame.display.flip()
        win.blit(bg, (0, 0))
        for obj in letter_buttons:
            if obj.guessed:
                pass
            else:
                obj.draw(win)
        easy.draw(win)
        hard.draw(win)
        display_name.update_text(" player name : " + str(name))
        display_name.draw(win)
        internet_status.draw(win)

    while True:  # main loop

        # quits the game wen close is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()

            # button mechanics for difficulty button
            if easy.is_over(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = "easy"
                    return

            if hard.is_over(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = "hard"
                    return

            # hover functionality for those buttons
            if easy.is_over(pygame.mouse.get_pos()):
                easy.update_color((200, 240, 240))
            else:
                easy.update_color((179, 220, 216))

            if hard.is_over(pygame.mouse.get_pos()):
                hard.update_color((200, 240, 240))
            else:
                hard.update_color((179, 220, 216))

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
                        letter = button_values[letter_buttons.index(button) + 1]
                        name += letter
            redraw_window()
# DRIVER CODE 1  + GUI END #####################################


# DRIVER CODE 1 ################################################

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
score, temp_Score = 0, 0

# DRIVER CODE 1 END ############################################

# GUI ##########################################################
# text boxes and buttons that show up on the screen
tries_left_button = Button((255, 255, 255), 105, 393, 80, 30, str(tries) + " tries left", 1)
category_button = Button((255, 255, 255), 20, 345, 200, 30, "category : " + category, 1)
welcome_player = Button((255, 255, 255), 25, 194, 200, 30, "welcome, " + name, 1)
save_and_exit = Button((179, 220, 216), 50, 400, 200, 30, "save and exit")
easy = Button((179, 220, 216), 350, 325, 60, 30, "Easy")
hard = Button((179, 220, 216), 450, 325, 60, 30, "Hard")
internet_status = Button((179, 220, 216), 300, 390, 80, 30, "internet status")
display_name = Button((255, 255, 255), 200, 280, 230, 30, " player name : ")
# GUI END ######################################################

start_menu()  # shows the start menu and takes the input(name, difficulty) from user
initialize_game()  # chooses a word and initialises all the values to default

while run:
    # we need to end the game if the player depletes his tries
    while tries > 0:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # gets the position of the mouse pointer
            if event.type == pygame.QUIT:
                close_game()

            # hover functionality for the buttons
            for button in letter_buttons:
                if button.is_over(pos):
                    if not button.guessed:
                        button.update_color((179, 220, 216))
                else:
                    button.update_color((255, 255, 255))

            for button in letter_buttons:
                if button.is_over(pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if not button.guessed:
                            # assigning the letter with its corresponding button
                            letter = button_values[letter_buttons.index(button) + 1]

                            if letter in secret_word and letter not in correct_letters_guessed:  # correct guess

                                # saving all the correct letters guessed
                                correct_letters_guessed.append(letter)

                                # updating te image
                                image = hangman_images["correct"]

                                # increasing the score of the player after every correct guess
                                if difficulty == "easy":
                                    temp_Score += 70
                                else:
                                    temp_Score += 100

                            display_secret_word(secret_word)  # updating the secret word on screen

                            if letter not in secret_word:  # wrong guess
                                tries -= 1  # decreasing the tries the player has
                                image = hangman_images["wrong"]  # updating the image

                            if word_guessed(secret_word, correct_letters_guessed):
                                tries = -1  # exits us out of the loop thus ending the round
                                score += 250  # increasing the score for winning the game

                                if len(secret_word) > 5:  # increasing the score for answering a lengthy word
                                    score += 100
                                score += temp_Score  # adds all the points gained by correct guesses

                            # changing the guessed attribute so that the button cannot be pressed twice
                            button.guessed = True
        redraw_game_window()

    redraw_game_window()  # for showing the winning image
    pygame.time.wait(1000)  # adds a pause of 1000 milliseconds
    end_round()  # shows the end screen and takes user input
    initialize_game()
