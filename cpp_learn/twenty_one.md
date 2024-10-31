# 类和面向对象
C++是一种多范式编成语言，支持过程编程和面向对象编程,它将数据和操作数据的方法组织为类和对象

这里的"对象"实际上是对现实世界中所存在的事物的一种抽象，
我们可以将人抽象为一个类Person,它拥有一些"属性"和"方法"

"属性"表示Person类所具有的特征，比如姓名，年龄，性别，通过这些特征,我们可以描述一个人的基本状态
"方法"表示Person类的行为和功能,比如吃饭，睡觉，行走，通过这些动作，我们可以描述一个"人"的动态行为
```c++
Person{
    name;
    gender;
    age;
        //吃饭的方法
        eat(){
    }
        //行走的方法
        walk(){
    }
}
```
这里的这个Person类只是一个"模具",空有概念，而无法表示一个具体的人，只有创造一个类的实例(也就是我们所说的对象)，比如"张三，18，男"，才能真正的使用

简而言之:"类"是现实世界中的实体在计算机世界中的抽象概念,类可以看作是对象的模板，它定义了对象的结构和行为方式,可以用来创建具有相同属性和行为的多个对象，而对象是"类"的实现

# 类的基本写法
```c++
class 类名{
    访问修饰符:
        //成员变量，表示类的属性，定义方式和变量一致
        //成员方法，表示类的行为,定义方式和函数一致
}; 分号表示结束一个类
```

访问修饰符:
private(私有)，public(公有)，protected(受保护)

public：被修饰的成员在类的内部，派生类(子类)的内部和类的对象外部都可以访问

private:被修饰的成员只能在定义该成员的类的内部访问

protected:被修饰的成员只能在定义该成员的类的内部以及派生类汇总访问

```c++
class MyClass{
public:
    //成员变量
    int myAttribute;
    //成员方法
    void myMethod(){
        //方法实现
    }
};
int main(){
    //创建对象
    MyClass obj;
    //访问属性
    obj.myAttribute=42;
    //调用方法
    obj.myMethod();
    return 0;
}
```

# 封装
封装的主要目的是为了保证数据的安全性
我们可以通过封装隐藏对象中一些不希望被外部所访问到的属性或方法
1. 将对象的属性名，设置为private,只能被类所访问
2. 提供公共的get和set的方法来获取和设置对象的属性


```c++
class Circle{
private:
    int radius;

public:
    //set方法设置属性
    void setRadius(int r){
        if(r>=0)
        radius = r;
        else std::cout<<"半径不能为负数"<<std::endl;
    }
    //get方法获取属性
    int getRadius(){
        return redius;
    }
};
```

使用封装，我们隐藏了类的一些属性，具体的做法是使用get方法获取属性,使用set方法设置属性
如果希望属性是只读的，则可以直接去掉set方法,如果希望属性不能被外部访问，则可以直接去掉get方法



# 构造函数
类的构造函数和结构体的构造函数类似，用于初始化对象的成员变量

构造函数与类同名，没有返回类型，并且在对象创建时自动调用,基本语法包括
1. 函数名:与类名字相同
2. 参数列表:可以有零个或者多个参数，用于在创建对象时传递初始化信息
3. 函数体: 用于执行构造函数的初始化逻辑

const string& personName 表示string类型对常量引用，你可以传递字符串参数，但是不能在函数中修改这个参数的值
```c++
class Person{
private:
    int age;
    string name;
public:
    //默认构造函数
    Person(){
        age=20;
        name="Tom"
    }
    //带参数的构造函数
    Person(int personAge,const string&personName){
        age=personAge;
        name=personName
    }
}
int main(){
    //使用默认构造函数创建对象
    Person person1;
    //使用带参数的构造函数创建对象
    Person person2(20,"jerry");

    return 0;
}
```
下面的是构造函数的成员初始化列表写法，这种写法允许在进入构造函数主体之前对类成员进行初始化
```c++
Person(int personAge,const string& personName): age(personAge),name(personName){}
```

# 继承
继承的方式使得一个类获取到其他类中的属性和方法,在定义类时，可以在类名后指定当前类的父类(超类),子类可以直接继承父类中的所有属性和方法,从而避免编写重复性的代码,此外我们还可以对子类进行扩展

假设我们有一个图形类Shape,它具有一个属性和一个方法,属性为类型，方法为求图形的面积
```C++
class Shape{
protected:
    string type; //形状类型
public:
    //构造函数
    Shape(const string& shapeType):type(shapeType){}

    //求面积的函数
    double getArea() const {
        return 0.0;
    }
    //获取形状类型
    string getType() const {
        return type;
    }
};
```
在上面的代码中，getArea函数使用const用来修饰，是用来保证该函数不会修改对象的状态，使用const能保证对对象的访问是安全的

