

## jvm

### 1.内存结构

#### 2.虚拟机栈

>-Xss  分配栈的大小

```java
-Xss 1m 
```



  栈太大，能创建的线程就少，降低效率





问题辨析3：

这三个哪些是线程安全的 。m1 不用考虑，m2\m3都要考虑

![image-20211014191948861](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211014191948.png)

#### 4、堆

##### 4.1定义

Heap 堆

- 通过new 关键字，创建对象都会使用堆内存

特点

- 线程共享，需要考虑线程安全的问题
- 有垃圾回收机制

##### 4.2 堆内存溢出

OutOfMemory

> -Xmx

```
-Xmx8M
```

通过这个设置堆的大小，调小一些，能更快发现堆内存溢出的问题



##### 4.3 堆内存诊断

1. jps 工具
查看当前系统中有哪些 java 进程
2. jmap 工具
查看堆内存占用情况 jmap - heap 进程id
3. jconsole 工具
图形界面的，多功能的监测工具，可以连续监测



```
jps 查看java进程

jmap -heap 进程ID  查看堆信息
```



> 案例

垃圾回收后，内存占用仍然很高

jvisualvm  可视化虚拟机



#### 5、方法区

##### 5.1 定义

![image-20211015195008078](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211015195008.png)

方法区是规范，元空间或者永久代都是它的一种实现



##### 5.2 组成

![image-20211015195113270](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211015195113.png)

![image-20211015195119490](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211015195119.png)



##### 5.3 方法区内存溢出

> 1.8版本   -XX:MaxMetaspaceSize=8M  设置元空间大小

![image-20211015195736878](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211015195736.png)



> 1.6的jdk，-XX:MaxPermSize=8m  同样的代码 

![image-20211015195815714](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211015195815.png)



##### 4.运行时常量池

- 常量池，就是一张表，虚拟机指令根据这张常量表找到要执行的类名、方法名、参数类型、字面量等信息
- 运行时常量池，常量池是 *.class 文件中的，当该类被加载，它的常量池信息就会放入运行时常量池，并把里面的符号地址变为真实地址



```java
javap -v HelloWorld.class #反编译
```

![image-20211015201932291](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211015201932.png)

上面是反编译之后的代码，常量池就是constant pool，运行时常量池，就是把上面的内容放进内存里



##### 5,5 StringTable

字符串池

```java
String s1 = "a";
String s2 = "b";
String s3 = "a" + "b";  // 这里有编译器自己优化的，常量池直接创建了ab这个东西，然后放入串池
String s4 = s1 + s2;  // 这相当于创建了StringBuilder，取出s1然后append("a")，取出s2,append("a"),然后toString()返回 toString，是new String("ab")的对象
String s5 = "ab";// 这个等于s5，直接取出StringTable里的"ab"
String s6 = s4.intern();
```

- 常量池中的字符串仅是符号，第一次用到时才变为对象
- 利用串池的机制，来避免重复创建字符串对象
- 字符串变量拼接的原理是 StringBuilder （1.8）
- 字符串常量拼接的原理是编译期优化
- 可以使用 intern 方法，主动将串池中还没有的字符串对象放入串池
  - 1.8 将这个字符串对象尝试放入串池，**如果有则并不会放入**，如果没有则放入串池， 会把串池中的对象返回
  - 1.6 将这个字符串对象尝试放入串池，**如果有则并不会放入**，如果没有会把此对象复制一份，放入串池， 会把串池中的对象返回

![image-20211016123408719](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211016123408.png)

1.8的过程：

如果没有string x ="ab"这一行，那么就是先运行到s，发现串池里面没有a和b，就丢进[a,b]，然后s创建了一个new String("ab")对象，然后运行到s2，就把s的这个"ab"丢进串池了。

【a,b,ab】.s2就是串池里面的ab，s也是。所以 s2==s



如果按图上面所示：执行到x的时候，会把"ab"丢入串池，【ab】，执行到s，就有【a,b,ab】s = new String("ab") ，然后执行intern方法，因为"ab"在串池里了，所以s就不放进去，s2取出串池里面的"ab"，所以 最后的结果是true，false



##### 5.6 StringTable的位置

![image-20211016211317418](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211016211317.png)

##### 5.7 StringTable 垃圾回收

也会发生垃圾回收

##### 5.8 StringTable 性能调优

调整 -XX:StringTableSize=桶个数
考虑将字符串对象是否入池



#### 6. 直接内存

##### 6.1定义

Direct Memory(性能比较高)

- 常见于 NIO 操作时，用于数据缓冲区
- 分配回收成本较高，但读写性能高
- 不受 JVM 内存回收管理 （还是会内存溢出）



> 性能对比

![image-20211023153308579](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023153308.png)





> 为什么直接内存比较快？

java复制文件，需要使用系统调用，然后从磁盘文件读取部分数据到系统缓存区，然后再从系统缓存区，复制到java缓冲区byte[]，然后再复制到另一份文件中。然后反复这样操作。

![image-20211023153457778](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023153457.png)





加入直接内存，java和系统都能直接访问直接内存的数据，**少了一次复制的过程**

