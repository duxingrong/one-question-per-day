class Solution:
    """
    458.可怜的小猪
    利用信息编码"通过实验得出的编码(a,b)恰好就是那个预先分配给有毒桶的编码"正是因为我们的实验设计就是以这种唯一映射为基础,确保有毒桶的"信息输出"能够直接反映到猪死亡的时序上，从而还原出桶的编码.
    """
    def poorPigs(self,buckets:int,minutesToDie:int,minutesToTest:int)->int:
        """
        (R+1)^p>=buckets ,通过数学推导求出p,这里不要用math.log会产生错误
        Args:
            buckets:桶的数量
            minutesToDie:猪喝水后的冷却时间
            minutesToTest: 总时长
        """
        R = minutesToTest//minutesToDie # 轮数,那每个小猪就有R+1种状态
        p = 0
        while (R+1)**p<buckets:
            p+=1

        return p

if __name__ == "__main__":
    solution  =Solution()
    print(solution.poorPigs(125,1,4))




