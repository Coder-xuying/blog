# java基础知识

## 基本功

#### java的特点

- 简单易学
- 跨平台
- 面向对象
- 安全
- 支持网络编程
- 编译与解释并存

#### jvm、jdk和jre之间的关系

jvm(java虚拟机)是运行java字节码文件的虚拟机，对不同的操作系统实现不同的jvm，就能够做到，对相同的字节码输出同样的结果。

JRE 是 Java 运行时环境。它是运行已编译 Java 程序所需的所有内容的集合，包括 **Java 虚拟机（JVM）**，Java 类库，java 命令和其他的一些基础构件。只能满足运行java程序，不能进行java开发。

JDK 是 Java Development Kit 缩写。它**拥有 JRE** ，还有编译器（javac）和工具（如 javadoc 和 jdb）。它能够创建和编译程序。

#### Java 和 C++的区别?

- 都是面向对象的语言，都支持封装、继承和多态
- java 不提供指针来直接访问内存，程序内存更加安全
- Java 有自动内存管理垃圾回收机制(GC)，不需要程序员手动释放无用内存。

- Java 的类是单继承的，C++ 支持多重继承；虽然 Java 的类不可以多继承，但是接口可以多继承。
- C ++同时支持方法重载和**操作符重载**，但是 Java 只支持方法重载

#### 8种基本类型

![image-20210708203651970](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210708203652.png)



对应的包装类`Byte`、`Short`、`Integer`、`Long`、`Float`、`Double`、`Character`、`Boolean` 。

> 装箱和拆箱

![image-20210708203708690](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210708203708.png)



> 包装类

Java 基本类型的包装类的大部分都实现了常量池技术。`Byte`,`Short`,`Integer`,`Long` 这 4 种包装类默认创建了数值 **[-128，127]** 的相应类型的缓存数据。`Character` 创建了数值在[0,127]范围的缓存数据

在默认数值类创建的元素，直接从常量池取，当值大于默认数值，之后就是创建在堆中创建新对象。  相比于对象类型， 基本数据类型占用的空间非常小。



#### == 和 equals

==对于引用类型来说 比较的是栈中的值，对于基本数据类型来说比较的是变量值

引用类型是堆中内存对象的地址比较 - String 



equals不做处理的话默认是==,但是一般会重写。(比如String类。就重写了)

String里面的equals是重写之后的。



> 常量池

`Byte`,`Short`,`Integer`,`Long` 这 4 种包装类默认创建了数值 **[-128，127]** 的相应类型的缓存数据，`Character` 创建了数值在[0,127]范围的缓存数据，`Boolean` 直接返回 `True` Or `False`。

![image-20210729184621849](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210729184621.png)



#### 为什么重写equals必须重写hashcode

equals和hashcode都是判断两个对象是否相等的方法。

- equals保证对象是绝对相等，而hashcode保证的是可能相等。比如有hash冲突的情况

- 一般hashcode的性能很快，先判断一下对象是否相等，如果不等就直接不等了

  如果不重写hashcode，可能会出现equals相等，hashcode散列值不等的情况。这就违背了对象相等的约定





#### 重载和重写的区别

**重载**：发生在**同一个类**中，**方法名相同**。参数类型不同，个数不同，方法返回值和修饰符可以不同。发生在**编译时期**。只有返回值不同不是重载，会报错

**重写**：发生在父子类中。方法名、参数列表必须相同，返回值范围小于等于父类，异常范围小于等于父类。**访问修饰符范围大于等于父类**，如果父类修饰符是private，子类无法重写



#### 枚举

```java
public enum PizzaStatus {
    ORDERED,
    READY, 
    DELIVERED; 
}
// 可以加上方法，更加
public boolean isDeliverable() {
    return getStatus() == PizzaStatus.READY;
}
```

##### 1.比直接定义常量的优势

**以这种方式定义的常量使代码更具可读性，允许进行编译时检查，预先记录可接受值的列表，并避免由于传入无效值而引起的意外行为。**



##### 2.使用 == 比较枚举类型

由于枚举类型确保JVM中仅存在一个常量实例，因此我们可以安全地使用 `==` 运算符比较两个变量。`==` 运算符可提供编译时和运行时的安全性。

```java
// 运行时安全性
Pizza.PizzaStatus pizza = null;
System.out.println(pizza.equals(Pizza.PizzaStatus.DELIVERED));//空指针异常
System.out.println(pizza == Pizza.PizzaStatus.DELIVERED);//正常运行


//编译时安全性
if (Pizza.PizzaStatus.DELIVERED.equals(TestColor.GREEN)); // 编译正常
if (Pizza.PizzaStatus.DELIVERED == TestColor.GREEN);      // 编译失败，类型不匹配
```

##### 在 switch 语句中使用枚举类型

```java
public int getDeliveryTimeInDays() {
    switch (status) {
        case ORDERED:
            return 5;
        case READY:
            return 2;
    }
    return 0;
}
```



##### 通过枚举实现一些设计模式

>单例模式

```java
public enum Single{
    INSTANCE;
    public static Single getInstance(){
        return INSTANCE;
    }
}
```

#### final,static,this,super 关键字总结

##### 1.final

用来修饰类、方法和变量

1. final **修饰的类不能被继承**，final 类中的所有成员方法都会被隐式的指定为 final 方法；
2. final **修饰的方法不能被重写**；
3. final 修饰的变量是常量，如果是基本数据类型的变量，则其数值一旦在初始化之后便不能更改；如果是引用类型的变量，则在对其初始化之后便不能让其指向另一个对象。

修饰局部变量：可以不初始化，但是使用之前一定要赋值

![image-20210622204523468](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210622204523.png)

修饰引用类型的变量，不能指向另一个对象，但是引用的值可以改变

```java
// 例如
final int[] arr = {1,2,3,4}
arr[0] = 5   // 合法
arr = {2,3,4} // 非法
```

---

修饰成员变量：

- 普通的成员变量：声明的时候必须赋值.或者代码块中赋值，或者构造器赋值

  ```java
  final int b = 0;
  {
      b=0;
  }
  ```

- 类变量:声明时赋值，或者静态代码块

  ```java
  final static int a= 0;
  static {
      a = 0;
  }
  ```

不初始化就会报错了

---

局部内部类和匿名内部类只能访问局部final变量。 (原因有点复杂)

##### this 关键字 和super 关键字

this 关键字用于引用类的**当前实例**。

super 关键字用于从子类访问父类的变量和方法



**使用 this 和 super 要注意的问题：**

- 在构造器中使用 `super()` 调用父类中的其他构造方法时，该语句必须处于构造器的首行，否则编译器会报错。另外，this 调用本类中的其他构造方法时，也要放在首行。
- this、super 不能用在 static 方法中。

**简单解释一下：**

被 static 修饰的成员属于类，不属于单个这个类的某个对象，被类中所有对象共享。而 this 代表对本类对象的引用，指向本类对象；而 super 代表对父类对象的引用，指向父类对象；所以， **this 和 super 是属于对象范畴的东西，而静态方法是属于类范畴的东西**。



##### static 关键字详解

1. 修饰成员变量和成员方法
2. 静态代码块
3. 修饰类(只能修饰内部类)
4. 静态导包(用来导入类中的静态资源，1.5 之后的新特性)



> 修饰成员变量和成员方法(常用)

被 static 修饰的成员属于类。被 static 声明的成员变量属于静态成员变量，静态变量 存放在 Java 内存区域的方法区。

方法区与 Java 堆一样，是各个线程共享的内存区域，它用于存储已被虚拟机加载的类信息、常量、静态变量、即时编译器编译后的代码等数据。虽然 Java 虚拟机规范把方法区描述为堆的一个逻辑部分，但是它却有一个别名叫做 Non-Heap（非堆），目的应该是与 Java 堆区分开来。

> 静态代码块

静态代码块定义在类中方法外, 静态代码块在非静态代码块之前执行(静态代码块 —> 非静态代码块 —> 构造方法)。 该类不管创建多少对象，静态代码块只执行一次.

