# import doctest
import random
from time import sleep


def MINIMUM_BET():
    """Constant function for the numeric value of the minimum possible bet.

    :return: an integer
    """
    return 10


def STARTING_MONEY():
    """Constant function for the numeric value of starting money that Player begins with.

    :return: an integer
    """
    return 100


def FACE_CARD_VALUE():
    """Constant function for the numeric value of face cards.

    :return: an integer
    """
    return 10


def ACE_CARD_VALUE():
    """Constant function for the numeric value of ace cards.

    :return: an integer
    """
    return 11


def DEALER_HIT_LIMIT():
    """Constant function for the numeric value of the dealer's hit limit.

    :return: an integer
    """
    return 14


def BLACKJACK_NUMBER():
    """Constant function for the numeric value of the blackjack number 21.

    :return: an integer
    """
    return 21


class Player:
    """
    This class represents a Player.

    >>> player = Player()
    >>> player.money
    100
    >>> player.wins
    0
    >>> player.losses
    0
    >>> player.draws
    0
    >>> player.hand
    []
    """

    def __init__(self):
        """
        Create an instance of the Player class.
        """
        self.money = STARTING_MONEY()
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.hand = []

    def __str__(self):
        """Provide an informal description of this Player object with the information currently stored.

        :return: a string of the information currently stored in this Player object

        >>> player = Player()
        >>> print(player)
        This Player has $100, won 0 games, lost 0 games, ended 0 games in a draw, and currently has these [] cards \
in their hand.
        """
        return f"This Player has ${self.money}, won {self.wins} games, lost {self.losses} games, ended {self.draws} " \
               f"games in a draw, and currently has these {self.hand} cards in their hand."

    def __repr__(self):
        """Provide the information currently stored in this Player object.

        :return: a string of information about this Player object

        >>> player = Player()
        >>> player
        Player(100, 0, 0, 0, [])
        """
        return f"Player({self.money}, {self.wins}, {self.losses}, {self.draws}, {self.hand})"

    def print_hand(self) -> None:
        """Print the names of the cards the Player currently has in their hand.

        :precondition: Player's hand attribute must be a list of Card class objects
        :postcondition: prints the correct name of cards currently in the player's hand
        :return: None

        >>> player = Player()
        >>> player.hand = [Card('5', 'Spades'), Card('Ace', 'Clubs')]
        >>> player.print_hand()
        Player's Hand: 5 of Spades, Ace of Clubs.
        """
        print("Player's Hand: ", end='')
        for card in self.hand:
            if card == self.hand[-1]:
                print(f"{card.name}.")
            else:
                print(f"{card.name}, ", end='')


class Dealer:
    """
    This class represents a Dealer.

    >>> dealer = Dealer()
    >>> dealer.hand
    []
    """

    def __init__(self):
        """
        Create an instance of the Dealer class.
        """
        self.hand = []

    def __str__(self):
        """Provide an informal description of this Dealer object with the information currently stored.

        :return: a string of the information currently stored in this Dealer object

        >>> dealer = Dealer()
        >>> print(dealer)
        This Dealer currently has a hand of [].
        """
        return f"This Dealer currently has a hand of {self.hand}."

    def __repr__(self):
        """Provide the information currently stored in this Dealer object.

        :return: a string with the information currently stored in this Dealer object

        >>> dealer = Dealer()
        >>> dealer
        Dealer([])
        """
        return f"Dealer({self.hand})"

    def print_hand(self) -> None:
        """Print the names of the cards the Dealer currently has in their hand.

        :precondition: Dealer's hand attribute must be a list of Card class objects
        :postcondition: prints the correct name of cards currently in the dealer's hand
        :return: None

        >>> dealer = Dealer()
        >>> dealer.hand = [Card('8', 'Hearts'), Card('King', 'Diamonds')]
        >>> dealer.print_hand()
        Dealer's Hand: 8 of Hearts, King of Diamonds.
        """
        print("Dealer's Hand: ", end='')
        for card in self.hand:
            if card == self.hand[-1]:
                print(f"{card.name}.")
            else:
                print(f"{card.name}, ", end='')


