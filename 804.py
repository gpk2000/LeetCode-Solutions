class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mappings = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        total = set()
        for word in words:
            rep = ''
            for ch in word:
                rep += mappings[ord(ch) - ord('a')]
            total.add(rep)
        return len(total)
