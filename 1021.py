class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        bad = []
        modifiedS = ''
        for i in range(len(S)):
            if S[i] == '(':
                stack.append([S[i], i])
            else:
                if len(stack) == 1:
                    bad.append([stack[-1][1], i])
                stack.pop()
        for i, j in bad:
            modifiedS += S[i + 1: j]
        return modifiedS
