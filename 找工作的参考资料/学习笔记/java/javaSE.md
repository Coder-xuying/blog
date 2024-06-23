## java基础

### 1.java简介

#### java特性和优势

- 简单性
- 面向对象
- 可移植性(跨平台)
- 高性能
- 分布式
- 动态性(通过反射实现的)
- 多线程
- 安全性健壮性

#### java三大版本

- javaSE：标准版(桌面程序，控制台)
- javaME：嵌入式开发(手机，小家电)
- javaEE：企业级开发(web段，服务器)

#### JDK、JRE、JVM

- JDK：java Development kit  (java 开发工具包)
- JRE：java Runtime Environment （java运行时环境）
- JVM: Java Virtual Machine

![image-20210208154732133](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210208154732.png)

#### java程序运行机制

- 编译型
  - 类似于把整个整本书翻译一下，
- 解释型
  - 说一句，翻译一句

![image-20210208161523976](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210208161524.png)

java是先编译，再解释。两个都有



### 2.java基础语法

#### 1.注释、标识符、关键字

> 注释

注释相当于**笔记**，是不会被执行的。让人更容易理解代码。**写注释是一个非常好的习惯**

- 单行注释 	`//​`

  ```java
  //输出xx
  ```

- 多行注释`/**/`

  ```java
  /*
  我是多行注释
  */
  ```

- javaDoc:文档注释 `/** */`

  ```java
  /**
  *文档注释
  */
  ```

> 标识符

**关键词**

![image-20210306155315645](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210306155315.png)

- 标识符应该以字母、$、下划线_开始
- 首字符之后，可以是上面那些和数字的任何组合
- 不能用关键字作为变量名或方法名
- 标识符是大小写敏感的
- 可以使用中文，但是不介意使用

#### 2、数据类型

**强类型语言**

要求变量的使用要严格规定，所有变量必须要先定义之后才能使用。

**弱类型语言**

> 基本类型

数值类型：

**字节：**计算机内最小的单位是位，`bit or b`，0101四位的一个数。一个字节是八位，B表示。1B = 8 bit

- 整数类型
  - byte: 一个字节
  - short：两个字节
  - int：四个字节
  - long：八个字节
- 浮点类型
  - float：四个字节
  - double：八个字节
- 字符类型
  - char：2个字节

boolean类型：1位。true和false

````java
/**
八大基本类型
*/
//整数
int num1 = 10; //最常用
byte num2 = 15;
short num3 = 30;
long num4 = 30L;

//小数，浮点数
float num5 = 50.1F;
double num6 = 3.1415926;

//字符
char name = 'x'; //是一个字符，不是串

//Boolean
Boolean flag = true;
````

**扩展**：

==整数==

二进制:0b

八进制：0

十六进制：0x

---

==浮点数==

float 是有限的，离散的，有舍入误差，接近但不等于

==避免使用浮点数进行比较==

**银行业务用什么？**  BigDecimal数据工具类

---



**字符**





> 引用类型



> 类型转换

运算中，不同类型的数据先转化为同一类型，然后进行计算

高容量的类型转换到低容量的类型是，需要用到强制转换，存在精度损失。 

**优先级**（由低到高）

byte，short，char，int，long，float，double

由低往高转就自动转换，由高往低需要强制转换

**注意**：

1. 存在内存溢出，那么数值就会出错，比如Byte最大值为127，如果把128转换成byte就会出现奇怪的数值
2. 不能对布尔值进行转换
3. 不要把对象类型转换为不相干的类型

- 强制转换 

  ```java
  int a = 120;
  Byte b = (int)a;
  ```

- 自动转换

3、变量、常量

> 变量

变量就是可以变化的量

java变量是程序中最基本的存储单元，其要素包括变量名，变量类型和**作用域**。

**作用域**：

- 类变量: `static`

  - 从属于类，和类一起创建，一起死亡

- 实例变量：从属于对象

  - 可以不初始化，会使用数据类型对应的默认值

  - ```java
    public class Demo{
        String name;
         public static void main(String[] args) {
            //局部变量：
           Demo demo =  new Demo();
           demo.name;//实例变量
        }
    }
    ```

- 局部变量：方法里面的

  - 必须声明和初始化

> 常量

常量就是一种特殊的变量的，被设定之后不允许改变。一般用大写字母表示

`final`



> 变量的命名规范

![image-20210306173052815](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210306173052.png)

#### 3、运算符

支持的运算符：

![image-20210308093639837](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210308093639.png)

使用除法的时候，记住int要转成浮点类型

做加法的时候，整数型如果没有long的话，做完运算之后都是int类型。

> 一元运算符

++ 、--

a++   先赋值，再自增

++a   先自增，再赋值

> 逻辑运算符

&&逻辑与

- 短路的，就是判断第一个不满足之后，就不判断第二个了

   ||逻辑或  

  !  非

----

位运算

A&B   与

A| B  或

~B  非

A^B 异或

效率高

> 三元运算符

x ?  y:  z    x为true则是y，否则是z

#### 4、文档注释

JavaDoc，用来生成自己的API

![image-20210308105050861](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210308105050.png)

加在类上面，就是类注释，加在方法上面就是方法注释

`javadoc -encoding UTF-8 -charset UTF-8  xxx.java`



### 3.java流程控制

#### 1.Scanner

```java
Scanner scanner = new Scanner(System.in);

scanner.hasNext();
String str = scanner.next();

//以回车为结束符，可以获得空格
scanner.hasNextLine();
String str = scanner.nextLine();

scanner.close();
```

- next
  - 一定要读到有效字符后才能结束输入
  - 对输入有效字符之前遇到的空白，next()方法会将其自动去掉
  - 只有输入有效字符后，才能将后面输入的空白作为分隔符或结束符
  - next()不能得到带有空格的字符串

#### 2、switch

```java
switch (i){
    case 1: break;
    case 2:
        System.out.println("ok");break;

    default:
        break;
}
```

每个case后面都加上break



#### 3、循环结构

> while循环

在循环里面，要设置条件让循环停止

要避免死循环

==do while==至少执行一次

> For循环

增强for

```java
int[] num = {10,20,30,40,50};
for (int i : num) {
    System.out.println(i);
}

```

---

break、continue、goto

### 4.java方法

> 命令行传参

在cmd中运行的时候注意到 package，需要退出到最外面的文件夹里，然后

```java
$java com.xy.xx.className  //必须写全类名
```

> 可变参数

- 一个方法最多只能有一个可变参数，而且必须放在最后面
- 接受到的那个可变参数是一个数组
- 在指定类型后加一个省略号

```java
 public static void main(String[] args) {
        test(1,2,3,4,5);
    }

    public static void test(int... i){
        for (int i1 : i) {
            System.out.println(i1);
        }
    }
```

### 5.java数组

数组的四个基本特点

- 长度是确定的，一旦被创建，大小不能改变
- 元素是相同类型
- 数组中的元素可以是任何数据类型，包括基本类型和引用类型
- 数组的变量属于引用类型，数组也可以看成对象

#### 初始化

> 静态初始化

```java
//静态初始化：创建+赋值
        int[] a = {1,2,3,4,5};
```

> 动态初始化

```java
//动态初始化,包含默认初始化
int[] b = new int[10];
b[0] = 10;//后期赋值
```

数组会有对应类型的默认值。

#### Arrays类

数组的工具类，里面有很多方法

```java
public static void main(String[] args) {
    int[] a  = {45,13,56,13,6,31,45};

    System.out.println(Arrays.toString(a));
    Arrays.sort(a);
    System.out.println(Arrays.toString(a));
    Arrays.fill(a,1);

}
```

### 6.面向对象

OOP的本质是：以类的方式组织代码，以对象的组织封装数据



三大特性：

- 封装
- 继承
- 多态

> 构造器

一个类即使什么都不写，也存在一个构造方法

```java
public class Person {
    String name;
    
    //构造方法
    public Person(){
        this.name = "xy";
    }
    
     //一旦定义了有参构造，无参就必须显示定义
    public Person(String name){
        this.name = name;
    }
}

```

构造器

- 和类名相同
- 没有返回值

作用：

- new 本质是在调用构造方法
- 初始化对象的值

> 创建对象内存分析

![image-20210311110324502](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210311110324.png)



##### 封装

该露的露，该藏的藏。*高内聚，低耦合*。高内聚就是类的内部数据操作细节自己完成，不允许外部干扰。低耦合：只暴露少量的方法给外部使用。

**属性私有，get/set方法**



##### 继承

继承的本质是对某一批类的抽象，从而实现对现实世界更好的建模。

extends扩展，子类是父类的扩展。

java里只有单继承，没有多继承

**Object类**：所有的类都是直接或间接继承Object类



> super

```java
public class Student extends Person {
     String name = "cc";

    //调用父类的构造器时，必须把super放在第一个
    public Student() {
        super();
    }

    public void test(String name){
        System.out.println(name);
        System.out.println(this.name);
        System.out.println(super.name);
    }
}
```

**super VS this**

![image-20210311191804800](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210311191804.png)

> 重写

```java
public class B {
    public void test(){
        System.out.println("B->test");
    }
}

public class A extends B {

    public  void test(){
        System.out.println("A->test");
    }
}

public class Application {
    public static void main(String[] args) {
        A a = new A();
        a.test();

        //父类的引用指向了子类
        B b = new A();  //子类重写了父类的方法
        b.test();
    }
}

//输出
//A->test
//A->test
```

重写：

- 需要有继承关系，子类重写父类的方法
  - 方法名必须相同
  - 参数列表必须相同
  - 修饰符：范围可以扩大，父类是private，子类可以变成public  （public > protected >Default>private）
  - private 的不能被重写

为什么需要重写：

- 父类的功能子类不一定需要，或者不一定满足

静态方法（类方法）无法重写，重写是对动态方法而言的，因为静态方法是随着类加载而加载的

```java
class A extend B ;   A 重写 B中的 test（）方法
A x1 = new A();
B x2 = new A();

x1.test();
x2.test();
//如果是static ，那么调用的方法和左边的引用有关
//如果是可以重写的方法，那么调用的都是子类的方法
```

static、private、final  修饰的方法不能重写

##### 多态



> instanceof

```java
Student student = new Student();

//类之间的关系是：Student 继承Person   
//Teacher 继承Person


System.out.println(student instanceof Person);

//这里会报错，因为student和Teacher没有关系
System.out.println(student instanceof Teacher);
```

instanceof是一个转换比较的过程



> 类型转换



##### static

