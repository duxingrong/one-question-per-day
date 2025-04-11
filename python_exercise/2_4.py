from typing import List
class Solution:
    """
    517.超级洗衣机
    每一步可以操控任意台洗衣机将其中的一件衣服交给邻位
    求数量相等的最少操作步数
    """
    def findMinMoves(self,machines:List[int])->int:
        """
        难点在于理解最少操作步数等于*最大单机差值*和*最大累积不平衡量的绝对值*
        直观理解：
            如果某台洗衣机需要移出很多衣物，这需要很多步骤
            如果某个区域总体失衡严重，衣服需要流动过这个区域，也需要根多步骤
        Args:
            machines: 机器台数
        Returns:
            result: 操作步数
        """
        total = sum(machines)
        n  = len(machines)

        if total%n != 0:
            return -1
        
        avg = total//n
        result = 0
        balance = 0 #累积不平衡量

        for clothes in machines:
            diff  = clothes-avg
            balance +=diff
            result = max(result, diff, abs(balance))

        return result