class Card:
    """
    This class represents a Card.

    >>> card = Card('5', 'Spades')
    >>> card.value
    5
    >>> card.name
    '5 of Spades'
    >>> card = Card('Ace', 'Hearts')
    >>> card.value
    11
    >>> card.name
    'Ace of Hearts'
    >>> card = Card('King', 'Diamonds')
    >>> card.value
    10
    >>> card.name
    'King of Diamonds'
    """

    def __init__(self, value: str, suit: str):
        """Create an instance of the Card class.

        :param value: a string
        :param suit: a string
        :precondition: value must be a string of an integer in range [2,10] or 'Jack' or 'Queen' or 'King' or 'Ace'
        :precondition: suit must be a string of 'Spades' or 'Hearts' or 'Diamonds' or 'Clubs'
        :postcondition: correctly instantiates a Card object
        """
        if value in ['Jack', 'Queen', 'King']:
            self.value = FACE_CARD_VALUE()
        elif value == 'Ace':
            self.value = ACE_CARD_VALUE()
        else:
            self.value = int(value)
        self.name = f"{value} of {suit}"

    def __str__(self):
        """Provide an informal description of this Card object with the information currently stored.

        :return: a string of the information currently stored in this Card object

        >>> card = Card('5', 'Spades')
        >>> print(card)
        A 5 of Spades card with a value of 5.
        """
        return f"A {self.name} card with a value of {self.value}."

    def __repr__(self):
        """Provide the information currently stored in this Card object.

        :return: a string with the information currently stored in this Card object

        >>> card = Card('5', 'Spades')
        >>> card
        Card(5, '5 of Spades')
        """
        return f"Card({self.value}, '{self.name}')"


