from Cards import *
# from random import *

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
    #Flip over the hidden card
    PlayingCard.flip(dealer.hand[1])
    if bust:
        print("You have gone bust. You lose!")
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
    for card in h.hand:
        if card.num == 1 and score < 11:
            score += 11
        elif card.num == 10 and score == 11 and h.size == 2:
            score = 21
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