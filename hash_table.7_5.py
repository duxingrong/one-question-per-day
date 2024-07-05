"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

示例：

输入：19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""
"""
把每次计算出来的n值都存在集合内，这样当出现循环时马上判断出重复不是快乐数
"""
class Solution:
    # 定义一个方法isHappy，用来判断一个整数是否是快乐数
    def isHappy(self, n: int) -> bool:        
        # 初始化一个集合，用于记录已经出现过的数字
        record = set()

        # 循环直到找到快乐数或者发现不是快乐数,无限循环
        while True:
            # 调用get_sum方法计算当前整数的下一个状态
            n = self.get_sum(n)
            # 如果当前整数变为1，说明找到了快乐数
            if n == 1:
                return True
            
            # 如果当前整数已经在记录中出现过，说明陷入了循环，不是快乐数
            if n in record:
                return False
            else:
                # 否则将当前整数加入记录集合
                record.add(n)

    # 定义一个辅助方法get_sum，用来计算一个整数的各位数字平方和
    def get_sum(self, n: int) -> int: 
        # 初始化新数字的值为0
        new_num = 0
        # 循环直到整数变为0
        while n:
            # 取整数的最低位
            r = n % 10
            # 将整数除以10，取整商
            n = n // 10
            # 将最低位的平方加到新数字上
            new_num += r ** 2
        # 返回计算得到的新数字
        return new_num
             

        
n=19
solution=Solution()
is_happy=solution.isHappy(n)
print(is_happy)