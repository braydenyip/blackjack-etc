from Cards import *
# from random import *
import tkinter as tk

class game_win:

def main():
    #initialize hands and deck
    d=Deck()
    dealer=Hand(d,2)
    player=Hand(d,2)
    #boolean game state vars
    stand=False
    bust=False
    #Flip the dealer's second card as is done in blackjack
    PlayingCard.flip(dealer.hand[1])

    dealer.print_hand()

    win=tk.Tk()

    win.mainloop()
    if is21(player):
        print("Blackjack!")
        return 0

    while not stand and not bust:
        player.print_hand()
        move="Wait"
        while move != "Hit" and move != "Stand":
            move=input("What do you want to do? :")
        if move == "Hit":
            #Hit -- add 1 card
            player.draw(d,1)
            if get_score(player) > 21:
                bust = True
            elif is21(player):
                stand = True
                print("21!")
        else:
            stand = True
    player.print_hand()
    #Flip over the hidden card
    PlayingCard.flip(dealer.hand[1])
    if bust:
        print("You have gone bust. You lose!")
        return 0
    while get_score(dealer) < 17:
        dealer.draw(d,1)
        dealer.print_hand()
    final_dealer = get_score(dealer)
    final_player = get_score(player)
    if (final_dealer > 21):
        print("Dealer has gone bust. You win!")
    elif (final_player > final_dealer):
        print("You got a higher score than the dealer. You win!")
    elif (final_player == final_dealer):
        print("You have tied with the dealer.")
    else:
        print("The dealer got a higher score than you. You lose!")
    return 0

def get_score(h): #returns the blackjack score of a hand
    score = 0
    b_score = 0
    a_score = 0
    for card in h.hand:
        if (card.num == 1): #Ace logic
            a_score = score + 1
            b_score = score + 11
            if b_score > 21 or a_score > 21: #if adding 11 busts or if either bust, take the lower a_score
                score = a_score
            elif b_score == 21: #if either produce a 21, default to that one
                score = b_score
            elif a_score == 21:
                score = a_score
            else: #if adding 11 does not bust nor produce a blackjack
                score = b_score
        else:
            score += min(card.num,10)
    return score

def is21(h):
    if (get_score(h) == 21):
        return True
    else:
        return False

if __name__ == '__main__':
    main()