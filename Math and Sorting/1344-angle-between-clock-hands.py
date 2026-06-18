#Description: Given two numbers, hour and minutes, return the smaller angle (in degrees) formed
#between the hour and the minute hand. Answers within 10-5 of the actual value will be accepted as correct.

#Approach: Firstly, if the hour or the minute is at 12 or 60 respectively, we take them as zero.
#Next, we know that the angle of the minute hand is minutes multiplied by angle covered per minute.
#For the hour hand, the angle is angle covered per hour multiplied by hour + angle covered by each minute
#multiplied by total minutes.
#Then, if the answer is greater than 180, we take the difference to be 360 - angle difference.

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if minutes == 60:
            minutes = 0
        if hour == 12:
            hour = 0
        angle_hour = 30 * hour + (0.5 * abs(minutes))
        angle_minute = 6 * abs(minutes)
        if angle_hour > angle_minute:
            diff = angle_hour - angle_minute
        else:
            diff = angle_minute - angle_hour
        diff = min(diff, 360 - diff)

        return diff

#Time Complexity: O(1)
#Space complexity: O(1)