```java
//静态代码块  匿名代码块   构造器  执行顺序及过程，执行一下下面的代码就清楚了
public class blockTest {
    {
        System.out.println("匿名代码块");
    }
    static {
        System.out.println("静态代码块");
    }

    public blockTest(){
        System.out.println("构造器");
    }

    public static void main(String[] args) {
        blockTest blockTest1 = new blockTest();

        System.out.println("============================");
        blockTest blockTest2 = new blockTest();

    }
}
```

```java
//静态导入包，就可以直接使用它的方法
import static java.lang.Math.*;
就可以直接使用Math中的方法
 public static void main(String[] args) {
 	Random();
 }
```

##### abstract

```java

//抽象类
public abstract class Action {

    //抽象方法，只有方法名字，没有方法的实现
    public abstract void doSomething();
}
```

特点：

- 不能new这个抽象类，只能靠子类去实现它
- 抽象类里面**可以写普通方法**，但是抽象方法必须在抽象类里面
- 就很像接口，但是约束更少一点。
- 类只能单继承
- 抽象类有构造方法

##### 接口

**专业的抽象，专门约束**

接口就是规范，定义的一组规则

接口可以多实现

```java
public interface UserService {
	//一般不会在接口中定义常量的    
    //接口中的常量默认是public static final
    public static final int AGE = 99;
    
    //接口中的方法默认是 public abstract
    public abstract void run();
}
```

![image-20210312153939946](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210312153940.png)



### 7.注解

Annotation

**注解的作用**:

- 对程序作出解释。
- 可以被其他程序（如：编译器）读取

注解的格式：@xxxx(value="") 可以加参数

#### 内置注解

![image-20210322182532298](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210322182532.png)

```java
@Deprecated //告诉我们这个方法不推荐程序员使用，但是可以使用，或者存在更好的方式
@SuppressWarnings("all")   //里面定义了参数，所有要传个参数进去 
```

#### 元注解

元注解的作用就是**负责注解其他注解**的注解。有4个

- @Target   ： 用于描述注解的使用范围
- @Retention ： 表示需要在什么级别保存该注释信息，用于描述注解的生命周期。（SOURCE<CLASS<**RUNTIME**）
- @Documented
- @Inherited

```java
@Target(value = {ElementType.METHOD})  //表示我们的注解可以用在哪些地方
@Retention(value = RUNTIME)  //表示我们的注解在哪里还有效。runtime>class>source
@Documented       //表示是否将我们的注解是否生成在JavaDOC中
@Inherited     //子类可以继承父类的注解    
@interface MyAnnotation{
//自定义的注解
}
```

#### 自定义注解

`@interface`  自动继承了java.lang.annotation.Annotation接口

![image-20210322184040619](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210322184040.png)

```java
/自定义注解
public class Test03 {

    @MyAnnotation3("nihao")
    @MyAnnotation2(name = "asihi") //如果没有默认值，就必须给注解赋值
    public void test(){

    }
}
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation2{

    //注解的参数：参数类型  + 参数名()   别忘了后面的()
    String name() default "默认值";
    int age() default 0;
    int id() default  -1;  //如果默认值为-1，代表不存在

}

@interface  MyAnnotation3{
    String value();  //只有一个值的时候，用value，就可以 @MyAnnotation3("nihao")不需要写参数名
}
```



### 8.反射

java有了反射机制，所有才变成了一个动态语言的一些特性

> 静态语言和动态语言

![image-20210322212920915](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210322212922.png)

> 反射

反射机制允许程序在执行期借助RecfletionAPI取得任何类的内部信息。

Class类是反射的核心类

#### 1、获得类对象的三种方式

```java
public class Test02 {
    public static void main(String[] args) throws ClassNotFoundException {
        Person person = new Student();
        System.out.println("这个认识"+person.name);
		//方式1
        Class c1 = person.getClass();
        System.out.println(c1.hashCode());

        //方式2
        Class<?> c2 = Class.forName("reflection.Student");
        System.out.println(c2.hashCode());

        //方式3
        Class<Student> c3 = Student.class;
        System.out.println(c3.hashCode());


        //方式4：基本内置类型的包装类有一个TYPE属性
        Class<Integer> c4 = Integer.TYPE;
        System.out.println(c4);
        //方式5：获得父类
        Class c5 = c1.getSuperclass();
        System.out.println(c5);
    }
}

class Person{
    public String name;
    public Person() {

    }
    public Person(String name) {
        this.name = name;
    }
    
}

class Teacher extends Person{
    public Teacher() {
        this.name = "老师";
    }
}

class Student extends Person{
    public Student() {
        this.name = "学生";
    }
}
```

#### 2、所有类型的CLass对象

```java
public class Test01 {
    public static void main(String[] args) {
        //alt可以选中多行
        Class<Object>       c1 = Object.class;        //类
        Class<Comparable>   c2 = Comparable.class;    //接口
        Class<String[]>     c3 = String[].class;        //一维数组
        Class<int[][]>      c4 = int[][].class;             //二维数组
        Class<Override>     c5 = Override.class;            //注解
        Class<ElementType>  c6 = ElementType.class;            //枚举
        Class<Integer>      c7 = Integer.class;             //基本数据类型
        Class<Void>         c8 = void.class;            //void
        Class<Class>        c9 = Class.class;           //Class

        System.out.println(c1);
        System.out.println(c2);
        System.out.println(c3);
        System.out.println(c4);
        System.out.println(c5);
        System.out.println(c6);
        System.out.println(c7);
        System.out.println(c8);
        System.out.println(c9);
    }
}
```

#### 3、类加载分析

java的内存：

- 堆
- 栈
- 方法区

![image-20210324212303969](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210324212304.png)

> **类的加载过程**:

- **类的加载**：将类的Class文件读入内存，并为之创建一个java.lang.Class对象，这个过程由**类加载器**完成。
- **类的链接**：将java 的二进制代码合并到JVM的运行状态中。
  - 验证:确保加载的类信息复合JVM规范
  - 准备：正式为类变量(static)分配内存，并设置初始值，这些内存都将在方法区中分配。
  - 解析：虚拟机的常量池内的符号引用(常量名)替换为直接引用(地址)的过程
- 初始化：
  - 执行类构造器<clinit>()方法的过程。类构造器<clinit>()方法是由编译期自动收集类中的所有**类变量**的赋值动作和静态代码块中的语句合并产生的
  - 当初始化一个类的时候，发现其父类还没有进行初始化，则需要先触发其父类的初始化。
  - 虚拟机会保证一个类的<clinit>()方法在多线程环境中被正确加锁和同步.

> 类的初始化

![image-20210325160254439](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210325160254.png)

被动引用：

```java
public class Test03 {

    static {
        System.out.println("Main类被加载");
    }

    public static void main(String[] args) {
        System.out.println(Son.m);  //这里不会有其他类被加载的过程
        Son[] sons = new Son[5];     //这里不会有其他类被加载的过程
    }
}

class Son extends Father{
    static {
        System.out.println("子类被加载");
    }
}

class Father{
    static final int m =8;

    static int M = 1;

    static {
        System.out.println("父类被加载");
    }
}
```





#### 4、类的加载器

类加载的作用：将class文件字节码内容加载到内存中，并将这些静态数据转换成方法区的运行时数据结构，然后在堆中生成一个代表这个类的java.lang.Class对象，作为方法区中类数据的访问入口。

![image-20210325161327698](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210325161327.png)

![image-20210325161230910](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210325161230.png)



类加载器有如下三种：

- 引导类加载器：JVM自带的类加载器，负责java平台核心库。rt.jar。该加载器无法直接获取
- 扩展类加载器：负责jre/lib/ext 目录下的jar包
- 系统类加载器：将指定项目的jar包加入进去，是最常用的加载器

```java
//获取系统类加载器
ClassLoader systemClassLoader = ClassLoader.getSystemClassLoader();
System.out.println(systemClassLoader);
//获取系统类加载器的父类--扩展类加载器
ClassLoader parent = systemClassLoader.getParent();
System.out.println(parent);
//获取扩展类加载器的父类加载器-- 根加载器 （c/c++）
ClassLoader parent1 = parent.getParent();
System.out.println(parent1);  //null，是c++编写的，java获取不到


//当前类的加载器
ClassLoader classLoader = Class.forName("reflection_.Test03").getClassLoader();
System.out.println(classLoader);
//jdk里的包是由根加载器
ClassLoader classLoader2 = Class.forName("java.lang.Object").getClassLoader();
System.out.println(classLoader2);

//如何获得系统类加载器的路径
System.out.println(System.getProperty("java.class.path"));
```

#### 5、获取类的信息

> 获得类的属性

```java
//getDeclaredxxx  在反射中能够获得所有的方法和属性，  getXXX只能获得public的。
// 同理 c1.getField("name");  只能获得public 需要用getDeclareField("name")


//只能找到public的属性
Field[] fields = c1.getFields();


//能找到所有的属性
Field[] declaredFields = c1.getDeclaredFields();
for (Field declaredField : declaredFields) {
    System.out.println(declaredField);
} 	
```

- getDeclaredxxx  在反射中能够获得**所有的**方法和属性，  getXXX只能获得**public**的。
- 同理 c1.getField("name");  只能获得public 。getDeclareField("name") 可以获得私有的
- getFields()只能找到public的属性。getDeclaredFields()能找到所有的属性

>获得类的方法

- getMethods()  获得**本类和父类**的所有public方法
- getDeclaredMethods() 只获得本类的所有方法，包括私有的
- c1.getDeclaredConstructor(int.class,String.class):获得指定构造器，这里的参数必须和构造器放参数的位置相同，否则会报错

```java
//获得方法     本类及其父类的所有public方法
Method[] methods = c1.getMethods();
for (Method method : methods) {
    System.out.println(method);
}

//获得本类的所有方法，包括私有的                  
Method[] declaredMethods = c1.getDeclaredMethods(); 
for (Field declaredField : declaredFields) {
   System.out.println(declaredField);
}


 //获得指定方法
Method getName = c1.getMethod("getName", null);
Method setName = c1.getMethod("setName", String.class);
System.out.println(getName);
System.out.println(setName);

//获得构造器
Constructor<?>[] constructors = c1.getConstructors();
for (Constructor<?> constructor : constructors) {
    System.out.println(constructor);
}

//获得指定构造器，这里的参数必须和构造器放参数的位置相同，否则会报错
Constructor<?> declaredConstructor = c1.getDeclaredConstructor(int.class,String.class);
System.out.println("指定"+declaredConstructor);
```

#### 6、创建对象

> 无参构造器创建对象

本质调用了User里的无参构造器，如果没有无参构造方法，就会报错

```java
 Class<?> c1 = Class.forName("reflection.User");

        //构造对象
        User user = (User) c1.newInstance(); //本质调用了User里的无参构造器，如果没有无参构造方法，就会报错
        System.out.println(user);
```

> 有参构造创建对象

