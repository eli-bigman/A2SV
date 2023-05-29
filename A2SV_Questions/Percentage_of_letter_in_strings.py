class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        letter_quantity  = 0
        for i in s:
            if i == letter:
                letter_quantity += 1
        percentage  = (letter_quantity/len(s)) * 100
        return round(percentage)
