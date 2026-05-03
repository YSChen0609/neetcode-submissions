# How will 2 cars be in a fleet?
# 1. p1 + k*v1 == p2 + k*v2 <= target, k<= (target-p2)/v2
# 2. if p1 < p2 and v1 > v2 
# What about NOT in a fleet?
# 1. p1 < p2 and v1 <= v2

# idea:
# pop the pos from the last, and compare the top(s) with it
# if criterion met, they are in the same fleet

# time: O(nlogn)
# space: O(1)


"""
target = 10
pos : [0, 2, 4]
spe : [2, 3, 1]
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the positions and speed
        pos, sp = zip(*sorted(zip(position, speed)))
        position, speed = list(pos), list(sp)
        
        res = 1 # num of fleets
        fleet_core, core_speed = position.pop(-1), speed.pop(-1) # init core
        while position:
            # pop a new car
            cur_pos, cur_sp = position.pop(-1), speed.pop(-1)
            # new car can't catch up to this fleet, update fleet core and res
            if (cur_sp <= core_speed or \
                (fleet_core-cur_pos)/(cur_sp-core_speed) > (target-fleet_core)/core_speed):
                fleet_core, core_speed = cur_pos, cur_sp
                res += 1

        return res








