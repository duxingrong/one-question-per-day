"""

缺失的第一个正数

给你一个未排序的整数数组nums,请你找出来其中没有出现的最小的正整数

请你实现时间复杂度0(n)并且只使用常数级别额外空间的解决方案

没有排序，排除二分法
常数级别额外空间,也不是堆吗?

**思路**

数组的范围限制:数组中的最小正整数范围应该在1到n+1之间,其中n是数组的长度,因为数组中如果包含了1到n的所有整数,缺失的最小正整数就是n+1

原地哈希:我们可以通过将每个数字放到对应的位置上来实现这一点,具体来说,数组中的每个值应该放在nums[i]=i+1的位置上,我们可以遍历数组,把每个正整数x放在x-1的位置上,前提是x处于1到n的范围内

交换元素,我们可以通过交换元素将每个数放到它应该在的位置,这样,最终遍历一遍数组,第一个nums[i]!=i+1的位置的地方,就是缺失的最小正整数,返回i+1


通俗的来说,我们通过原地交换,保证了只要元素处于数组范围内,就一定可以放在正确的位置上,所以,如果所有的能放到正确位置上的元素都放到了正确的位置上,那第一个不符合nums[i]=i+1的位置,不就是缺失的最小正整数吗?

并且我们只处理0-n之间的数字,不用在乎数组中的0和负数,始终明确我们要做的是把能放到正确位置的元素全部归位

"""

from typing import List


class Solution:
    def firstMissingPositive(self,nums:List[int])->int:
        n = len(nums)

        ## 交换数组
        for i in range(n):
            ## 注意这里是while,可以一直进行
            while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]: ## 这里一定要这么写，不能写nums[i]!=i+1,因为要保证交换位置的元素不想等,否则进入死循环
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] ## 这里注意右边一定先写nums[i],位置不能变,不然过不了

        ## 然后遍历一遍,第一个不满足的位置就是最小的缺失正整数
        for i in range(n):
            if nums[i]!=i+1:
                return i+1

        ## 只有全部都满足,那就是说明数组刚刚好,最小的正整数就是len+1
        return n+1

"""
第二种方法就是直接原地修改数组,我们把出现过的1~n的元素的索引变成负数,当作标记(所以首先就要把负数和0改成n+1)
"""
class Solution:
    def firstMissingPositive(self,nums:List[int])->int:
        n = len(nums)
        
        ## 改值
        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=n+1

        ## 修改出现值的索引符号,作为标记
        for i in range(n):
            num = abs(nums[i])
            if num<=n:
                ## 把num应该在的位置的元素符号变为-
                nums[num-1] = -abs(nums[num-1]) ## abs是为了防止--得正了

        for i in range(n):
            if nums[i]>0:
                return i+1

        ## 都通过了,就返回n+1
        return n+1



"""
为什么没想到最简单的呢?
"""
class Solution:
    def firstMissingPositive(self,nums:List[int])->int:
        tmp = set(nums)
        for i in range(1,len(nums)+2): ## 这里甚至写的+2,可以少些一行代码,佩服
            if i not in tmp:
                return i



