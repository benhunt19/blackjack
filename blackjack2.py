import random
import time

class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit
        self.value()

    # giving the cards value
    def value(self):
        if self.num <= 10:
            self.value = self.num
        if self.num >= 11:
            self.value = 10

    # giving the cards names
    def viewcard(self):
        if self.num <=10 and self.num >= 2:
            print(self.num,'of', self.suit)
        if self.num == 11:
            print('Jack of ', self.suit)
        if self.num == 12:
            print('Queen of ', self.suit)
        if self.num == 13:
            print('King of ', self.suit)
        if self.num == 1:
            print('Ace of ', self.suit)

class Deck:

    def __init__(self):
        self.allcards = []
        self.build()

    # builds the deck of cards when a 'Deck' is created
    def build(self):
        for j in ['Hearts', 'Diamonds', 'Spades', 'Clubs']:
            for i in range(1, 14):
                self.allcards.append(Card(i, j))

    # shuffles them using the fisher-yates shuffle
    def shuffle(self):
        for i in range(len(self.allcards)-1, 0, -1):
            rand = random.randint(0, i)
            self.allcards[i], self.allcards[rand] = self.allcards[rand], self.allcards[i]

class Player:
    playermat = []
    def __init__(self, name):
        self.name = name
        self.playermat.append(self)
        self.cards = []
        self.playing = 1

    def give_card(self, card):
        self.cards.append(card)

    def read_cards(self):
        for i in range(len(self.cards)):
            self.cards[i].viewcard()

    def read_name(self):
        print(self.name)

    def val(self):
        p = 0
        for k in range(len(self.cards)):
            p += self.cards[k].value
        return p

    def change_playing_status(self):
        self.playing = False


# ------------ starting the game -------------------



def blackjack():

    you = Player('you')

    playerlist = ['The Dealer', 'Edward', 'Joe', 'Tom', 'Allen', 'Howell', 'Ben']

    # taking the correct input
    initial = True
    while initial == True:
        playernum = input('how many players would you like to play against? ')
        if playernum.isnumeric():
            playernum = int(playernum)
            if playernum <= 7 and playernum >= 1:
                playernum = int(playernum) +1
                initial = False
            else:
                print('Please enter a number between 1 and 7')
        else:
            print('Please enter a number between 1 and 7')

    # creating the players as objets
    for i in range(int(playernum - 1)):
        Player(playerlist[i])

    print('you will be playing up against\n')
    for i in range(1, int(playernum)):
        Player.playermat[i].read_name()
    time.sleep(2)

    # creating a deck of cards and shuffles
    deck = Deck()
    deck.shuffle()
    card_number = 0
    print('\n')

    # gives all players two cards
    for j in range(2):
        for i in range(int(playernum)):
            Player.playermat[i].give_card(deck.allcards[j*int(playernum) + i])
            card_number += 1

    print('the dealer has dealt the cards. Leaving you with:','\n')
    Player.playermat[0].read_cards()
    print('\n')

    # GAME LOOP
    playing = True

    while playing == True:
        if Player.playermat[0].playing == 1:

            # taking the stick or twist input
            input_correct = False
            while input_correct == False:
                move = input('Enter "t" for twist or "s" for stick: ')
                if move == "t" or move == "s":
                    input_correct = True
                else:
                    print('Incorrect input... ')

            # gives a new card if you twist
            if move == "t":
                Player.playermat[0].give_card(deck.allcards[card_number])
                card_number += 1
                print('Your cards are now: ')
                Player.playermat[0].read_cards()
                print('\n')

                if Player.playermat[0].val() > 21:
                    print('------YOU HAVE GONE BUST-------\nyou have finished with a total of: ',Player.playermat[0].val(), '\n')
                    Player.playermat[0].change_playing_status()

            # is stuck, changes playing status to False
            if move == 's':
                print('You have finished with a total of: ', Player.playermat[0].val())
                Player.playermat[0].change_playing_status()

        # the other players who are still in all go, twisting if their total is under 17
        for i in range(1,playernum):
            time. sleep(1)
            if Player.playermat[i].playing == 1 and Player.playermat[i].val() < 17:
                Player.playermat[i].give_card(deck.allcards[card_number])
                card_number += 1
                print(Player.playermat[i].name, 'has twisted')

            elif Player.playermat[i].playing == 1 and Player.playermat[i].val() >= 17:
                print(Player.playermat[i].name, 'has stuck')
                Player.playermat[i].change_playing_status()

        # determining if the game is over if there's more than one player playing
        number_playing = 0
        for i in range(playernum):
            if Player.playermat[i].playing == True:
                number_playing += 1
        if number_playing == 0:
            playing = False

    # revealing everyone's cards and final values
    for i in range(1, playernum):
        time.sleep(3)
        print('\n', Player.playermat[i].name,'has the cards:')
        Player.playermat[i].read_cards()
        print('And therefore a total of: ', Player.playermat[i].val(), '\n')

    # finds the highest cards (under 21) and therefore the winning names
    final_scores = []
    for i in range(playernum):
        if Player.playermat[i].val() <= 21:
            final_scores.append(Player.playermat[i].val())
    winning_score = max(final_scores)
    winning_names = []
    for i in range(playernum):
        if Player.playermat[i].val() == winning_score:
            winning_names.append(Player.playermat[i].name)

    # Prints the name of the winner / winners
    if len(winning_names) > 1:
        print(' '.join(winning_names), 'are the winners !')
    elif len(winning_names) == 1 and winning_names[0] == Player.playermat[0].name:
        print(' '.join(winning_names), 'win !')
    elif len(winning_names) == 0:
        print('All players are bust')
    else:
        print(' '.join(winning_names), 'wins !')

blackjack()