"""
每日温度

给你一个整数数组temperatures,其中temperatures[i]表示第i天的气温

请你返回一个数组answer,其中：

answer[i] = 从第i天开始，要等多少天才会出现更高的温度

如果之后都不会出现更高的温度，则

answer[i] = 0 

时间复杂度 O(n)
空间复杂度 O(n)

"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """单调递减栈，栈里存下标，不存温度"""

    i = 0 # 表示当前是第几天
    stack = [] # 单调递减栈
    n = len(temperatures) # 一共多少天
    ans = [0] * n # 结果数组


    while i<n : # 栈里剩下的下标不用管，因为它们后面没有更高温度，答案保持默认的 0

        # 第i天的温度和栈中的来比较
        while stack and temperatures[i]> temperatures[stack[-1]]:
            prev = stack.pop()
            ans[prev] = i - prev


        # 这两步每一天都必须做
        stack.append(i)
        i+=1 

    return ans

if __name__== "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    ans = daily_temperatures(temperatures)
    print(ans)