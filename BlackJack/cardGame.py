import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
        	deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
    	#card passes in is from card class deal method
    	#i.e Deck.deal() --> 
    	#single Card(suit, rank)
        self.cards.append(card)
        self.value += values[card.rank]

        #track aces
        if card.rank == 'Ace':
        	self.aces += 1
    
    def adjust_for_ace(self):

    	#if total value > 21 and I still have an ace
    	#than change my ace to be a 1 instead of an 11
    	# self.aces or self.aces > 0
        while self.value > 21 and self.aces > 0:
        	self.value -= 10
        	self.aces -= 1


class Chips:
    
    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
	
	while True:
		try:
			chips.bet = int(raw_input("How many chips would you like to bet? "))
		except:
			print("Sorry please provide an integer!")
		else:
			if chips.bet > chips.total:
				print("Sorry you do not have enough chips! You have : {}".format(chips.total))
			else:
				break


def hit(deck,hand):
	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_ace()


def hit_or_stand(deck,hand):
	gloabl playing #to control an upcoming while loop

	while True:
		x = raw_input("Hit or Stand? Enter h or s") #HIT #hh #stand

		if x[0].lower == 'h':
			hit(deck,hand)
		elif c[0].lower() == 's':
			print("Player Stands Dealer's Turn")
			playing = False
		else:
			print("Sorry, I did not understand the input. Please enter valid input.")


def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and player tie! PUSH")




while True:
	# print an openinf statement

	print("Welcome to BLACKJACK")

	# Create & shuffle the deck, deal two cards for each player
	deck.Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand = add_card(deck.deal())
	dealer_hand = add_card(deck.deal())

	# set up the Player's chips
	player_chips = Chips()

	# prompt the player for their bet
	take_bet(player_chips)

	# show cards (but keep one dealer card hidden)
	show_some(player_hand,dealer_hand)

	while playing: # recall this variable from our hit_or_stand function

		# prompt for player to hit or stand
		hit_or_stand(deck,player_hand)

		# show cards (but keep one dealer card hidden)
		show_some(player_hand,dealer_hand)

		# if player's hand exceeds 21, run player_busts() and break out of loop
		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)

			break

	# ifplayer's hasn't bursted, play Dealer's hand until Dealer reaches 17
	if player_hand.value <= 21:

		# dealer_hand.value < player_hand.value or dealer_hand.value < 17
		while dealer_hand.value < 17:
			hit(deck,dealer_hand)

        # Show all cards
		show_all(player_hand,dealer_hand)

		# run different winning scenarios:
		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_busts(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)
		else:
			push(player_hand,dealer_hand)

	# inform player of their chips total
	print("\nPlayer total chips are at : {}".format(player_chips.total))

	# ask to play again
	new_game = raw_input("Would you like to play another hand? y/n ")

	if new_game[0].lower() == 'y':
		playing = True
		continue
	else:
		print("Thank you for playing!")
		break