一个类中的静态代码块可以有多个，位置可以随便放，它不在任何的方法体内，JVM 加载类时会执行这些静态的代码块，如果静态代码块有多个，JVM 将按照**它们在类中出现的先后顺序依次执行它们**，**每个代码块只会被执行一次。**

静态代码块对于定义在它之后的静态变量，可以赋值，但是不能访问.



> 静态内部类

静态内部类与非静态内部类之间存在一个最大的区别，我们知道非静态内部类在编译完成之后会隐含地保存着一个引用，该引用是指向创建它的外围类，但是静态内部类却没有。没有这个引用就意味着：

1. 它的创建是不需要依赖外围类的创建。
2. 它不能使用任何外围类的非 static 成员变量和方法。

实现单例模式

```java
public class Singleton {

    //声明为 private 避免调用默认构造方法创建对象
    private Singleton() {
    }

   // 声明为 private 表明静态内部该类只能在该 Singleton 类中被访问
    private static class SingletonHolder {
        private static final Singleton INSTANCE = new Singleton();
    }

    public static Singleton getUniqueInstance() {
        return SingletonHolder.INSTANCE;
    }
}
```

当 Singleton 类加载时，静态内部类 SingletonHolder 没有被加载进内存。只有当调用 `getUniqueInstance()`方法从而触发 `SingletonHolder.INSTANCE` 时 SingletonHolder 才会被加载，此时初始化 INSTANCE 实例，**并且 JVM 能确保 INSTANCE 只被实例化一次。**

这种方式不仅具有延迟初始化的好处，而且由 JVM 提供了对线程安全的支持。









## 面向对象



#### 构造方法有哪些特点？是否可被 override?

特点：

1. 名字与类名相同。
2. 没有返回值，但不能用 void 声明构造函数。
3. 生成类的对象时自动执行，无需调用。

构造方法不能被 override（重写）,但是可以 overload（重载）,所以你可以看到一个类中有多个构造函数的情况。

#### 面向对象三大特征

- 封装
  - 简单讲就是把对象的属性和方法结合成一个独立的整体，隐藏实现细节，并提供对外访问的接口
  - 安全，增加代码复用性，模块化
- 继承
  - 继承父类的方法，并自己进行扩展，解决了代码重用的问题
  - 
- 多态
  - 基于对象所属类的不同，外部对同一个方法的调用，实际执行的逻辑不同
  - **如果是成员变量：编译看左边，运行看左边**
  - **如果是成员方法：编译看左边，运行看右边**  -- 依赖动态绑定
  - **如果是静态方法：编译看左边，运行看左边**
  - **子类的扩展方法，如果左侧是父类，那么这个方法就无法使用**
  - 实现多态的技术称为：动态绑定（dynamic binding），是指在执行期间判断所引用对象的实际类型，根据其实际的类型调用其相应的方法
  - 优点：灵活性，接口行，扩展性

#### 反射

通过反射你可以获取任意一个类的所有属性和方法，你还可以调用这些方法和属性。**控制改变在运行时的行为的程序**

> 优缺点

**优点**：

- 代码更加灵活，避免将程序写死到代码里，为各种框架提供开箱即用的功能提供了便利

缺点：

- 安全问题。无视泛型参数的安全检查、访问私有变量等
- 性能比较慢(不过这是大量使用的情况下才能察觉到)



反射赋予了jvm动态编译的能力。动态编译可以最大限度的体现Java的灵活性（多态）。

> 应用场景

像 Spring/Spring Boot、MyBatis 等等框架中都大量使用了反射机制。**这些框架中也大量使用了动态代理，而动态代理的实现也依赖反射。**

##### 获取 Class 对象的四种方式

如果我们动态获取到这些信息，我们需要依靠 Class 对象。Class 类对象将一个类的方法、变量等信息告诉运行的程序。Java 提供了四种方式获取 Class 对象:

**1.知道具体类的情况下可以使用：**

```java
Class alunbarClass = TargetObject.class;
```

但是我们一般是不知道具体类的，基本都是通过遍历包下面的类来获取 Class 对象，通过此方式获取 Class 对象不会进行初始化

**2.通过 `Class.forName()`传入类的路径获取：**

```javascript
Class alunbarClass1 = Class.forName("cn.javaguide.TargetObject");
```

**3.通过对象实例`instance.getClass()`获取：**

```java
TargetObject o = new TargetObject();
Class alunbarClass2 = o.getClass();
```

**4.通过类加载器`xxxClassLoader.loadClass()`传入类路径获取:**

```java
Class clazz = ClassLoader.loadClass("cn.javaguide.TargetObject");
```

通过类加载器获取 Class 对象不会进行初始化，意味着不进行包括初始化等一些列步骤，静态块和静态对象不会得到执行

#### 注解

##### 注解的作用

- **格式检查：**告诉编译器信息，比如被@Override标记的方法如果不是父类的某个方法
- **减少配置：**运行时动态处理，得到注解信息，实现代替配置文件的功能；依赖于反射
- **减少重复工作**：比如junit的@Test注解

##### 注解是如何工作的？

- 元注解(比如**@Target**、**@Retention**、**@Documented**、**@Inheritedn**)的用户是jvm，是在字节码层面工作的。
- 自定义注解，用户是每个使用注解的类，通过反射获取注解类的信息





#### 异常

![image-20210708211731173](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210708211731.png)

> try-catch-finally

`finally` 语句块将在方法返回之前被执行。

**在以下 3 种特殊情况下，`finally` 块不会被执行：**

1. 在 `try` 或 `finally`块中用了 `System.exit(int)`退出程序。但是，如果 `System.exit(int)` 在异常语句之后，`finally` 还是会被执行
2. 程序所在的线程死亡。
3. 关闭 CPU。

> try-catch-resources

Java 中类似于`InputStream`、`OutputStream` 、`Scanner` 、`PrintWriter`等的资源都需要我们调用`close()`方法来手动关闭，

```java
Scanner scanner = null;
try {
    scanner = new Scanner(new File("D://read.txt"));
    while (scanner.hasNext()) {
        System.out.println(scanner.nextLine());
    }
} catch (FileNotFoundException e) {
    e.printStackTrace();
} finally {
    if (scanner != null) {
        scanner.close();
    }
}
```

就比较繁琐，我们如果把声明和赋值都放进try里面就是小标题里的·`try-catch-resources`，就可以做到出现异常自动关闭

```java
try (Scanner scanner = new Scanner(new File("test.txt"))) {
    while (scanner.hasNext()) {
        System.out.println(scanner.nextLine());
    }
} catch (FileNotFoundException fnfe) {
    fnfe.printStackTrace();
}
```

#### IO

> 什么是序列化?什么是反序列化?

简单来说：

- **序列化**： 将数据结构或对象转换成二进制字节流的过程
- **反序列化**：将在序列化过程中所生成的二进制字节流的过程转换成数据结构或者对象的过程



**序列化的主要目的是通过网络传输对象或者说是将对象存储到文件系统、数据库、内存中**



>transient

这个关键字的作用就是阻止变量序列化。 被 `transient` 修饰的变量值不会被持久化和恢复(序列化和反序列化)。

- `transient` 只能修饰变量，不能修饰类和方法。
- `transient` 修饰的变量，在反序列化后变量值将会被置成类型的默认值。例如，如果是修饰 `int` 类型，那么反序列后结果就是 `0`。
- `static` 变量因为不属于任何对象(Object)，所以无论有没有 `transient` 关键字修饰，均不会被序列化。

##### Java 中 IO 流分为几种?

- 按照流的流向分，可以分为输入流和输出流；
- 按照操作单元划分，可以划分为字节流和字符流；
- 按照流的角色划分为节点流和处理流。

