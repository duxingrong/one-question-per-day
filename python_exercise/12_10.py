"""
比较含退格的字符串

给定S和T两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果，#代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空

输入： S ="ab#c" T = "ad#c"
输出: true 
S和T都会变成"ac"

"""


"""
利用栈，遇到一个#，就pop(),但是使用了两次for 循环
"""
class Solution():
    def backspaceCompare(self,S:str,T:str)->bool:

        return self.get_st(S) == self.get_st(T)

    def get_st(self,s:str):
        st = []
        for i in range(len(s)):
            if s[i]=="#" :
                if st:
                    st.pop()
            else:
                st.append(s[i])
        return st
    

"""
优化方法，从后向前使用双指针
同时从后向前遍历S和T，记录#的数量，模拟消除的动作，当#用完了，就开始比较S[i]和T[j]
"""

class Solution():
    def backspaceCompare(self,S:str,T:str)->bool:
        #指针
        i = len(S)-1
        j = len(T)-1 
        #记录#数量
        S_backspace = 0
        T_backspace = 0

        while i>=0 or j>=0:
            while i>=0:
                if S[i]=="#":
                    i-=1
                    S_backspace+=1
                else:
                    if S_backspace>0:
                        S_backspace-=1
                        i-=1
                    else: #此时遍历的这个字符，他就是最终会存在的，那么等待和T中的进行比较
                        break
    
            while j>=0:
                if T[j]=="#":
                    j-=1
                    T_backspace+=1
                else:
                    if T_backspace>0:
                        T_backspace-=1
                        j-=1
                    else: #此时遍历的这个字符，他就是最终会存在的，那么等待和T中的进行比较
                        break        
            #后半部分#消除完了，接下来比较当前位置的值
            if i>=0 and j>=0:
                if S[i]!=T[j]:
                    return False 
            elif i>=0 or j>=0: #一个字符串找到了待比较的字符，另一个没有
                return False

            i-=1
            j-=1

        return True  


if __name__=="__main__":
    S = "ab#c"
    T = "ad#c"
    solution = Solution()
    print(solution.backspaceCompare(S,T))