```C++
class Circle: public Shape{
private:
    int radius; //园的半径

public:
    //构造函数，调用Shape的构造函数，初始化了类型为"circle"
    Circle(int circleRadius):Shape("Circle"),radius(circleRadius){}

    //重写基类的方法
    double getArea() const override {
        return 3.14*radius*radius;//圆的面积公式
    }
    //获取半径
    int getRadius() const {
        return radius;
    }
};
```
在上面的代码中，图形类拥有shape属性和getArea,getType方法,而子类在父类这些属性和方法的基础上新增了radius属性和getRadius方法,并且在子类和父类中都有getArea这个方法,这被称为方法的重写，方法的重写需要override关键字.其意思是子类重写父类的方法，并提供自己的实现

重写条件：要重写基类的方法，子类中的方法必须与基类中的方法名称和参数类型相同。只有在这种情况下，子类方法会覆盖基类的方法


# 多态
多态常常和继承紧密相连，它允许不同的对象使用相同的接口进行操作，但在运行时表现出不同的行为,多态性使得可以使用基类类型的指针或引用派生类的对象，从而在运行时选择调用相应的派生类方法

c++中实现多态性的方法是通过virtual虚函数，比如下面的示例
```c++
class Shape{
public:
    virtual double calculateArea() const=0;
};
class Circle : public Shape{
private:
    int radius;
public:
    double calculateArea() const override {
        return 3.14*radius*radius;
    }
};
class Rectangle: public Shape {
private:
    int width;
    int height;
public:
    //构造函数，用于初始化width和height
    Rectangle(int w,int h):width(w),height(h){}
    //为了确保返回是double，显式转化
    double calculateArea() const override {
        return static_cast<double>(width*height);
    }
};
```
这里的virtual 在父类中定义了一个虚函数，而=0表示这是一个纯虚函数，即定义的函数在基类没有实现，但是要求它的派生类都必须提供这个函数的实现,这种抽象的方法使得Shape类成为一个抽象基类,不能被实例化,只能被用作派生其他类的基类

然后两个派生类Circle和Rectangle则是重写了calculateArea方法,他们提供了各自的实现，有着不同的计算逻辑


```c++
int main(){
    std::vector<Shape*> shapes;
    shapes.push_back(new Rectangle(4,5));
    shapes.push_back(new Circle(3));

    for (const Shape* shape: shapes){
        std::cout<<"Area:"<<shape->calculateArea()<<std::endl;
    }
    return 0;
}
```

# 代码编写
铺垫良久，Shape类应该具有方法获取面积和类型
```c++
class Shape{
public:
    //const =0; 表示纯虚构函数
    virtual double calculateArea() const =0;
    virtual string GetType() const=0;
};
```

然后两个类Circle 和Rectangle都继承Shape
```c++
class Rectangle : public Shape{
public:
    //初始化参数类表
    Rectangle(int width,int height):width(width),height(height){}
    //计算面积
    double calculateArea() const override {
        return static_cast<double>(width*height);
    }
    //获取类型
    std::string GetType() const override {
        return "Rectangle";
    }
private:
    int width;
    int height;
};
```
```c++
class Circle : public Shape{
public:
    //初始化参数列表
    Circle(int radius): radius(radius){}
    //计算面积
    double calculateArea() const override {
        return 3.14*radius*radius;
    }
    //获取类型
    std::string GetType() const override{
        return "Circle";
    }
private:
    int radius;
};
```
定义一个容器vector，用来放置建立的对象
```c++
int main(){
    //定义一个容器，用来放置Shape类型
    std::vector<Shape*> shapes;
    return 0;
}
```
Shape*是一个指针类型，表示指向Shape对象的指针,你可以用来来引用Shape类型的对象,也可以用来引用派生类的对象

```c++
while(true){
    string type;
    std::cin>>type;
    if (type=="end"){
        break;
    }
    if (type=="rectangle"){
        int width,height;
        std::cin>>width>>height;
        shapes.push_back(new Rectangle(width,height));
    }else if(type=="circle"){
        int radius;
        std::cin>>radius;
        shapes.push_back(new Circle(radius));
    }
}
```
遍历列表输出面积
引入iomanip库文件中的内容，当使用fixed时，浮点数会以固定小数点格式输出
setprecision()函数用于设置浮点数的精度,即小数点后的位数
std::fixed<<std::setprecision(2)

```c++
for (const Shape* shape: shapes){
    std::cout<<shape->GetType()<<" area: "<<fixed<<setprecision(2)<<shape->calculateArea()<<endl;
}
```
