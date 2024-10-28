# if条件语句
```c++
if (condition){
    //执行代码快
} else{
//执行代码快
}
```

也可以用else-if 来添加多个分支结构
```c++
if (有西瓜)
{
    //如果有西瓜，则执行代码
} else if(有苹果) {
    //没有西瓜，有苹果，那就执行这里的代码
} else {
    //都没有，那就执行这里的代码
}
```

# 关系运算符
== : 相等
<  : 小于
>  : 大于
>= : 大于等于
<= : 小于等于
!= : 不等于

# 逻辑运算符
&& : 与
|| : 或
!  : 非

# break
break就是用来终止离它最近的while,do while, for 语句的，break之后的代码都不会执行

如果if 的代码只有一句的话，可以直接将这行语句放在if 之后 ，无需用{}
```c++
while(std::cin>>a>>b)
{
    if(a==0 && b==0)break;
    std::cout<<a+b<<std::endl;
}
```

# continue
用于控制跳出循环，他只能出现在 循环的内部，不过满足条件后，是跳过当前循环迭代的剩余部分,但是仍然继续循环



