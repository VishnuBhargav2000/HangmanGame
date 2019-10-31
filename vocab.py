# DRIVER CODE 2 ############################################
import random
animals = ["animals", "cat", "bat", "dog", "bear", "whale", "lion", "pig", "goat", "cow", "snake"]
food = ["food", "apple", "banana", "pear", "pizza", "pie", "beef", "taco", "cheese", "carrot", "peanut"]
geography = ["geography", "mountain", "lake", "ocean", "hill", "valley", "cliff", "bay", "peninsula", "range", "plains"]
military = ["military", "tank", "jet", "nuke", "rank", "war", "sergeant", "trench", "rifle", "uniform", "orders"]
space = ["space", "star", "planet", "moon", "vacuum", "meteor", "comet", "asteroid", "gravity", "mars", "jupiter"]
nature = ["nature", "tree", "breeze", "desert", "plains", "bugs", "sky", "clouds", "river", "forest", "beach"]
vehicles = ["vehicles", "car", "bus", "truck", "plane", "train", "boat", "blimp", "bike", "wagon", "horse"]
music = ["music", "rock", "country", "rap", "fuzz", "metal", "folk", "riff", "chord", "scale", "octave"]
instruments = ["instruments", "tuba", "guitar", "bass", "harmonica", "violin", "cello", "piano", "drums", "trombone", "saxophone"]
household = ["household", "phone", "kitchen", "closet", "room", "curtains", "carpet", "attic", "basement", "garage", "driveway"]
history = ["history", "medieval", "ancient", "ruins"]
technology = ["technology", "phone", "wire", "signal", "antenna", "display"]
fantasy = ["fantasy", "dragon", "princess", "sword", "magic", "dungeon", "goblin", "elf", "orc", "hobbit", "unicorn"]
gaming = ["gaming", "role", "shooter", "strategy", "simulation", "sandbox", "tactical", "steam", "twitch", "indie"]
school = ["school", "pencil", "paper", "textbook", "teacher", "lunch", "locker", "backpack", "grades", "finals"]
internet = ["internet", "wifi", "broadband", "network", "gateway", "router", "provider", "neutrality", "piracy", "reddit"]
parties = ["parties", "drunk", "wasted", "dancing", "barfing", "social", "music", "guests", "surprise", "frat", "sorority"]
math = ["math", "division", "addition", "fraction", "algebra", "calculus", "equation"]
entertainment = ["entertainment", "radio", "streaming", "netflix", "comedy", "play", "sports", "music", "poetry", "park"]
art = ["art", "painting", "singing", "sculpture", "sketch", "draw", "paint", "palette", "design", "portrait"]

# CATEGORY MASTER LIST
category_list = [animals, art, food, fantasy, geography, military, math, music, entertainment, space, nature, vehicles
                , instruments, technology, household, history, school, parties, internet]


def choose_word():
    while True:
        category_Selected = random.choice(category_list)
        word = random.choice(category_Selected)
        category = category_Selected[0]
        if category != word:
            return word, category

# DRIVER CODE 2 END ############################################
