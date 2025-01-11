"""
左右文本对齐

给定一个单词数组words和一个长度maxWidth，重新排版单词，使其成为每行恰好有maxWidth个字符,且左右两端对齐的文本

你应该使用'贪心算法'来放置给定的单词，也就是说，尽可能地多往每行中放置单词。必要时可用空格' '来填充，使得每行恰好有maxWidth个字符

要求尽可能均匀分配单词间的空格数量，如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数

文本的最后一行应为左对齐,且单词之间不插入额外的空格

注意:
- 每个单词是指非空格字符组成的字符序列
- 每个单词的长度大于0，小于等于maxWidth
- 输入单词数组words至少包含一个单词

输入: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

"""
from typing import List


class Solution():
    def fullJustify(self,words:List[str],maxWidth:int)->List[str]:
        
        ## 变量
        current_line = [] # 当前行的列表
        current_length = 0 # 当前行的长度
        result = [] # 结果集

        for word in words:

            ## 现有的长度+当前单词的长度+所以要的空格
            if current_length+len(word)+len(current_line)>maxWidth:
                ## 说明这一行可以收网了
                space = maxWidth-current_length

                if len(current_line)==1: # 如果这一行只有一个单词
                    result.append(current_line[0]+' '*space)
                else: # 算出单词之间的空格以及多余的空格
                    space_per_gap = space//(len(current_line)-1)
                    extra_space = space%(len(current_line)-1)                   

                    line = ''
                    for i in range(len(current_line)-1):
                        line+= current_line[i]
                        ## 对于前extra_space个间隙,额外增加一个空格，保证尽可能平均
                        line+=' '*(space_per_gap+(1 if i<extra_space else 0))
                    line+=current_line[-1]
                    result.append(line)

                current_line = []
                current_length = 0

            current_line.append(word)
            current_length+=len(word)

        ## 处理最后一行，左对齐
        last_line = ' '.join(current_line)
        last_line+= " "*(maxWidth-len(last_line))
        result.append(last_line)

        return result


if __name__=="__main__":
    solution = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(solution.fullJustify(words,maxWidth))
    words = ["What","must","be","acknowledgment","shall","be"]
    print(solution.fullJustify(words,maxWidth))   

        


