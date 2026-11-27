class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            #Need to use tuples because during sort the position and the speed will change
            cars.append((position[i],speed[i]))
        cars.sort(reverse=True)

        stack = []
        for pos,spd in cars:
            time = (target-pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)