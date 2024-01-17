# https://leetcode.com/problems/decoded-string-at-index/

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        """
        out of memory
        :param s:
        :param k:
        :return:
        """
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        tape = ""
        for i in s:
            if 'a' <= i <= 'z':
                tape += i
            else:
                tape *= int(i)
            if len(tape) >= k:
                return tape[k - 1]
        return tape[k - 1]

    def decodeAtIndex2(self, s: str, k: int) -> str:
        """
        use math to calculate
        """
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        baseTape = ""
        repeat = 1
        for i in s:
            if i.isalpha():
                baseTape *= repeat
                baseTape += i
                repeat = 1
            else:
                repeat *= int(i)
            print(baseTape, ' ', repeat)
            if len(baseTape) * repeat >= k:
                return baseTape[k % len(baseTape) - 1]
        return baseTape[k % len(baseTape) - 1]

    def decodeAtIndex3(self, s: str, k: int) -> str:
        """
        use math to calculate, only store the length
        """
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        baseTapeLenArr = [0]
        currStrLen = 0
        currBaseIndex = 0
        for i in s:
            if 'a' <= i <= 'z':
                baseTapeLenArr[currBaseIndex] += 1
                currStrLen += 1
            else:
                currStrLen *= int(i)
                baseTapeLenArr.append(currStrLen)
                currBaseIndex += 1

            if currStrLen >= k:
                break
        for i in range(len(baseTapeLenArr) - 1, 0, -1):
            currBaseRepeat = baseTapeLenArr[i]
            remain = k % currBaseRepeat

        return


if __name__ == '__main__':
    s = Solution()
    # print(s.decodeAtIndex2("ha22", 5))
    print(s.decodeAtIndex2("qgd883bxr7", 2458))
    # print(s.decodeAtIndex2("leet2code3", 10))
    # print(s.decodeAtIndex("a2345678999999999999999", 1))
# print(s.decodeAtIndex(
#     'cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg', 480551547))
