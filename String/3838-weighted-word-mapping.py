#Description: You are given an array of strings words, where each string represents a word containing lowercase
#English letters. You are also given an integer array weights of length 26, where weights[i] represents the
#weight of the ith lowercase English letter. The weight of a word is defined as the sum of the weights of
#its characters.

#Approach: We initialize an empty string to hold the final answer. Then, we iterate through each character
#in each word, adding up the corresponding weights. Once we reach the end of the world, we calculate its
#modulo with 26 and use it to convert it into a letter using the reverse alphabet. Then we simply concatenate
#it to the final string.

class Solution:
    def mapWordWeights(self, words, weights):
        str = ""
        for word in words:
            count = 0
            for letter in word:
                count += weights[ord(letter.lower()) - 97]
            count %= 26
            str += (chr(ord('z') - count))
        return str

#Time Complexity: O(n) where n is the combined length of words
#Space complexity: O(1)