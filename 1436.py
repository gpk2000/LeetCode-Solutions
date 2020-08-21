class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mapping = dict()
        for A, B in paths:
            mapping[A] = B
        start = paths[0][0]
        while start in mapping:
            start = mapping[start]
        return start
            
            
