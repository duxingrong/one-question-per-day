# 再次熟悉利用for循环构建链表
```c++
第一步，创建虚拟头节点
ListNode *dummyHead = ListNode(0);
ListNode *cur = dummyHead;
第二步，创建节点并且和链表连接
for (int i==0; i<n; i++){
    int data;
    std::cin>>data;
    ListNode *newNode = new ListNode(data);
    cur->next = newNode;
    cur = cur->next
}
```

# 找链表元素
可以利用while循环来实现,此时还要加上if来增加容错
```c++
cur  = dummyHead;
while (m--){
    if (cur==NULL){
        break;
    }
    cur = cur->next;
}
```

# 打印元素
```c++
if (cur == NULL || cur==dummyHead){
    std::cout<<"Output position out of bounds."
}else{
    std::cout<<cur->val<<std::endl;