先获取有参构造方法，然后往里面添加参数就可以创建对象。

```java
//调用的是有参构造
Constructor<?> constructor = c1.getConstructor(int.class,String.class);  //User 两个属性age，name
User user2= (User) constructor.newInstance(  18,"xu");
System.out.println(user2);
```

>反射调用方法

```java
//通过反射使用类的方法
User user3 = (User) c1.newInstance();
Method setName = c1.getDeclaredMethod("setName", String.class);
//激活方法，往哪个对象传入参数
//invoke(对象,方法的值)
setName.invoke(user3, "test_");
System.out.println(user3.getName());
```

> 通过反射操作属性

这里是直接暴力改值，并没有调用set方法

```java
//通过反射给属性赋值
User user4 = (User) c1.newInstance();
Field name = c1.getDeclaredField("name");
name.setAccessible(true);    //关闭private修饰   
name.set(user4, "test_2");
System.out.println(user4.getName());
```

使用反射调用方法效率没有普通调用高，如果想用反射效率高一些就关闭AC  `method.setAccessible(true);`

#### 7、通过反射获得泛型

```java
//测试类
public void test01(Map<String ,User> map, List<User> list){
    System.out.println("test01");
}
public Map<String ,User> test02(){
    System.out.println("test02");
    return null;
}


Method method01 = Test07.class.getMethod("test01", Map.class, List.class);
Type[] genericParameterTypes = method01.getGenericParameterTypes();
for (Type genericParameterType : genericParameterTypes) {
    System.out.println("=========");
    if (genericParameterType instanceof ParameterizedType){
        Type[] actualTypeArguments = ((ParameterizedType) genericParameterType).getActualTypeArguments();
        for (Type actualTypeArgument : actualTypeArguments) {
            System.out.println(actualTypeArgument);
        }
    }
}

   //获得返回值的泛型
Method method2 = Test07.class.getMethod("test02");
Type genericReturnType = method2.getGenericReturnType();
if(genericReturnType instanceof ParameterizedType){  //判断里面的是不是这个泛型属性
    Type[] actualTypeArguments = ((ParameterizedType) genericReturnType).getActualTypeArguments();
    for (Type actualTypeArgument : actualTypeArguments) {
        System.out.println("--"+actualTypeArgument);
    }
}
```

#### 8、通过反射获取注解的信息(spring注解)

```java
@Table("学生")
class Student{
    @Filed(name = "age",type = "int",length = 10)
    private int age;
    @Filed(name = "name",type = "string",length = 10)
    private String name;

    public Student(){

    }
    public Student(int age, String name) {
        this.age = age;
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

//类名的注解
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@interface Table{
    String value();
}

//属性的注解
@Target(ElementType.FIELD)  
@Retention(RetentionPolicy.RUNTIME)  //必须要有这个才能在运行时获得里面的值
@interface Filed{
    String name();
    String type();
    int length();
}
```

---

获取类的注解

```java
Class<?> c1 = Class.forName("reflection.Student");
Annotation[] annotations = c1.getAnnotations();
//获取注解
for (Annotation annotation : annotations) {
    System.out.println(annotation);
}
```

获取类的注解的值

```java
Class<?> c1 = Class.forName("reflection.Student");
//获取注解的值
Table table = c1.getAnnotation(Table.class); //获取指定注解
String value = table.value();
System.out.println(value);
```

获取属性的注解的值

```java
Class<?> c1 = Class.forName("reflection.Student");

Field name = c1.getDeclaredField("name"); //通过反射获取属性的信息
Filed annotation = name.getAnnotation(Filed.class);  //根据上面获取的熟悉感从里面获取出注解的信息
//直接输出注解里的值
System.out.println(annotation.name()); 
System.out.println(annotation.length());
```

### 9、网络编程

#### 1.1、网络通信的要素

![image-20210708110706362](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210708110706.png)



#### 1.2 Ip

类 InetAddress

- 唯一定位一台网络上计算机
- 127.0.0.1 ： 本机 localhost
- ip地址分类
  - ipv4/ipv6
  - 公网
  - ABCD 类地址
  - 192.168.xx。xx



```java
InetAddress inetAddress = InetAddress.getByName("www.baidu.com");
System.out.println(inetAddress.getHostAddress());
System.out.println(inetAddress.getHostName());
```

#### 1.3端口

- 公有端口
  - HTTP：80
  - Https：443
  - FTP：21
  - Telent ：23

![image-20210708112756297](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210708112756.png)



```java
InetSocketAddress socket = new InetSocketAddress("127.0.0.1", 8080);
System.out.println(socket);
System.out.println(socket.getHostName()); // host
System.out.println(socket.getPort());
```

#### 1.4 通信协议

TCP/TP协议簇

TCP、UDP

![image-20210724160553252](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210724160553.png)

#### 1.5 TCP



### 10、IO

#### 1.流的概念

> 什么是流

内存与存储设备之间传输数据的**通道**。

![image-20210715162903385](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715162903.png)





#### 2.流的分类

> 按方向 （重要）

输入流：存储设备的内容 -》 内存中

输出流：内充中的内容-》存储设备

> 单位

字节流：以字节为单位，可以读写所有数据

字符流：以字符为单位，只能读写文本数据

> 功能

节点流：具有实际传输数据的读写功能

过滤流：在节点流的基础上增强功能

#### 3.字节流

##### 1.父类

父类是一个**抽象类**：

InputStream：

![image-20210715163408104](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715163408.png)

OutputStream:

![image-20210715163502593](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715163502.png)

##### 2.文件字节流

![image-20210715163634253](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715163634.png)

![image-20210715163704362](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715163704.png)



```java
FileInputStream fis = new FileInputStream("d:\\a.txt");
// 单个字节读取
//            int data = 0;
//            while((data=fis.read())!=-1){
//                    System.out.println((char) data);
//            }
//            fis.close();

//输出流
FileOutputStream fos = new FileOutputStream("d:\\b.txt");
//一次读多个字节
byte[] buf = new byte[3];
int count=0;
while( (count = fis.read(buf))!=-1 ){
    System.out.println(new String(buf,0,count));
    // 0-count就是写的长度
    fos.write(buf,0,count);
}
```

##### 3.字节缓冲流

![image-20210715165557092](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715165557.png)

![image-20210715165659689](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715165659.png)

```java
 @Test
public  void Demo02() throws Exception{

    FileInputStream fis = new FileInputStream("d://a.txt");
    BufferedInputStream bis = new BufferedInputStream(fis);
    int data = 0;

    /**
                 * bis里面有缓冲区 8k ， 第二次读就不用重新读文件
                 *  private static int DEFAULT_BUFFER_SIZE = 8192;
                 *  也可以自己弄一个缓冲区，byte[] buf = new byte[1024];
                 *  data = bis.read(buf);
                 */
    while((data=bis.read())!=-1){
        System.out.print((char) data);
    }
    bis.close();
    fis.close();
}
```



> output

![image-20210715174831066](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715174831.png)



```java
BufferedOutputStream bos = new BufferedOutputStream(fos);
bos.write("heelow".getBytes());  // 这个先写入缓冲区，并不在文件里面
bos.flush();  // 写一次刷新一次，将数据刷新进去
bos.close(); // close的时候会一次性的把缓冲区的所有数据都放进文件
```

##### 4、对象流

![image-20210715175449269](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715175449.png)

```java
		/**
         * 使用ObjectOutputStream
         * Student 必须要实现Serializable接口
         * Student 里面的类属性也要实现Serializable接口 ，比如加了个属性是Teacher类
         * 序列化过程
         * @throws Exception
         */
@Test
public void Demo3() throws Exception {
    Student student = new Student();
    FileOutputStream fos = new FileOutputStream("d:\\student.txt");

    ObjectOutputStream ois = new ObjectOutputStream(fos);
    ois.writeObject(student);
    ois.writeObject(student);
    ois.writeUTF(new String("hello,word"));
    ois.close();
}


		/**		
         * 反序列化
         * @throws Exception
         */
@Test
public void Demo4() throws Exception{
    FileInputStream fis = new FileInputStream("d:\\student.txt");
    ObjectInputStream ois = new ObjectInputStream(fis);
    Student student = (Student) ois.readObject();
    Student student2= (Student) ois.readObject();
    String str = ois.readUTF();
    System.out.println(student.id);
    System.out.println(student2.name);
    System.out.println(str);
}
```



Student类

```java
public class Student implements Serializable {

    private static final long serialVersionUID = 7564399836964512135L;
     int id = 1;
     String name;
}  // 在序列化之前加上版本号之后，即使修改了Student也能反序列化,否则会报错
```



注意事项：

- 序列化必须实现Serializable接口
- 序列化类中对象属性也要实现Serializable接口
- 序列化版本号ID
- 使用`transient` 修饰属性，这个属性不会被序列化(值没有了)
- 静态属性不能被序列化

当要序列化多个对象的话，用集合来完成(比如list等)。

#### 4.编码方式

> 字符编码

![image-20210715202737882](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715202738.png)



当编码和解码用到的方式不一样的时候，会出现乱码

#### 5.字符流

![image-20210715203114406](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715203114.png)

读的是中文，乱码 了，中文一个汉字是三个字节，字节流读的话就是一次读一个字节，就出现问题了。



##### 1.字符流父类(抽象类)

![image-20210715203157926](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715203158.png)

> Reader

![image-20210715203225329](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715203225.png)





> writer

![image-20210715203306833](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715203306.png)



##### 2、文件字符流

![image-20210715203337911](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715203338.png)

![image-20210715203405765](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715203405.png)



> FileReader

**默认是UTF-8**

```java
@Test
public void Demo5() throws  Exception{
    FileReader fr = new FileReader("d:\\hello.txt");
    int data= 0;
    //这里是读取一个字符，好好学习读四次
    while ((data= fr.read())!=-1){  
        System.out.print((char)data);
    }
    System.out.println("1");
    FileReader fr2 = new FileReader("d:\\hello.txt");

    // 建立一次读取的缓冲区
    char[] buf = new char[3];
    int count = 0;
    while((count=fr2.read(buf))!=-1){
        System.out.println(new String(buf,0,count));
    }

    fr.close();
    fr2.close();
}
```

> FileWriter

换行要加上\n



```java
/**
     * 字符流只能复制文本文件，不能复制图片或者二进制文件(无法解析，就变成乱码了)
     * 使用字节流可以复制任意文件
     */
@Test
public void Demo01() throws Exception{
    FileReader fr = new FileReader("d:\\hello.txt");
    FileWriter fw  = new FileWriter("d:\\write.txt");
    int data = 0;
    while((data=fr.read())!=-1){
        fw.write(data);
        fw.flush();
    }
    fw.close();
    fr.close();
}
```

