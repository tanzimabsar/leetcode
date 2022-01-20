#!/usr/bin/env python3.9.9

import unittest
import logging, sys
from src import highscoringwords

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)


class TestHighScoringWords(unittest.TestCase):
    def setUp(self):
        self.leaderboard = highscoringwords.HighScoringWords(
            "data/sample_wordlist.txt", "data/letterValues.txt"
        )
        logger.addHandler(stream_handler)

    def test_raise_assert_if_files_not_found(self):
        leaderboard = highscoringwords.HighScoringWords(
            "data/sample_wordlist.txt", "data/letterValues.txt"
        )
        self.assertRaises(FileNotFoundError)

    def test_highest_scoring_words_leaderboard(self):
        logger.info("Added Logger!")
        word_list = self.leaderboard.valid_words
        self.assertEquals(
            self.leaderboard.build_leaderboard_for_word_list(word_list=word_list),
            [
                "aardvarks",
                "aardwolves",
                "aardvark",
                "aardwolf",
                "aarrghh",
                "aasvogels",
                "aasvogel",
                "aahing",
                "aarrgh",
                "aahed",
                "aargh",
                "aahs",
                "aah",
                "aaliis",
                "aalii",
                "aals",
                "aal",
                "aas",
                "aa",
            ],
        )

        """
        
        """

    def test_create_leaderboard_for_letters(self):
        """
        Behavioural test for creating a leaderboard from
        a random set of characters

        This should return a list of valid words in the order of scores
        """
        leaderboard = highscoringwords.HighScoringWords(
            "data/wordlist.txt", "data/letterValues.txt"
        )
        list_of_results, scores = leaderboard.build_leaderboard_for_letters(
            "bulx"
        )

        self.assertNotIn("bull", list_of_results)

        list_of_results, scores = leaderboard.build_leaderboard_for_letters(
            "deora"
        )

        self.assertNotIn("derazs", list_of_results)
        self.assertIn("read", list_of_results)

    def test_ordering_of_leader_board(self):
        leaderboard = highscoringwords.HighScoringWords(
            "data/sample_wordlist.txt", "data/letterValues.txt"
        )
        leaderboard, scores = leaderboard.build_leaderboard_for_word_list()
        self.assertEquals(scores[0], ('aardwolves', 17))

    def tearDown(self):
        logger.removeHandler(stream_handler)
