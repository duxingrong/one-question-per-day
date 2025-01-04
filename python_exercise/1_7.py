"""
我的日程安排表|||

当k个日程存在一些非空交集时(即,k个日程包含了一些相同时间),就会产生k次预订

给你一些日程安排[startTime,endTime),请你在每个日程安排添加后,返回一个整数k,表示所有先前日程安排会产生的最大k次预订

实现一个MyCalendarThree类来存放你的日程安排,你可以一直添加新的日程安排

MyCalendarThree()初始化对象
int book(int startTime,int endTime)返回一个整数k,表示日历中存在的k次预订的最大值


**利用差分数组,非常巧妙的只记录变化的时间点,然后通过累加来找到最大k次预订,神奇**

"""

class MyCalendarThree:

    def __init__(self):
        ## 用字典来记录每个时间段,起始时间=+1,结束时间=-1
        self.diff = {}

    def book(self,startTime:int,endTime:int)->int:

        ## 维护字典
        self.diff[startTime] = self.diff.get(startTime,0)+1  ## 如果在字典中出现了,就是+1,如果没出现,默认0,然后+1
        self.diff[endTime]   = self.diff.get(endTime,0)-1

        ## 维护最大预订数
        current_booking = 0 
        max_booking = 0
        for time in sorted(self.diff): ## 按key来排序
            current_booking += self.diff[time]
            max_booking = max(max_booking,current_booking)

        return max_booking