##### 3.字符缓冲流

![image-20210715205452187](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715205452.png)

> reader

![image-20210716090739609](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210716090739.png)



```java
public void Demo03() throws Exception{
    FileReader fr = new FileReader("d:\\write.txt");
    BufferedReader bfr = new BufferedReader(fr);

    //        // 缓冲读
    //        char[] buf = new char[1024];
    //        int count;
    //        while((count=bfr.read(buf))!=-1){
    //            System.out.println(new String(buf,0,count));
    //        }

    // 一行一行的读
    String line = null;
    while ( (line=bfr.readLine())!=null){
        System.out.println(line);
    }
    bfr.close();  // 会把fr一起关闭
}
```

> write

![image-20210716090759017](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210716090759.png)



```java
@Test
public void Demo04() throws Exception{
    FileWriter fw = new FileWriter("d:\\BW.txt");
    BufferedWriter bw = new BufferedWriter(fw);

    for (int i = 10; i > 0; i--) {
        bw.write("好好学习");
        bw.newLine();  // 写入换行符，可以根据操作系统匹配是\n 还是\r\n
        bw.flush();
    }
    bw.close();
}
```

##### 4、打印流

![image-20210716092000705](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210716092000.png)



```java
@Test
public void Demo05() throws Exception{
    PrintWriter pw = new PrintWriter("d:\\print.txt");
    pw.println(97);
    pw.println(true);
    pw.println(3.14);
    pw.println('a');
    pw.close();

}
/**
文件里的内容如下：
97
true
3.14
a
*/
```

##### 5、转换流

![image-20210716092428159](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210716092428.png)

对内存中的字节和硬盘中的字符进行转换的流。。 可以设置编码格式

> InputStreamReader

![image-20210716092546712](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210716092546.png)



![image-20210716092557632](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210716092557.png)

```java
@Test
public void Demo06() throws Exception{
    FileInputStream fis = new FileInputStream("d:\\BW.txt");
    InputStreamReader isr = new InputStreamReader(fis,"utf-8"); // 编码格式和文件的编码一样，不然就乱码了
    int data = 0;

    while((data=isr.read())!=-1){
        System.out.print((char) data);
    }
    isr.close();
}
```

> OutputStreamWriter

```java
@Test
public void Demo10() throws Exception{
    FileOutputStream fos = new FileOutputStream("d:\\out.txt");
    OutputStreamWriter osw = new OutputStreamWriter(fos,"utf-8");
    for (int i = 10; i > 0; i--) {
        osw.write("你好呀\n");
        osw.flush();
    }

    osw.close();
}
```

#### 6.File类

![image-20210716094025339](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210716094025.png)

##### 1.基本操作

> 分割符

```java
// 1. 分隔符
public static void separator(){
    sout("路径分隔符" + File.pathSeparator);
    sout("名称分隔符" + File.separator);
}
```

> 文件操作

```java
 // 2. 文件操作
  public static void fileOpen(){
    // 1. 创建文件
    if(!file.exists()){ // 是否存在
    	File file = new File("...");
    	boolean b = file.creatNewFile();
    }
    
    // 2. 删除文件
    // 2.1 直接删除
    file.delete(); // 成功true
    // 2.2 使用jvm退出时删除
    file.deleteOnExit();
    
    // 3. 获取文件信息
    sout("获取绝对路径" + file.getAbsolutePaht());
    sout("获取路径" + file.getPath());
    sout("获取文件名称" + file.getName());
    sout("获取夫目录" + file.getParent());
    sout("获取文件长度" + file.length());
    sout("文件创建时间" + new Date(file.lashModified()).toLocalString());
    
    // 4. 判断
    sout("是否可写" + file.canWrite());
    sout("是否是文件" + file.isFile());
    sout("是否隐藏" + file.isHidden());
  }
```

> 文件夹操作和FileFilter

```java
public class Demo{
  
  // 文件夹操作
  public static void directoryOpe() throws Exception{
    // 1. 创建文件夹
    File dir = new File("d:\\aaa\\bb\\ccc");
    sout(dir.toString());
    if(!dir.exists()){
      //dir.mkdir(); // 只能创建单级目录,创建上面的就会失败
      dir.mkdirs(); // 创建多级目录
    }
    
    // 2. 删除文件夹
    // 2.1 直接删除
    dir.delete(); // 只能删除最底层空目录，比如ccc是空，就会被删掉
    // 2.2 使用jvm删除
    dir.deleteOnExit();
    
    // 3. 获取文件夹信息
 	sout("获取绝对路径" + dir.getAbsolutePaht());
    sout("获取路径" + dir.getPath());
    sout("获取文件名称" + dir.getName());
    sout("获取夫目录" + dir.getParent());
    sout("获取文件长度" + dir.length());
    sout("文件夹创建时间" + new Date(dir.lashModified()).toLocalString());
    
    // 4. 判断
    sout("是否是文件夹" + dir.isFile());
    sout("是否隐藏" + dir.isHidden());
    
    // 5. 遍历文件夹，只有当前这层文件夹里的东西
    File dir2 = new File("d:");  
    String[] files = dir2.list();
    for(String string : files){
      sout(string);
    }
    
    // FileFilter接口的使用，过滤
      /**
      满足条件的返回true，就会在数组里面保存
      */
    File[] files2 = dir2.listFiles(new FileFilter(){
      
      @Override
      public boolean accept(File pathname){
        if(pathname.getName().endsWith(".jpg")){
          return true;
        }
        return false;
      }
    });
      
    for(File file : files2){
      sout(file.getName());
    }
    
  }
}
```

##### 2.递归遍历和递归删除

```java
psvm(String[] args){
  listDir(new File("d:\\myfiles"));
}
public static void listDir(File dir){
  File[] files = dir.listFiles();
  sout(dir.getAbsolutePath());
  if(files != null && files.length > 0){
    for(File file : files){
      if(file.isDirectory()){
        listDir(file); // 递归
      }else {
        sout(file.getAbsolutePath());
      }
    }
  }
}
```

```java
public static void deleteDir(File dir){
  File[] files = dir.listFiles();
  if(files != null && files.length > 0){
    for(File file : files){
      if(file.idDirectory()){
        deleteDir(file); // 递归
      }else{
        // 删除文件
        sout(file.getAbsolutePath() + "删除" + file.delete());
      }
    }
  }
}
```



#### 7、Properties

![image-20210716104218888](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210716104219.png)

## 集合

![image-20210422100710306](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422100710.png)



**数组**：

- 长度必须指定，不能更改
- 只能保存同意类型的元素
- 使用数组进行增加/删除（扩容），比较麻烦(需要申请一个新的数组，再拷贝之前的数组)

**集合**：

- 可以动态保存多个对象
- 提供了一系列方便的操作对象的方法：add remove set get
- 使用集合添加，删除新元素的代码比较简洁

### 1、集合的框架体系

- 集合主要有两组：单列集合，双列集合
  - 单列集合就是只有一个值
  - 双列集合就是存放键值对的
- Collection 接口有两个重要的子接口List ，Set  都是单列的
  - ![image-20210422101952290](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422101952.png)
- Map接口实现的子类，是双列集合，存放的K-V
  - ![image-20210422102001151](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422102001.png)





### 2、Collection

- 有些Collection的实现类，可以存放重复的元素，有些不可以
- 有些Collection的实现类，有些是有序的(List)，有些是无序的(Set)
- Collection没有直接的实现类，都是通过他的子类Set，List实现的

#### 2.1、 Collection的常用方法和遍历

##### 1.常用方法

```java
 List list = new ArrayList<>();
         //add 添加单个元素
         list.add("jack");
         list.add(176); // 自动装箱了，Integer对象
         list.add(true);
        list.add(2);
         //remove
        System.out.println(list);
        
        list.remove(2);
        //list.remove(new Integer(2));
        list.remove(true);
        System.out.println(list);

			//contains查找元素是否存在
        System.out.println(list.contains("jack"));

        //size :获取元素的个数
        System.out.println(list.size());

        // isEmpty()
        System.out.println(list.isEmpty());

        //clear 清空
	//        list.clear();
	//        System.out.println(list);

        //addAll 添加多个与元素
        List list2 = new ArrayList();
        list2.addAll(list);
        System.out.println(list2);

        //containsAll 看一个集合是否包含于另一个集合
        System.out.println(list.containsAll(list2));


        //删除和另一个集合重合的所有元素
        list.add("test");
        list2.add("nihao");
        list.removeAll(list2);
        System.out.println(list);
```

==当list删除数字的时候，list.remove(2)删除的是index为2的那个元素，而不是删除数字2。list添加int元素的时候自动装箱了，存放的是Integer的对象，所以可以这样指定删除==--`list.remove(new Integer(2));`

##### 2 Collection遍历

> Iterable迭代器

- Iterator对象称为迭代器，主要用于遍历Collection集合中的元素
- 所有实现了Collection接口的集合类都有一个iterator()方法，返回一个迭代器
- Iterator仅用于遍历集合，本身并不存放数据

```java
public interface Iterable<T> {
    /**
     * Returns an iterator over elements of type {@code T}.
     *
     * @return an Iterator.
     */
    Iterator<T> iterator();
}
```

![image-20210422104354122](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422104354.png)



在使用iterator.next()方法之前必须先用iterator.hasNext()进行检测。否则如果没有下一条记录就会抛出

`NoSuchElementException`异常

```java
package com.xy.collection;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class CollectionIterator {
    public static void main(String[] args) {
        List list = new ArrayList();
        list.add(new Book("caiji",11));
        list.add(new Book("xuih",981));
        list.add(new Book("caioashoiiji",12));
        list.add("javc");
        Iterator iterator = list.iterator();
        while (iterator.hasNext()){
            Object obj = iterator.next(); //返回的元素类型是Object
            System.out.println(obj);
        }

       
    }
}
class Book{
    private String name;
    private int price;

    public Book(String name, int price) {
        this.name = name;
        this.price = price;
    }
    @Override
    public String toString() {
        return "Book{" +
                "name='" + name + '\'' +
                ", price=" + price +
                '}';
    }
}

```

==itit快捷生成迭代器模板  ctrl+j 可以查看快捷键==

> 增强for循环

```java
public static void forPrint(List list){
        for (Object book : list) {
            System.out.println(book);
        }
    }
```

增强for的底层本质也是迭代器

可以理解成简化版本的迭代器

#### 2.2 List

##### 1、List接口的相关方法

Collection里的方法，List和Set都可以用

List里的一些方法，Set是不能使用的

**List的一些特点**

```java
List list = new ArrayList();
//1.list集合类中元素有序（添加和取出的顺序一致），且可以重复
list.add("jav");
list.add("das");
list.add("das");
list.add("daoj");
System.out.println(list);
//2、list里的元素是有索引的
System.out.println(list.get(3)); // das

//3.List接口的实现类很多
```