def create_shuffled_deck() -> list:
    """Create a shuffled deck of 52 traditional playing cards.

    :precondition: Card class must be in module
    :postcondition: creates a shuffled deck of 52 playing cards made up of Card class objects
    :return: a list
    """
    deck = [Card(value, suit) for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']
            for value in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']]
    random.shuffle(deck)
    return deck


def get_player_bet(player: Player) -> int:
    """Ask user for input on how much they want to bet in this round of Blackjack.

    :param player: an instance of the Player class
    :precondition: player must be an instance of the Player class
    :postcondition: successfully gets the user's desired bet amount
    :raises ValueError: if player.money is lower than the minimum possible bet
    :return: an integer
    """
    if player.money < MINIMUM_BET():
        raise ValueError
    print(f"Dealer: Alright, you currently have ${player.money}."
          f"\nDealer: Feeling lucky? How much ya wanna bet this round?")
    desired_bet = False
    while not validate_desired_bet(desired_bet, player.money):
        desired_bet = input(f"(Enter a whole number between {MINIMUM_BET()} and {player.money})"
                            f"\nPlayer: ")
    return int(desired_bet)


def validate_desired_bet(bet: str, max_bet: int) -> bool:
    """Evaluate whether bet is a valid number between the minimum possible bet and max_bet.

    :param bet: a string
    :param max_bet: an integer
    :precondition: bet must be a string
    :precondition: max_bet must be an integer
    :postcondition: correctly evaluates whether bet is a valid choice
    :return: True or False

    >>> validate_desired_bet('15', 30)
    True
    >>> validate_desired_bet('5', 50)
    False
    >>> validate_desired_bet('101', 100)
    False
    """
    return True if bet in [f"{num}" for num in range(MINIMUM_BET(), max_bet + 1)] else False


def blackjack_round(player: Player, dealer: Dealer, deck: list) -> str:
    """Play one round of Blackjack.

    :param player: an instance of the Player class
    :param dealer: an instance of the Dealer class
    :param deck: a list of Card objects
    :precondition: player must be an instance of the Player class
    :precondition: dealer must be an instance of the Dealer class
    :precondition: deck must be a list of Card objects
    :postcondition: correctly carries out a round of Blackjack
    :return: a string
    """
    initial_deal(player, dealer, deck)
    deal_cards_for_dealer(dealer, deck)
    dealer_hand_value = add_card_values(dealer.hand)
    if dealer_hand_value > BLACKJACK_NUMBER():
        return 'win'
    deal_cards_for_player(player, dealer, deck)
    player_hand_value = add_card_values(player.hand)
    if player_hand_value > BLACKJACK_NUMBER():
        return 'lose'
    if player_hand_value > dealer_hand_value:
        return 'win'
    elif player_hand_value < dealer_hand_value:
        return 'lose'
    else:
        return 'draw'


def initial_deal(player: Player, dealer: Dealer, deck: list) -> None:
    """Create a hand of two cards for beginning of blackjack round.

    :param player: an instance of the Player class
    :param dealer: an instance of the Dealer class
    :param deck: a list of Card objects
    :precondition: deck must be a list of Card objects
    :precondition: player must be an instance of the Player class
    :precondition: dealer must be an instance of the Dealer class
    :postcondition: adds 2 cards from the top of the deck to the dealer's and player's hands
    :return: None

    >>> test_dealer = Dealer()
    >>> test_player = Player()
    >>> test_deck = [Card('5', 'Spades'), Card('6', 'Spades'), Card('7', 'Spades'), Card('8', 'Spades')]
    >>> initial_deal(test_player, test_dealer, test_deck)
    <BLANKLINE>
    Dealer: Let's begin. I will now deal us both two cards.
    Dealer's Hand: 5 of Spades, 7 of Spades.
    Dealer's Hand Value: 12
    Player's Hand: 6 of Spades, 8 of Spades.
    Player's Hand Value: 14
    """
    print("\nDealer: Let's begin. I will now deal us both two cards.")
    sleep(2)
    for num in range(2):
        dealer.hand.append(deck.pop(0))
        player.hand.append(deck.pop(0))
    dealer.print_hand()
    print(f"Dealer's Hand Value: {add_card_values(dealer.hand)}")
    player.print_hand()
    print(f"Player's Hand Value: {add_card_values(player.hand)}")
    sleep(2)


def deal_cards_for_dealer(dealer: Dealer, deck: list) -> None:
    """Deal cards into dealer's hand until dealer's hand value meets the hit limit.

    :param dealer: an instance of the Dealer class
    :param deck: a list of Card objects
    :precondition: dealer must be an instance of the Dealer class
    :precondition: deck must be a list of Card objects
    :postcondition: correctly adds cards to dealer's hand until the hand value meets the hit limit
    :return: None

    >>> test_dealer = Dealer()
    >>> test_dealer.hand = [Card('King', 'Hearts'), Card('2', 'Diamonds')]
    >>> test_deck = [Card('5', 'Spades'), Card('6', 'Spades'), Card('7', 'Spades'), Card('8', 'Spades')]
    >>> deal_cards_for_dealer(test_dealer, test_deck)
    <BLANKLINE>
    Dealer: Alright, my turn.
    Dealer: My hand total is 12.
    Dealer: I draw a 5 of Spades, my hand now totals 17.
    Dealer's Hand: King of Hearts, 2 of Diamonds, 5 of Spades.
    Dealer: I will stand with a total of 17.
    """
    hand_value = add_card_values(dealer.hand)
    print(f"\nDealer: Alright, my turn."
          f"\nDealer: My hand total is {hand_value}.")
    while hand_value <= DEALER_HIT_LIMIT():
        dealt_card = deck.pop(0)
        dealer.hand.append(dealt_card)
        hand_value = add_card_values(dealer.hand)
        print(f"Dealer: I draw a {dealt_card.name}, my hand now totals {hand_value}.")
        dealer.print_hand()
        sleep(2)
    print(f"Dealer: I will stand with a total of {hand_value}.")
    sleep(2)


def deal_cards_for_player(player: Player, dealer: Dealer, deck: list) -> None:
    """Deal card into the player's hand until they bust or the user decides to stand.

    :param player: an instance of the Player class
    :param dealer: an instance of the Dealer class
    :param deck: a list of Card objects
    :precondition: player must be an instance of the Player class
    :precondition: dealer must be an instance of the Dealer class
    :precondition: deck must be a list of Card objects
    :postcondition: correctly adds cards to player's hand until they bust or user decides to stand
    :return: None
    """
    players_turn = True
    while players_turn:
        player_hand_value = add_card_values(player.hand)
        if player_hand_value < BLACKJACK_NUMBER():
            if get_user_choice(player, dealer) == '1':
                dealt_card = deck.pop(0)
                player.hand.append(dealt_card)
                player_hand_value = add_card_values(player.hand)
                print(f"\nDealer: You draw a {dealt_card.name}, your hand now totals {player_hand_value}.")
                player.print_hand()
                sleep(1)
            else:
                players_turn = False
        else:
            players_turn = False


def add_card_values(hand: list) -> int:
    """Sum the the values of the Card objects in the hand list.

    :param hand: a list of Card objects
    :precondition: hand must be a list of Card objects
    :postcondition: sums the value of all cards in the hand and returns the integer
    :return: an integer

    >>> test_hand = [Card('5', 'Spades'), Card('6', 'Spades')]
    >>> add_card_values(test_hand)
    11
    """
    card_total = 0
    ace_in_hand = False
    for card in hand:
        if card.value == ACE_CARD_VALUE():
            ace_in_hand = True
        card_total += card.value
    if ace_in_hand and card_total > BLACKJACK_NUMBER():
        card_total -= 10
    return card_total


def get_user_choice(player: Player, dealer: Dealer) -> str:
    """Ask user for input to decide to hit or stand.

    :param player: an instance of the Player class
    :param dealer: an instance of the Dealer class
    :precondition: player must be an instance of the Player class
    :precondition: dealer must be an instance of the Dealer class
    :postcondition: successfully gets the user input to hit or stand
    :return: a string
    """
    choice = False
    while not validate_user_choice(choice):
        print(f"\nDealer: What would you like to do?")
        print(f"Dealer's Hand Value: {add_card_values(dealer.hand)}")
        player.print_hand()
        print(f"Player's Hand Value: {add_card_values(player.hand)}")
        for num, option in enumerate(['Hit', 'Stand'], 1):
            print(f"{num} - {option}")
        choice = input('\nPlease enter the number corresponding to your choice here: ')
    return choice


def validate_user_choice(choice: str) -> bool:
    """Evaluate if user's input is a valid choice.

    :param choice: a string
    :precondition: choice must be a string
    :postcondition: correctly evaluates if choice is a valid decision
    :return: True or False

    >>> validate_user_choice('1')
    True
    >>> validate_user_choice('2')
    True
    """
    return True if choice in [f"{num}" for num, option in enumerate(['Hit', 'Stand'], 1)] else False


def evaluate_round_result(player: Player, bet: int, round_result: str) -> None:
    """Allocate score and bet correctly depending on round_result.

    :param player: an instance of the Player class
    :param bet: an integer
    :param round_result: a string
    :precondition: player must be an instance of the Player class
    :precondition: bet must be an integer
    :precondition: round_result must be a string of 'win' or 'lose' or 'draw'
    :postcondition: evaluate outcome of the round to allocate score and bet correctly
    :return: None

    >>> evaluate_round_result(Player(), 20, 'win')
    <BLANKLINE>
    Dealer: You win that one. You countin' cards or something?
    <BLANKLINE>
    >>> evaluate_round_result(Player(), 20, 'lose')
    <BLANKLINE>
    Dealer: I win that round. Better luck next time, kiddo.
    <BLANKLINE>
    >>> evaluate_round_result(Player(), 20, 'draw')
    <BLANKLINE>
    Dealer: That round is a draw. Keep your wager.
    <BLANKLINE>
    """
    if round_result == 'win':
        print("\nDealer: You win that one. You countin' cards or something?\n")
        player.money += (bet * 2)
        player.wins += 1
    elif round_result == 'lose':
        print("\nDealer: I win that round. Better luck next time, kiddo.\n")
        player.money -= bet
        player.losses += 1
    elif round_result == 'draw':
        print("\nDealer: That round is a draw. Keep your wager.\n")
        player.draws += 1


def blackjack():
    """
    Play a game of Blackjack with a deck of 52 traditional playing cards.
    """
    deck = create_shuffled_deck()
    player = Player()
    dealer = Dealer()
    print("Dealer: Saddle on up cowboy, let's play some blackjack.\n")
    while len(deck) > 0:
        try:
            bet = get_player_bet(player)
            round_result = blackjack_round(player, dealer, deck)
        except IndexError:
            print("\nDealer: We're outta cards. That's it for today.")
        except ValueError:
            print("\nDealer: Alright, this is just sad. Time for you to go home.")
            break
        else:
            evaluate_round_result(player, bet, round_result)
        finally:
            player.hand = []
            dealer.hand = []
    print(f"\nPlayer: Whew, what a day at the casino!"
          f"\nPlayer: I won {player.wins} rounds, lost {player.losses}, and {player.draws} rounds ended in a draw."
          f"\nPlayer: And I'm leaving with ${player.money} in my pocket!")


def main():
    """
    Drive the program.
    """
    blackjack()
    # doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()
