# 指针
c++中的指针就像是一个地址的引用，它帮助我们访问和操作存储在计算机内存中的数据

通俗的理解它就是一个指示牌，写着某个地方的地址,这个地址指向计算机内存中的一个特定位置，那里存储了一些数据

想要声明指针，需要使用*符号:
```c++
int *ptr //声明一个指向整数的指针
int* ptr //这样也是对的
```

指针想要存放某个变量的地址，需要先使用取址符&获取地址
```c++
int x=10;
int *ptr =&x; //将指针初始化为变量x的地址
```
想要获取这个地址值，需要使用*符号来访问，这个过程称为解引用
```c++
value = *ptr;//获取ptr指针指向的值(等于x的值)
```

指针和数组之间有密切的联系，数组名本质上是一个指向数组第一个元素的指针
```c++
int arr[3]={1,2,3};
int *ptr =arr; //数组名arr就是指向arr[0]的指针
```

指针还可以执行加法，减法等算术操作，以访问内存中的不同位置
```c++
int arr[5]={1,2,3,4,5};
int *ptr = arr; //指向数组第一个元素的指针
int value =*(ptr+2); //获取数组的第三个元素的值
```

除此之外，还有一个特殊的空指针值，通常表示为nullptr,用于表示指针不指向任何有效的内存地址
```c++
int *ptr = nullptr; //初始化为空指针
```


# 链表
与数组不同，链表的元素存储可以是连续的，也可以是不连续的，每个数据除了存储本身的信息(data数据域)之外，还存储有一个指示着下一个元素的地址的信息(next指针域)，给人的感受就好像这些元素是通过一条链串起来的

链表的第一个节点的存储位置被称为`头指针`,然后通过next指针域找到下一个节点，直到找到最后一个节点，最后一个节点的next指针域并不存在，也就是空的，在C++中，用null来表示这是一个空指针

为了简化链表的插入和删除操作，我们经常在链表的第一个节点前添加一个节点，称为虚拟头节点(dummyNode),头节点的数据域可以是空的，但是指针域指向第一个节点的指针


知识点:
头指针是链表指向第一个节点的指针，访问链表的入口，经常使用头指针表示链表，头指针是链表必须的

头节点是为了方便操作添加的，不存储实际的数据，头节点不一定是链表必须的


# 定义链表节点
传统的定义变量的方式只能使用一种数据结构，无法处理链表这种既包含数据域名，又包含指针域的复合结构，这就需要使用到`struct`结构体，结构体是一种用户自定义的数据类型，比如想要定义一个Person的结构体
```c++
struct Person{
    //使用数据类型 成员变量的形式来定义
    int age ;
    std::string name;
};
```

链表节点的结构体
```c++
struct ListNode{
    int val;  //存储节点的数据 
    ListNode *next; //下一个节点也是链表节点,所以指针的类型也要是LIstNode
};
```

结构体只是一个'模具',创建的Person结构体虽然具有age,name，但它只是一个Person的概念，无法表示具体的人，只有`初始化`后才能真正的使用

初始化结构体的方式有很多，我们这里使用构造函数的方式来进行构造函数的名称与结构体的名称相同，和其他函数不一样的是，构造函数没有返回类型，除此之外类似于其他的函数，构造函数也有一个(可能为空)的参数列表和一个函数体(可能为空)
链表结构体的构造函数代码如下:
```C++
ListNode(int x): val(x),next(nullptr){}
```
这里的`ListNode(int x)`表示定义一个接受整数参数x的名称为ListNode的构造函数(名称和结构体相同)
`:`表示初始化链表的开始，`val(x)`表示链表数据域的值被初始化为传递的参数`x`.
`next(nullptr)`则表示next指针被初始化为nullptr，表示没有下一个节点

完整的代码
```c++
struct ListNode {
    int val ;
    ListNode *next;
    ListNode(int x): val(x),next(nullptr) {}
};
```

# 链表的插入
如何完成在链表的结尾新插入链表的节点呢?
1. 创建一个新的链表节点，初始化它的值为val
2. 将新的节点放入到链表的尾部，接入链表，也就是当前链表的尾部next指向新节点
3. 新接入的链表节点变为链表的尾部

假设cur来表示当前链表的尾节点
```c++
ListNode *newNode = new ListNode(val); //通过new构造一个新的节点，节点的值为val
cur->next = newNode;  //cur节点的next节点是新节点，从而将新节点接入链表
cur=cur->next; //新插入的节点变更为新的尾节点，即cur发生了变更
```

知识点:

`new` 是一个运算符，它的作用就是在堆内存中动态分配内存空间，并返回分配内存的地址，使用方式一般为指针变量= new 数据类型 
```c++
int *arr =new int[5];//分配一个包含5个整数的数组的内存空间，并返回一个地址，指针arr指向这个地址
```

箭头语法(->):用于通过指针访问指针所指向的对象的成员，cur是一个指向ListNode结构体对象的指针，而next是ListNode结构体内部的一个成员变量(指向下一个节点的指针),使用cur->next表示访问cur所指的节点的next成员变量

cur->next 等价于 *(cur).next
```c++
ListNode *cur = new ListNode();
cur->val =10; //使用箭头语法设置节点的值
cur->next = nullptr; //将next指向nullptr
```
