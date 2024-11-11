# 并查集理论基础

并查集常用来解决连通性问题
主要有两个功能:
- 将两个元素添加到一个集合中。
- 判断两个元素在不在同一个集合。


## 原理讲解 
如何将两个元素添加到同一个集合中呢？

思路: 

我们将三个元素A，B，C(分别是数字)放在同一个集合，其实就是将三个元素连通在一起，如何连通呢？

只需要用一个一纬数组来表示，即`father[A]=B`,`father[B]=C`这样就表述A与B与C连通了(有向连通图)

```python
def join(u,v):
    u = find(u) #寻找u的根
    v = find(v) #寻找v的根
    if u==v :  #如果发现根相同，则说明在一个集合，不用两个节点相连直接返回
        return 
    father[V]=u
def find(u):
    if u==father[u]:  #如果根就是自己，直接返回
        return u
    else:
        return find(father[u]) #如果根不是自己，就根据数组下标一层一层向下找
```

我们的目的是判断三个元素是不是在同一个集合里
给出A： `father[A]=B` `father[B]=C` 找到根为C
给出B： `father[B]=C` 找到根为C

如何表示C也在同一个元素里呢？我们需要`father[C]=C`,即C的根也为C，这样就方便表示A，B，C都在同一个集合里了.
所以father数组初始化的时候要`father[i]=i`,默认自己指向自己
```python
def init():
    for i in range(n):
        father[i]=i
```

最后我们判断两个元素是否在同一个集合里，就需要通过find函数找到两个元素是否属于同一个根
```python
def isSame(u,v):
    u = find(u)
    v = find(v)
    return u == v
```

## 路径压缩
在实现find函数的过程中，我们知道，通过递归的方式，不断获取father数组下标对应的数量，最终找到这个集合的根
例如上面的   `father[A]=B`  `father[B]=C`  我们递归了多次,我们的目的只需要知道这些节点在同一个根下就可以，所以我们需要路径压缩，除了根节点外的其他节点全部都挂载到根节点下，这样我们在寻根的时候就很快，只需要一步
如何实现呢？只需要在递归中，让father[u] = find(father[father[u]]) 接住就好了 `father[A]=C`
因为在find函数向上寻找根节点，father[u]表述u的父节点，那么让father[u]直接获取find函数返回的根节点，这样就让节点u的父节点编成根节点
```python
def find(u):
    if u == father[u]:
        return u
    else:
        father[u]=find(father[u])
        return father[u]
```
路径压缩的效果并不是针对当前递归过程中的查找，而是为了加速未来的查找。一旦路径压缩完成，下次查找同一个节点时，只需要一步就能找到根节点，无需再次递归


## 并查集模板
```python
class DisjointSet():
    def __init__(self,n):
        self.length = n
        self.father = [0]*n

    #初始化
    def init(self): 
        for i in range(n):
            self.father[i]=i

    #寻找根
    def find(self,u):
        if u == father[u]:
            return u
        else:
            father[u]=self.find(father[u])
            return father[u]
    
    #判断u和v是否找到同一个根
    def isSame(self,u,v):
        u = self.find(u)
        v = self.find(v)
        return  u==v 

    #将v->u这条边加入并查集
    def join(self,u,v):
        u =self.find(u)
        v =self.find(v)
        if u==v:
            return  #如果已经在一个集合,就不用操作了
        father[v]=u
       
```
这里要注意在join函数中，我们需要寻找u和v的根，然后再进行连线在一起，而不是直接用u和v连线在一起











