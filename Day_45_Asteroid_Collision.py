class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            # While there is a collision: current asteroid is negative and top is positive
            while stack and a < 0 and stack[-1] > 0:
                # If top is smaller, it explodes (pop)
                if stack[-1] < -a:
                    stack.pop()
                    continue
                # If they are equal, both explode (pop and break)
                elif stack[-1] == -a:
                    stack.pop()
                break  # If top is larger, current asteroid explodes (so break without pushing)
            else:
                stack.append(a)
        return stack
