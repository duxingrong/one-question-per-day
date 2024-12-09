"""
长按键入

你的朋友正在使用键盘输入他的名字name,偶尔，在键入字符c时，按键可能会被长按，而字符可能被输入1次或者多次

你将会检查键盘输入的字符typed，如果它对应的可能是你的朋友的名字(其中一些字符可能被长按),那么就返回True

name = "alex" typed = "aaleex"
True

name = "saeed" typed = "ssaaedd"
False

"""

"""
在for 循环遍历typed时，要考虑长按字符的情况，即如果当前字符与前一个字符相同，则继续跳过，而不增加index
在循环结束时，要确保index完全遍历了name的所有字符
"""
class Solution():
    def isLongPressedName(self,name:str,typed:str)->bool:

        index= 0 #这个指针指向name
        for i in range(len(typed)):
            if index<len(name) and typed[i]==name[index]: #第一种情况，就是正确，那么index+1
                index+=1
            elif i>0  and typed[i]==typed[i-1]: #这里处理了长按就跳过，以及到index遍历完后，只有值一直不变才跳过
                continue
            else: #处理了开局就不同，以及中途typed[i]!= typed[i-1]
                return False

        return index==len(name) #如果index没有遍历完，还是False


if __name__=="__main__":
    name = "leelee" 
    typed = "lleeleee"
    solution =Solution()
    result = solution.isLongPressedName(name,typed)
    print(result)
