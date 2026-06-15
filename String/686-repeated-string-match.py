#Description: Given two strings a and b, return the minimum number of times you should
#repeat string a so that string b is a substring of it. If it is impossible for b
#to be a substring of a after repeating it, return -1.

#Approach: Similar to question 796, we can add string a onto itself until we get b in the modified string.
#However, we also need to know when to stop, so we need to only check the smallest count in which string b
#can fit into modified string. Hence, we do ceil(length(b)/length(a)) plus some factor to account for
#edge cases. Finally, if we still don't get an answer we return -1.

class Solution:
    def repeatedStringMatch(self, a, b):
        len_b = len(b)
        len_a = len(a)
        modified_str = a
        count = 1
        while count < ceil(len_b/len_a) + 3 :
            if b in modified_str:
                return count
            else:
                modified_str += a
                count += 1
        return -1