> 常用方法

```java
package com.xy.集合.list_;

import java.util.ArrayList;
import java.util.List;

public class ListMethod {
    public static void main(String[] args) {
        // 左边是编译类型
        List list = new ArrayList();
        list.add("张三分");
        list.add("贾宝玉");
        // 1、add(index,element)在索引位置添加元素
        list.add(1,"xy");

        // 2、addAll(index,Collection)，在索引位置添加多个元素
        list.addAll(1,new ArrayList());
        // 3、get(index)获取index位置的元素
        // 4、indexOf(element) 返回元素第一次出现的index
        list.indexOf("贾宝玉");

        // 5、lastIndexOf(element) 元素最后一次出现的index
        list.lastIndexOf("贾宝玉");


        // 6、set(index,NewElement)  替换index位置的元素
        list.set(0,"替换");
        System.out.println(list);

        // 7、subList(start,end) 返回index为[start,end)的元素集合
        List list1 = list.subList(0, 2);
        
        // 8、remove(index) 删除索引位置的元素
        System.out.println(list1);
    }
}
```

>List的三种遍历方式

ArrayList 、Vector、LinkedList都可以使用这几种方式

1.迭代器

2.增强for
3.普通for循环

![image-20210422112819132](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422112819.png)



##### 2、ArrayList

###### 1.注意事项

- 可以放所有的元素，包括**null**，可以加多个
- ArrayList由数组实现数据存储的
- ArrayList基本等同于Vector，ArrayList是线程不安全的，在多线程情况下，不建议使用ArrayList
  - ![image-20210422141635111](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422141635.png)
  - 没有用synchronize修饰方法

###### 2.底层源码

- ArrayList维护了一个Object类型的数组`transient Object[] elementData` 
  - **transient**  表示该属性不会被序列化
- 当使用无参构造器创建ArrayList对象时，则初始elementData容量为0.第一次添加，扩容elementData为10，如果需要再次扩容，扩容elementData为之前的1.5倍(**向下取整**)
- 使用指定大小的构造器，则初始elementData容量为指定大小，如果需要扩容，直接扩容elementData为之前的1.5倍



> 无参构造



![image-20210422143132881](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422143132.png)

```java
private static final Object[] DEFAULTCAPACITY_EMPTY_ELEMENTDATA = {};
```

第一次添加数据

![image-20210422143319095](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422143319.png)

1.先确定是否要扩容

2.然后再执行赋值操作



![image-20210422143823875](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422143823.png)

![image-20210422143833695](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422143833.png)

确定minCapacity的数量为10，进入下面的方法

![image-20210422143910628](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422143910.png)

(1)modCount 记录集合修改的次数

(2)如果elementData的大小不够，就用grow扩容 (if   10-0>0?)



![image-20210422144521844](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422144522.png)

分析：

第一次进来：

- oldCapacity = 0
- ![image-20210422144619834](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422144619.png)
  - 这里位运算，右移1位，相当于除以2，所以就是我们说的1.5倍
  - 但是第一次进来的时候为0，则新的容量是0
  - 第二次和以后，都是按照1.5倍扩容
- 第一次进入了下面的判断
  - ![image-20210422144728932](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422144728.png)
  - 所以第一次的容量是minCapacity，结合上面的分析这里的值为10
- 扩容使用的是Arrays.copyof(),这种方式可以保留之前的数据



第二次进来，进不去grow方法，因为![image-20210723110611701](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210723110611.png)  <0的





==add方法每次都要去判断一下是否需要扩容==

> 有参构造扩容

![image-20210422150103165](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422150103.png)

```java
this.elementData = new Object[initialCapacity]; //创建了一个指定大小的Object数组
```

后面的扩容和前面的无参扩容一样。1.5倍

##### 3、Vector

###### 1.注意事项

- 底层也是一个对象数组。`protected Object[] elementData;`
- 是线程安全的。都有synchronized修饰
- 效率比ArrayList要低

> 和ArrayList的比较

![image-20210422212944677](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210422212944.png)

###### 2.源码分析

> 无参构造

```java
public Vector() {
    this(10);   // 无参构造的时候vector就把容量置位10了，后面就不用判断
}

vector.add(i);

public synchronized boolean add(E e) {
        modCount++;
        ensureCapacityHelper(elementCount + 1);
        elementData[elementCount++] = e;
        return true;
}

// 确定是否需要扩容
private void ensureCapacityHelper(int minCapacity) {
        // overflow-conscious code
        if (minCapacity - elementData.length > 0)
            grow(minCapacity);
}

private void grow(int minCapacity) {
        
        int oldCapacity = elementData.length;
       //   protected int capacityIncrement;  默认为0
        int newCapacity = oldCapacity + ((capacityIncrement > 0) ?
                                         capacityIncrement : oldCapacity);
        if (newCapacity - minCapacity < 0)
            newCapacity = minCapacity;
        if (newCapacity - MAX_ARRAY_SIZE > 0)
            newCapacity = hugeCapacity(minCapacity);
        elementData = Arrays.copyOf(elementData, newCapacity);
}

protected int capacityIncrement; 
因为capacityIncrement的值为0，所以newCapacity = oldCapacity+oldCapacity
```

> 有参构造

```java
public Vector(int initialCapacity) {
        this(initialCapacity, 0); 
}
```

==可以自定义capacityIncrement，也就是手动指定扩容的大小。==

```java
public Vector(int initialCapacity, int capacityIncrement) {
        super();
        if (initialCapacity < 0)
            throw new IllegalArgumentException("Illegal Capacity: "+
                                               initialCapacity);
        this.elementData = new Object[initialCapacity];
        this.capacityIncrement = capacityIncrement;
}
```

##### 4、LinkedList

###### 1.注意事项

- LinkedList底层维护了一个双向链表
- LinkedList维护了两个属性first和last，分别指向首节点和尾节点
- 每个节点(Node对象)里面又维护了prev、next、item三个属性，prev指向前一个，next指向后一个节点，最终实现双向链表，item是存放数据的
- LinkedList的添加和删除，不是通过数组完成的，相对来说效率较高
- 也是**不是线程安全**的

###### 2.源码分析

> 添加元素分析

```java
public LinkedList() {
}

//执行add方法
public boolean add(E e) {
        linkLast(e);
        return true;
}

//根据源码，可以知道新节点是加在尾部的
void linkLast(E e) {
        final Node<E> l = last;  // 第一次进来last为null
        final Node<E> newNode = new Node<>(l, e, null); //Node(Node<E> prev, E element, Node<E> next) prev和next都是空，也就是一个独立的Node
        last = newNode;   
        if (l == null)
            first = newNode; //第一次进来，到这里了，first和last都指向这个Node节点
        else
            l.next = newNode;
        size++;				// 里面的元素有1个
        modCount++;			// 修改的次数，1次
    }
```

> 删除节点分析

remove总共有三种，一个是删除index位置的，一个删除指定对象的，一个就是直接删除首部，这里分析的是删除首部的方法remove()

```java
public E remove() {
   
    return removeFirst();
}

 public E removeFirst() {
     final Node<E> f = first;
     if (f == null)  //防止删的是空的
         throw new NoSuchElementException();
     return unlinkFirst(f);
 }	


private E unlinkFirst(Node<E> f) {
    // assert f == first && f != null;
    final E element = f.item;
    final Node<E> next = f.next;
    f.item = null;
    f.next = null; // help GC
    first = next; 
    if (next == null)  //这里还判断了删除之后是否是空链表了
        last = null;
    else
        next.prev = null;
    size--;
    modCount++;
    return element;
}
```

> 常用方法

```java
//修改元素
linkedList.set(1,4);

//获取元素
linkedList.get(1);
linkedList.getFirst();
linkedList.getLast();


```



> 和ArrayList的比较

![image-20210423214122374](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210423214129.png)

#### 2.3 Set

##### 1、Set接口和常用方法

- 无序的，添加和取出的顺序是不一致的，没有索引
- 不允许重复元素，只能有一个null
- ![image-20210423214756001](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210423214756.png)

> 常用方法

**常用方法和Collection接口一样**

```java
set.add();
set.remove();

```

> 遍历

```java
//迭代器
Iterator iterator = set.iterator();
    while (iterator.hasNext()) {
        Object next =  iterator.next();
        System.out.println(next);
}

//增强for循环
for (Object o : set) {
    System.out.println(o);
}
```

不能使用普通for循环来遍历，因为没有索引

##### 2、HashSet

- 底层是HashMap

```java
public HashSet() {
    map = new HashMap<>();
}
```

- 可以存放null，但是只能有1个
- HashSet不保证元素是有序的，取决于hash后，再确定索引的结果(存放和元素的取出顺序不能保证是一样的)
- 不能有重复的元素/对象



```java
package 集合.set;
import java.util.HashSet;
import java.util.Set;

public class HashSetTest {
    public static void main(String[] args) {
        Set set= new HashSet();
        set.add("tom");
        set.add(new Dog("tom")); //true
        set.add(new Dog("tom")); // true
        System.out.println(set);

        //留一个悬念
        set.add(new String("hs"));//true
        set.add(new String("hs"));//false
        System.out.println(set);
    }
}

class Dog{
    private String name;

    public Dog(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Dog{" +
                "name='" + name + '\'' +
                '}';
    }
}
```

###### 1、HashMap底层

HashMap的底层是  数组+链表+红黑树

> 数组加链表的结构

```java
package 集合.set;

public class HashSetStructure {
    public static void main(String[] args) {
        //模拟一个HashSet的底层，其实也就是HashMap的底层

        //1.创建一个数组，数组的类型是Node[]
        Node[] table = new Node[16];
        Node jop = new Node("jop", null);
        Node jso = new Node("jso", null);
        table[2] =jop ;
        jop.next = jso;


        System.out.println(table);

    }
}

class Node{
    //存储数据，可以指向下一个节点
    Object item;
    Node next;

    public Node(Object item, Node next) {
        this.item = item;
        this.next = next;
    }
}
```

![image-20210424105851454](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210424105851.png)

> 底层结论

- HashSet底层是HashMap
- 添加一个元素时，**先计算它的hash值**，然后将这个hash值转化为索引值
- 找到存储数据的table表，看这个索引位置有没有存放元素
- 如果没有，直接加入
- 如果有，则调用equals比较，如果相同，就放弃添加，如果不相同，则放到最后
- 在java8中，如果**一条链表的元素个数到达TREEIFY_THRESHOLD(默认是8)**,并且**table的大小>=MIN_TREEIFY_CAPACITY(默认是64)**，链表就会转化成红黑树



