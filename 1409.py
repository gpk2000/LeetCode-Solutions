class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = []
        for i in range(1, m + 1):
            arr.append(i)
        positions = []
        for el in queries:
            index = arr.index(el)
            arr.remove(el)
            arr.insert(0, el)
            positions.append(index)
        return positions
