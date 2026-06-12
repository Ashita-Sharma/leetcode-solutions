#Description: You are given an integer array prices where prices[i] is the price of the ith item in a shop.
#Return an integer array answer where answer[i] is the final price you will pay for the ith item of
#the shop, considering the special discount.

#Approach Description: We loop through each price and check if any of the prices after it are smaller.
#If a smaller price exists, we append the discounted price to our result list and break out of the loop,
#to move on to the next item. If we cannot find a valid discount, we directly append the original price.
#The last element cannot have a discount so it is added directly.

class Solution:
    def finalPrices(self, prices):
        res = []
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    res.append(prices[i]-prices[j])
                    break
            else:
                res.append(prices[i])
        res.append(prices[-1])
        return res


#Time Complexity: O(n*n)
#Space complexity: O(n)