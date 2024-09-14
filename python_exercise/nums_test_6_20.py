
#数组是存放在连续内存空间上的相同类型数据的集合
"""二分法查找元素"""

def binary_search(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:#如果不加=号，当nums=[11]时，找不出target
        mid=(low+high)//2
        guess=nums[mid]
        if target==guess:
            return mid
        elif guess>target:
            high=mid-1
        elif guess<target:
            low=mid+1
    return-1
nums=[1,3,5,7,9,11,13,15,17,19]
target=11
result=binary_search(nums,target)
if result!=-1:
    print('目标元素的索引为',result)
else:
    print('没有发现目标元素')





        
