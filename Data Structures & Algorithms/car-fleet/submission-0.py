class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        for i in range(len(position)):
            time=(target-position[i])/speed[i]
            cars.append((position[i], time))
        cars.sort(reverse=True)
        max_time=0
        fleet=0

        for pos, time in cars:
            if time>max_time:
                fleet+=1
                max_time=time
        return fleet



        