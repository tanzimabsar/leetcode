#!/usr/bin/env python3.9.9

__author__ = "Tanzim Absar"

from tracemalloc import start
from typing import List
import operator
from itertools import permutations

from cairo import FillRule


class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = (
        100  # the maximum number of items that can appear in the leaderboard
    )
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(
        self, validwords: str = "wordlist.txt", lettervalues: str = "letterValues.txt"
    ):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """

        try:
            with open(validwords) as f:
                self.valid_words = f.read().splitlines()

            with open(lettervalues) as f:
                for line in f:
                    (key, val) = line.split(":")
                    self.letter_values[str(key).strip().lower()] = int(val)
        except FileNotFoundError as e:
            raise (FileNotFoundError, "Please make sure both input files exist")

    def build_leaderboard_for_word_list(self, word_list) -> List:
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.

        Returned list of words are only top MAX_LEADERBOARD_LENGTH (100)
        :return: The list of top words.
        """

        leaderboard = {}

        for word in word_list:
            leaderboard[word] = 0
            for letter in word:
                # letter values will be constant
                leaderboard[word] += self.letter_values[letter]

        results = sorted(leaderboard.items(), key=operator.itemgetter(1), reverse=True)
        return [i[0] for i in results][: self.MAX_LEADERBOARD_LENGTH]

    def _sort_leaderboard(self, leaderboard):
        """
        Sorts the word-score dictionary in reverse order of score.
        Words of equal scores are sorted alphabetically.
        """
        return sorted(leaderboard.items(), key=operator.itemgetter(1), reverse=True)

    def build_leaderboard_for_letters(
        self, starting_letters: str, word_list: List
    ) -> List:
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words
        that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant.
        If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.
        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return: The list of top buildable words.
        """
        from itertools import permutations

        # filter the word list to search through some of them
        filtered_word_list = [x for x in word_list if len(x) <= len(starting_letters)]

        # create a list of combinations of letters, order matters
        all_permutations = [''.join(p) for p in permutations(starting_letters)]

        results = []

        for possible_match in all_permutations:
            for index, value in enumerate(possible_match):
                substring = possible_match[index: len(possible_match)]
                if substring in filtered_word_list:
                    results.append(substring)

        return results