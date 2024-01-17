# https://leetcode.com/problems/sort-colors/description/
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r, w, b = 0, 0, len(nums) - 1  # stand for each next position
        while w <= b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] == 1:
                w += 1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1


from scapy.all import sniff, IP


# 定义回调函数来处理捕获的数据包
def process_packet(packet):
    if IP in packet:
        ip_packet = packet[IP]
        print(f"Source IP: {ip_packet.src}, Destination IP: {ip_packet.dst}")




if __name__ == '__main__':
    s = Solution()
    # nums = [2, 0, 2, 1, 1, 0]
    # nums = [1, 0, 1]
    # nums = [1, 2, 2, 2, 2, 0, 0, 0, 1, 1]
    # s.sortColors(nums)
    # print(nums)
    # 捕获网络数据包
    sniff(filter="ip", prn=process_packet, count=10)