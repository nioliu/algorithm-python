import copy
from collections import defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) <= 0:
            return []
        wordLen = len(words[0])
        aimLen = wordLen * len(words)

        wordsMap = defaultdict(int)
        for w in words:
            wordsMap[w] += 1

        mem = {}  # 存储上一个结果

        def findNext(currLen, currIndex, currMap):
            if currLen == aimLen:
                return currLen, True
            if currIndex + currLen + wordLen > len(s):
                return currLen, False
            # 下一个需要对比的字符串
            nextStr = s[currIndex + currLen:currIndex + currLen + wordLen]

            if currMap[nextStr] > 0:
                currMap[nextStr] -= 1
                return findNext(currLen + wordLen, currIndex, currMap)

            return currLen, False

        res = []
        for i in range(len(s)):
            beginLen = 0
            beginMap = copy.deepcopy(wordsMap)
            if i > wordLen:
                # 说明之前肯定已经记录过了，直接用之前的map，并跳转到相应的index
                lastLen, beginMap = mem[i - wordLen]
                beginLen = lastLen - wordLen
                beginMap[s[i - wordLen:i]] += 1  # 补充一个
            maxLen, ok = findNext(beginLen, i, beginMap)
            if ok:
                res.append(i)
            mem[i] = (maxLen, beginMap)

        return res


from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len, n = len(words) * word_len, len(s)
        words_count = Counter(words)
        results = []

        for i in range(word_len):
            left = i
            right = i
            # 计算当前用到的word的统计
            current_count = Counter()

            while right + word_len <= n:
                # 获取当前单词
                word = s[right:right + word_len]
                right += word_len

                if word in words_count:
                    current_count[word] += 1

                    # 如果不够了，就一直将左指针向右移动，直到够为止
                    while current_count[word] > words_count[word]:
                        current_count[s[left:left + word_len]] -= 1
                        left += word_len

                    # 如果满足条件，则加入到结果中
                    if right - left == total_len:
                        results.append(left)

                # 如果这个单词根本不在words里面，则重新开计数
                else:
                    current_count.clear()
                    left = right

        return results


if __name__ == '__main__':
    s = Solution()
    # s1 = "wordgoodgoodgoodbestword"
    s1 = "barfoothefoobarman"
    # words = ["word", "good", "best", "good"]
    words = ["foo", "bar"]
    print(s.findSubstring(s1, words))
