"""

查找常用字符

给你一个字符串数组words,请你找出所有在words的每个字符串中都出现的共用字符(包括重复字符),并以数组形式返回，你可以按任意顺序返回答案

words = ["bella","label","roller"] 输出['e','l','l']

还是创建很多的内存来存哈希表,然后每个字符取最小值，也就是每个都有的字符的次数

"""


from typing import List

class Solution():
    def commonChars(self,words:List[str])->List[str]:
        total_hash = [float('inf')]*26
        for word in words:
            hash  = [0]*26
            for i in range(len(word)): #每个字符串的字符个数
                hash[ord(word[i])-ord('a')] +=1
            for i in range(26):
                total_hash[i]=min(total_hash[i],hash[i])

        result = []
        for i in range(26):
            while total_hash[i]> 0:
                result.append(chr(i+ord('a')))
                total_hash[i]-=1

        return result


if __name__ =="__main__":
    words = ["bella","label","roller"]
    solution = Solution()
    result = solution.commonChars(words)
    print(result)

        