![](https://camo.githubusercontent.com/77d37587f21dae01f02785c69549b3ef02b37a4ab1ab6f17fe44a737b17a4ee0/68747470733a2f2f6d792d626c6f672d746f2d7573652e6f73732d636e2d6265696a696e672e616c6979756e63732e636f6d2f323031392d362f494f2d2545362539332538442545342542442539432545362539362542392545352542432538462545352538382538362545372542312542422e706e67)

![image-20210729193905785](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210729193905.png)

##### 既然有了字节流,为什么还要有字符流?

问题本质想问：**不管是文件读写还是网络发送接收，信息的最小存储单元都是字节，那为什么 I/O 流操作要分为字节流操作和字符流操作呢？**

回答：字符流是由 Java 虚拟机将字节转换得到的，问题就出在这个过程还算是非常耗时，并且，如果我们不知道编码类型就很容易出现乱码问题。所以， I/O 流就干脆提供了一个直接操作字符的接口，方便我们平时对字符进行流操作。如果音频文件、图片等媒体文件用字节流比较好，如果涉及到字符的话使用字符流比较好。



#### IO多路复用

文章

https://blog.csdn.net/XueyinGuo/article/details/113096163

#### BigDecimal

浮点数**精度丢失**，不能正确判断，于是BigDecimal类可以解决这个问题

```java
float a = 1.0f - 0.9f;
float b = 0.9f - 0.8f;
System.out.println(a);// 0.100000024
System.out.println(b);// 0.099999964
System.out.println(a == b);// false
```

```java
BigDecimal a = new BigDecimal("1.0");
BigDecimal b = new BigDecimal("0.9");
BigDecimal c = new BigDecimal("0.8");

BigDecimal x = a.subtract(b); 
BigDecimal y = b.subtract(c); 
System.out.println(Objects.equals(x, y)); /* true */
```

> 大小比较

```java
BigDecimal a = new BigDecimal("1.0");
BigDecimal b = new BigDecimal("0.9");
System.out.println(a.compareTo(b));// 1
```

> 保留小数

通过 `setScale`方法设置保留几位小数以及保留规则。保留规则有挺多种，不需要记，IDEA会提示。

```java
BigDecimal m = new BigDecimal("1.255433");
BigDecimal n = m.setScale(3,BigDecimal.ROUND_HALF_DOWN);
System.out.println(n);// 1.255
```

> 总结

BigDecimal 主要用来操作（大）浮点数，BigInteger 主要用来操作大整数（超过 long 类型）。

BigDecimal 的实现利用到了 BigInteger, 所不同的是 BigDecimal 加入了小数位的概念









#### 5、接口和抽象类

- 抽象类可以存在普通成员函数，接口只能存在public abstract 方法
- 抽象类中的成员变量可以是各种类型的，接口中的成员变量只能是public static final
- 抽象类只能继承一个，接口可以实现多个

接口是为了约束行为的有无。 `like a` bird like a aircrafrt（像这个一样可以飞行）

抽象类是对子类的相同行为抽象出来的，为了代码复用。 `is a` BMW is a car



#### sleep，wait，join，yield

1.锁池

所有竞争同步锁的线程，都在里面。sync。。对象的锁被某一个线程拿到了，其他线程就进去等了

2.等待池

wait方法，线程就进入等待池。等待池的线程不去竞争同步锁。只有调用notify或者notifyall，采取竞争。notify()是随机从等待池中选出一个放入锁池。notifyAll（）是将等待池中的所有线程都放进去。

> sleep和wait

- sleep是Thread的静态本地方法，wait是Object类的本地方法





#### 12.泛型

泛型提供了编译时类型安全检测机制，该机制允许程序员在编译时检测到非法的类型。泛型的本质是参数化类型，操作的数据类型被指定为一个参数。java的泛型是伪泛型，因为 Java 在编译期间，所有的泛型信息都会被擦掉，这也就是通常所说**类型擦除**。

我们可以通过反射机制破坏泛型，从这里可以看出，类型擦除

```java
List<Integer> list = new ArrayList<>();

list.add(12);
//这里直接添加会报错
list.add("a");
Class<? extends List> clazz = list.getClass();
Method add = clazz.getDeclaredMethod("add", Object.class);
//但是通过反射添加，是可以的
add.invoke(list, "kl");
```

泛型一般有三种使用方式:泛型类、泛型接口、泛型方法。



#### 深拷贝和浅拷贝

> 引用拷贝和对象拷贝

**引用拷贝**：   两个地址是相同的，其实是同一个对象

```java
Teacher teacher = new Teacher("riemann", 28);
Teacher teacher2 = teacher;  
```

![image-20210708204845074](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210708204845.png)





**对象拷贝**:  两个对象的地址不同，创建新的对象

```java
Teacher teacher = new Teacher("riemann", 28);
Teacher otherTeacher = (Teacher) teacher.clone();
```

![image-20210708204936297](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210708204936.png)



浅拷贝和深拷贝都属于对象拷贝。但是他们有区别，区别在于对象的引用类型

> 浅拷贝和深拷贝



**浅拷贝**：  通过下图可以知道，当我们修改student2里面的teacher对象时，student1里面也会改变

![image-20210708205053605](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210708205053.png)

**深拷贝**：深拷贝是一个整个独立的对象拷贝，深拷贝会拷贝所有的属性,并拷贝属性指向的动态分配的内存。



![image-20210708205137252](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210708205137.png)



#### 对象相等和引用相等

![image-20210708205705113](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210708205705.png)









## 多线程

### 1.线程和进程

进程是程序的一次执行过程。一个进程里面有很多个线程，线程共享进程的堆和方法区(元空间)。每个线程有自己的程序计数器、虚拟机栈、本地方法栈。

#### 程序计数器、虚拟机栈和本地方法栈为什么是私有的

**程序计数器**私有主要是为了**线程切换后能恢复到正确的执行位置**。

为了**保证线程中的局部变量不被别的线程访问到**，虚拟机栈和本地方法栈是线程私有的。

### 2.多线程

#### 1.为什么使用多线程？

线程可以看成是轻量级的进程，线程的切换和调度的成本远远小于进程。现在的计算机基本都是多核的，意味着多个线程可以同时运行，这减少了线程上下文切换的开销。

现在的系统用户访问量大，动不动就要求千万级的并发量。多线程并发编程式高并发的基础。

为了充分利用CPU的资源。

#### 2.使用多线程会有什么问题？

并发编程的目的就是为了能提高程序的执行效率提高程序运行速度，但是并发编程并不总是能提高程序运行速度的，而且并发编程可能会遇到很多问题，比如：**内存泄漏、死锁、线程不安全**等等。

##### 内存泄露和内存溢出

> 内存泄露

说的是**申请的内存空间没有被正确释放**，导致后续程序里的这块内存被永远占用(不可达)，如果这块内存空间的指针不存了，这块内存就永远不可达。(10个人，10张纸，有一个跑路了，就只剩下9张，这样的人一多，最后一张纸都没了)

> 内存溢出

内存溢出是指存储的数据超出了指定空间的大小，这时数据就会越界。常见的溢出是在栈空间里。java中的OOM

#### 3、线程的生命周期和状态

NEW、RUNNABLE、BLOCKED、WAIT、TIMEWAIT、TERMINATED

新生态、运行态、阻塞、等待、超时等待、终止



状态切换，线程创建，就是NEW，使用start()方法，就变成READY，获得CPU的时间片之后就处于RUNNING

jvm里面没有区分就绪态和运行态？ 因为现在操作系统用的是时间片调度，每一次进程获取到CPU的时间片进行运行，只有0.01-0.02s，特别快就没了，也就是回到了ready，所以jvm使用RUNNABLE包含了这两个状态。

#### 4、上下文切换

线程在执行过程中会有自己的**运行条件和状态**（也称**上下文**），如计数器、栈信息等。当发生下列几种情况就会发生切换：

- 主动让出CPU，sleep(),wait()
- 时间片用完了
- 调用了阻塞类型的系统中断，请求IO

线程切换意味着需要保存当前线程的上下文，留待线程下次占用 CPU 的时候恢复现场，加载另一个线程的上下文



#### 5、为什么我们不能直接调用 run() 方法？

因为我们是要在多线程的环境下执行，调用start()方法会执行线程的准备工作，会使线程进入就绪态，当获取到CPU的时间片时，就会自动执行run()方法。这是多线程下的工作。如果直接用run方法，就变成main线程下的一个普通方法，不是多线程了

#### 6、threadLocal

https://www.bilibili.com/video/BV1SJ41157oF?from=search&seid=2499275041109457778



- 解决线程安全问题
  - 比如我写的项目里面用到的kryo序列化框架，

### 3、锁

介绍各种锁的文章

https://tech.meituan.com/2018/11/15/java-lock.html



#### 说说sleep()方法和wait()方法的区别

相同点：

- 两个都可以暂停线程的执行

不同点：

- sleep()不释放锁，wait释放锁
- wait()通常用于线程间交互，sleep()用于暂停执行
- wait()被调用之后，需要其他线程调用同一个对象的notify()或者notifyall方法或者使用wait(time)超时后自动苏醒。sleep()执行完成后，线程自动苏醒
- sleep()会让出cpu执行时间，强制上下文切换。可以理解成，不需要这个锁的线程能够获得cpu的资源继续执行。



#### synchronized 关键字

**`synchronized` 关键字解决的是多个线程之间访问资源的同步性。**`synchronized`关键字可以保证被它修饰的方法或者代码块在任意时刻只能有一个线程执行。(以前是重量级锁，1.6之后加了多个锁的东西。在后面有)



##### Synchronized 关键字最主要的三种使用方式

1.修饰实例方法，锁的是当前对象的实例

2.修饰静态方法，锁的是这个类

3.修饰代码块：指定加锁的对象



#####  构造方法可以使用 synchronized 关键字修饰么？

先说结论：**构造方法不能使用 synchronized 关键字修饰。**

构造方法本身就属于线程安全的，不存在同步的构造方法一说。



##### 讲一下 synchronized 关键字的底层原理

查看编译的字节码文件，可以看到当**synchronized锁代码块**的时候，使用**`monitorenter` 和 `monitorexit` 指令**，代码块的内容放在这两个指令之间。

当执行 `monitorenter` 指令时，线程试图获取锁也就是获取 **对象监视器 `monitor`** 的持有权。会尝试获取对象的锁，如果锁的计数器为 0 则表示锁可以被获取，获取后将锁计数器设为 1 也就是加 1。在

执行 `monitorexit` 指令后，将锁计数器设为 0，表明锁被释放。如果获取对象锁失败，那当前线程就要阻塞等待，直到锁被另外一个线程释放为止。



synchronized锁方法的情况下，使用了`ACC_SYNCHRONIZED` 标识而不是上面两个指令，该标识指明了该方法是一个同步方法。

**两者的本质都是对对象监视器 monitor 的获取。**



##### 说说 JDK1.6 之后的 synchronized 关键字底层做了哪些优化

JDK1.6 对锁的实现引入了大量的优化，如偏向锁、轻量级锁、自旋锁、适应性自旋锁、锁消除、锁粗化等技术来减少锁操作的开销。锁主要存在四种状态，依次是：**无锁状态、偏向锁状态、轻量级锁状态、重量级锁状态**，会随着锁的竞争逐渐升级。只能升不能降级

> 偏向锁

针对于一个线程而言的, 线程获得锁之后就不会再有解锁等操作了。假如有两个线程来竞争该锁话, 那么偏向锁就失效了, 进而升级成轻量级锁了。

我的理解：偏向锁的设计是为了优化vector等线程安全的集合，当没有多线程的时候，因为以前只有重量级锁，那么使用vector就很慢，但是优化出了偏向锁之后，锁的消耗就少了。可以算是一个弥补吧

> 轻量级锁

有线程A和线程B来竞争对象c的锁，这时线程A和线程B同时将对象c的MarkWord(对象的信息，内存地址等)复制到自己的锁记录中, 两者竞争去获取锁, 假设线程A成功获取锁, 并将对象c的对象头中的线程ID(MarkWord中)修改为指向自己的锁记录的指针, 这**时线程B仍旧通过CAS去获取对象c的锁**, 获取失败. 此时为了提高获取锁的效率, **线程B会循环去获取锁**, 这个循环是有次数限制的, 如果在循环结束之前CAS操作成功, 那么线程B就获取到锁, **如果循环结束依然获取不到锁, 则获取锁失败, 对象c的MarkWord中的记录会被修改为重量级锁, 然后线程B就会被挂起**, 之后有线程C来获取锁时, 看到对象c的MarkWord中的是重量级锁的指针, 说明竞争激烈, 直接挂起.

> 重量级锁

获取不到锁就马上进入**阻塞状态**的锁，我们称之为**重量级锁**。需要等待那个持有锁的线程释放锁，然后再把我们从阻塞的状态唤醒，我们再去获取这个方法的锁。

> 自旋锁

线程从**运行态**进入**阻塞态**这个过程，是非常耗时的.线程从阻塞态唤醒也是一样，也是非常消耗时间的。

所以设计了一种锁，不是获取不到锁就立马进入阻塞状态，而是等待一段时间，看看这段时间有没其他人把这锁给释放了。也就是while()  ，，里面可以设定次数。如果循环一定的次数还拿不到锁，那么它才会进入阻塞的状态。

> 自适应自旋锁

上面的自旋锁，是设定次数之后，所有的自旋锁都按照这个次数进行旋转。

自适应自旋锁就牛逼了，它不需要我们人为指定循环几次，它自己本身会进行判断要循环几次。能够根据**线程最近获得锁的状态**来调整循环次数。

> 乐观锁

没出问题之前不加锁，如果出现了冲突，我们在想办法解决。 CAS 机制

> 悲观锁

重量级锁、自旋锁和自适应自旋锁，进入方法之前，就一定要先加一个锁，这种我们为称之为悲观锁



##### 谈谈 synchronized 和 ReentrantLock 的区别(开始)

共同点：

- 都是可重入锁
  - 可以再次获取自己的内部锁。如果不可锁重入的话，获取自己的内部锁(再次获取这个对象的锁)就会造成死锁。

区别：

- synchronized 依赖于 JVM 而 ReentrantLock 依赖于 API
  - ReentrantLock依靠try/catch 和 lock()和unlock()实现的
- ReentrantLock 比 synchronized 增加了一些高级功能
  -  可以指定是公平锁还是非公平锁。synchronized只能是非公平锁
  -  **等待可中断** :`ReentrantLock`提供了一种能够中断等待锁的线程的机制，通过 `lock.lockInterruptibly()` 来实现这个机制。也就是说**正在等待的线程可以选择放弃等待**，改为处理其他事情。
  -  **可实现选择性通知**：`ReentrantLock`，可以借助于`Condition`接口与`newCondition()`方法。实现绑定多个条件



#### volatile 关键字

##### 1. CPU 缓存模型

 **CPU 缓存则是为了解决 CPU 处理速度和内存处理速度不对等的问题。**

![image-20210725112335930](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210725112336.png)



**CPU Cache 的工作方式：**

先复制一份数据到 CPU Cache 中，当 CPU 需要用到的时候就可以直接从 CPU Cache 中读取数据，当运算完成后，再将运算得到的数据写回 Main Memory 中。但是，这样存在 **内存缓存不一致性的问题** ！比如我执行一个 i++操作的话，如果两个线程同时执行的话，假设两个线程从 CPU Cache 中读取的 i=1，两个线程做了 1++运算完之后再写回 Main Memory 之后 i=2，而正确结果应该是 i=3。

##### 2、 讲一下 JMM(Java 内存模型)

> 并发编程的三个重要特性

- 原子性
- 可见性
- 有序性

> JMM

在当前的 Java 内存模型下，线程可以把变量保存**本地内存**（比如机器的寄存器）中，而不是直接在主存中进行读写。这就可能造成一个线程在主存中修改了一个变量的值，而另外一个线程还继续使用它在寄存器中的变量值的拷贝，造成**数据的不一致**。

==每个线程都有自己的工作内存(本地内存)==

![image-20210725112455817](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210725112455.png)

要解决这个问题，就需要把变量声明为 **`volatile`** ，这就指示 JVM，这个变量是共享且不稳定的，每次使用它都到主存中进行读取。

**`volatile` 关键字 除了防止 JVM 的指令重排 ，还有一个重要的作用就是保证变量的可见性。**

可见性：就是线程A工作内存变量a变了，线程B里的内存变量a也会变成同样的

有序性：jvm编译的时候，有指令重排，volatile通过内存屏障，禁止指令进行重排序优化

还有一个原子性，volatile不能满足

##### 3.怎么保证可见性

Java内存模型定义了如下8种 **原子操作** 来实现主内存和工作内存之间的交互协议：

- read(读取) ：从主内存读取数据
- load(载入) ：将主内存读取到的数据写入工作内存
- use(使用) ：从工作内存读取数据来计算
- assign(赋值) ：将计算好的值重新赋值到工作内存中去
- store(存储) ：将工作内存数据写入到主内存
- write(写入) ：将store过去的变量赋值给主内存中的变量
- lock(锁定) ：将主内存变量加锁，标识为线程独占状态
- unlock(解锁) ：将主内存变量解锁，解锁后其他线程可以锁定该变量

![image-20210805192118574](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210805192125.png)

上面的图可以知道，线程2改变了flag之后，线程1不知道的



如何让线程1知道？

1. 加锁：同一个时间只有一个线程能read到flag这个变量
   1. read的时候用lock锁住，write完就解锁
   2. 加锁，就变成单线程执行了。**优化：降低锁的粒度，只有需要的时候加锁**
2. 事件响应模式：多个线程都可以read到flag这个变量，但是当有任何一个线程修改了这个变量的值，需要通知其他线程，使得自己工作内存中的缓存数据失效。
   1. **MESI缓存一致性协议**：多个CPU从主内存读取同一个数据到各自的高速缓存，当其中某个CPU修改了缓存里的数据，该数据会马上同步回主内存，其他CPU通过总线嗅探机制可以感知到数据的变化从而将自己缓存里的数据失效。
   2. 过程如下：
      1. flag被volatile修饰
      2. 线程2对flag做完assign之后，就给flag加一把锁，然后store
      3. **当store操作将flag值写回主内存的时候，需要经过CPU的总线，就会触发总线嗅探机制，通知其他CPU缓存失效**
      4. write之后，会unlock释放锁

volatile实现的将上面的两个方法结合起来了，降低了锁的粒度。

##### 4.怎么防止指令重排

即只要程序的最终结果 与它顺序化情况的结果相等，那么指令的执行顺序可以与代码顺序不一致，此过程叫指令的 重排序。

JVM能根据处理器特性(CPU多级缓存系统、多核处 理器等)适当的对机器指令进行重排序，使机器指令能更符合CPU的执行特性，最大限度的 发挥机器性能。

>as-if-serial

**不管怎么重排序**,程序的执**行结果不能被改变**。

编译器和处理器不会对存在数据依赖关系的操作做重排序， 因为这种重排序会改变执行结果。如果不存在数据依赖关系，就可能被重排序



> JVM的内存屏障

![image-20210805195419758](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210805195419.png)



volatile的实现：

- 在每个volatile写操作的前面插入一个StoreStore屏障。
- 在每个volatile写操作的后面插入一个StoreLoad屏障。
- 在每个volatile读操作的后面插入一个LoadLoad屏障。
- 在每个volatile读操作的后面插入一个LoadStore屏障。 

![image-20210805195436160](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210805195436.png)



![image-20210805195442437](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210805195442.png)





> synchronized 关键字和 volatile 关键字的区别

`synchronized` 关键字和 `volatile` 关键字是两个互补的存在，而不是对立的存在！

- **`volatile` 关键字**是线程同步的**轻量级实现**，所以 **`volatile `性能肯定比`synchronized`关键字要好** 。但是 **`volatile` 关键字只能用于变量而 `synchronized` 关键字可以修饰方法以及代码块** 。
- **`volatile` 关键字能保证数据的可见性，但不能保证数据的原子性。`synchronized` 关键字两者都能保证(通过解锁的时候要把数据刷回主内存保证的可见性)。**
- **`volatile`关键字主要用于解决变量在多个线程之间的可见性，而 `synchronized` 关键字解决的是多个线程之间访问资源的同步性。**





#### 线程池

线程池的好处：

- 降低资源的消耗
- 提高响应的速度(创建和销毁十分浪费资源)
- 方便管理

线程复用，控制最大并发数，管理线程

##### 1、线程池创建线程四大方法

```java
Executors.newSingleThreadExecutor()  //只有一个线程跑
Executors.newFixedThreadPool(5); //有五个线程跑
Executors.newCachedThreadPool();//电脑支持几个就有几个跑
```

> newCachedThreadPool

```java
public static ExecutorService newCachedThreadPool() {
        return new ThreadPoolExecutor(0, Integer.MAX_VALUE,  // 核心线程数为0
                                      60L, TimeUnit.SECONDS,
                                      new SynchronousQueue<Runnable>());
}
```

SynchronousQueue的大小为1(有界队列)。但是这个消息队列可以这样理解，你要把元素放进去，必须另一端有人已经等着用这个元素才行，所以这个元素实际上只是从这个队列过了一下。所以新任务一过来，就创建新的线程，线程数量是2^32-1

>newFixedThreadPool

```java
public static ExecutorService newFixedThreadPool(int nThreads) {
        return new ThreadPoolExecutor(nThreads, nThreads,
                                      0L, TimeUnit.MILLISECONDS,
                                      new LinkedBlockingQueue<Runnable>());
 }
```

固定线程数量，阻塞队列是无界的，所以任务一多，就全放在阻塞队列里面去了，然后可能导致cpu和内存飙升服务器挂掉。

>newScheduledThreadPool

```java
public ScheduledThreadPoolExecutor(int corePoolSize) {
        super(corePoolSize, Integer.MAX_VALUE, 0, NANOSECONDS,
              new DelayedWorkQueue());
    }
```

还是核心的线程数自己设置，但是最大线程数没有上限, **这个可以开启定时任务**

值得关心的是DelayedWorkQueue这个阻塞队列，它是ScheduledThreadPoolExecutor的静态内部类。简单的说，DelayedWorkQueue是一个无界队列，它能按一定的顺序对工作队列中的元素进行排列。

>newSingleThreadExecutor

在ScheduledThreadPoolExecutor(1)的基础上做了增强，不仅确保只有一个线程顺序执行任务，也保证线程意外终止后会重新创建一个线程继续执行任务



##### 2.七大参数

```java
public ThreadPoolExecutor(int corePoolSize,  // 核心线程池大小
                              int maximumPoolSize,   //最大核心线程数大小
                              long keepAliveTime,   // 超时了，没有人调用就会释放
                              TimeUnit unit,   // 超时单位
                              BlockingQueue<Runnable> workQueue,  // 阻塞队列
                              ThreadFactory threadFactory,		// 线程工厂，创建线程的，一般不动
                              RejectedExecutionHandler handler// 拒绝策略) 
```

![image-20210806093914576](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210806093914.png)

**参数的解释**：

核心线程数： 1和2窗口，一直开着

最大线程数：1-5，3-5开始是不开着的，如果候客区(阻塞队列)满了，那么就必须来上班

超时的单位：设定单位

超时等待：如果业务都处理的差不多了，设置了1h，1h之后还是没人去3,4,5窗口，那么就下班了（释放）

阻塞队列：就是候客区的大小

线程工厂：使用默认的Executors.defaultThreadFactory()

拒绝策略：如果1-5窗口满了，候客区也满了，还有人进来，那么就要让他等待或者走开。 (RejectedExecutionHandler 有四种实现类，也就是四个拒绝策略)





##### 3、四大拒绝策略

```java
/**
 * 四种拒绝策略
 * 1.ThreadPoolExecutor.AbortPolicy()  超过了我们的服务数量，就抛出异常
 * 2.new ThreadPoolExecutor.CallerRunsPolicy()   哪来的去哪里，交给送进来的线程执行
 * 3.ThreadPoolExecutor.DiscardPolicy()   队列满了就丢掉任务，不会抛出异常
 * 4.ThreadPoolExecutor.DiscardOldestPolicy()  队列满了，尝试去和最早的竞争，也不会抛出异常
 */
```

##### 4.阻塞队列

- **无界队列**
  - LinkedBlockingQueue。使用该队列做为阻塞队列时要尤其当心，当任务耗时较长时可能会导致大量新任务在队列中堆积最终导致OOM。
- **有界队列**
  - 遵循FIFO原则的队列如ArrayBlockingQueue
  - 优先级队列如PriorityBlockingQueue
  - 使用有界队列时队列大小需和线程池大小互相配合，线程池较小有界队列较大时可减少内存消耗，降低cpu使用率和上下文切换，但是可能会限制系统吞吐量。
- **同步移交队列**

##### 5.最大线程数如何选取

> CPU密集型

CPU密集型也是指计算密集型，大部分时间用来做计算逻辑判断等CPU动作的程序称为CPU密集型任务。该类型的任务需要进行大量的计算，主要**消耗CPU资源**，任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低。**计算密集型任务同时进行的数量应当等于CPU的核心数。** 配置cpu数目**(n) +1**个线程的线程池

> IO密集型

IO密集型任务指任务需要执行大量的IO操作，涉及到网络、磁盘IO操作，对CPU消耗较少。IO密集型任务线程并不是一直在执行任务，则应配置尽可能多的线程，如2*CPU数目**(2n)**。



##### 6、为什么要先添加队列，而不是先创建最大线程

因为一进来任务就创建线程的话，那么之后还要销毁线程，而线程池的作用就是为了减少创建和销毁线程，这些操作的开销比较大。



#### AQS

AQS 核心思想是，如果被请求的共享资源空闲，则将当前请求资源的线程设置为有效的工作线程，并且将共享资源设置为锁定状态。如果被请求的共享资源被占用，那么就需要一套线程阻塞等待以及被唤醒时锁分配的机制，这个机制 AQS 是用 CLH 队列锁实现的，即将暂时获取不到锁的线程加入到队列中。

> AQS原理图

![image-20210710161701312](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210710161701.png)

AQS 使用一个 int 成员变量来表示同步状态，通过内置的 FIFO 队列来完成获取资源线程的排队工作。AQS 使用 CAS 对该同步状态进行原子操作实现对其值的修改。

**AQS 定义两种资源共享方式**

- Exclusive（独占）：只有一个线程能执行，如`ReentrantLock`。又可分为公平锁和非公平锁：
  - 公平锁：按照线程在队列中的排队顺序，先到者先拿到锁
  - 非公平锁：当线程要获取锁时，无视队列顺序直接去抢锁，谁抢到就是谁的
- **Share**（共享）：多个线程可同时执行，如` CountDownLatch`、`Semaphore`、 `CyclicBarrier`、`ReadWriteLock` 我们都会在后面讲到。



### 4、死锁

#### 1.什么是死锁及产生的条件

死锁简单的讲，就是多个线程同时被阻塞了。他们都在等待某个资源被释放，由于无限期的阻塞，程序无法正常终止。(例子：线程A有资源1，等待资源2，线程B有资源2，等待资源1，那么就陷入死锁了)



死锁产生的四大条件：

1. 互斥条件：该资源任意一个时刻只由一个线程占用。
2. 请求与保持条件：一个进程因请求资源而阻塞时，对已获得的资源保持不放。
3. 不剥夺条件:线程已获得的资源在未使用完之前不能被其他线程强行剥夺，只有自己使用完毕后才释放资源。
4. 循环等待条件:若干进程之间形成一种头尾相接的循环等待资源关系。

#### 2.如何预防和避免死锁

*如何预防死锁？* 破坏死锁的产生的必要条件即可：

1. **破坏请求与保持条件** ：一次性申请所有的资源。
2. **破坏不剥夺条件** ：占用部分资源的线程进一步申请其他资源时，如果申请不到，可以主动释放它占有的资源。
3. **破坏循环等待条件** ：靠按序申请资源来预防。按某一顺序申请资源，释放资源则反序释放。破坏循环等待条件。

*如何避免死锁*？

借助于**算法（比如银行家算法）对资源分配进行计算评估，使其进入安全状态。** (可以看一下操作系统的这部分算法介绍)











## 集合

### String

#### String 、StringBuffer、StringBuilder

`String `是final修饰，不可变。每次操作都生成新的String对象       final  char[] value;

`StringBuffer` 和`StringBuilder`都是在原对象上操作

StringBuffer是线程安全的，方法都是synchronized修饰的。StringBuild是不安全的.

多线程情况下使用StringBuffer

### List

> ArrayList

- ArrayList 可以存放所有元素，包括null（多个）
- 底层是数组
- ArrayList不是线程安全的，没有用synchronize修饰方法。

#####  Arraylist 和 Vector 的区别?

- `ArrayList` 是 `List` 的主要实现类，底层使用 `Object[ ]`存储，适用于频繁的查找工作，线程不安全 ；
- `Vector` 是 `List` 的古老实现类，底层使用`Object[ ]` 存储，线程安全的。

#####  Arraylist 与 LinkedList 区别?

1. **是否保证线程安全：** `ArrayList` 和 `LinkedList` 都是不同步的，也就是**不保证线程安全**；
2. **底层数据结构：** `Arraylist` 底层使用的是 **`Object` 数组**；`LinkedList` 底层使用的是 **双向链表** 数据结构（JDK1.6 之前为循环链表，JDK1.7 取消了循环。
3. 插入和删除是否受元素位置的影响：
   - `ArrayList` 采用数组存储，所以插入和删除元素的时间复杂度受元素位置的影响。 比如：执行`add(E e)`方法的时候， `ArrayList` 会默认在将指定的元素追加到此列表的末尾，这种情况时间复杂度就是 O(1)。但是如果要在指定位置 i 插入和删除元素的话（`add(int index, E element)`）时间复杂度就为 O(n-i)。因为在进行上述操作的时候集合中第 i 和第 i 个元素之后的(n-i)个元素都要执行向后位/向前移一位的操作。
   - `LinkedList` 采用链表存储，所以，如果是在头尾插入或者删除元素不受元素位置的影响（`add(E e)`、`addFirst(E e)`、`addLast(E e)`、`removeFirst()` 、 `removeLast()`），近似 O(1)，如果是要在指定位置 `i` 插入和删除元素的话（`add(int index, E element)`，`remove(Object o)`） 时间复杂度近似为 O(n) ，因为需要先移动到指定位置再插入。
4. **是否支持快速随机访问：** `LinkedList` 不支持高效的随机元素访问，而 `ArrayList` 支持。快速随机访问就是通过元素的序号快速获取元素对象(对应于`get(int index)`方法)。
5. **内存空间占用：** ArrayList 的空间浪费主要体现在在 list 列表的结尾会预留一定的容量空间，而 LinkedList 的空间花费则体现在它的每一个元素都需要消耗比 ArrayList 更多的空间（因为要存放直接后继和直接前驱以及数据）。

##### ArrayList 的扩容机制

1.如果使用**无参构造方法**，那么直接创建长度为10的数组。如果指定长度，初始容量就是指定的长度

2.**int newCapacity = oldCapacity + (oldCapacity >> 1),所以 ArrayList 每次扩容之后容量都会变为原来的 1.5 倍左右**

3.扩容其实是创建一个新的数组，然后把原来的数组拷贝进去。`arraycopy()` 需要目标数组，将原数组拷贝到你自己定义的数组里或者原数组，而且可以选择拷贝的起点和长度以及放入新数组中的位置 `copyOf()` 是系统自动在内部新建一个数组，并返回该数组。



### Set

##### comparable 和 Comparator 的区别

- `comparable` 接口实际上是出自`java.lang`包 它有一个 `compareTo(Object obj)`方法用来排序。这个要在类中继承这个接口，然后重写方法
- `comparator`接口实际上是出自 java.util 包它有一个`compare(Object obj1, Object obj2)`方法用来排序。这个可以直接传给方法。

#####  比较 HashSet、LinkedHashSet 和 TreeSet 三者的异同



`HashSet` 是 `Set` 接口的主要实现类 ，`HashSet` 的底层是 `HashMap`，线程不安全的，可以存储 null 值；

`LinkedHashSet` 是 `HashSet` 的子类，能够按照添加的顺序遍历；

`TreeSet` 底层使用红黑树，能够按照添加元素的顺序进行遍历，排序的方式有自然排序和定制排序



### Map

##### Map

- `HashMap`： JDK1.8 之前 `HashMap` 由数组+链表组成的，数组是 `HashMap` 的主体，链表则是主要为了解决哈希冲突而存在的（“拉链法”解决冲突）。JDK1.8 以后在解决哈希冲突时有了较大的变化，当链表长度大于阈值（默认为 8）（将链表转换成红黑树前会判断，如果当前数组的长度小于 64，那么会选择先进行数组扩容，而不是转换为红黑树）时，将链表转化为红黑树，以减少搜索时间
- `LinkedHashMap`： `LinkedHashMap` 继承自 `HashMap`，所以它的底层仍然是基于拉链式散列结构即由数组和链表或红黑树组成。另外，`LinkedHashMap` 在上面结构的基础上，增加了一条双向链表，使得上面的结构可以保持键值对的插入顺序。同时通过对链表进行相应的操作，实现了访问顺序相关逻辑。
- `Hashtable`： 数组+链表组成的，数组是 `Hashtable` 的主体，链表则是主要为了解决哈希冲突而存在的
- `TreeMap`： 红黑树（自平衡的排序二叉树）



##### HashMap 和 Hashtable 的区别

1. **线程是否安全：** `HashMap` 是非线程安全的，`HashTable` 是线程安全的,因为 `HashTable` 内部的方法基本都经过`synchronized` 修饰。（如果你要保证线程安全的话就使用 `ConcurrentHashMap` 吧！）；
2. **效率：** 因为线程安全的问题，`HashMap` 要比 `HashTable` 效率高一点。
3. **对 Null key 和 Null value 的支持：** `HashMap` 可以存储 null 的 key 和 value，但 null 作为键只能有一个，null 作为值可以有多个；HashTable 不允许有 null 键和 null 值，否则会抛出 `NullPointerException`。
4. **初始容量大小和每次扩充容量大小的不同 ：** ① 创建时如果不指定容量初始值，`Hashtable` 默认的初始大小为 11，之后每次扩充，容量变为原来的 2n+1。`HashMap` 默认的初始化大小为 16。之后每次扩充，容量变为原来的 2 倍。② 创建时如果给定了容量初始值，那么 Hashtable 会直接使用你给定的大小，而 `HashMap` 会将其扩充为 2 的幂次方大小（`HashMap` 中的`tableSizeFor()`方法保证，下面给出了源代码）。也就是说 `HashMap` 总是使用 2 的幂作为哈希表的大小,后面会介绍到为什么是 2 的幂次方。
5. **底层数据结构：** JDK1.8 以后的 `HashMap` 在解决哈希冲突时有了较大的变化，当链表长度大于阈值（默认为 8）（将链表转换成红黑树前会判断，如果当前数组的长度小于 64，那么会选择先进行数组扩容，而不是转换为红黑树）时，将链表转化为红黑树，以减少搜索时间。Hashtable 没有这样的机制。

##### 多线程解决Map集合安全的问题

三种方式

- 使用Collections.synchronizedMap(Map)创建线程安全的map集合；
- Hashtable
- ConcurrentHashMap

ConcurrentHashMap，他的性能和效率明显高于前两者。

##### Collections.synchronizedMap是怎么实现线程安全的？

使用排斥锁mutex.  使用Synchronized(this.mutex)实现的。对象锁

##### 2.HashTable

使用Synchronized锁了方法。效率低

> HashTable和HashMap的不同

Hashtable 是不允许**键或值为 null** 的，HashMap 的键值则都可以为 null。Hashtable在我们put 空值的时候会直接抛空指针异常。

HashMap则是让key==null 的情况下hash值为0

**初始化容量不同**：HashMap 的初始容量为：16，Hashtable 初始容量为：11，两者的负载因子默认都是：0.75。

**扩容机制不同**：当现有容量大于总容量 * 负载因子时，HashMap 扩容规则为当前容量翻倍，Hashtable 扩容规则为当前容量翻倍 + 1。

**迭代器不同**：HashMap 中的 Iterator 迭代器是 fail-fast 的，而 Hashtable 的 Enumerator 不是 fail-safe 的

因为迭代器不一样。遍历过程做操作会有异常。



>快速失败（fail—fast）    **安全失败（fail—safe）**

**快速失败（fail—fast）**是java集合中的一种机制， 在用迭代器遍历一个集合对象时，如果遍历过程中对集合对象的内容进行了修改（增加、删除、修改），则会抛出Concurrent Modification Exception。

java.util.concurrent包下的容器都是**安全失败**，可以在多线程下并发使用，并发修改。(HashTable也是安全失败)

`java.util`包下面的所有的集合类都是**fail-fast**的(除了HashTabel比较特殊)

##### 3.concurrentHashMap

> **1.7：**

![image-20210728212423368](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210728212430.png)

HashEntry跟HashMap差不多的，但是不同点是，他使用volatile去修饰了他的数据Value还有下一个节点next。

```text
  transient volatile HashEntry<K,V>[] table;
```

ConcurrentHashMap 采用了**分段锁**技术，其中 Segment 继承于 ReentrantLock。ConcurrentHashMap 支持Segment 数量的线程并发。





**PUT方法**：

1. 计算要 put 的 key 的位置，获取指定位置的 Segment。

2. 如果指定位置的 Segment 为空，则初始化这个 Segment.

   **初始化 Segment 流程：**

   1. 检查计算得到的位置的 Segment 是否为null.
   2. 为 null 继续初始化，使用 Segment[0] 的容量和负载因子创建一个 HashEntry 数组。
   3. 再次检查计算得到的指定位置的 Segment 是否为null.
   4. 使用创建的 HashEntry 数组初始化这个 Segment.
   5. 自旋判断计算得到的指定位置的 Segment 是否为null，使用 CAS 在这个位置赋值为 Segment.

3. Segment.put 插入 key,value 值。

不断的自旋获得锁，指定次数的自旋操作，超过次数之后，就进入阻塞



> 1.8

![image-20210728213158953](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210728213159.png)

的初始化是通过**自旋和 CAS** 操作完成的。里面需要注意的是变量 `sizeCtl` ，它的值决定着当前的初始化状态。

- -1 说明正在初始化
- -N 说明有N-1个线程正在进行扩容



**PUT**

1. 根据 key 计算出 hashcode 。
2. 判断是否需要进行初始化。
3. 即为当前 key 定位出的 Node，如果为空表示当前位置可以写入数据，利用 CAS 尝试写入，失败则自旋保证成功。
4. 如果当前位置的 `hashcode == MOVED == -1`,则需要进行扩容。
5. 如果都不满足，则利用 synchronized 锁写入数据。
6. 如果数量大于 `TREEIFY_THRESHOLD` 则要转换为红黑树。

## jvm

### 1.类的生命周期

 https://blog.csdn.net/zhengzhb/article/details/7517213

### 6、GC怎么判断对象可以被回收

- 引用技术法：每个对象有一个引用技术属性，新增一个引用就+1，释放就减1，为0就可以回收。java中用的不是这个，这是其他语言的
- 可达性分析法：从GC roots 开始向下搜索，搜索所走过的路劲，称为引用链。当一个对象到GC roots没有任何引用链连接时，此对象不可用.**这是java用的**

java中GC roots的对象：

- 虚拟机栈中引用的对象
- 方法区静态属性引用的对象
- 方法区中常量引用的对象
- JNI中引用的对象



![image-20210624155358785](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210624155358.png)



### 21、java内存

![image-20210709182535044](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210709182535.png)



![image-20210709182446603](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210709182446.png)





#### 为什么要将永久代替换成元空间？



- 整个永久代有一个 JVM 本身设置的固定大小上限，无法进行调整，而元空间使用的是直接内存，受本机可用内存的限制，虽然元空间仍旧可能溢出，但是比原来出现的几率会更小。
- 元空间里面存放的是类的元数据，这样加载多少类的元数据就不由 `MaxPermSize` 控制了, 而由系统的实际可用空间来控制，这样能加载的类就更多了。
- 在 JDK8，合并 HotSpot 和 JRockit 的代码时, JRockit 从来没有一个叫永久代的东西, 合并之后就没有必要额外的设置这么一个永久代的地方了

# go

### 1.基础

#### 1.new 和make的区别

- new
  - 只接受一个参数，参数是一个类型，并且返回一个指向该类型内存地址的指针。
  - new会把分配的内存置为0，也就是赋0值
  - 
- make
  - make 也是用于内存分配的，但是和 new 不同，它只用于 chan、map 以及 slice 的内存创建
  - make返回的类型是这三个类型的本身，因为这三个本身就是引用类型

### 2.常见的数据结构实现原理

#### 1.channel

```GO
type hchan struct {
    qcount   uint           // 当前队列中剩余元素个数
    dataqsiz uint           // 环形队列长度，即可以存放的元素个数
    buf      unsafe.Pointer // 环形队列指针 (指向底层存储元素)
    sendx    uint           // 队列下标，指示元素写入时存放到队列中的位置
    recvx    uint           // 队列下标，指示元素从队列的该位置读出
    
    recvq    waitq          // 等待读消息的goroutine队列
    sendq    waitq          // 等待写消息的goroutine队列
    
  	elemtype *_type         // 元素类型
    elemsize uint16         // 每个元素的大小
    
  	lock mutex              // 互斥锁，chan不允许并发读写
    closed   uint32            // 标识关闭状态
}
```

- 环形队列（数据）：qcount，队列内部元素的个数，dataqsize-整个队列的长度，sendx-写入时的下标，recvx-读数据时的下标
- 等待队列（）：
  - 从channel读，如果channel缓冲区为空或者没有缓冲区。goroutine会阻塞，并放进recvq队列中
  - 向channel写，如果channel缓冲区已满或者没有缓冲区，goroutine会被阻塞，并放进sendq队列中
  - 通常，recvq和sendq至少有一个为空。除非同一个goroutine使用select语句向channel一边写数据，一边读数据。
- 类型信息，类型和类型大小（用于在buf中定位元素位置）
- 锁：一个channel同时仅允许被一个goroutine读写

##### channel读写和关闭

- 向一个channel中写数据：
  - 先看recvq队列有没有元素，如果有的话，那么说明缓冲区没数据，从recvq中取出G，把数据写入G中，然后唤醒G，结束。
  - recvq队列没有元素，看缓冲区有无多余的位置，如果有，就将数据写入缓冲区，结束。
  - 如果缓冲区无多余的位置，将代写数据写入G，将G加入到sendq队列中，进入睡眠，等待唤醒
- 向channel读数据：
  - sendq队列不为空且没有缓冲区，直接从sendq中取出G，读取G中的数据，把G唤醒，结束过程。
  - sendq队列不为空，有缓冲区，说明缓冲区满了，那么直接从缓冲区中读数据，把G中的数据放入缓冲区尾部，唤醒G，结束过程
  - sendq队列为空，缓冲区有数据，直接从缓冲区中读数据，结束过程
  - sendq队列为空， 缓冲区没数据，将G加入recvq队列，进入睡眠，等待唤醒
- 关闭channel：
  - 关闭channel时会把recvq和sendq中的G全部唤醒，把recvq本该写入G的数据位置变为nil，sendq中的G全部panic。
  - panic的其他场景
    - 关闭值为nil的channel
    - 关闭已经被关闭的channel
    - 向已经关闭的channel写数据



select的case语句读channel不会阻塞，尽管channel中没有数据。这是由于case语句编译后调用读channel时会明确传入不阻塞的参数，此时读不到数据时不会将当前goroutine加入到等待队列，而是直接返回。

> range

通过range可以持续从channel中读出数据，好像在遍历一个数组一样，当channel中没有数据时会阻塞当前goroutine，与读channel时阻塞处理机制一样。

```GO
func chanRange(chanName chan int) {
    for e := range chanName {
        fmt.Printf("Get element from chan: %d\n", e)
    }
}
```

如果向此channel**写数据的goroutine**退出时，系统检测到这种情况后会**panic**，**否则range将会永久阻塞**。



#### 2.slice

底层结构有三个变量分别是len,cap和底层数组的指针

```go
type slice struct {
    array unsafe.Pointer
    len   int
    cap   int
}
```

> 创建slice

```go
slice := make([]int, 5, 10)  // 0,0,0,0,0-0-0-0-0-0
slice := array[5:7]  //其实地址从数组的5开始，len是切的长度，cap是数组之后剩的容量，比如数组长度为10，则len=2，cap=5
```

> slice扩容

- 容量足够，直接在数组后面加数据
- 容量不够，进行append操作会扩容，扩容会产生新的地址，cap变为原来的两倍
- 如果cap追加多个数据，**两倍也不够**，**会继续扩容直到cap>len;(此时不是整倍的扩容了)；**

> 多切片共用空间

- 多切片共用相同的数组空间时，其**结果会相互影响**但是其**len值不会相互影响**； 扩容



#### 3.map

##### 1。结构

map的底层结构，buckets指向**桶数组的指针**（数据都存放在桶里）

```go
type hmap struct {
     /* 重要*/
    count     int 
    // 代表哈希表中的元素个数，调用len(map)时，返回的就是该字段值。
    flags     uint8 
    // 状态标志，下文常量中会解释四种状态位含义。
    B         uint8  
    // buckets（桶）的对数log_2
    // 如果B=5，则buckets数组的长度 = 2^5=32，意味着有32个桶
    noverflow uint16 
    // 溢出桶的大概数量
    hash0     uint32 
    // 哈希种子
    buckets    unsafe.Pointer 
    // 指向buckets数组的指针，数组大小为2^B，如果元素个数为0，它为nil。
    oldbuckets unsafe.Pointer 
    // 如果发生扩容，oldbuckets是指向老的buckets数组的指针，老的buckets数组大小是新的buckets的1/2;非扩容状态下，它为nil。
    
    nevacuate  uintptr        
    // 表示扩容进度，小于此地址的buckets代表已搬迁完成。
    extra *mapextra 
    // 这个字段是为了优化GC扫描而设计的。当key和value均不包含指针，并且都可以inline时使用。extra是指向mapextra类型的指针。
 }

```

- map中buckets存的是个指针，所以如果map1 = map2，那么map1和map2就都用了同一个桶的引用，修改其中的一个map，另外一个的值也会被修改

桶的结构

```go
#编译之后的桶的结构
type bmap struct {
  topbits  [8]uint8
  keys     [8]keytype
  values   [8]valuetype
  pad      uintptr
  overflow uintptr
  // 溢出桶
}

```

- key和value分开放的，而不是别的语言里key和value一起存放。源码里-这样的好处是在某些情况下可以省略掉 padding字段，节省内存空间。



##### 2.创建

- 创建一个随机的hash种子
- 根据传入的内容，计算出最少需要的bucket数-B
- 再创建用于保存桶的数组

##### 3.查找

- 通过hash种子计算key的hash值，使用hash值取模m（m表示桶的数量）找到对应的桶
- 使用hash的高8位字节，这个是tophash的值，去tophash数组找相等的
- 如果tophash数组中有相等的，就取出下标，去key数组里面进行key的比较
- 如果当前的桶里没有找到相等的tophash，就进溢出桶里面找
- 直到所有的桶都找完，如果中间找到了，就返回 h[key] 的指针
- 如果没有找到，就返回对应类型的0值（**注意：不是nil**）

#### 4.扩容

> 扩容时机

- 超过装载因子阈值，源码里定义的阈值是 6.5
- 溢出桶数量过多
