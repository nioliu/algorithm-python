# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        if len(s) % 2 != 0:
            return False
        match_dict = {"(": ")", "{": "}", "[": "]"}
        stack = []
        i = 0
        while i < len(s):
            curr_char = s[i]
            if curr_char not in match_dict.keys():
                if len(stack) != 0:
                    last_char = stack.pop()
                    if match_dict[last_char] != curr_char:
                        return False
                else:
                    return False
            else:
                stack.append(curr_char)
            i += 1
        return len(stack) == 0


if __name__ == '__main__':
    s2 = Solution()
    print(s2.isValid("{()[}}"))
