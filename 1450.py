class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        working = 0
        for i in range(len(endTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                working += 1
        return working
