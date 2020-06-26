class Card:
    """ Este metodo crea cartas españolas. Se inicializa con Card(suit, rank) integers"""
    
    suits = ["Clubs", "Diamonds", "Hearts", "Clubs"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6",
             "7", "8", "9", "10", "Jack", "Queen", "King"]
    
    def __init__(self, suit = 0, rank = 0):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])
    
    def cmp(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank:
            #if self.rank == 13 and other.rank == 1:  ##Ativar cuando Ace sea mayor
                #return -1
            return 1
        if self.rank < other.rank:
           # if self.rank == 13 and other.rank == 1:  ##Ativar cuando Ace sea mayor
                #return 1
            return -1
        return 0
    
    def __eq__(self, other):
        return self.cmp(other) == 0
    
    def __le__(self, other):
        return self.cmp(other) <= 0
    
    def __ge__(self, other):
        return self.cmp(other) >= 0
    
    def __lt__(self, other):
        return self.cmp(other) < 0
    
    def __gt__(self, other):
        return self.cmp(other) > 0
    
    def __ne__(self, other):
        return self.cmp(other) != 0
#*******************************End of the class Cards*************************************************

class Deck:
    """ Crea un Deck de 52 cartas, no necesita parámetros """
    
    def __init__(self):
        self.cards = [Card(suit, rank) 
                      for suit in range(4) 
                      for rank in range(1, 14)]
        
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i +  str(self.cards[i]) + "\n"
            #end for
        return s
    
    def shuffle(self):
        import random
        rng = random.Random()
        rng.shuffle(self.cards)
            #end for
        #end function shuffle
        
    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        return False
    
    def pop(self):
        return self.cards.pop()
    
    def is_empty(self):
        return self.cards == []    
    
    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break
            card = self.pop()
            hand = hands[i % num_hands]
            hand.add(card)