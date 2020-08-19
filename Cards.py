# These Cards classes allows users to make flexible playing cards for virtual card-based games.
# The class PlayingCard simulates a standard playing card.
# Note that Ace is intended to be 1, Jack 11, Queen 12, King 13, and Joker 0
# Suits should be strings, e.g. "hearts" for hearts, "blue" for a blue "Uno" card, etc.
# The cards are linked list elements, in order to create a deck.
# opened is a Boolean which represents if the card is face up or face down. True for face up

from random import *

class PlayingCard:

     def __init__(self,suit='hearts',num=1,opened=True):
        self.suit = suit
        self.num = num
        self.opened = opened
        self.img_path = "assets/game-assets/AH.png"
        update_img_path(self)

    def randomize_card(self): #Randomizes a single card

        self.suit = choice(['spades', 'hearts', 'clubs', 'diamonds'])
        self.num = randrange(1, 14)

    def flip(self): #Changes the visual side shown

        if self.opened:
            self.opened = False #backside

        else:
            self.opened = True

    def print_card(self): #Prints the identity of the card to the terminal
        if not self.opened:
            print("Hidden")
        else:
            if(self.num == 1):
                print("Ace ")
            elif(self.num == 11):
                print("Jack ")
            elif(self.num == 12):
                print("Queen ")
            elif(self.num == 13):
                print("King ")
            else:
                print("{0}".format(self.num))
            print("of {0}".format(self.suit))

    def update_img_path(self):
        self.img_path = "assets/game-assets/"
        if (self.num == 1):
            self.img_path += "A"
        elif (self.num == 11):
            self.img_path += "J"
        elif (self.num == 12):
            self.img_path += "Q"
        elif (self.num == 13):
            self.img_path += "K"
        else:
            self.img_path += str(self.num)

        if (self.suit == 'spades'):
            self.img_path += "S"
        elif (self.suit == 'clubs'):
            self.img_path += "C"
        elif (self.suit == 'diamonds'):
            self.img_path += "D"
        else:
            self.img_path += "H"

class Hand:

    def __init__(self,deck,n):
        self.hand = []
        self.hand = deck.draw(n)
        self.size = len(self.hand)

    def print_size(self):
        print(self.size)

    def draw(self,deck,n): #draw a card from the deck. if no cards can be drawn, return None
        drawn=deck.draw(n)
        l=len(drawn)
        if l == 0:
            return None
        else:
            self.size += l
            self.hand += drawn

    def print_hand(self):
        for i in range(self.size):
            PlayingCard.print_card(self.hand[i])
            print('')



class Deck:

    def __init__(self): #Initializing produces a new shuffled deck
        self.deck=[]
        for suit in ['spades', 'hearts', 'clubs', 'diamonds']:
            for n in range(1,14):
                self.deck.append(PlayingCard(suit,n))
        shuffle(self.deck)
        self.deck_size = len(self.deck)

    def draw(self,n): #Return as many as n cards from the deck as a list
        drawn=[]
        if self.deck_size < n:
            n = self.deck_size  #Function will draw as many cards as it can, if it cannot draw the requested amount
        for i in range(n):
            drawn.append(self.deck.pop(0))
        return drawn










    

