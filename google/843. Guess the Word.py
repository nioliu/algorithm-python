# https://leetcode.com/problems/guess-the-word/description/?envType=study-plan-v2&envId=google-spring-23-high-frequency
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
from typing import List


class Master:
    def guess(self, word: str) -> int:
        return -1


class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        """
        简而言之，就是在words里面找到secret, master.guess会自动输出结果，如果找到了就直接跳出即可
        :param words:
        :param master:
        :return:
        """
        index = 0
        while index < len(words):
            i = words[index]
            matches = master.guess(i)
            if 6 == matches:
                return

            def get_matches(target, word):
                """
                return the matches counts just as the guess function
                """
                res = 0
                for k, v in enumerate(target):
                    if v == word[k]:
                        res += 1
                return res

            new_words = []
            for w in words:
                if w == i:
                    continue
                if get_matches(i, w) == matches:
                    new_words.append(w)

            words = new_words
            index = 0
