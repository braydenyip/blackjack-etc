from Cards import *
# from random import *

def main():
    d=Deck()
    dealer=Hand(d,2)
    player=Hand(d,2)
    dealer.print_hand()
    player.print_hand()
    return 0


if __name__ == '__main__':
    main()