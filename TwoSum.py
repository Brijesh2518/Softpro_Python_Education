nums=[2,7,11,15]
target=9
class Solution:
   def twoSum(self, num, target):
    num_map = {}

    for i,num in enumerate(num):
        if target - num in num_map:
            return [num_map[target-num],i] #num_map[2]
        num_map[num] = i
    return []