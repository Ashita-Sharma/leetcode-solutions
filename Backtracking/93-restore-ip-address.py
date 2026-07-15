'''Description: A valid IP address consists of exactly four integers separated by single dots. Each integer
is between 0 and 255 (inclusive) and cannot have leading zeros. Given a string s containing only digits,
return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder
or remove any digits in s. You may return the valid IP addresses in any order.'''

'''Approach: An ip address contains exactly 4 segments jointed together by ".", and cannot have leading zeroes. So, we
shall implement a backtracking solution similar to the combinations question. First, we shall create a "valid" helper 
function that will check for any leading zeroes and if the number falls within bounds (0,255), and returns true/false 
accordingly. we will also create a DFS-like function that will segment the string into sizes of 1,2,3 and if the subtrings 
are valid, the 4 segments will be joined by .s and returned as output, then the function backtracks to find the 
other possible cases.'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = []

        def valid(seg):
            return not (len(seg) > 1 and seg[0] == '0') and int(seg) <= 255

        def dfs(i, ip):
            if len(ip) > 4:
                return

            if i == len(s) and len(ip) == 4:
                output.append(".".join(ip))
                return

            for l in [1, 2, 3]:
                seg = s[i:i+l]
                if seg and valid(seg):
                    ip.append(seg)
                    dfs(i + l, ip)
                    ip.pop()

        dfs(0, [])
        return output

# Time Complexity: O(1)
# Space Complexity: O(1)