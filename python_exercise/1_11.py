"""

有效数字

给定一个字符串s,返回s是否是一个有效数字

一般的，一个有效数字可以用以下的规则之一定义:
1. 一个整数后面跟着一个可选指数
2. 一个十进制数后面跟着一个可选指数

一个整数定义为可选符号'-'或'+'后面跟着数字
一个十进制数定义为一个可选符号'-'和'+'后面跟着下述规则:
1. 数字后跟着一个小数点
2. 数字后跟着一个小数点.再跟着数位
3. 一个小数点.后跟着数位

指数 定义为指数符号'e'或'E'，后面跟着一个整数。
数字 定义为一个或者多个数位

举例:
'123'是有效的整数
'123.45'是有效的十进制数
'-123.45e+6'是有效的数字(带有指数部分)
'abc'不是有效的数字
'1e10'是有效的数字(只有指数部分)

- 去掉多余的空格
- 如果以'+'和'-'开头，就跳过
- 如果遇到小数点，确保小数点后有数字，并且小数点只能有一个，并且不能在e后面
- 如果遇到'e'或者'E',它后面必须跟着一个整数(可以带符号)

"""

class Solution():
    def isNumber(self,s:str)->bool:
        ## 可以说这个题目对标志的充分利用
        has_num = False #有无数字
        has_e   = False #有无e
        has_dot = False #有无小数点

        s = s.strip() ## 去除空格
        index = 0

        # 去掉开局的符号
        if s[index]==  "+" or s[index]=="-":
            index+=1

        while index<len(s):
            ## 判断是否是数字
            if s[index].isdigit():
                has_num = True
            elif s[index]=='e'or s[index]=='E': ## 只能出现一次，并且前面必须有数字
                if has_e or not has_num:
                    return False
                has_e = True
                has_num = False ## 这里重置，是为了保证e后面一定有数字

                ## 允许后面带一个符号
                if index+1<len(s) and (s[index+1]=='-' or s[index+1]=="+"):
                    index+=1

            elif s[index]== ".": ## 小数点只能有一个，并且不能在e后面
                if has_e or has_dot:
                    return False
                has_dot = True
            else :
                ## 其他字符，直接False
                return False
            ## 遍历
            index +=1

        return has_num ## 这里是为了和e打配合,如果e后面没有的数字，那就不是有效数字，且这时候has_num = False ，所以直接返回has_num就好


if __name__=="__main__":
    solution = Solution()
    s1 = '1e10'
    s2 = '1e-1'
    s3 = '1.01'
    print(solution.isNumber(s1))
    print(solution.isNumber(s2))
    print(solution.isNumber(s3))












