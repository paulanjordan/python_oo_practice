"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """ It is instantiated with a path to a file on disk that contains words, one word per line.
    It reads that file, and makes an attribute of a list of those words.
    it prints out “[num-of-words-read] words read”"""

    def __init__ (self, text_file_path):
        self.text_file_path = text_file_path

    def __repr__(self):
        return f"Selecting word from {self.text_file_path}"

    def random(self):
        """returns a random work from the list of words"""
        f = open(f"{self.text_file_path}", "r")
        lines = f.readlines()
        return random.choice(lines).replace('\n', '')


class SpecialWordFinder(WordFinder):
    """Uses WordFinder, but does not return blank lines or comment lines"""

        def random(self):
        """returns a random work from the list of words"""
        f = open(f"{self.text_file_path}", "r")
        lines = f.readlines()
        if not random.choice(lines).startswith("#") and not random.choice(lines).startswith(" "):
            return random.choice(lines).replace('\n', '')
