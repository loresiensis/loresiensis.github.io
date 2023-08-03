import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
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
        return 'The deck has: '+ deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
    
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card) #card is going to be dealed 
        self.value += values[card.rank]
        
        #Track aces
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces: #while <21 and I still have an ace! 
            self.value -= 10
            self.aces -= 1
            

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips): #Cuando uses una función normalmente querras pasar un argumento, aquí vamos a pasar chips que es
                     #la clase que hemos creado antes, y que tiene los atributos bet y total que vamos a usar ahora
        
    while True:
        
        try:
            chips.bet = int(input('Place your bet: '))
        except:
            print('Oops, please enter a number')
        else:
            if chips.bet > chips.total:
                print(f'Oops, you dont have enough chips. You have: {chips.total}')
            else:
                break

def hit(deck,hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input('Would you like to Hit or Stand? Enter Hit or Stand: ')
        
        if x.lower() == 'hit':
            hit(deck,hand)
            print("You chose to hit!")
        elif x.lower() == 'stand':
            print("Player Stands! Dealer's Turn")
            playing = False
        else:
            print("Sorry, I don't understand. Please type Hit or Stand")
            
        break

def show_some(player,dealer):
    #Show only one of the dealer's cards
    print("\nDEALER'S HAND: ")
    print("One card hidden")
    print(f"Second card is: {dealer.cards[1]}")
    #Show all of the player's cards
    print("\nPLAYER'S HAND: ")
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):
    
    #Show all the dealer's cards
    print("\nDEALER'S HAND: ")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's Hand is: {dealer.value}")
    
    #Show all of the player's cards
    print("\nPLAYER's HAND: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's Hand is: {player.value}")

def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS! DEALER BUSTED")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("DEALER WINS! PLAYER BUSTED")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie!")

while True:
    # Print an opening statement
    
    print("Welcome to Blackjack!")

    
    # Create & shuffle the deck, deal two cards to each player
    
    bj_deck = Deck()
    bj_deck.shuffle()
    
    
    dealer_hand = Hand()
    dealer_hand.add_card(bj_deck.deal())
    dealer_hand.add_card(bj_deck.deal())
    
    player_hand = Hand()
    player_hand.add_card(bj_deck.deal())
    player_hand.add_card(bj_deck.deal())
    
        
    # Set up the Player's chips
    
    player_chips = Chips()
    print(f"You start with 100 chips")
    
    
    # Prompt the Player for their bet
    
    take_bet(player_chips)

    
    # Show cards (but keep one dealer card hidden)
    
    show_some(player_hand,dealer_hand)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        
        hit_or_stand(bj_deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        
        show_some(player_hand,dealer_hand)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(bj_deck,dealer_hand)
    
        # Show all cards
        
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    
    # Inform Player of their chips total
    
    print(f"\nPlayer's Total Chips are at: {player_chips.total}")
    
    # Ask to play again
    
    replay_choice = input('Play again? (Yes or No): ')
        
    if replay_choice.lower() == 'yes':
        playing = True
    else:
        print('Oh, okay :( maybe next time. Thank you for playing!')
        break

