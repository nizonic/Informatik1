#!/usr/bin/env python3

import random
import difflib

class WordLogic(object):

    def __init__(self, num_words, len_words):
        self.num_words = num_words
        self.len_words = len_words

    def find_words_with_right_size(self):
        with open("resource/words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def word_selection(self):
        #words = self.find_words_with_right_size()
        #random.shuffle(words)
        words = []
        with open("words.txt") as f:
            word_list = f.read().splitlines()
            words.append(random.choices(word_list, k = self.num_words // 3))
            boss = random.choice(words)
            while True:
                word = random.choice(word_list)
                if word not in words and self.is_similar(boss, word, 0.4):
                    words.append(word)
                    if len(words) == self.num_words:
                        break
            return words


        # TODO: instead of returning a random sample of words, use the strategy described in task 2


    def is_similar(self, a, b, threshold):
        return difflib.SequenceMatcher(None, a, b).ratio() > threshold


if __name__ == "__main__":
    g = WordLogic(5, 5)
    print(g.is_similar("babui", "bababui", 0.8))
    print(g.word_selection())