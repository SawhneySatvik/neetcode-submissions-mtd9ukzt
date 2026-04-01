class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(speed))]
        cars = sorted(cars, key=lambda tup: tup[0], reverse=True)

        fleets = []

        for car in cars:
            pos, s= car
            time = (target-pos)/s

            if not fleets or fleets[-1] < time:
                fleets.append(time)
        
        return len(fleets)