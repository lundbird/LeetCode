class Solution:
    def titleToNumber(self, s: str) -> int:
        alphabet_size = 26
        mult = 1
        total = 0
        for char in s[::-1]:
            val = ord(char) - 64
            total += val * mult
            mult *= alphabet_size
        return total
            