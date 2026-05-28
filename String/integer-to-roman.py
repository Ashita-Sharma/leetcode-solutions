#Description: Given the Roman numericals and an integer, convert the integer into Roman numericals
#following all the standard rules of writing them.

#Approach Description: We start from the highest denomination(1000) and multiply that numerical by the
#quotient of the integer and the denomination and repeat it until we reach the lowest possible denomination.
#We store the denomination and its symbol in a list of pairs and append the values into the final list
#that we join to convert into a string.

class Solution:
    def intToRoman(self, num):
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        res = []

        for value, symbol in value_symbols:
            if num == 0:
                break
            count = num // value
            res.append(symbol * count)
            num -= count * value

        return ''.join(res)

#Time Complexity: O(1) as we will go through all symbols regardless of how large or small the given integer is
#Space Complexity: O(1) as the list of value-symbol pairs will stay the same.