# 本节课程学习的基础



## C++函数基础
程序的启动，都是从main函数开始的，所以我们必须要先写一个main函数
```c++
int main()
{
return 0;
}
```
这里int 是返回的类型，main是函数名字，()里面的是形参列表，它定义了函数在被调用的时可以接受的参数类型，参数之间用逗号分割
ps: main函数返回类型一定是int

函数的形参列表就是我们往盒子扔进去的东西，我们可以把衣服或者水果放进去，而函数体是我们放进去的东西要经历的处理过程，经过函数的处理之后，返回的内容就是我们想要的结果

c++内置库 iostream 提供了输入(cin)和输出(cout)的功能

## 变量
需要在创建变量的时候指定他的类型，方便计算机存储
```c++
int a,b;
int a;
int b;
```
## 写入数据
```c++
std::cin>>a>>b;
```
std是一个命名空间，::符号是作用域操作符,在使用C++的便准库的时候，需要使用命名空间限定符来指明要使用的内容位于哪个命名空间中,为了避免不同标准库之间变量名冲突

输入运算符>> 
用于将数据从输入流读取到变量中
```c++
int number;
std::cin>>number;

int a,b ;
std::cin>>a>>b;
```
### 输出结果
```c++
std::cout<<result<<std::endl;
```
我们在输出结果的时候，每一个结果都需要单独占一行，std::endl就是这个作用，表示结束当前行

## 如何做到连续输入a，b
这里利用while循环
```c++
while (std::cin>>a>>b){
}
```
## 完整代码
```c++
#include <iostream>
int main(){
    int a,b;
    while (std::cin>>a>>b){
    int result=a+b;
        std::cout<<result<<std::endl;}
        }
    return 0;
```

## 数据类型
整型:
1. int 整数类型
2. char 字符类型
3. bool 布尔类型
浮点型:
4. float 单精度浮点数类型
5. double 双精度浮点数类型