![image-20211023153828874](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023153828.png)



> 直接内存溢出

![image-20211023154043218](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023154043.png)







##### 6.2 分配和回收原理

这个不受jvm管理，所以要查看变化可以看系统内存的占用(**任务管理器)**

system.gc() 会回收直接内存

**直接内存 会被回收掉**，但是不是被垃圾回收器回收的，而是unsafe这个底层类操作的。

> 释放原理

- 使用了 Unsafe 对象完成直接内存的分配回收，并且回收需要主动调用 freeMemory 方法
- ByteBuffer 的实现类内部，使用了 Cleaner （虚引用）来监测 ByteBuffer 对象，一旦ByteBuffer 对象被垃圾回收，那么就会由 ReferenceHandler 线程通过 Cleaner 的 clean 方法调用 freeMemory 来释放直接内存

![image-20211023154610878](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023154610.png)





![image-20211023154918039](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023154918.png)

**虚引用**对象cleaner，这里的this是bytebuffer对象(关联起来)，后面的new xxx 相当于丢个了线程进去(里面有unsafe类的释放方法)。，如果它关联的对象被回收，就会cleaner会触发clean方法，clean方法里面会执行这个任务线程的run方法。  (**referanceHandler观测这些虚引用对象**，来完成上面的操作)

```java
public class Cleaner extends PhantomReference<Object> {}

cleaner = Cleaner.create(this, new Deallocator(base, size, cap));

// 任务
private static class Deallocator implements Runnable{
    public void run() {
        if (address == 0) {
            // Paranoia
            return;
        }
        unsafe.freeMemory(address);
        address = 0;
        Bits.unreserveMemory(size, capacity);
    }
}
```





> -XX:+DisableExplicitGC 禁用显示的gc

System.gc() 就是显示的垃圾回收，是FULL GC ，效率很低 

上面这个参数可以让System.gc() 没有用



但是禁用了这个，**直接内存就没法被显示回收了**，只能真正的垃圾回收时，才回收去，会较长时间的占用内存。  **可以手动的用unsafe类释放内存**

 



### 2.垃圾回收

