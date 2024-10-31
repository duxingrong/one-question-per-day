# 栈

栈这种数据结构只能在一侧(栈顶那一侧)进行插入和删除操作，而且是先进后出,允许进行插入和删除的那一端是栈顶，与之对应的一端是栈底。如果一个栈不包含任何元素，这个栈就被称为空栈

c++标准库中提供了一个名为std::stack的栈容器适配器,需要引入头文件
```c++
#include <stack>
```
创建栈:
```c++
stack<int> st;
stack<数据类型> 栈名称;
```


栈的常用操作:
empty(): 判断栈是否为空栈，如果为空返回true,否则返回false
push(): 进栈操作,将新的元素加入到栈中,新的元素成为栈顶元素
pop():出栈操作，栈顶元素从栈中离开
top():取出栈顶元素，但是不会移除它
size(): 获取栈的长度

```c++
st.push(1);
st.push(10);
st.push(100);
st.pop();

int topNumber = st.top();
bool isEmpty = st.empty();
int stackSize = st.size();
```


