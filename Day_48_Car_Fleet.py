class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(position)
        cars = sorted(zip(position, speed), reverse=True)
        fleet_count = 0
        max_time = -1
        for pos, spd in cars:
            time = (target - pos) * 1.0 / spd
            if time > max_time:
                fleet_count += 1
                max_time = time
        return fleet_count
