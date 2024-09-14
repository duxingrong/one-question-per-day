"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)
"""

class Solution():
    def canConstruct(self,ransom:'str',magazine:'str')->bool:
        hash1=[0]*26       
        hash2=[0]*26 
        for i in  magazine:
            hash1[ord(i)-ord('a')]+=1
        
        for i in ransom :
            hash2[ord(i)-ord('a')]+=1
       
        return all(hash2[i] <= hash1[i] for i in range(26))  
        # all(...)：这个内置函数接受一个可迭代对象作为参数，并返回 True 如果可迭代对象中的所有元素都是 True，否则返回 False。

            
ransom='ab'
magazine='aab'
solution=Solution()
is_OK=solution.canConstruct(ransom,magazine)
print(is_OK)
