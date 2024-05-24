import random as rnd
import math

cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')
card_values = {
    'S2': 2,
    'S3': 3,
    'S4': 4,
    'S5': 5,
    'S6': 6,
    'S7': 7,
    'S8': 8,
    'S9': 9,
    'S10': 10,
    'SJ': 11,
    'SQ': 12,
    'SK': 13,
    'SA': 14
}

card1 = rnd.choice(cards)
card2 = rnd.choice(cards)
card3 = rnd.choice(cards)

card_order = ([card_values[card1], card_values[card2], card_values[card3]])


def check_straight(card1, card2, card3):
    card_order.sort()
    if card_order[1] == card_order[0] + 1 and card_order[2] == card_order[1] + 1:
       return card_order[2]
    else:
        return 0


def check_3ofa_kind(card1, card2, card3):
    if card_order[0] == card_order[1] and card_order[0] == card_order[2]:
        return card_order[0]
    else:
        return 0


def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0


# def play_cards(left1, left2, left3, right1, right2, right3):
#     if left_total > right_total:
#         return -1
#     elif left_total == right_total:
#         return 0
#     elif left_total < right_total:
#         return 1
