#Description: You are given a personal information string s, representing either an email address
#or a phone number.

#Approach: Based on the rules, we can first check if "@" is in the string. If yes, then we follow the rules
#by splitting the list into name and domain. Then, we can return the correct format.
#For the phone number, we add all the numbers into a string. If the length is greater than 10, we add
#the extra length as "*" in front of the string. Add the "*"s and then concatenate the last four numbers
#normally. Return the string.


class Solution:
    def maskPII(self, s):
        if "@" in s:
            name,domain=s.split("@")
            name=name.lower()
            domain=domain.lower()
            name=name[0]+"*****"+name[-1]
            return name+"@"+domain
        else:
            gg=""
            for x in s:
                if x.isdigit():
                    gg+=x
            l=len(gg)
            if l>10:
                return "+"+"*"*(l-10)+"-***-***-"+gg[-4:]
            return "***-***-"+gg[-4:]

#Time Complexity: O(n)
#Space complexity: O(1) for email, O(n) for phone number