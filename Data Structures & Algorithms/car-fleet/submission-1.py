class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            eta = (target - pos)/spd

            if not stack or eta  > stack[-1]:
                stack.append(eta)

        return len(stack)

