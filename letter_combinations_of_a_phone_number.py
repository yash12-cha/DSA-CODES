from typing import List

class LetterCombinations:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        self.digit_to_letters = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        self.result = []
        self.solve(0, "", digits)
        return self.result

    def solve(self, index: int, current: str, digits: str):
        if index == len(digits):
            self.result.append(current)
            return

        letters = self.digit_to_letters[digits[index]]
        for letter in letters:
            self.solve(index + 1, current + letter, digits)

digits = "23"
letter_combinations = LetterCombinations()
ans = letter_combinations.letterCombinations(digits)
print(ans)

'''
Time complexity:
O(4^n), where n is the number of digits (each digit can map to up to 4 letters, as in the case of digit 7 and 9)

Space complexity:
O(4^n) to store all possible combinations
'''