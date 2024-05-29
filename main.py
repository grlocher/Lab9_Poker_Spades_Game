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

def check_straight(card1, card2, card3):
    card_order = ([card_values[card1], card_values[card2], card_values[card3]])
    card_order.sort()
    if card_order[1] == card_order[0] + 1 and card_order[2] == card_order[1] + 1:
       return max(card_order)
    else:
        return 0


def check_3ofa_kind(card1, card2, card3):
    card_order = ([card_values[card1], card_values[card2], card_values[card3]])
    if card_order[0] == card_order[1] and card_order[0] == card_order[2]:
        return card_order[0]
    else:
        return 0


def check_royal_flush(card1, card2, card3):
    card_order = ([card_values[card1], card_values[card2], card_values[card3]])
    card_order.sort()
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0


def play_cards(left1, left2, left3, right1, right2, right3):
    # Types of hands
    left_hand_straight = check_straight(left1, left2, left3)
    left_hand_3ofa_kind = check_3ofa_kind(left1, left2, left3)
    left_hand_royal_flush = check_royal_flush(left1, left2, left3)

    right_hand_straight = check_straight(right1, right2, right3)
    right_hand_3ofa_kind = check_3ofa_kind(right1, right2, right3)
    right_hand_royal_flush = check_royal_flush(right1, right2, right3)

    # Straight
    if left_hand_straight and right_hand_straight:
        if left_hand_straight > right_hand_straight:
            return -1
        elif left_hand_straight < right_hand_straight:
            return 1
        else:
            return 0
    elif left_hand_straight and not right_hand_straight:
        return -1
    elif not left_hand_straight and right_hand_straight:
        return 1

    # 3 of a kind
    elif left_hand_3ofa_kind and right_hand_3ofa_kind:
        if left_hand_3ofa_kind > right_hand_3ofa_kind:
            return -1
        elif left_hand_3ofa_kind < right_hand_3ofa_kind:
            return 1
        else:
            return 0
    elif left_hand_3ofa_kind and not right_hand_3ofa_kind:
        return -1
    elif not left_hand_3ofa_kind and right_hand_3ofa_kind:
        return 1

    # Royal Flush
    elif left_hand_royal_flush and not right_hand_royal_flush:
        return -1
    elif not left_hand_royal_flush and right_hand_royal_flush:
        return 1
    else:
        return 0
