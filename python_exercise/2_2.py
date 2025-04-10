from functools import lru_cache
from typing import List

class Solution:
    """
    403.青蛙过河
    青蛙上一步跳了k个单位，那么这一次只能选择跳k-1,k,k+1个单位
    青蛙每一步必须踩到石头上，初始默认在第一块石头上,第一步只能跳跃1个单位
    """

    def canCross(self, stones: List[int]) -> bool:
        """
        Args:
            stones: 石头的序列,青蛙默认在0，也就是第一块石头上

        Returns:
            bool 青蛙是否可以过河
        """
        if stones[1] != 1:
            return False
            
        stones_set = set(stones)
        last_stone = stones[-1]
        
        @lru_cache(maxsize=None)
        def helper(position, jump):
            if position == last_stone:
                return True
                
            for next_jump in [jump - 1, jump, jump + 1]:
                if next_jump <= 0:
                    continue
                    
                next_position = position + next_jump
                if next_position in stones_set and helper(next_position, next_jump):
                    return True
                    
            return False
            
        return helper(1, 1)  # 从第二个石头开始，初始跳跃距离为1


if __name__ == "__main__":
    solution = Solution()
    stones = [0,1,3,5,8,12,17]
    stones = [0,1,2,3,4,8,9,11]
    print(solution.canCross(stones))