[1.如何判断对象可以回收](#1.如何判断对象可以回收)
[2.垃圾回收算法](2.垃圾回收算法)
[3.分代垃圾回收](3.分代垃圾回收)
[4.垃圾回收器](4.垃圾回收器)
[5.垃圾回收调优](5.垃圾回收调优)



#### 1.如何判断对象可以回收

##### 1.1 引用计数法

每个对象都有个计数器，如果被引用了就+1，少一个引用就减1



会有循环引用的问题

![image-20211023161520942](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023161521.png)





##### 1.2 可达性分析

- Java 虚拟机中的垃圾回收器采用可达性分析来探索所有存活的对象
- 扫描堆中的对象，看是否能够沿着 GC Root对象 为起点的引用链找到该对象，找不到，表示可以回收
- 哪些对象可以作为 GC Root ?



> GC Root的对象

https://www.bilibili.com/video/BV1yE411Z7AP?p=51&spm_id_from=pageDriver 这个视频将GC root的对象的

```bash
jmap - dump:format=b,live,file=1.bin 进程id (可以使用jps命令查询)

#dump 表示存放到文件里
```

![image-20211023162408779](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023162408.png)





> 线程也是gc root

线程都有自己的虚拟机栈，所以栈帧和**局部变量引用的对象(关注点事对象，不是引用)**都是，方法参数引用的对象也是

![image-20211023162550746](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023162550.png)

##### 1.3  四种引用

1. 强引用
- 只有所有 GC Roots 对象都不通过【强引用】引用该对象，该对象才能被垃圾回收
2. 软引用（SoftReference） **(内存不足时，只要没有gc root的强引用了)**
- 仅有软引用引用该对象时，在垃圾回收后，**内存仍不足**时会再次出发垃圾回收，回收软引用对象
- **可以配合**引用队列来释放软引用自身
3. 弱引用（WeakReference）  **（只要没有gc root的强引用了）**
- 仅有弱引用引用该对象时，在垃圾回收时，**无论内存是否充足**，**都会**回收弱引用对象
- **可以配合**引用队列来释放弱引用自身
4. 虚引用（PhantomReference）
- **必须配合引用队列使用**，主要配合 ByteBuffer 使用，被引用对象回收时，会将虚引用入队，由 Reference Handler 线程调用虚引用相关方法释放直接内存
5. 终结器引用（FinalReference）
- 无需手动编码，但其内部配合引用队列使用，在垃圾回收时，**终结器引用入队**（**被引用对象暂时没有被回收**），再由 Finalizer 线程 (**优先级低**)通过终结器引用找到被引用对象并调用它的 finalize方法，**第二次 GC 时才能回收被引用对象**。
- 第一次gc只能让终结期去引用队列，执行finalize方法，而且finalizer线程优先级低，可能要等一段时间才能执行这个finalize方法。第二次gc才回收这个对象



实线的是强引用

![image-20211023163031116](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023163031.png)



> 软引用-例子

![image-20211023164343047](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023164343.png)

![image-20211023164834251](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023164834.png)

list强引用softReference ， softReference 软引用byte[] 数组。当内存不足的时候，这些byte[] 数组有的会被回收。就不回造成内存溢出了



*清理软引用*： 引用队列

```java
ReferenceQueue<byte[]> queue = new ReferenceQueue();
// 关联引用队列 当软引用关联的byte[]数组被回收时，软引用就加入到queue中去
softReference<byte[]> ref = new softReference(new byte[4MB],queue);
```

移除无用的软引用代码如下： queue.poll()就是弹出软引用队列里的软引用，然后删掉它。

![image-20211023205704138](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023205711.png)

> 弱引用实例

![image-20211023205932645](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023205932.png)



#### 2.垃圾回收算法

##### 2.1 标记清除算法

![image-20211023210403304](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023210403.png)



第一步标记，标记GC root 不可达的对象(图中灰色的部分)，第二步清除第一步标记的对象。

这里的清除并不是删除，而是记录起止位置放进一个空闲列表，然后下次分配内存就到空闲列表中看有没有合适的大小。



优缺点：

- 只用标记，速度很快
- 容易产生内存碎片

##### 2.2 标记整理

![image-20211023211001274](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023211001.png)



需要拷贝移动内存对象，就会导致地址改变，那么引用的指向也需要跟着修改

优缺点：

- 没有内存碎片
- 速度慢

##### 2.3 复制算法

![image-20211023211243786](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211023211243.png)

先标记，然后把有记录的直接复制到to区，然后把from的都删掉



- 没有内存碎片
- 占用双倍的内存空间



##### 2.3 分代回收

堆内存分为好几块

![image-20211024095553454](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211024095600.png)



- 对象首先分配在伊甸园区域
- **新生代空间不足时，触发 minor gc**，伊甸园和 from 存活的对象使用 copy 复制到 to 中，存活的 对象年龄加 1并且交换 from to  （指向这两个区域的指针改变，理解应该是这样）
  - 伊甸园不足的时候发生第一次垃圾回收
  - 第二次新生代空间不足的时候，伊甸园和from都会发生垃圾回收
- minor gc 会引发 stop the world，暂停其它用户的线程，等垃圾回收结束，用户线程才恢复运行 
- **当对象寿命超过阈值时，会晋升至老年代，最大寿命是15（对象头里面年龄参数用4bit存放）** 
- 当老年代空间不足，会先尝试触发 minor gc(先看新生代够不够存)，如果之后空间仍不足，那么**触发 full gc**，STW的时 间更长

#### 3.相关JVM参数

| 含义               | 参数                                                         |
| ------------------ | ------------------------------------------------------------ |
| 堆初始大小         | -Xms                                                         |
| 堆最大大小         | -Xmx 或 -XX:MaxHeapSize=size                                 |
| 新生代大小         | -Xmn 或 (-XX:NewSize=size + -XX:MaxNewSize=size )            |
| 幸存区比例（动态） | -XX:InitialSurvivorRatio=ratio 和 -XX:+UseAdaptiveSizePolicy (动态的调整辛存去的比例) |
| 幸存区比例         | XX:SurvivorRatio=ratio  (默认为8，8是Eden的大小 ，  8:1:1)   |
| 晋升阈值           | -XX:MaxTenuringThreshold=threshold  （根据垃圾回收器不同，年龄阈值也不同，有的是15） |
| 晋升详情           | XX:+PrintTenuringDistribution                                |
| GC详情             | -XX:+PrintGCDetails -verbose:gc  （发生垃圾回收，打印他的详情） |
| FullGC 前 MinorGC  | -XX:+ScavengeBeforeFullGC （full gc前先做一次minorGC）       |



##### TestDemo

```java
  // jvm参数： -Xms20M -Xmx20M -XX:+UseSerialGC -XX:+PrintGCDetails -verbose:gc
    public static void main(String[] args) {

    }
}

/**输出
Heap
 def new generation   total 9216K, used 2026K [0x00000000fec00000, 0x00000000ff600000, 0x00000000ff600000)
  eden space 8192K,  24% used [0x00000000fec00000, 0x00000000fedfa988, 0x00000000ff400000)
  from space 1024K,   0% used [0x00000000ff400000, 0x00000000ff400000, 0x00000000ff500000)
  to   space 1024K,   0% used [0x00000000ff500000, 0x00000000ff500000, 0x00000000ff600000)
 tenured generation   total 10240K, used 0K [0x00000000ff600000, 0x0000000100000000, 0x0000000100000000)
   the space 10240K,   0% used [0x00000000ff600000, 0x00000000ff600000, 0x00000000ff600200, 0x0000000100000000)
 Metaspace       used 3184K, capacity 4496K, committed 4864K, reserved 1056768K
  class space    used 344K, capacity 388K, committed 512K, reserved 1048576K
*/
```



```java

static int _5M = 5 * 1024 *1024;
static int _7M = 7 * 1024 *1024;
static int _8M = 8 * 1024 *1024;
// jvm参数： -Xms20M -Xmx20M -Xmn10M -XX:+UseSerialGC -XX:+PrintGCDetails -verbose:gc
public static void main(String[] args) {
    ArrayList<byte[]> list = new ArrayList<>();
    list.add(new byte[_8M]);
}
```

可以来测试各个阶段垃圾回收之后，各区的占用大小，



### 3.垃圾回收器

三类垃圾回收器

1. 串行
- 单线程
- 堆内存较小，适合个人电脑
2. 吞吐量优先
- 多线程
- 堆内存较大，多核 cpu
- 让单位时间内，STW 的时间最短 0.2 0.2 = 0.4，垃圾回收时间占比最低，这样就称吞吐量高
3. 响应时间优先
- 多线程
- 堆内存较大，多核 cpu
- 尽可能让单次 STW 的时间最短 0.1 0.1 0.1 0.1 0.1 = 0.5



#### 3.1 串行

> -XX:+UseSerialGC=Serial(新生代的) + SerialOld(老年代的)

Serial：标记复制

SerialOld ： 标记整理

![image-20211024121949710](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211024121949.png)



#### 3.2 吞吐量优先

**并行**

```java
// 并行的垃圾回收器，(jdk1.8 默认开启) ，下面随便开启一个，就会选择两个算法使用
-XX:+UseParallelGC 或者 -XX:+UseParallelOldGC(标记整理算法) 

-XX:+UseAdaptiveSizePolicy   //自动调整新生代的大小(eden和from的比例)
 
    

-XX:GCTimeRatio=ratio   // 调整吞吐量 1/(1+ratio)  -> 会自动调大堆的内存，来减少垃圾回收的次数，增加吞吐量
-XX:MaxGCPauseMillis=ms  //最大暂停毫秒数，最大是200ms。 和上面的吞吐量是相对的

    
-XX:ParallelGCThreads=n //控制垃圾回收的线程数    
```

ParallelOldGC(标记整理算法)

![image-20211024122414826](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211024122414.png)



#### 3.3 响应时间优先 (CMS  需要好好看别人的博客)

并发失败的话，CMS会退化为SerialOld垃圾回收器(因为内存碎片太多了，并发不起来)，SerialOld清理一次，再变回CMS

标记清除

**并发**   可以不用 stw

```java
-XX:+UseConcMarkSweepGC 或者 -XX:+UseParNewGC ~ SerialOld
-XX:parallelGCThreads=n(默认为4) ~ -XX:ConcGCThreads=threads
-XX:CMSInitiatingOccupancyFraction=percent  // 内存占比，设置到多少比例，开始垃圾回收。 给用户线程预留一些空间
-XX:+CMSScavengeBeforeRemark
```

![image-20211025100444070](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211025100444.png)



最后这个并发清理的时候，因为用户线程还在运行，所以还会产生一些垃圾，就叫浮动垃圾，需要下次垃圾回收才能清理。



#### 3.4 G1

![image-20211025101411555](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211025101411.png)

> 适用场景

- 同时注重吞吐量和低延迟，默认暂停目标200ms
- **超大堆内存**，会将堆划分为多个大小相等的Region
- 整体上 **标记+整理** ，两个区域之间是复制算法

> 相关JVM参数

-XX:+UseG1GC

-XX:G1HeapRegionsize=size

-XX:MaxGCPauseMillis=time



##### 1.G1回收阶段

![image-20211025101937243](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211025101937.png)



> young Collection

![image-20211025102003511](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211025102003.png)

堆内存划分为一个个区域。E代表Eden

Eden满了，就会发生young Collection。会stw 。使用复制算法，进入幸存区

![image-20211025103626890](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211025103626.png)

如果幸存区的一些对象年龄到了，就会去老年代。如果不满的就去另外一个幸存区 （from to）

![image-20211025103705075](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211025103705.png)



> Young Collection + CM

- 初始标记，在新生代GC时，进行GC root的标记 (stw
- 老年代占用达到阈值事，进行并发标记(不会stw)，由下面的jvm参数决定
  - -XX:InitiatingHeapOccupancyPercent=percent  （默认45%）  如下图O的区域大于45%，就并发标记

![image-20211025104034302](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211025104034.png)



> Mixed Collection

**实际上，G1只用了复制算法**

会对E、S、O进行全面的垃圾回收

- 最终标记 会STW     (避免并发标记阶段产生的垃圾)
- 拷贝存活 会STW (复制算法)
- -XX:MaxGCPauseMillis=ms

![image-20211025104418349](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211025104418.png)

MIXed 清理的时候，E和S区域会使用复制算法，将对象放进S (to区)，如果有的对象年龄够了，就去S区域。然后O区域也会回收，有两种情况。

- 第一种如果暂停时间能够达到，那么所有的O区域就使用标记复制算法。 
- 第二种，如果全部使用标记复制算法，stw时间太长，超过了设置的暂停时间，G1会预先知道哪些O区里面的垃圾比较多，然后只对一部分S去进行回收。(如图中，有黄色的O区域并没有发生回收)

##### 2.FUll GC



串行收集才 叫full gc 。 并发下执行垃圾回收，并不是full gc。只有垃圾产生的速度大于回收的速度，退化为串行，才有full gc (日志里面会带full gc的名字)

![image-20211025110842049](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211025110842.png)

##### 3. young Collection 跨代引用  (需要查一下资料)



如果old区的对象，引用了Eden区。  G1中把Old区域划分为很多card。上面这种情况，就被称为脏card。 

新生代里面会有一个 Remembered Set 记录这些脏card。然后 标记的时候直接去遍历这个Set里面的东西

![image-20211025111306225](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211025111306.png)



##### 4.remark （重标记） 搜一下文章

黑白灰  (三色标记- 看博客吧)

![image-20211026092329612](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026092329.png)





##### 5、jdk8做的一些优化

> JDK 8u20 字符串去重

优点：节省大量内存
缺点：略微多占用了 cpu 时间，新生代回收时间略微增加
`-XX:+UseStringDeduplication  默认是开启的`

```java
String s1 = new String("hello"); // char[]{'h','e','l','l','o'}
String s2 = new String("hello"); // char[]{'h','e','l','l','o'}
```



- 将所有新分配的字符串放入一个队列
- 当新生代回收时，G1并发检查是否有字符串重复
- 如果它们值一样，让它们引用同一个 char[]
- 注意，与 String.intern() 不一样
  - String.intern() 关注的是字符串对象
  - 而字符串去重关注的是 char[]
  - 在 JVM 内部，使用了不同的字符串表

上面的s1和s2，垃圾回收之后，都指向同一个char[] ，回收其中的一个



> JDK 8u40 并发标记类卸载

所有对象都经过并发标记后，就能知道哪些类不再被使用，当一个类加载器的所有类都不再使用，则卸载它所加载的所有类

`-XX:+ClassUnloadingWithConcurrentMark` 默认启用



卸载条件： (一般都是自定义类加载器)

- 类的实例都被回收掉
- 类加载器里所有的类都不在使用

> JDK 8u60 回收巨型对象

g1中有巨型区。

- 一个对象大于 region 的一半时，称之为巨型对象
- G1 不会对巨型对象进行拷贝
- 回收时被优先考虑
- G1 会跟踪老年代所有 incoming 引用，这样老年代 incoming 引用为0 的巨型对象就可以在新生代垃圾回收时处理掉  ==》(**如果没有人在老年代引用这个巨型对象，就会在新生代垃圾回收的时候处理掉，这是为了更早的处理巨型对象**)

![image-20211026093303298](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026093303.png)



##### 6、jdk9做的增强

>并发标记起始时间的调整

- 并发标记必须在堆空间占满前完成，否则退化为 FullGC(fullgc的stw时间长)
- JDK 9 之前需要使用 -XX:InitiatingHeapOccupancyPercent(堆占用比例，达到多少就垃圾回收)
- JDK 9 可以动态调整(一开始设置好比例之后，在运行过程中会收集数据，动态调整比例，预留更大的堆空闲空间)
  - -XX:InitiatingHeapOccupancyPercent 用来设置初始值
  - 进行数据采样并动态调整
  - 总会添加一个安全的空档空间



### 4. JVM调优  (跳过了)

```
// 查看虚拟机运行参数
"C:\Program Files\Java\jdk1.8.0_91\bin\java” -XX:+PrintFlagsFinal -version | findstr "GC"
```

预备知识

- 掌握 GC 相关的 VM 参数，会基本的空间调整
- 掌握相关工具
- 明白一点：调优跟应用、环境有关，没有放之四海而皆准的法则



### 5、类加载和字节码技术







#### 1.类文件的结构



> 根据 JVM 规范，类文件结构如下

![image-20211026100538365](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026100538.png)





> 实例展示

![image-20211026101600982](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026101601.png)

![image-20211026101619965](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026101620.png)





##### 1.魔数

> 魔数 magic  - 身份标识

![image-20211026100755311](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026100755.png)



##### 2.版本信息

> minor_version major_version  版本信息

![image-20211026100859062](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026100859.png)



##### 3 常量池

8-9字节表示常量池里面有多少项

![image-20211026101023229](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026101023.png)

0000000 ca fe ba be 00 00 00 34 00 23 **0a 00 06 00** 15 09

第#1项 0a(10，需要查表，如下图，找到value为10的) 表示一个 Method 信息，00 06 和 00 15（21） 表示它引用了常量池中 #6 和 #21 项来获得这个方法的【所属类】和【方法名】

![image-20211026101230472](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026101230.png)





![image-20211026101529426](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026101529.png)

**init表示构造方法**



上面这些第几项的前两位代表 常量类型(去表格里面找)，之后的话根据类型会有不同的构造

例如：

- Method 信息 后面跟两个4字节 代表 所属类和所属方法名。
- utf8串，后面4字节是长度，然后这个长度的字节就是这个串表示的字符串



##### 4 访问标识 access_flag

查表

![image-20211026102912302](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026102912.png)



![image-20211026102950655](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026102950.png)

21 = 20+1 即public + super

##### 5. 类和父类 

==this_class 和super——class==

![image-20211026103026099](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026103026.png)



05 对应的 this_class  06对应的super_class 



##### 6. 接口数量和接口信息

 后两个字节0000 对应的是接口数量

因为为0 ，所以没有接口的信息。不然和常量池找对应项一样。再之后两个字节0000对应成员变量的信息，因为是0，所以后面的fields[fields_count]没有。



##### 7.成员变量数量和信息

> 成员变量信息

成员变量对照表，为了压缩字节，B代表byte。。。等等

![image-20211026103436531](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026103436.png)







##### 8.方法数量和信息



> Method信息

之后两个字节是方法数量，0002 ，两个方法，主方法、构造方法



然后我们开始看一下方法的信息  `<init>` 构造方法的信息

![image-20211026103850284](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026103850.png)

![image-20211026103914775](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026103914.png)

![image-20211026103928368](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026103928.png)



这些都是根据规则，查表找对应的信息，查常量池获取信息。



##### 9 附加属性

![image-20211026104025084](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026104025.png)



00 01 表示附加属性数量
00 13 表示引用了常量池 #19 项，即【SourceFile】
00 00 00 02 表示此属性的长度
00 14 表示引用了常量池 #20 项，即【HelloWorld.java】



#### 2.字节码技术

##### 2.1 javap工具

可以反编译字节码文件

`javap -v HelloWord.class`  -v显示详细信息

![image-20211026112912464](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211026112912.png)

##### 2.2 图解

> java代码

```java
package cn.itcast.jvm.t3.bytecode;
/**
* 演示 字节码指令 和 操作数栈、常量池的关系
*/
public class Demo3_1 {
public static void main(String[] args) {
int a = 10;
int b = Short.MAX_VALUE + 1;
int c = a + b;
System.out.println(c);
}
}
```

> 编译之后的字节码文件

```java
F:\01-代码\01-java\leetcode_pratice\target\test-classes>javap -v test4.class
Classfile /F:/01-代码/01-java/leetcode_pratice/target/test-classes/test4.class
十月 27, 2021 10:54:31 上午 java.util.Currency info
INFO: currency.properties entry for 1111 is ignored because of the invalid country code.
  Last modified 2021-10-27; size 577 bytes
  MD5 checksum c6df5324e97def4d852531df39723cf8
  Compiled from "test4.java"
public class test4
  minor version: 0
  major version: 52
  flags: ACC_PUBLIC, ACC_SUPER
Constant pool:
   #1 = Methodref          #7.#25         // java/lang/Object."<init>":()V
   #2 = Class              #26            // java/lang/Short
   #3 = Integer            32768
   #4 = Fieldref           #27.#28        // java/lang/System.out:Ljava/io/PrintStream;
   #5 = Methodref          #29.#30        // java/io/PrintStream.println:(I)V
   #6 = Class              #31            // test4
   #7 = Class              #32            // java/lang/Object
   #8 = Utf8               <init>
   #9 = Utf8               ()V
  #10 = Utf8               Code
  #11 = Utf8               LineNumberTable
  #12 = Utf8               LocalVariableTable
  #13 = Utf8               this
  #14 = Utf8               Ltest4;
  #15 = Utf8               main
  #16 = Utf8               ([Ljava/lang/String;)V
  #17 = Utf8               args
  #18 = Utf8               [Ljava/lang/String;
  #19 = Utf8               a
  #20 = Utf8               I
  #21 = Utf8               b
  #22 = Utf8               c
  #23 = Utf8               SourceFile
  #24 = Utf8               test4.java
  #25 = NameAndType        #8:#9          // "<init>":()V
  #26 = Utf8               java/lang/Short
  #27 = Class              #33            // java/lang/System
  #28 = NameAndType        #34:#35        // out:Ljava/io/PrintStream;
  #29 = Class              #36            // java/io/PrintStream
  #30 = NameAndType        #37:#38        // println:(I)V
  #31 = Utf8               test4
  #32 = Utf8               java/lang/Object
  #33 = Utf8               java/lang/System
  #34 = Utf8               out
  #35 = Utf8               Ljava/io/PrintStream;
  #36 = Utf8               java/io/PrintStream
  #37 = Utf8               println
  #38 = Utf8               (I)V
{
  public test4();
    descriptor: ()V
    flags: ACC_PUBLIC
    Code:
      stack=1, locals=1, args_size=1
         0: aload_0
         1: invokespecial #1                  // Method java/lang/Object."<init>":()V
         4: return
      LineNumberTable:
        line 8: 0
      LocalVariableTable:
        Start  Length  Slot  Name   Signature
            0       5     0  this   Ltest4;

  public static void main(java.lang.String[]);
    descriptor: ([Ljava/lang/String;)V
    flags: ACC_PUBLIC, ACC_STATIC
    Code:
      stack=2, locals=4, args_size=1
         0: bipush        10
         2: istore_1
         3: ldc           #3                  // int 32768
         5: istore_2
         6: iload_1
         7: iload_2
         8: iadd
         9: istore_3
        10: getstatic     #4                  // Field java/lang/System.out:Ljava/io/PrintStream;
        13: iload_3
        14: invokevirtual #5                  // Method java/io/PrintStream.println:(I)V
        17: return
      LineNumberTable:
        line 10: 0
        line 11: 3
        line 12: 6
        line 13: 10
        line 14: 17
      LocalVariableTable:
        Start  Length  Slot  Name   Signature
            0      18     0  args   [Ljava/lang/String;
            3      15     1     a   I
            6      12     2     b   I
           10       8     3     c   I
}
SourceFile: "test4.java"

```

类加载，就是会把这个字节码文件读入到内存。

> 常量池载入运行时常量池

![image-20211027105548374](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027105548.png)

只选取了部分。



> 方法字节码载入方法区

main的方法

![image-20211027105648800](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027105648.png)

> main线程开始运行，分配栈帧内存

![image-20211027105738424](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027105738.png)

![image-20211027105752190](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027105752.png)

局部变量 4和最大操作数栈的深度2



> 执行引擎执行字节码 (笔记直接复制吧)

就是读取指令，读入到栈中，存放到槽位slot里，然后根据函数对栈里的数据进行操作。 i++里面的iinc 1,1 表示槽位1里的数据直接+1。



。。。



##### 2.3 条件判断指令



![image-20211027110749139](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027110749.png)

几点说明：
byte，short，char 都会按 int 比较，因为操作数栈都是 4 字节
goto 用来进行跳转到指定行号的字节码

![image-20211027110811301](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027110811.png) ![image-20211027110821662](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027110821.png)



##### 2.4 构造方法

> <cinit>()v

![image-20211027111008327](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027111008.png) ![image-20211027111014851](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027111014.png)

编译器会按从上至下的顺序，收集所有 static 静态代码块和静态成员赋值的代码，合并为一个特殊的方法 <cinit>()V



> <init>()v

![image-20211027111228662](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027111228.png) ![](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027111243.png)



编译器会按从上至下的顺序，收集所有 {} 代码块和成员变量赋值的代码，形成新的构造方法，但**原始构造方法内的代码总是在最后**



##### 2.5 方法调用

![image-20211027112225105](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027112225.png)  ![image-20211027112233414](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027112233.png)



- new 是创建【对象】，给对象分配堆内存，执行成功会将【对象引用】压入操作数栈
- dup 是复制操作数栈栈顶的内容，本例即为【对象引用】，为什么需要两份引用呢，**一个是要配合 invokespecial 调用该对象的构造方法 "<init>":()V （会消耗掉栈顶一个引用）**，另一个要配合 astore_1 赋值给局部变量
- 最终方法（final），私有方法（private），构造方法都是由 invokespecial 指令来调用，属于静态绑定，**速度比invokevirtual 快**。一下子就能找到方法
- 普通成员方法是由 invokevirtual 调用，属于动态绑定，**即支持多态**
- 成员方法与静态方法调用的另一个区别是，执行方法前是否需要【对象引用】
- 比较有意思的是 d.test4(); 是通过【对象引用】调用一个静态方法，可以看到在调用invokestatic 之前执行了 pop 指令，把【对象引用】从操作数栈弹掉了😂 。  **test4是静态方法，实际上只需要invokestatic即可，不需要用对象引用，所以加上的话会多两条没有用的指令**
- 还有一个执行 invokespecial 的情况是通过 super 调用父类方法



##### 2.6 多态的原理

vtable是虚方法表，里面有方法的地址。 链接的时候你用的哪个方法就已经确定了。



当执行 invokevirtual 指令时，
1. 先通过栈帧中的对象引用找到对象
2. 分析对象头，找到对象的实际 Class
3. Class 结构中有 vtable，**它在类加载的链接阶段就已经根据方法的重写规则生成好了** 
4. 查表得到方法的具体地址
5. 执行方法的字节码



##### 2.7 try catch







> finally

finally 就是finally里面的代码都复制一份，然后放在try里面和catch里面。 catch捕获不到的异常，finally也复制过去一份

![image-20211027163420394](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211027163420.png)

##### 2.8 synchronized

```java
public static void main(String[] args) {
    Object lock = new Object();
    synchronized (lock) {
    System.out.println("ok");
    }
}
```

![image-20211029153840291](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211029153840.png)



方法级别的 synchronized 不会在字节码指令中有所体现



#### 3.编译器处理

所谓的 语法糖，其实就是指 java 编译器把 *.java 源码编译为 *.class 字节码的过程中，自动生成
和转换的一些代码，主要是为了减轻程序员的负担，算是 java 编译器给我们的一个额外福利（给糖吃嘛）



注意，以下代码的分析，借助了 javap 工具，idea 的反编译功能，idea 插件 jclasslib 等工具。另外，编译器转换的结果直接就是 class 字节码，只是为了便于阅读，给出了 几乎等价 的 java 源码方式，并不是编译器还会转换出中间的 java 源码，切记。

##### 3.1 默认构造器(编译器自动帮我们加上)

```java
public class Candy1 {
}

// 编译之后
public class Candy1 {
    // 这个无参构造是编译器帮助我们加上的
    public Candy1() {
    super(); // 即调用父类 Object 的无参构造方法，即调用 java/lang/Object."
    <init>":()V
    }
}
```



##### 3.2 自动拆装箱

```java
public static void main(String[] args) {
    Integer x = 1;
    int y = x;
}


// 编译之后
public static void main(String[] args) {
    Integer x = Integer.valueOf(1); // 装箱
    int y = x.intValue();  // 拆箱
}
```



##### 3.3 泛型集合取值

```java
public static void main(String[] args) {
    List<Integer> list = new ArrayList<>();
    list.add(10); // 实际调用的是 List.add(Object e)
    Integer x = list.get(0); // 实际调用的是 Object obj = List.get(int index);
}


编译之后实际上是这样的
// 需要将 Object 转为 Integer
Integer x = (Integer)list.get(0);
// 需要将 Object 转为 Integer, 并执行拆箱操作
int x = ((Integer)list.get(0)).intValue();
```





可以看到这里的add 方法的参数实际上是object, 擦除了字节码上的泛型信息，LocalVariableTypeTable 保留了方法参数泛型的信息，后面使用checkcast进行检查

![image-20211029154552799](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211029154552.png)



>LocalVariableTypeTable 局部变量类型表

![image-20211029154856076](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211029154856.png)



> 使用反射获取这些信息

```java
Method test = Candy3.class.getMethod("test", List.class, Map.class);
Type[] types = test.getGenericParameterTypes();
for (Type type : types) {
    if (type instanceof ParameterizedType) {
        ParameterizedType parameterizedType = (ParameterizedType) type;
        System.out.println("原始类型 - " + parameterizedType.getRawType());
        Type[] arguments = parameterizedType.getActualTypeArguments();
        for (int i = 0; i < arguments.length; i++) {
        	System.out.printf("泛型参数[%d] - %s\n", i, arguments[i]);
        }
    }
}
```

![image-20211029155229071](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211029155229.png)



##### 3.4 可变参数

jdk5加入的新特性

可变参数 String... args 其实是一个 String[] args ，从代码中的赋值语句中就可以看出来。
同样 java 编译器会在编译期间将上述代码变换

```java
public class Candy4 {
    // String... args  会被编译成String[] args
	public static void foo(String... args) {
        String[] array = args; // 直接赋值
        System.out.println(array);
    }
    public static void main(String[] args) {
    	foo("hello", "world");
    }
}
```



##### 3.5 foreach循环

```java
public static void main(String[] args) {
    int[] array = {1, 2, 3, 4, 5}; // 数组赋初值的简化写法也是语法糖哦
    for (int e : array) {
    	System.out.println(e);
    }
}

// 编译之后，相当于下面的
int[] array = new int[]{1, 2, 3, 4, 5};

for(int i = 0; i < array.length; ++i) {
    int e = array[i];
    System.out.println(e);
}



```

```java
#集合的情况
    
List<Integer> list = Arrays.asList(1,2,3,4,5);
for (Integer i : list) {
	System.out.println(i);
}

Iterator iter = list.iterator();
while(iter.hasNext()) {
    Integer e = (Integer)iter.next();
    System.out.println(e);
}
```

注意
foreach 循环写法，能够配合数组，以及所有实现了 Iterable 接口的集合类一起使用，其中
Iterable 用来获取集合的迭代器（ Iterator ）



##### 3.6 Switch 



从 JDK 7 开始，switch 可以作用于字符串和枚举类，这个功能其实也是语法糖，例如：

>switch 配合 String 和枚举使用时，变量不能为null，原因分析完语法糖转换后的代码应当自然清楚



###### 字符串

![image-20211029160221053](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211029160221.png) ![image-20211029160228703](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211029160228.png)

可以看到，执行了两遍 switch，第一遍是根据字符串的 hashCode 和 equals 将字符串的转换为相应byte 类型，第二遍才是利用 byte 执行进行比较。



> 为什么第一遍时必须既比较 hashCode，又利用 equals 比较呢？

hashCode 是为了提高效率，减少可能的比较；而 equals 是为了防止 hashCode 冲突，例如 BM 和 C. 这两个字符串的hashCode值都是2123 

###### 枚举类

会把枚举类编程数组，然后给枚举类里面的元素赋值，后面再比较整数值

![image-20211029161252341](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211029161252.png)





> 枚举类的字节码生成

![image-20211029161406005](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211029161406.png)



##### 3.7 try-with - resources

```java
try(资源变量 = 创建资源对象){
} catch( ) {
}
```

其中资源对象需要实现 AutoCloseable 接口，例如 InputStream 、OutputStream 、
Connection 、Statement 、ResultSet 等接口都实现了 AutoCloseable ，使用 try-withresources
可以不用写 finally 语句块，编译器会帮助生成关闭资源代码，例如



> 编译后，会自动增加finally ，里面有关闭的代码

![image-20211029162250277](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211029162250.png)



为什么要设计一个 addSuppressed(Throwable e) （添加被压制异常）的方法呢？是为了防止异常信息的丢失（想想 try-with-resources 生成的 fianlly 中如果抛出了异常）



往e里面添加了close的异常，因为finally的代码会往try和catch里面copy一份，那么就不会遗漏这个异常的信息

##### 3.10 (语法糖重写桥接 **这节和下一节- 未看视频**)

3.11



#### 4、类加载阶段

