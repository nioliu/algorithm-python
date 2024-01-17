# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {}  # record the str in the begining for current substr
        res = 0
        curr_res = 0  # curr sub string with no repeat length
        curr_begin = 0
        for i in range(len(s)):
            # 如果之前出现过
            if s[i] in record:
                # 如果出现的位置在begin之前，则只更新
                if record[s[i]] < curr_begin:
                    record[s[i]] = i
                    curr_res += 1
                # 否则重新计算
                else:
                    res = max(curr_res, res)
                    curr_res = i - record[s[i]]
                    curr_begin = record[s[i]] + 1
                    record[s[i]] = i
            else:
                curr_res += 1
                record[s[i]] = i
        return max(res, curr_res)

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        简化后
        """
        record = {}  # record the str in the begining for current substr
        res = 0
        curr_begin = 0
        for i in range(len(s)):
            # 如果之前出现过
            if s[i] in record and record[s[i]] >= curr_begin:
                # 如果出现的位置在begin之前，则只更新, 否则重新计算
                res = max(i - curr_begin, res)
                curr_begin = record[s[i]] + 1  # 更新为后一个位置
            # 更新位置
            record[s[i]] = i

        return max(res, len(s) - curr_begin)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
