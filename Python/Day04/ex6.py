#!/usr/bin/python  
# -*- coding: utf-8 -*-
from random import randrange

class Card(object):
    """牌"""

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def suite(self):
        return self._suite

    @suite.setter
    def suite(self, suite):
        self._suite = suite

    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, face):
        self._face = face
    
    def __str__(self):
        all_suites = ('♠', '♥', '♣', '♦')
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s %s' % (all_suites[self._suite], face_str)
    
class Pocker(object):
    """一副牌"""

    def __init__(self):
        self._cards = []
        self._current = 0
        for suit in range(4):
            for face in range(1, 14):
                card = Card(suit, face)
                self._cards.append(card)
    
    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌"""
        self._current = 0
        cards_len = len(self._cards)
        for index in range(cards_len):
            pos = randrange(cards_len)
            self._cards[index], self._cards[pos] = \
                self._cards[pos], self._cards[index]
    
    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    def has_next(self):
        return self._current < len(self._cards)

class Player(object):
    """玩家"""

    def __init__(self, name):
        self._name = name
        self._cards_in_hand = []

    @property
    def name(self):
        return self._name
    
    @property
    def cards_in_hand(self):
        return self._cards_in_hand

    def want(self, card):
        self._cards_in_hand.append(card)
    
    def collate(self, collate_key):
        self._cards_in_hand.sort(key = collate_key)
    
def get_key(card):
    return (card.suite, card.face)

def main():
    p = Pocker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.want(p.next)
    for player in players:
        print(player.name + ':', end=' ')
        player.collate(get_key)
        for card in player.cards_in_hand:
            print(card, end=' ')
        print()

if __name__ == '__main__':
    main()