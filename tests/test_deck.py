from ultimatni_prirucka.deck import Deck, Card
import pytest
from dataclasses import FrozenInstanceError

from random import shuffle


def test_create_card():
    Card('barva', 'hodnota')


def test_create_deck():
    Deck()


def test_deck_has_52_cards():
    deck = Deck()
    assert len(deck) == 52


def test_can_be_shuffled():
    deck = Deck()
    shuffle(deck)


def test_look_at_card():
    deck = Deck()
    card = deck[0]
    assert card == Card("diamond", "2")


def test_look_at_cards():
    deck = Deck()
    first_three_cards = deck[0:3]


def test_card_is_immutable():
    card = Card("b", "h")
    with pytest.raises(FrozenInstanceError):
        card.colour = "b2"  # TODO: improve