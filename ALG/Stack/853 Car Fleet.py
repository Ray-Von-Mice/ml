class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
            time consume for i = (target - pos[i])/speed[i]
            target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
            time[0] = (12 - 10) / 2 = 1
            time[1] = (12 - 8) / 4 = 1
            time[2] = 12 / 1 = 12
            time[3] = (12 - 5) / 1 = 7
            time[4] = (12 - 3) / 3 = 3
            a car starting behind a previous car, but taking the same or less time means -> it's faster and can catch up -> merge
        '''
        n = len(position)
        if n == 1:
            return 1
        
        pos_speed = [ (p, s) for p, s in zip(position, speed)]
        pos_speed.sort(reverse = True)

        fleet = 0
        prevTime = float("-inf")
        for i in range(0, n):
            curTime = (target - pos_speed[i][0]) / pos_speed[i][1]
            if curTime > prevTime:
                fleet += 1
                prevTime = curTime

        return fleet