import unittest
from main import check_straight, check_3ofa_kind, check_royal_flush, play_cards


class TestPokerSpadesGame(unittest.TestCase):
    def test_check_straight(self):
        self.assertEqual(check_straight('S2', 'S3', 'S4'), 4)  # Checking sequential
        self.assertEqual(check_straight('S5', 'S6', 'S7'), 7)  # Checking another sequential
        self.assertEqual(check_straight('S10', 'SJ', 'SQ'), 12)  # Checking another sequential
        self.assertEqual(check_straight('S10', 'S5', 'S6'), 0)  # Checking non-straight
        self.assertEqual(check_straight('S7', 'S9', 'S8'), 9)  # Checking non-ordered straight

    def test_check_3ofa_kind(self):
        self.assertEqual(check_3ofa_kind('S9', 'S9', 'S9'), 9)  # Checking three of a kind
        self.assertEqual(check_3ofa_kind('SA', 'SA', 'SA'), 14)  # Checking Ace three of a kind
        self.assertEqual(check_3ofa_kind('S8', 'S10', 'S10'), 0)  # Checking non-three of a kind
        self.assertEqual(check_3ofa_kind('S2', 'S3', 'S6'), 0)  # Checking non-three of a kind

    def test_check_royal_flush(self):
        self.assertEqual(check_royal_flush('SQ', 'SK', 'SA'), 14)  # Checking royal flush
        self.assertEqual(check_royal_flush('SA', 'SK', 'SQ'), 14)  # Checking royal flush, non-sequential
        self.assertEqual(check_royal_flush('SA', 'SK', 'SA'), 0)  # Checking non-royal flush with royals
        self.assertEqual(check_royal_flush('S2', 'S3', 'S4'), 0)  # Checking sequential straight

    def test_play_cards(self):
        # Straight
        self.assertEqual(play_cards('S10', 'SJ', 'SQ', 'S8', 'S9', 'S10'), -1)  # Left winner
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S6', 'S7', 'S8'), 1)  # Right winner
        self.assertEqual(play_cards('S10', 'SJ', 'SQ', 'S10', 'SJ', 'SQ'), 0) # Draw

        # 3 of a Kind
        self.assertEqual(play_cards('S9', 'S9', 'S9', 'S8', 'S8', 'S8'), -1) # Left wins
        self.assertEqual(play_cards('S9', 'S9', 'S9', 'SA', 'SA', 'SA'), 1) # Right winner

        # Royal Flush
        self.assertEqual(play_cards('SA', 'SK', 'SQ', 'S9', 'S10', 'SJ'), -1)  # Left winner
        self.assertEqual(play_cards('S9', 'S10', 'SJ', 'SA', 'SK', 'SQ'), 1)  # Right winner
        self.assertEqual(play_cards('SA', 'SK', 'SQ', 'SK', 'SQ', 'SA'), 0)  # Draw


if __name__ == '__main__':
    unittest.main()