# These Cards classes allows users to make flexible playing cards for virtual card-based games.
# The class PlayingCard simulates a standard playing card.
# Note that Ace is intended to be 1, Jack 11, Queen 12, King 13, and Joker 0
# Suits should be strings, e.g. "hearts" for hearts, "blue" for a blue "Uno" card, etc.
# The cards are linked list elements, in order to create a deck.
# opened is a Boolean which represents if the card is face up or face down. True for face up

from random import randrange, shuffle, choice

class PlayingCard:  #Simulates cards from a deck of normal cards

    def __init__(self,suit='BlkJoker',num=0,opened=True): #Initializing without specifying suit or number gives a joker.

        self.suit = suit
        self.num = num
        self.opened = opened
        self.bj_num = min(self.num, 10) #Converts face cards into tens

    def randomize_card(self): #Randomizes a single card

        self.suit = choice(['spades', 'hearts', 'clubs', 'diamonds'])
        self.num = randrange(1, 14)

    def flip(self): #Changes the visual side shown

        if self.opened:
            self.opened = False
        else:
            self.opened = True

    def print_card(self): #Prints the identity of the card to the terminal

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

class Hand:

    def __init__(self,deck,n):
        self.hand = []
        self.hand = deck.draw(n)
        self.size = len(self.hand)

    def print_size(self):
        print(self.size)

    def draw(self,n,deck): #draw a card from the deck. if no cards can be drawn, return None
        drawn=deck.draw(n)
        l=len(drawn)
        if l == 0:
            return None
        else:
            self.size += l
            self.hand+=drawn

    def print_hand(self):
        for i in range(self.size):
            PlayingCard.print_card(self.hand[i])
            print('')



class Deck:

    def __init__(self,jokers=False): #Initializing produces a new shuffled deck
        self.deck=[]
        if jokers:
            self.deck.append(PlayingCard('BlkJoker',0))
            self.deck.append(PlayingCard('RedJoker',0))
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










    

