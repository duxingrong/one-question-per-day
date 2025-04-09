"""

273.整数转换为英文表示

将非负整数num转换为其对应的英文表示

num = 123
"One Hundred Twenty Three"

num = 12345
"Twelve Thousand Three Hundred Forty Five"

"""

class Solution:
    """
    每次处理三个数字，加上对应的单位
    """
    def __init__(self):
        """
        初始化数字转英文所需的映射数据。
        """
        self.ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self,num:int):
        """
        Args:
            num: 数字

        Returns :
            str: 数字对应的英文,若num为0，返回"Zero"
        """
        if num == 0:
            return "Zero"
        result = ""
        thousandIndex = 0
        while num>0:
            if num%1000 != 0 :
                result = self.helper(num%1000)+self.thousands[thousandIndex]+" " +result
            num//=1000
            thousandIndex+=1

        return result.strip()

    def helper(self,num:int)->str:
        """
        核心，利用递归思想处理三位数字的英文

        Args:
            num: 数字

        Returns:
            str: 递归转成英文
        """
        if num<20:
            return self.ones[num]+" "
        elif num<100:
            return self.tens[num//10]+ " "+self.helper(num%10)
        else:
            return self.ones[num//100] + " Hundred " +self.helper(num%100)


if __name__=="__main__":
    solution = Solution()
    result = solution.numberToWords(12345)
    print(result)

