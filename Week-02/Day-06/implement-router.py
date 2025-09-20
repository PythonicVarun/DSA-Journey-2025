"""
Problem: Implement Router
Date: 20-09-2024
Difficulty: Medium
Time taken: ~8 minutes
Link: https://leetcode.com/problems/implement-router/
"""

import hashlib
from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class Router:

    def __init__(self, memoryLimit: int):
        self.router = []
        self.seen = set()
        self.limit = memoryLimit
        self.distMap = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = [source, destination, timestamp]
        hash = hashlib.md5(str(packet).encode("utf-8")).hexdigest()
        if hash in self.seen:
            return False

        if len(self.router) == self.limit:
            _packet = self.router.pop(0)
            self.seen.remove(hashlib.md5(str(_packet).encode("utf-8")).hexdigest())
            self.distMap[_packet[1]].pop(0)

        self.router.append(packet)
        self.seen.add(hash)
        self.distMap[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.router:
            return []

        packet = self.router.pop(0)
        self.seen.remove(hashlib.md5(str(packet).encode("utf-8")).hexdigest())
        self.distMap[packet[1]].pop(0)
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        packets = self.distMap[destination]
        return bisect_right(packets, endTime) - bisect_left(packets, startTime)


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