> 扩容机制和转成红黑树机制

- HashSet底层是HashMap,第一次添加时，table数组扩容到16，临界值(threshold)是16*加载因子(loadFactor=0.75) = 12、
- 如果table(table的size是只要添加元素进去就+1，不管你是添加到哪个链表上)数组使用到了临界值12，就会扩容到16\*2 =32,临界值 = 32*0.75 = 24,依次类推
- 在java8中，如果**一条链表的元素个数到达TREEIFY_THRESHOLD(默认是8)**,并且**table的大小>=MIN_TREEIFY_CAPACITY(默认是64)**，链表就会转化成红黑。否则仍然采用数组扩容机制
- 这里table的大小不是指里面有元素的个数，而是table里的node[n] ,这里的n的值到64，就会让大于8的链表转成红黑树

###### 2、源码分析

> 第一次add

```java
public HashSet() {
    map = new HashMap<>();
}

set.add("java")的分析
    
//执行add
public boolean add(E e) { // e="java"
    //private static final Object PRESENT = new Object(); PRESENT是null
    return map.put(e, PRESENT)==null;
}
// key:java ，value = PRESENT(static的，这里的PRESENT就是站位用的)
public V put(K key, V value) {
    return putVal(hash(key), key, value, false, true);
}

null的hash为0.计算hash还进行了异或操作，并不仅仅是调用hashCode()方法 
/**计算了一下hash值，没有研究
// h>>>16是无符号右移16位，也就是让hash值的高16参与运算，会让得到的下标更加散列。更好的抵御哈希冲突
static final int hash(Object key) {
    int h;
    return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
}
*/

//执行putVal算法
```

==putVal的分析==

```java
final V putVal(int hash, K key, V value, boolean onlyIfAbsent, boolean evict) {
    
    Node<K,V>[] tab; Node<K,V> p; int n, i;//定义了辅助变量
    if ((tab = table) == null || (n = tab.length) == 0) // table就是hashmap的一个数组，类型是Node[]
        n = (tab = resize()).length;
    
    // 根据计算的hash值，得到key应该存放在table表的哪个索引位置
    // 并把这个位置的对象，赋给P
    //  判断 P 是否为空
    
    if ((p = tab[i = (n - 1) & hash]) == null)
        // 如果p是null，创建一个Node，放有key和value = PRESENT，hash值也存进去了(是为了之后和key相同的节点进行比较)，最后的null是链表的下一个点。然后把node放到位置i（hash对应的值）
        tab[i] = newNode(hash, key, value, null);
    else {
        Node<K,V> e; K k;
        if (p.hash == hash &&
            ((k = p.key) == key || (key != null && key.equals(k))))
            e = p;
        else if (p instanceof TreeNode)
            e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
        else {
            for (int binCount = 0; ; ++binCount) {
                if ((e = p.next) == null) {
                    p.next = newNode(hash, key, value, null);
                    if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                        treeifyBin(tab, hash);
                    break;
                }
                if (e.hash == hash &&
                    ((k = e.key) == key || (key != null && key.equals(k))))
                    break;
                p = e;
            }
        }
        if (e != null) { // existing mapping for key
            V oldValue = e.value;
            if (!onlyIfAbsent || oldValue == null)
                e.value = value;
            afterNodeAccess(e);
            return oldValue;
        }
    }
    ++modCount;
    if (++size > threshold)  //看是否大于阈值，12就扩容
        resize();
    afterNodeInsertion(evict); // void afterNodeInsertion(boolean evict) { }这个方法是null，给hashmap的其他子类使用的，比如linkedlistMap。
    return null;
}
```

resize方法

```java
 final Node<K,V>[] resize() {
     Node<K,V>[] oldTab = table;
     int oldCap = (oldTab == null) ? 0 : oldTab.length;
     int oldThr = threshold;
     int newCap, newThr = 0;
     if (oldCap > 0) {
         if (oldCap >= MAXIMUM_CAPACITY) {
             threshold = Integer.MAX_VALUE;
             return oldTab;
         }
         else if ((newCap = oldCap << 1) < MAXIMUM_CAPACITY &&
                  oldCap >= DEFAULT_INITIAL_CAPACITY)
             newThr = oldThr << 1; // double threshold
     }
     else if (oldThr > 0) // initial capacity was placed in threshold
         newCap = oldThr;
     else {               // zero initial threshold signifies using defaults
         newCap = DEFAULT_INITIAL_CAPACITY; 								//新的容量
         // static final float DEFAULT_LOAD_FACTOR = 0.75f; 
         // static final int DEFAULT_INITIAL_CAPACITY = 1 << 4;
         newThr = (int)(DEFAULT_LOAD_FACTOR * DEFAULT_INITIAL_CAPACITY); 	// 这是一个临界值，加载因子*容量
     }
     if (newThr == 0) {
         float ft = (float)newCap * loadFactor;
         newThr = (newCap < MAXIMUM_CAPACITY && ft < (float)MAXIMUM_CAPACITY ?
                   (int)ft : Integer.MAX_VALUE);
     }
     threshold = newThr;  										// 临界值
     @SuppressWarnings({"rawtypes","unchecked"})
     Node<K,V>[] newTab = (Node<K,V>[])new Node[newCap];    	//新建了一个容量为16的Table
     table = newTab;										//table变成16了
     if (oldTab != null) {
         for (int j = 0; j < oldCap; ++j) {
             Node<K,V> e;
             if ((e = oldTab[j]) != null) {
                 oldTab[j] = null;
                 if (e.next == null)
                     newTab[e.hash & (newCap - 1)] = e;
                 else if (e instanceof TreeNode)
                     ((TreeNode<K,V>)e).split(this, newTab, j, oldCap);
                 else { // preserve order
                     Node<K,V> loHead = null, loTail = null;
                     Node<K,V> hiHead = null, hiTail = null;
                     Node<K,V> next;
                     do {
                         next = e.next;
                         if ((e.hash & oldCap) == 0) {
                             if (loTail == null)
                                 loHead = e;
                             else
                                 loTail.next = e;
                             loTail = e;
                         }
                         else {
                             if (hiTail == null)
                                 hiHead = e;
                             else
                                 hiTail.next = e;
                             hiTail = e;
                         }
                     } while ((e = next) != null);
                     if (loTail != null) {
                         loTail.next = null;
                         newTab[j] = loHead;
                     }
                     if (hiTail != null) {
                         hiTail.next = null;
                         newTab[j + oldCap] = hiHead;
                     }
                 }
             }
         }
     }
     return newTab;
 }
```

> add相同元素分析

```java
final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
                   boolean evict) {
        Node<K,V>[] tab; Node<K,V> p; int n, i;
        if ((tab = table) == null || (n = tab.length) == 0)
            n = (tab = resize()).length;
    
    // 添加相同的元素之后，这里的i是有值的所以进入else方法
        if ((p = tab[i = (n - 1) & hash]) == null)
            tab[i] = newNode(hash, key, value, null);
    
    	// 下面的判断有三种情况
     /**
     1.和头元素是一样的，不能添加
     2.和头元素不一样，链表已经是红黑树结构，按照红黑树的方式进行比较，
     3.和头元素不一样，链表也不是红黑树结构，就遍历整个链表，查看有没有相同的元素，如果有，就不能添加，如果没有尾插(还有其他操作，看整个源码分析)
     */
        else {
            		// 辅助变量，开发技巧：定义局部变量的时候，在需要的地方创建，不要一开始都定义了
            Node<K,V> e; K k;
            // 这里的p是table[i]这个位置的头元素。如果头元素和准备添加的key的hash值一样
            // 并且如果头元素的key和添加的key是一样的 (k = p.key) == key 或者(key != null && key.equals(k)
            //这里的(key != null && key.equals(k) 指的是，如果key是不一样的，并且key不是null，内容相同，也不能添加
            if (p.hash == hash &&
                ((k = p.key) == key || (key != null && key.equals(k))))
                e = p;
            
            // 判断p是不是红黑树，如果是红黑树，就按照红黑树的方式进行比较
            // 如果是红黑树就调用putTreeVal添加
            else if (p instanceof TreeNode)
                e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
            
            // 上面都不满足的话，就是 既和头元素不是同一个元素，又不是红黑树的结构，那么进入这里
          
            else {
                // 将整个链表遍历,这里是死循环，由break退出
                for (int binCount = 0; ; ++binCount) {
                     // 如果都不一样，那么说明添加的元素是没有的，就把元素放到链表的最后
                    // 这里 e = p.next 其实是在移动p的位置，既进行了判断，又把节点往后移动了一个,这里有两个指针
                    if ((e = p.next) == null) {
                        p.next = newNode(hash, key, value, null);
                        // TREEIFY_THRESHOLD = 8
                        // 这里添加节点之后，查看链表是否到达8个节点，
                        // 如果达到了，就对当前这个链表进行树化，也就是转成红黑树
                        // 调用树化方法，进去还需要判断，看是否表的长度大于64，如果小于64，就先不转红黑树，而是扩大table表(源码看下面)
                        if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                            treeifyBin(tab, hash);
                        break;
                    }
                    // 如果有一个元素和要添加的元素是一致的就添加失败(这里和第一个if是一样的)
                    if (e.hash == hash &&
                        ((k = e.key) == key || (key != null && key.equals(k))))
                        break;
                    p = e;
                }
            }
            if (e != null) { // existing mapping for key
                V oldValue = e.value;
                if (!onlyIfAbsent || oldValue == null)
                    e.value = value;
                afterNodeAccess(e);
                return oldValue;
            }
        }
        ++modCount;
        if (++size > threshold)
            resize();
        afterNodeInsertion(evict);
        return null;
    }
```

```java
final void treeifyBin(Node<K,V>[] tab, int hash) {
    int n, index; Node<K,V> e;
    // static final int MIN_TREEIFY_CAPACITY = 64;
    // 判断table表的大小，如果小于64，就先不树化，先扩容table表
    if (tab == null || (n = tab.length) < MIN_TREEIFY_CAPACITY)
        resize();
    // 上面条件不成立时，才转化为红黑树
    else if ((e = tab[index = (n - 1) & hash]) != null) {
        TreeNode<K,V> hd = null, tl = null;
        do {
            TreeNode<K,V> p = replacementTreeNode(e, null);
            if (tl == null)
                hd = p;
            else {
                p.prev = tl;
                tl.next = p;
            }
            tl = p;
        } while ((e = e.next) != null);
        if ((tab[index] = hd) != null)
            hd.treeify(tab);
    }
}
```

##### 3、LinkedHashSet



###### 1、说明

