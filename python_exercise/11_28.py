"""
旋转数组

给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。使用空间复杂度O(1)的原地算法解决这个问题

举例:
nums = [1,2,3,4,5,6,7],k=3
输出:  [5,6,7,1,2,3,4]
"""


"""
第一种，整体反转然后再反转，
其他语言就整体反转，然后前k个反转，后面的再反转
"""
def function(nums,k):
    #要注意k的大小
    k = k%len(nums)
    #反转整个数组
    nums.reverse() 
    #分段再反转
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums


"""
第二种
仔细观察元素的移动规律，每个元素都会经历一个"循环链",从索引i开始，一次移动到(i+k)%n,在移动到((i+k)+k) %n,直到回到原点i，这个可以通过数学的模运算性质得出
例如:
数组[1,2,3,4,5,6,7]，k=3,从索引0开始:
nums[0]->nums[3]->nums[6]->nums[2]->nums[5]->nums[1]->nums[4]->nums[0]
每个元素恰好被访问一次，形成一个完整的循环链
并非所有的情况都只会有一个循环链，如果n和k有公因数，会产生多个独立的循环链
为了覆盖所有:
1. 每完成一个循环链后，从下一个未访问的元素开始新的链
2. 记录访问的元素数量(count),当count ==n 时，结束
"""
def rotate_cyclic(nums,k):
    k = k%len(nums)
    count = 0 #记录处理过的个数
    start = 0 #第一个循环链

    #开始循环赋值
    while count<len(nums):
        current = start
        prev = nums[start]
        #循环链开始
        while True:
            next_idx = (current+k)%len(nums)#去模数找要替换的位置
            nums[next_idx],prev = prev,nums[next_idx] 
            count +=1#更新访问过的元素数
            current = next_idx 
            if current == start : #代表这一条循环链结束了
                break
        #下一条循环链启动
        start+=1
    return nums




nums = [1,2,3,4,5,6,7]
k=3
nums =rotate_cyclic(nums,k) 
print(nums)
