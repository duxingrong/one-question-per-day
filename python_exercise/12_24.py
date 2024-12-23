"""

机器人能否返回原点

在二维平面上,有一个机器人从原点(0,0)开始,给出它的移动顺序,判断这个机器人在完成移动后是否在(0,0)处结束

移动顺序由字符串表示.字符move[i]表示其第i次移动.机器人的有效动作有R(右),L(左),U(上)和D(下).如果机器人在完成所有动作后返回原点,则返回true.否则返回false 

注意：机器人"面朝"的方向无关紧要."R"将始终使机器人向右移动一次,"L"始终让机器人向左移动等.此外，假设每次移动机器人的移动幅度相同

"UD" true
"LL" false

侮辱智商了属于是

"""

class Solution():
    def judgeCircle(self,s:str)->bool:
        #位置记录 pos[0]:上下 pos[1]:左右
        pos = [0,0] 
        for char in s:
            if char == "R":
                pos[1]+=1
            elif char == "L":
                pos[1]-=1
            elif char == "U":
                pos[0]+=1
            elif char == "D":
                pos[0]-=1
            
        return pos == [0,0]


