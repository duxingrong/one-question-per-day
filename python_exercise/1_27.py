"""

214.最短回文串

给定一个字符串s,你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串


这道题目的难点就是快速的找到最长前缀回文串,然后将后面多余的反转放到开头就好了
利用KMP，并且构造特殊的字符串s+#+s[::-1]


"""

class Solution:
    def shortestPalindrome(self,s:str)->str:

        # 构造特殊的字符串
        temp = s +'#'+s[::-1]
        n= len(temp)
        lps = [0]*n # KMP的LPS数组

        # 计算LPS数组
        j = 0 # 记录前缀匹配的长度
        for i in range(1,n):
            while j>0 and temp[i]!= temp[j]:
                j = lps[j-1] # 失败回退

            if temp[i]==temp[j]:
                j +=1

            lps[i]=j

        # lps[-1]代表了最长前缀回文串的长度,所以将后面的反转放到最前面，就是最短回文串
        l = lps[-1]
        return s[l:][::-1] + s


if __name__ == "__main__":
    # 测试
    sol = Solution()
    print(sol.shortestPalindrome("abcd"))  # 输出: "dcbabcd"
    print(sol.shortestPalindrome("aacecaaa"))  # 输出: "aaacecaaa"
