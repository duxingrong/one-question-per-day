# 数组
C++中的数组时一种用于存储相同数据类型的元素的数据结构

这里科普什么叫做数据结构，数据结构就是数据在计算中被组织和存储的形式

数组的特点
1. 固定大小，数组声明的时候就确定了大小
2. 相同数据类型
3. 在内存中是连续存储的
4. 下标访问

c++中声明数组的方式是 
```c++
dataType arrayName[arraySize]
//例如
int myArray[5]; //在c++中，未初始化的局部变量数组的每个元素时不确定的，会包含内存中的垃圾值,如果数组是全局变量或定义为static，则会自动初始化为0
```
c++中使用大括号{}初始化数组的元素，也可以逐个赋值
```c++
int arr[5]={1,2,3,4,5}
int arr[3];
arr[0]=10;
arr[1]=4;
arr[2]
```
访问数组的元素，利用下标(从0开始)

利用for循环遍历所有的元素
```c++
for (int i=0; i<nums.size(),i++){
     std::cout<<nums[i]<<" ";
}
```
# vector
如果不清楚元素的确切个数，请使用vector

vector，作为c++标准库中的一个容器类，表示对象的集合，它可以动态地存储一组元素

这里注意要使用的话，一定要调用头文件,创建方式为vector<类型>名称

```c++
#include <vector>
vector<int>nums;
```

还有一些特殊的创建方式

创建一个包含整数元素的容器并且初始化元素
```c++
vector<int> myVector={1,3,4,5,6};
```
创建一个包含10个元素的数组，这里会将元素初始化为0
```c++
vector<int> myVector{10};
```
创建一个包含10个元素的数组并且指定初始化
```c++
vector<int> myVector{10,-1};
```
vector之所以可以调整大小，就是因为他拥有函数`push_back`
`push_back`负责将一个值推送到vector的尾端

同样的，我们可以使用下标索引vector的值
```c++
int value=vector[0];
```
还可以只用.size()来获取vector长度
```c++
int size=myVector.size();
```
vector除了.size() ,push_back, 还有下面三种内置函数
```c++
myVector.pop_back(); //删除vector末尾的元素
myVector.clear(); //清空vector中的所有元素
myVector.empty(); //判断vector是否为空
```






