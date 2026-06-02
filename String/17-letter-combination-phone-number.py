#Description: Given a string containing digits from 2-9 inclusive, return all possible letter
# combinations that the number could represent. Return the answer in any order.

#Approach Description: Let us start by creating a dictionary for all possible letters. Then, we shall go
# over every letter for each number one by one, appending the next possible letters to it and so on until the
#length of string is equal to length of number string provided(i.e. we have traversed all possible cases).
#Then, we add those strings to our result array and return the final output.

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(idx, comb):
            if idx == len(digits):
                res.append(comb[:])
                return

            for letter in digit_to_letters[digits[idx]]:
                backtrack(idx + 1, comb + letter)

        res = []
        backtrack(0, "")

        return res

#Time Complexity: O(n)
#Space complexity: O(n)