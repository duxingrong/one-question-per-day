# 练习vector的遍历和访问操作

创建一个n个元素的容器，容器的默认值为0
```c++
vector<int> nums = vector<int>(n,0);
```

通过输入流给数组赋值的话，可以直接赋值
```c++
std::cin>>nums[i];
```

这里最后需要注意的是我们的这个题目要求的是每个结果都需要后面添加一行空行
```c++
std::cout<<result<<std::endl; 
```
这里这个std::endl; 是将光标换行的意思,不是直接空一行

所以我们还需要将光标向下移动一行，才是空一行
```c++
std::cout<<result<<std::endl;
std::cout<<std::endl;
```

本节课我们练习了容器的遍历和元素访问的操作，这是因为容器(数组)的遍历是经常使用的
