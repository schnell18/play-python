#!/usr/bin/env python

from random import choice
from random import shuffle

coin = choice(["heads", "tails"])
print(coin)

cards = ["jack", "queen", "king"]
print(cards)
shuffle(cards)
print(cards)
