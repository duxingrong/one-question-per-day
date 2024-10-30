# 链表的插入

1. 找到要插入的位置的前一个节点，将之命名为cur,要插入的位置的下一个节点，将之命名为tmp,它们之间的关系是cur->next = tmp
2. 创建一个新的链表newNode,将cur的next指针指向newNode,即cur->next = newNode
3. 将newNode的next指针指向tmp,即newNode->next = tmp
```c++
ListNode *newNode = new ListNode(data);
ListNode *tmp = cur->next;
cur->next = newNode;
newNode->next = tmp;
```

# 删除链表的过程
只要找到删除节点的前一个节点cur，并将其next指针设置为指向当前节点的下下个节点，从而跳过了下一个节点，实现了节点的删除操作

# 打印链表
在函数内部，定义了一个名为cur的指针，它初始化指向head,即链表的头节点
什么时候链表迭代到最后一个节点呢？检查当前节点cur的下一个节点是否存在(不为NULL),当前节点的下一个节点为NULL时说明下一个节点为空节点，即链表的末尾
```c++
void printLinklist(ListNode* head){
    ListNode *cur = head;
    while(cur->next!=NULL){
        std::cout<<cur->next->val<<" ";
        cur = cur->next;
    }
    std::cout<<std::endl;
}
```
# 如何判断位置不合法?
当插入的位置n是一个小于等于0的数或者n大于链表的长度时，插入的位置不合法
我们这里链表的长度时刻在变化，所以我们可以提前定义一个变量listLen来指代链表的长度
```c++
int listLen=k;
if (n<=0 || n>listLen){
    std::cout<<"Insertion position is invalid."<<endl;
    continue; //及时跳出
}
```