- LinkedHashSet是HashSet的子类
- LinkedHashSet底层是一个LinkedHashMap，底层维护了一个数组+双向链表
- LinkedHashSet根据元素的hashCode值来决定元素的存储位置，同时使用链表维护元素的次序，使得元素看起来是以插入顺序保存的
- LinkedHashSet不允许添加重复元素

![image-20210425195806943](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210425195807.png)

###### 2、底层源码

```java
根据下面的图可以看到，table表里存放的元素类型为Entry，可以知道Entry和Node是有关系的
// 它的add操作和HashSet是一样的，唯一的区别就是里面的链表是双向链表，而且有首尾指针指向第一个插入的节点和最后一个插入的节点
// 当元素个数和table表的size大于了之后，扩容和HashSet一样，树化也一样

// Entry是LinkedHashMap的内部类
static class Entry<K,V> extends HashMap.Node<K,V> {
    Entry<K,V> before, after;
    Entry(int hash, K key, V value, Node<K,V> next) {
        super(hash, key, value, next);
    }
}
```

![image-20210425201522829](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210425201523.png)

#### 2.4、TreeSet

> 源码

```java
/*
1、构造器把传入的比较器对象，赋值给了TreeSet的底层TreeMap的一个属性comparator
*/

public TreeSet(Comparator<? super E> comparator) {
    this(new TreeMap<>(comparator));
}
-----treeSet 底层是treeMap
public TreeMap(Comparator<? super K> comparator) {
    this.comparator = comparator;
}



public boolean add(E e) {
    return m.put(e, PRESENT)==null;
}

// put方法里的
/*
把我们传入的compare对象赋值给cpr
*/
Comparator<? super K> cpr = comparator;
if (cpr != null) {
    do {
        parent = t;
        // 在这里调用cpr的compare方法进行比较
        cmp = cpr.compare(key, t.key);
        // 二叉排序树，
        if (cmp < 0)
            t = t.left;
        else if (cmp > 0)
            t = t.right;
        //如果比较的结果为0，就是两个相同的时候，就直接返回去了，不加入
        else
            return t.setValue(value);
    } while (t != null);
}
```



### 3 Map

#### 1.Map接口和常用方法

###### 1.特点(JDK8的)

- Map用于保存具有映射关系的数据:key -value
- Map里的数据可以是任何类型的，被封装在HashMap$Node里
- Map里的key是不能重复的，当有相同的key时，就等价于替换
- map里的value是可以重复的
- map里的key可以为null，只能有1个，value可以为多个null
- 一般用String类作为map的key
- key和value之间存在单向的一对一关系，通过指定的key总能找到对应的value



> 结构，可以在去看看博客

![image-20210426160134412](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210426160134.png)

```java
package com.xy.集合.map;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Test {
    public static void main(String[] args) {
        Map map = new HashMap<>();
        map.put("1","xy");
        map.put(new N(),new P());
        map.put("3","xy2");
        Set set = map.keySet();
        Collection value = map.values();
        System.out.println(set);
        System.out.println(map);
        /**
         * 1.key - value 实际上是HashMap$Node节点里的元素
         * 2.k-v为了方便程序员遍历，还创建了EntrySet集合，这个集合存放的元素类型为Entry
         * 一个Entry对象就有 k,v   transient Set<Map.Entry<K,V>> entrySet;
         * 3.entrySet中，定义的类型是Map.Entry。但是实际存放的还是HashMap$Node，因为这个node实现了Entry
         * 4.把HashMap$Node对象存放到entrySet 方便我们遍历，因为Map.Entry 提供了重要方法 getKey()，getValue
         */
    }
}
class N{
}
class P{
}
```

###### 2.常用方法

```java
package com.xy.集合.map;

import java.util.HashMap;
import java.util.Map;

public class MapMethod {
    public static void main(String[] args) {
        Map map = new HashMap();
        map.put("no1","xy");
        map.put("no2","xy2");
        map.put("no3","xy2");
        //移除
        map.remove("no1");
        //获取key对应的value
        Object no2 = map.get("no2");
        System.out.println(no2);
        // map里的元素个数
        System.out.println(map.size());
        //判断个数是否为0
        System.out.println(map.isEmpty());
        // 查看是否有指定的key
        System.out.println(map.containsKey("no2"));
        // 清空
        map.clear();
        System.out.println(map);
    }
}
```

###### 3.六大遍历方式

```java
package com.xy.集合.map;

import java.util.*;

public class MapFor {
    public static void main(String[] args) {
        Map map = new HashMap();
        map.put("xy","xuying");
        map.put("xy1","xuying1");
        map.put("xy2","xuying2");

        key_for(map);
    }


    // 取出所有的key，通过key取出value
    static void key_for(Map map){
        Set keySet = map.keySet();
        //1、增强for
        for (Object key : keySet) {
            System.out.println(key+"-"+map.get(key));
        }

        System.out.println("--------迭代器");
        Iterator iterator = keySet.iterator();
        //2、迭代器
        while (iterator.hasNext()) {
            Object key =  iterator.next();
            System.out.println(key+"-"+map.get(key));
        }
    }

    // 直接取出所有的value
    static void value_for(Map map){
        Collection values = map.values();
        // 这里可以使用Collection的遍历方式,增强for循环和迭代器
        
        // 3、
        for (Object value : values) {
            System.out.println(value);
        }
        
        // 4、
        Iterator iterator = values.iterator();
        while (iterator.hasNext()) {
            Object value =  iterator.next();
            System.out.println(value);
        }
    }


    static void entry_for(Map map){
        // 5、
        System.out.println("---entrySet的增强for方法");
        Set entrySet = map.entrySet();
        for (Object entry : entrySet) {
            Map.Entry m = (Map.Entry) entry;
            System.out.println(m.getKey()+"-"+m.getValue());
        }

        // 6、
        System.out.println("---entrySet的迭代器");
        Iterator iterator = entrySet.iterator();
        while (iterator.hasNext()) {
            // 这个节点的类型是HashMap$Node，可以向下转型成Map.Entry，因为这个有getKey 和getValue的方法
            Map.Entry entry = (Map.Entry) iterator.next(); 
            System.out.println(entry.getKey()+"-"+entry.getValue());  
        }
    }
}
```

#### 2、HashMap

###### 源码分析

HashSet那里已经讲过了

> 当put同一个key时

```java
final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
                   boolean evict) {
        Node<K,V>[] tab; Node<K,V> p; int n, i;
        if ((tab = table) == null || (n = tab.length) == 0)
            n = (tab = resize()).length;
        if ((p = tab[i = (n - 1) & hash]) == null)
            tab[i] = newNode(hash, key, value, null);
        else {
            Node<K,V> e; K k;
            
            /*进入这里，
            我们发现，当前节点和添加之后的节点hash相同，并且equals也相同，直接进入第一个if语句里,e = p
            */
            if (p.hash == hash &&
                ((k = p.key) == key || (key != null && key.equals(k))))
                e = p;
            else if (p instanceof TreeNode)
                e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
            /*
            当前节点不是树结构，而且equals不同，那么就在链表里面遍历比较
            */
            else {
                for (int binCount = 0; ; ++binCount) {
                    // 如果整个链表都没有同一个元素，那么就挂在链表尾部，此时e= null，跳出循环了
                    if ((e = p.next) == null) {
                        p.next = newNode(hash, key, value, null);
                        if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                            treeifyBin(tab, hash);
                        break;
                    }
                    //如果里面有相同的，那么就break出去了，此时e不是null
                    if (e.hash == hash &&
                        ((k = e.key) == key || (key != null && key.equals(k))))
                        break;
                    p = e;
                }
            }
            // e 不是null时，就把新的value赋值给了e，也就是更新了
            if (e != null) { // existing mapping for key
                V oldValue = e.value;
                if (!onlyIfAbsent || oldValue == null)
                    e.value = value;
                afterNodeAccess(e);
                return oldValue;
            }
        }
        ++modCount;
        if (++size > threshold)
            resize();
        afterNodeInsertion(evict);
        return null;
    }
```

#### 3、HashTable

###### 1、注意事项

- 存放的元素是键值对
- hashtable的键和值都不能为null，否则会抛出NullPointerException异常
- hashtable的使用方法和HashMap基本一样
- **hashTable是线程安全的，hashMap是线程不安全的**



###### 2、源码分析

```java
// 可以看出初始化容量为11，加载因子为0.75
public Hashtable() {
        this(11, 0.75f);
}
/*
1、hashTable底层是一个数组，元素是Hashtable的内部类Entry，实现了Map.Entry
2、临界值是11*0.75 = 8 向下取整
*/

```

![image-20210428211345806](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210428211345.png)

> 扩容机制

```java
public synchronized V put(K key, V value) {
    // Make sure the value is not null
    if (value == null) {
        throw new NullPointerException();
    }

    // Makes sure the key is not already in the hashtable.
    Entry<?,?> tab[] = table;
    int hash = key.hashCode();
    int index = (hash & 0x7FFFFFFF) % tab.length;
    @SuppressWarnings("unchecked")
    Entry<K,V> entry = (Entry<K,V>)tab[index];
    for(; entry != null ; entry = entry.next) {
        if ((entry.hash == hash) && entry.key.equals(key)) {
            V old = entry.value;
            entry.value = value;
            return old;
        }
    }
	//用这个方法增加节点
    addEntry(hash, key, value, index);
    return null;
}


private void addEntry(int hash, K key, V value, int index) {
    modCount++;

    Entry<?,?> tab[] = table;
    /**
    当count大于阈值的时候，就进入rehash方法，进行扩容
    */
    if (count >= threshold) {
        // Rehash the table if the threshold is exceeded
        rehash();

        tab = table;
        hash = key.hashCode();
        index = (hash & 0x7FFFFFFF) % tab.length;
    }

    // Creates the new entry.
    @SuppressWarnings("unchecked")
    Entry<K,V> e = (Entry<K,V>) tab[index];
    tab[index] = new Entry<>(hash, key, value, e);
    count++;
}


protected void rehash() {
    int oldCapacity = table.length;
    Entry<?,?>[] oldMap = table;

    // overflow-conscious code
    // 扩容的机制，乘以2加1
    int newCapacity = (oldCapacity << 1) + 1;
    if (newCapacity - MAX_ARRAY_SIZE > 0) {
        if (oldCapacity == MAX_ARRAY_SIZE)
            // Keep running with MAX_ARRAY_SIZE buckets
            return;
        newCapacity = MAX_ARRAY_SIZE;
    }
    Entry<?,?>[] newMap = new Entry<?,?>[newCapacity];

    modCount++;
    threshold = (int)Math.min(newCapacity * loadFactor, MAX_ARRAY_SIZE + 1);
    table = newMap;

    for (int i = oldCapacity ; i-- > 0 ;) {
        for (Entry<K,V> old = (Entry<K,V>)oldMap[i] ; old != null ; ) {
            Entry<K,V> e = old;
            old = old.next;

            int index = (e.hash & 0x7FFFFFFF) % newCapacity;
            e.next = (Entry<K,V>)newMap[index];
            newMap[index] = e;
        }
    }
}
```

