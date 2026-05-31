#Daily Challenge 31/05/26

#Description:You are given an integer mass, which represents the original mass of a planet.
# You are further given an integer array asteroids, where asteroids[i] is the mass of the ith asteroid.
# You can arrange for the planet to collide with the asteroids in any arbitrary order.
# If the mass of the planet is greater than or equal to the mass of the asteroid, the asteroid is destroyed
# and the planet gains the mass of the asteroid. Otherwise, the planet is destroyed.
# Return true if all asteroids can be destroyed. Otherwise, return false.

#Approach Description: First, let us sort the array in ascending order to make calculations easy.
#Next, iterating for each element in array, if the mass of planet is greater than or equal to the asteroid,
#add its mass to the planet mass. If not possible, return false. Return true if reached end of array.

class Solution:
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        for x in asteroids:
            if mass >= x:
                mass += x
            else:
                return False
        return True

#Time Complexity: O(nlogn) due to sorting algorithm
#Space complexity: O(1)

