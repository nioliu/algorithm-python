from collections import defaultdict


# 真正的元素
class Element:
    def __init__(self, v):
        self.v = v


class DisjointSet:
    # 集合，但并不是真正的集合
    def __init__(self, nums: []):
        # 值-元素，包装一下，方便解题的其他信息的存储
        self.vToElement = {}
        # 代表元素的集合对应的大小，用于合并集合，将大的合并到小的下面
        self.elToSize = {}
        # 元素对应的代表元素
        self.elToHeadEl = {}
        for n in nums:
            el = Element(n)
            self.vToElement[n] = el
            self.elToSize[el] = 1
            self.elToHeadEl[el] = el

    def queryHeadByV(self, v):
        """
        尝试通过v来查找。如果有重复的v，则可能返回错误的答案。
        :param v:
        :return:
        """
        return self.queryHead(self.vToElement[v])

    def queryHead(self, el: Element):
        """
        查找元素的代表元素
        """
        if not el:
            return None

        # 统计路途上的所有元素
        elStack = []
        curr = el
        while self.elToHeadEl[curr] != curr:
            elStack.append(curr)
            curr = self.elToHeadEl[curr]

        # 更新头元素，不需要更新原头节点的代表集合大小，因为不会再用到了
        while elStack:
            self.elToHeadEl[elStack.pop()] = curr

        return curr

    def isSameSet(self, el1: Element, el2: Element) -> bool:
        """
        判断两个元素是否在同一个节点内
        """
        if not self.elToHeadEl[el1] or not self.elToHeadEl[el2]:
            return False
        return self.queryHead(el1) == self.queryHead(el2)

    def union(self, el1: Element, el2: Element):
        """
        合并两个元素所在的集合，也就是连接两个元素（图连通），所以这两个元素就是在同一个机会了
        """
        if self.isSameSet(el1, el2):
            return
        head2 = self.queryHead(el2)
        head1 = self.queryHead(el1)
        smallH = head2 if self.elToSize[head2] < self.elToSize[head1] else head1
        bigH = head1 if smallH is head2 else head1
        self.elToHeadEl[bigH] = smallH
        self.elToSize[smallH] += self.elToSize[bigH]
        self.elToSize.pop(bigH)
        return


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    d = DisjointSet(nums)
    for i in range(len(nums)):
        d.queryHeadByV(nums[i])
