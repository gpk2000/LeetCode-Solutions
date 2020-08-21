class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        decrypted_str = ''
        for ch in s:
            if ch == '#':
                num = stack.pop()
                num += stack.pop()
                num = num[::-1]
                left = ''
                while stack:
                    left += str(chr(ord('a') + int(stack.pop()) - 1))
                left = left[::-1]
                decrypted_str += left
                decrypted_str += str(chr(ord('a') + int(num) - 1))
            else:
                stack.append(ch)
        left = ''
        while stack:
            left += str(chr(ord('a') + int(stack.pop()) - 1))
        left = left[::-1]
        return decrypted_str + left
