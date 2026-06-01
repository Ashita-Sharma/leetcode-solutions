#Description:A shop is selling candies at a discount. For every two candies sold, the shop gives
# a third candy for free. The customer can choose any candy to take away for free as long as the
# cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.

#Approach Description: First, let us sort the array in descending order. Next, we shall take the most expensive
#candies and get the third most expensive one for free, repeating until the end. For the remainder candies, they
#will be the cheapest ones so we can easily buy them and add them to our total cost as well.

class Solution:
    def minimumCost(self, cost):
        total_cost = 0
        cost.sort(reverse=True)

        l = len(cost)

        num_three = l // 3
        mod_three = l % 3

        pos = 0
        for i in range(0, num_three):
            first_candy = cost[pos]
            total_cost = total_cost + first_candy
            pos+=1
            second_candy = cost[pos]
            total_cost = total_cost + second_candy
            pos+=2

        for i in range(0, mod_three):
            candy = cost[pos]
            total_cost = total_cost + candy
            pos+=1

        return total_cost

#Time Complexity: O(nlogn) due to sorting used
#Space complexity: O(1)