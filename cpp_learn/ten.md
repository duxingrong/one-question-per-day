# string的使用
字符表示单个字符，每个字符用单引号扩起来，比如'a'

字符串是一个可变长度的字符序列，可以包含多个字符，用双引号扩起来，比如"hello"


## 引入头文件
使用string 类型必须包含头文件<string>,作为标准库的一部分，string也被定义在命名空间std中

```c++
#include<string>
using std::string;
```

## 声明和初始化
```c++
string s1; //默认初始化，s1是一个空的字符串
string s2="hello"; //初始化一个值为hello的字符串
string s3(5,'a');  //连续5个字符'a'组成的串 ''
```

## 字符串的操作
和数组类似，字符串也提供了一系列对字符串的操作方法

加法:
```c++
string s1="hello";
string s2="world";
string s3=s1+" "+s2;
```

使用.size()获取字符串的长度
```c++
int length = s1.size();
```

使用下标来访问字符串中每一位字符
```c++
char c1 = s1[i]; 
```

使用empty()来判断字符串是否为空
```c++
if(s1.empty()){
//如果为空就执行，否则为false
}
```

## 输入输出string
```c++
int main(){
    string s;
    std::cin>>s;
    std::cout<<std::endl;
    return 0;
}
```

这个程序仿照整数，实现了从标准输入中读取文本，并将读取到的每个单词(以空格分隔)诸行输出到屏幕
```c++
int main(){
    string word;
    while(std::cin>>word){ //反复读取，直到到达末尾
        std::cout<<word<<std::endl;
    }
}
```
因为字符串读取到空格就会停止，表示这是一个单词，但现在我们需要读取完整的一行，这就要求我们遇到空格不会停止，这里就需要使用getline(),它会一直读取字符，直到遇到换行符(Enter键)或文件结束符(如果从文件读取)才算结束

```c++
#include<iostream>
#include<string>
using namespace std;
int main()
{
    string line;
    getline(cin,line);
    cout<<line<<endl;
}
```

## 在很多的判断中，我们通常会只用flag来当作标志，以便用来对程序进行调整
这在机器人中非常容易遇到，我们一个函数可以设置1,2,一个是启动代码，然后这时候就需要告诉机器人，下一次调用这个函数的时候，就是结束代码
利用flag =0 1,之间来回切换


## printf函数
用来指定保留几位小数,需要引入头文件<stdio.h>或者<cstdio>
```c++
#include<stdio.h>
int main(){
double number = 3.14159265359;
printf("%.2f\n",number);
return 0;
}
```

最后需要注意的是整数/整数得到的还是整数，这里要保留小数，就需要定义的时候，将sum定义成小数float











