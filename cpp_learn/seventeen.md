# Set集合

C++中的集合std::set用于允许存储一组不重复的元素，并且元素的值按照有序排列，set基于红黑树实现，支持高效的关键字查询操作，可以用来检查一个关键字是否在set中

无序集合unordered-set类似于集合(Set),但是不会按照元素的值进行排序，而是由哈希函数的结果决定的

multiset则是一个用于存储一组元素，允许元素重复，并按照元素的值进行有序排列的集合

# set的使用

使用集合set需要先引入头文件
```c++
#include <unordered-set>
#include <set>
```

创建一个集合
```c++
unordered-set<int> mySet;
set<int> mySet;
multiset<int> myMultiSet;
```

想要向集合中插入元素需要使用insert()方法
```C++
mySet.insert(1);
mySet.insert(2);
mySet.insert(3);
```
想要往集合里删除元素需要使用erase方法
```c++
mySet.erase(1);
```
find()方法用于查找特定元素是否存在于集合中，如果find()方法找到了要查找的元素，他会返回指向该元素的迭代器，如果没有找到要查找的元素，它会返回一个指向集合的end()的迭代器,表示没有找到,所以可以通过是否等于end()，来确定集合中是否有要查找的元素
```c++
if (mySet.find(i) !=mySet.end()){ //只要不等于，就说明在集合里面
}
```





