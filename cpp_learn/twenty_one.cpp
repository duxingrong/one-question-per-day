/*
考虑一个简单的图形类层次结构,包括基类Shape和两个派生类Rectangle和Circle,每个类都有一个用于计算面积的方法,你的任务是编写一个程序，根据输入数据创建一个图形对象，然后计算并输出其面积

输入描述:
输入包括多行，每行包含一个图形的描述,描述的第一个单词是图形类型(rectangle或者circle),然后是与该图形相关的参数，对于矩形，参数是宽度和高度，对于圆形，参数是半径，输入以单词end结束

对于每个图像描述，输出其类型和面积，使用两位小数点精度输出面积

rectangle 5 3
circle 2
end

Rectangle area: 15.00
Circle area: 12.56
*/

#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
// 抽象Shape类
class Shape {
public:
  // 获取类型
  virtual std::string GetType() const = 0;
  // 计算面积
  virtual double GetArea() const = 0;
};
// 两个子类
class Rectangle : public Shape {
public:
  // 构造函数
  Rectangle(int width, int height) : width(width), height(height) {}
  // 计算面积
  double GetArea() const override {
    return static_cast<double>(width * height);
  }
  // 获取类型
  std::string GetType() const override { return "Rectangle"; }

private:
  int width;
  int height;
};
class Circle : public Shape {
private:
  int radius;

public:
  Circle(int radius) : radius(radius) {}

  std::string GetType() const override { return "Circle"; }

  double GetArea() const override { return 3.14 * radius * radius; }
};

int main() {
  // 创建一个容器存放对象
  std::vector<Shape *> shapes;
  while (true) {
    std::string type;
    std::cin >> type;
    if (type == "end") {
      break;
    } else if (type == "rectangle") {
      int width, height;
      std::cin >> width >> height;
      shapes.push_back(new Rectangle(width, height));
    } else if (type == "circle") {
      int radius;
      std::cin >> radius;
      shapes.push_back(new Circle(radius));
    }
  }
  // 范围for循环打印
  for (const Shape *shape : shapes) {
    std::cout << shape->GetType() << " area: " << std::fixed
              << std::setprecision(2) << shape->GetArea() << std::endl;
  }
  return 0;
}
