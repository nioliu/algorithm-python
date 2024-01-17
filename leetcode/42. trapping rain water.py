# https://leetcode.com/problems/trapping-rain-water/
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for curr in range(len(height)):
            # 如果当前高度大于历史栈顶高度
            while stack and height[curr] > height[stack[-1]]:
                # 弹出栈顶
                top = stack.pop()
                # 如果之前没有任何元素，则说明没有可以形成水坑的机会，直接跳过，没有可以积水的地方
                if not stack:
                    break
                # 否则，得到水平距离，包含了top所在位置的水坑，所以这里取的还是历史栈顶，
                # 即比top高的前一个元素的位置
                distance = curr - stack[-1] - 1
                # 取前一个和当前高度的最小值，减去top的高度，说明是可以填坑的最大高度
                bounded_height = min(height[curr], height[stack[-1]]) - height[top]
                # 距离*高度即为当前可以填补的高度，
                # 在top高度之下的坑，肯定已经被其他元素给填补过了（即和top元素之间形成的坑）
                res += distance * bounded_height
            # 将当前高度加入栈中
            stack.append(curr)
        return res

    def trap(self, height: List[int]) -> int:
        """
        时间复杂度是一样的，只不过上面那个是边遍历，边添加
        :param height:
        :return:
        """
        # 1. find the first bigger than curr
        stack = [0]
        aux = [-1] * len(height)
        for h in range(1, len(height)):
            while stack and height[h] >= height[stack[-1]]:
                n = stack.pop()
                aux[n] = h
            stack.append(h)

        print(aux)
        curr = 1
        res = 0
        while curr < len(height):
            if aux[curr] == -1:
                curr += 1
                continue
            dest = curr
            # 如果前一个位置比当前大，找到最后一个比前一个位置小的最大值
            while aux[dest] != -1:
                dest = aux[dest]
                if height[dest] > height[curr - 1]:
                    break
            bar = height[curr]
            if curr > 0 and height[curr - 1] > height[curr]:
                bar = min(height[curr - 1], height[dest])
                res += bar - height[curr]
            for i in range(curr + 1, dest):
                res += bar - height[i]
            curr = dest
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([0, 7, 1, 4, 6]))
    print(s.trap([4, 2, 0, 3, 2, 5]))
    print(s.trap([2, 0, 2]))
