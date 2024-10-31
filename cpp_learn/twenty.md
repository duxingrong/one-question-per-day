# 队列
在排队过程中，想要加入队列，需要在队伍的最后一位(也被称为队尾)入队，想要离开队列，需要从队伍的第一位(也被称为队头)出队

队列是在队尾进行插入，在队头进行删除,满足先进先出

C++中使用队列需要引入头文件
```c++
#include <queue>
```

队列中的元素必须是相同的数据类型
```c++
queue<string> q;
```
队列的常用操作有以下几种
empty(): 判断队列是否为空.如果队列为空返回true,否则返回false
push():  入队操作，将新的元素添加到队列的尾部
pop():   出队操作，移除队列的头部元素
front(): 访问队列的头部元素,但不会将其移除
size():  获取队列的长度，即队列中元素的数量
```C++
q.push("jack");
q.push("Mike");
q.pop();
string name = q.front();
bool isEmpty = q.empty();
int queueSize = q.size();
```




