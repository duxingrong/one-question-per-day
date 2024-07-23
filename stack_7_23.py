from typing import List

class Solution:
    def evalRPN(self, s: List[str]) -> int:
        stack = []
        for i in s:
            i=i.strip()
            if i in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                elif i == "/":
                    # 保证整除，并且向零方向取整
                    stack.append(int(a / b))
            else:
                stack.append(int(i))
        return stack.pop()

# 测试代码
s = ["2", "1","+","3", "*"]
solution = Solution()
result = solution.evalRPN(s)
print(result)  # 输出 9
