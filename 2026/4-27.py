"""
最多可以参加多少场会议

给你一个二维数组events,其中

events[i] = [start,end]
表示第i场会议可以在第start天到第end天之间任意选择一天参加

规则：

每一天最多只能参加异常会议

请你返回： 最多可以参加多少场会议



每天把已经开始的会议加入堆；
删掉已经过期的会议；
如果还有可参加的会议，就参加结束最早的那场。

"""
import heapq

def max_events(events: list[list[int]]) -> int:
    
    events.sort() # 首先将会议按照时间进行排序

    day = 0 # 当前是第几天
    i = 0  # 指向下一场还没有加入堆的会议
    heap = [] # 小根堆，存放当前可参加会议的结束时间
    ans = 0  # 已参加的会议数量
    n = len(events)

    while i < n or heap : # 只要还有会议没有处理完，或者堆里面还有可参加的会议，就要继续
        # 先确定从哪一天开始
        if not heap:
            day  = events[i][0]


        # 把当前能参加的会议全部加入进来
        while i < n and events[i][0]<=day:
            start , end = events[i]
            heapq.heappush(heap,end)
            i+=1 

        # 把当天已经无法参加的会议给排除掉
        while heap and heap[0]<day :
            heapq.heappop(heap)

        
        # 当天选一场会议来参加
        if heap:
            heapq.heappop(heap)
            ans +=1 

            # 要下一天了
            day+=1 

    return ans


if __name__ == "__main__":
    events = [[1, 2], [1, 2], [1, 6], [2, 2]]
    print(max_events(events))  # 3