> Hashtable和HashMap对比

![image-20210428212447259](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210428212447.png)



#### 4、properties

###### 1、基本介绍

- 继承Hashtable类 ，并实现了Map接口，也是使用键值对的形式保存数据
- 使用特点和hashtable累死
- Properties可以用于xx.properties文件读取，加载数据到Properties类对象，并进行读取和修改
- 工作中，xxx.properties文件常用作配置文件，使用IO读取
- properties的键和值不能为null

> 常用方法

```java
package com.xy.集合.map;

import java.util.Properties;

public class PropertiesTest {
    public static void main(String[] args) {
        Properties properties = new Properties();
        // 增加和修改
        properties.put("jopn",100);
        properties.put("jopn",10);  // 有相同的key，值就是替换
        properties.put("jopn2",10);
        System.out.println(properties);
        
        // 如何获取对应的值,查找
        properties.get("jopn");
        //删除
        properties.remove("jopn2");
        System.out.println(properties);
    }
}
```

和HashSet的机制很像

#### 5、TreeMap

###### 1.底层源码分析

```java
//构造器和TreeSet一样，可以自己创建Compare对象进行比较

/**
调用put方法
*/
public V put(K key, V value) {
    Entry<K,V> t = root;
    // 第一次添加时，t为空进入
    if (t == null) {
        /*
        这里比较的时候，如果传入的key为空，那么就会抛出异常
        **/
        compare(key, key); // type (and possibly null) check
		// 将k-v的值封装到内部类Entry里去了
        root = new Entry<>(key, value, null);
        size = 1;
        modCount++;
        return null;
    }
    int cmp;
    Entry<K,V> parent;
    // split comparator and comparable paths
    
    // 之后加入的节点
    Comparator<? super K> cpr = comparator;
    if (cpr != null) {
        do {
            parent = t;
            cmp = cpr.compare(key, t.key);
            if (cmp < 0)
                t = t.left;
            else if (cmp > 0)
                t = t.right;
            else
                return t.setValue(value);
        } while (t != null);
    }
    else {
        if (key == null)
            throw new NullPointerException();
        @SuppressWarnings("unchecked")
        Comparable<? super K> k = (Comparable<? super K>) key;
        do {
            parent = t;
            cmp = k.compareTo(t.key);
            if (cmp < 0)
                t = t.left;
            else if (cmp > 0)
                t = t.right;
            else
                return t.setValue(value);
        } while (t != null);
    }
    Entry<K,V> e = new Entry<>(key, value, parent);
    if (cmp < 0)
        parent.left = e;
    else
        parent.right = e;
    fixAfterInsertion(e);
    size++;
    modCount++;
    return null;
}
```



### 4、如何选择集合实现类

![image-20210429104543183](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210429104543.png)

### 5、Collections工具类

#### 介绍

- Collections是一个操作Set、List和Map等集合的工具类
- Collections提供了一系列静态的方法对集合元素进行排序、查询和修改操作

> 方法

```java
package com.xy.集合.Collecitions_;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class CollectionsMethod {
    public static void main(String[] args) {
        List list = new ArrayList();
        list.add("tom");
        list.add("tom");
        list.add("simit");
        list.add("king");
        list.add("milan");
        System.out.println(list);

        // 反转
        System.out.println("反转");
        Collections.reverse(list);
        System.out.println(list);

        // 打乱顺序
        System.out.println("随机打乱顺序");
        Collections.shuffle(list);
        System.out.println(list);

        // 排序
        System.out.println("排序之后");
        Collections.sort(list);
        System.out.println(list);
        // 这个可以放一个比较器控制sort
//        Collections.sort(list,(o1,o2)->{
//            return 1;
//        });

        // 交换
        System.out.println("交换0、1出的元素");
        Collections.swap(list,0,1);
        System.out.println(list);

        //自然顺序的最大元素
        System.out.println(Collections.max(list));
        // 也可以放一个比较器进去，控制比较
        // 长度最大的
        Collections.max(list,(o1,o2)->{
            return ((String)o1).length() - ((String)o2).length();
        });

        //最小,和上面一样
        Collections.min(list);

        //出现的次数
        System.out.println("tom 出现的次数"+Collections.frequency(list, "tom"));

        // 拷贝
        ArrayList newList = new ArrayList();
        // 这里的newLIst不能直接拷贝list，因为copy源码里面要比较两个list的size
        // 如果newList里面存的元素小于list，就抛出异常
        // 这里copy的话需要先往newLIst里面填充list长度的元素
//        Collections.copy(newList,list);
//        System.out.println(newList);
        
        // 替换,将原来的值查看有没有，如果有的话就替换成tom
        Collections.replaceAll(list,"tom","汤姆");
    }
}

```





## JVM

### 1.jvm的位置 

![image-20210313143524323](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210313143524.png)



### 2.jvm的体系结构

![image-20210403150237493](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210403150237.png)





### 3、类加载器

作用:加载Class文件

- 虚拟机自带的加载器
- 启动类（根)加载器    boot   ext的父加载器，无法获取到，因为是c、c++编写的 
- 扩展类加载器     ext                 // ExtClassLoader     \jre\lib\ext
- 应用程序（系统）类加载器 app   //AppClassLoader  

**双亲委派机制**：

先从app->ext->boot 查找，找到了之后还要继续往后，最后执行高一等级的类

1. 类加载器收到类加载的请求，将这个请求向上委托给父类加载器去完成，一直向上委托，直到启动类加载器，
2. 启动加载器检查是否能够加载当前这个类，能加载就结束，使用当前的加载器，否则抛出异常，通过子加载器加载

> 自己的理解

就是我们加载一个类，首先先去查找当前这个类的加载器有没有加载这个类，如果没有的话就委托当前类加载的器的父加载器去find一下有没有加载这个类，然后一直委托到根加载器(BootstrapClassLoader)。中间如果有任何一个加载器已经加载过这个类了，就直接返回。

如果都没加载过这个类，那么就从根加载器开始看能不能加载这个类，如果根加载器加载不了，就让下一级的加载器加载，持续这个过程一直到应用程序类加载器加载。如果都加载不了，就是CLass not find了。

参考博客:https://www.cnblogs.com/ITPower/p/13205903.html

> 为什么要有双亲委派机制

```cmd
#两个原因: 
#1. 沙箱安全机制, 自己写的java.lang.String.class类不会被加载, 这样便可以防止核心API库被随意修改
#2. 避免类重复加载. 比如之前说的, 在AppClassLoader里面有java/jre/lib包下的类, 他会加载么? 不会, 他会让上面的类加载器加载, 当上面的类加载器加载以后, 就直接返回了, 避免了重复加载.
```



### 4、native关键字

凡是带了native关键字的，说明java的作用范围达不到了，会去调用底层C语言的库，会进入本地方法栈
调用本地方法接口 JNI：扩展java的使用，融合不同的编程语言为java所用

private native void start0();

> 沙箱安全机制

==查一下==

> 方法区存了哪些东西

### 5、栈

线程结束，栈内存也就释放了，对于栈来说，不存在垃圾回收问题

> 栈里面存的东西

8大基本类型，对象引用，实例的方法





![image-20210404183439254](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210404183439.png)



### 6、堆

> 三种jvm

- sun公司的    -- hotsopt  (我们用的)
- Oracle  -- JRockit
- IBM   -- j9VM

==我们学习的都是HotSpot==

heap，一个JVM只有一个堆内存，堆内存的大小是可以调解的

存放了 类，方法，常量，变量和所有引用类型的真实对象



堆内存细分为三个区域：

- 新生区(伊甸园区)

  -  伊甸园
  -  幸存0区
  -  幸存1区

  老年区

- 永久区（元空间，方法区）

GC垃圾回收，主要在伊甸园和养老区

OOM错误，堆内存满了

==jdk8以后，永久区改了名字-元空间==

> 新生区

- 类诞生和成长的地方，甚至死亡。
- 伊甸园：所有的对象都是在这new出来的  (对象太大的话会在老年区那出来)
- 幸存区（0，1）：

> 永久区

- jdk1.6之前：永久代，常量池在方法区
- jdk1.7: 永久代，但是慢慢退化了，去永久代，常量池在堆中
- jdk1.8之后：无永久代，常量池在元空间

>

默认情况下，分配的总内存是电脑内存的1/4，而初始化的内存是：1/64

```java
-Xms1024m -Xmx1024m -XX:+PrintGCDetails

public class test {
    public static void main(String[] args) {
        long max = Runtime.getRuntime().maxMemory();
        long total = Runtime.getRuntime().totalMemory();

        System.out.println("max="+max+"字节"+(max/(double)1024/1024)+"M");
        System.out.println("total="+max+"字节"+(total/(double)1024/1024)+"M");
    }
}
```

![image-20210404192636234](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210404192636.png)

这里这两个相加得到的大小就是981.5M，元空间并不在这里

### 7、GC垃圾回收方法

新生区，幸存区from，幸存区to，老年区

- 轻GC（普通的GC）    新生区，偶尔在幸存区
- 重GC（全局GC）         老年区

> 引用计数法

![image-20210313143538527](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210313143538.png)

成本：

- 计数器
- 次数为0的就被清理了

> 复制算法

from  和to 区，**谁空谁是to**，然后伊甸园区和from区的垃圾就去往to区。当一个对象经历了15次(默认值)GC都没有死，就去了养老区

- 好处：没有内存的碎片
- 坏处：浪费了内存空间(幸存区有一个为空)

复制算法最佳使用场景：对象存活度较低的时候：新生区

> 标记清除法

两次扫描：第一次标记存活的对象，第二次清楚没有标记的对象

==可达性分析算法==

缺点：

- 两次扫描严重浪费空间
- 会产生内存碎片

优点:

- 不需要额外的空间

> 标记压缩

在标记清楚方法上进行优化：

- 压缩
  - 防止内存碎片的产生
  - 再次扫描，然后把对象整理一下，有了移动的成本



全程应该为**标记清除压缩算法**

小优化：先标记清除几次，之后再压缩一次

> 总结

内存效率：复制算法>标记清除算法>标记压缩(时间复杂度)

内存整齐度：复制算法=标记压缩>标记清除算法

内存利用率：标记压缩 = 标记清除算法>复制算法





GC ->分代收集算法

年轻代：

- 存活率低
- 复制算法

老年代：

- 存活率高，区域大
- 标记清除+标记压缩 混合实现

#### JMM

java memory model



它是干嘛的？ 官方，博客
