class Rank:
    def __eq__(self, other):
        return self.symbol == other.symbol

    def __str__(self):
        return self.__class__.__name__


class King(Rank):
    symbol = 'K'


class Six(Rank):
    symbol = '6'


class Jack(Rank):
    symbol = 'J'


class Five(Rank):
    symbol = '5'


class Queen(Rank):
    symbol = 'Q'


class Ten(Rank):
    symbol = '10'


class Ace(Rank):
    symbol = 'A'


class Three(Rank):
    symbol = '3'


class Eight(Rank):
    symbol = '8'


class Four(Rank):
    symbol = '4'


class Two(Rank):
    symbol = '2'


class Seven(Rank):
    symbol = '7'


class Nine(Rank):
    symbol = '9'


RANKS = dict(zip(['King', 'Six', 'Jack', 'Five', 'Queen', 'Ten', 'Ace',
                  'Three', 'Eight', 'Four', 'Two', 'Seven', 'Nine'],
                 [King, Six, Jack, Five, Queen, Ten, Ace, Three, Eight,
                  Four, Two, Seven, Nine]))


class Suit:
    def __str__(self):
        return self.__class__.__name__

    def __eq__(self, other):
        return type(self) == type(other)


class Diamonds(Suit):
    color = 'red'


class Hearts(Suit):
    color = 'red'


class Spades(Suit):
    color = 'black'


class Clubs(Suit):
    color = 'black'


SUITS = dict(zip(['Diamonds', 'Hearts', 'Spades', 'Clubs'],
                 [Diamonds, Hearts, Spades, Clubs]))


class Card(Rank, Suit):
    def __init__(self, rank, suit):
        self._rank = rank()
        self._suit = suit()

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return '%s of %s' % (self.rank, self.suit)

    def __repr__(self):
        return '%s of %s' % (self.rank, self.suit)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit


class CardCollection:
    def __init__(self, collection=()):
        self.deck = list(collection)

    def __getitem__(self, index):
        return self.deck[index]

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return str(self.deck)

    def draw(self, index):
        return self.deck.pop(index)

    def draw_from_top(self):
        return self.draw(-1)

    def draw_from_bottom(self):
        return self.draw(0)

    def top_card(self):
        return self.deck[-1]

    def bottom_card(self):
        return self.deck[0]

    def add(self, card):
        self.deck.append(card)

    def index(self, card):
        return self.deck.index(card)


STANDARD_DECK_RANKS = [King, Queen, Jack, Ten, Nine, Eight,
                       Seven, Six, Five, Four, Three, Two, Ace]

BELOTE_DECK_RANKS = [King, Queen, Jack, Ten, Nine, Eight, Seven, Ace]

SIXTY_SIX__DECK_RANKS = [King, Queen, Jack, Ten, Nine, Ace]

DECK_SUITS = [Diamonds, Clubs, Hearts, Spades]


def StandardDeck():
    return CardCollection([Card(rank, suit) for suit in DECK_SUITS
                           for rank in STANDARD_DECK_RANKS])


def BeloteDeck():
    return CardCollection([Card(rank, suit) for suit in DECK_SUITS
                           for rank in BELOTE_DECK_RANKS])


def SixtySixDeck():
    return CardCollection([Card(rank, suit) for suit in DECK_SUITS
                           for rank in SIXTY_SIX__DECK_RANKS])
