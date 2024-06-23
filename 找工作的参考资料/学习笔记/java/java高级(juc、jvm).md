## 多线程

进程   程序  线程



进程是程序的一次执行过程，一个进程里面包含至少一个线程（多个线程就是一个东西同时做好多个事情）

#### 一、线程的三种创建方式

##### 1.继承Thread 

1. 继承Thread类
2. 重写run方法
3. 创建线程对象使用.start方法执行

```java
public class TestThead  extends Thread{

    @Override
    public void run() {
        for (int i = 200; i > 0; i--) {
            System.out.println("我在看代码"+i);
        }
    }

    //main是主线程
    public static void main(String[] args) {
        TestThead testThead = new TestThead();

        testThead.start();
        for (int i = 0; i < 2000; i++) {
            System.out.println("我在学习多线程"+i);
        }
    }
}
```

```
线程开启不一定立即执行，由CPU调度，
线程是交替执行的
要调用start()方法，而不是run()
```



##### 2. 实现Runnable接口

1. 实现Runnable接口
2. 重现run方法
3. 创建线程对象
4. 创建thread对象作代理，将线程对象放入其中，调用start方法执行



```java
public class TestThread3 implements Runnable{
    @Override
    public void run() {
        for (int i = 2000; i > 0; i--) {
            System.out.println("我在看代码"+i);
        }
    }

    public static void main(String[] args) {
        TestThread3 testThread3 = new TestThread3();
//        Thread thread = new Thread(testThread3);
//        thread.run();
        new Thread(testThread3).start();
        for (int i = 0; i < 2000; i++) {
            System.out.println("我在学习多线程"+i);
        }
    }
}
```

推荐使用这种,避免单继承局限性，灵活方法，方便同一个对象被多个线程使用。

##### 3、实现Callable接口

```java
public class TestCallable implements Callable<Boolean> {

    public Boolean call() throws Exception {
        System.out.println("test");
        return true;
    }

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        TestCallable testCallable = new TestCallable();
        ExecutorService ser = Executors.newFixedThreadPool(3);
        Future<Boolean>  r1 = ser.submit(testCallable);
        Boolean rs1 = r1.get();
        ser.shutdown();
    }
}
```

#### 静态代理

- 真实对象和代理对象都要实现同一个接口
- 代理对象要代理真实对象
- 好处
  - 代理对象可以做很多真实对象做不了的事情
  - 真实对象专注做自己的事情

```java
public class StaticProxy {
    public static void main(String[] args) {
        new MarryCompany(new You()).marry();
    }
}

interface Marry{
    void marry();
}
class You implements Marry{

    @Override
    public void marry() {
        System.out.println("xy结婚啦，开心");
    }
}
class MarryCompany implements Marry{

    private Marry target;

    public MarryCompany(Marry target) {
        this.target = target;
    }

    @Override
    public void marry() {
        before();
        this.target.marry();
    }

    public void before(){
        System.out.println("布置场地");
    }
}
```



#### 二、lambda表达式

函数式编程的思想

1. 函数式接口  （接口里只有一个方法）
2. 接口声明的变量
3. 使用lambda表达式简化

lambda表达式 从类中简化而来的过程

```java
//1.一个函数式接口
interface Test{
    void test();
}

//2.外部实现类
class demo01 implements Test{

    @Override
    public void test() {
        System.out.println("外部实现类");
    }
}
//        3.静态内部类
static class demo02 implements Test{

    @Override
    public void test() {
        System.out.println("静态内部类");
    }
}

//4.局部内部类
class demo04 implements Test{

    @Override
    public void test() {
        System.out.println("局部内部类");
    }
}

//5.匿名内部类
test = new Test() {
    @Override
    public void test() {
        System.out.println("匿名内部类");
    }
};

//6.lambda
 test = ()->System.out.println("lambda");

```

```java
//lambda自身的简化
interface TestLambda{
    void test(int a);  //也可以定义多个参数，这样之后的简化就不能去掉括号了
}
TestLambda testLambda;
//        简化过程
testLambda = (int a)->{
    System.out.println("测试"+a);
};
testLambda = (a)->{
    System.out.println("测试"+a);
};

testLambda = a->{
    System.out.println("测试"+a);
};

testLambda = a-> System.out.println("测试"+a);
```

#### 三、线程

> 线程状态

五大状态：

- 新生状态
- 就绪状态
- 阻塞状态
- 运行状态
- 死亡状态

![image-20210313143137409](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210313143144.png)

> 线程方法

```java
SetPriority(int xxx)  //更改线程的优先级
sleep(long xx)  //休眠，毫秒
join()     //等待线程终止
yield()		//暂停当前执行的线程对象，并执行其他线程
interrupt()  //中断线程，别用这个
isAlive()	//测试线程是否处于活动状态
```

> 线程停止

```java
// 1. 线程正常停止，利用次数，不建议死循环
// 2. 建议使用标志位，
// 3. 不要使用stop或destroy等jdk废除的方法
public class TestStop implements Runnable{
    private boolean flag = true;
    public void run() {
        int i = 0;
        while (flag)
        {
            System.out.println("run thread"+i++);
        }
    }


    public void stop(){
        this.flag  = false;
    }

    public static void main(String[] args) {
        TestStop testStop = new TestStop();
        new Thread(testStop).start();
        for (int i = 0; i < 7000; i++) {
            System.out.println("main"+i);
            if(i == 900){
                testStop.stop();
                System.out.println("线程结束");
            }
        }
    }
}

```

> 线程休眠

```java
//sleep（time）毫秒数
// sleep存在InterruptedException
// sleep模拟网络延时，倒计时
//每一个对象都有一个锁，sleep不会放过
```

>线程礼让

yield() 方法，A从调度中出来，然后线程重新竞争，所以有可能礼让不成功

> 线程强制执行

join（）方法，可以直接阻塞其他线程

> 线程的五个状态

![image-20210313143200643](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210313143200.png)

> 线程优先级

```
thread.getPriority()
thread.setPriority()
```

> 守护线程

![image-20210313143209708](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210313143209.png)

```java
//虚拟机不用等待守护线程，所以守护线程还在运行，用户线程执行完了之后，就程序结束

//设置成守护线程
new Thread().setDaemon(true);
```

#### 四、同步

线程不安全，多个线程调用同一个对象，就会不安全

synchronizd方法，相当于一个锁

> 不安全的案例

```java
ublic class UnSafeBuyTicket {
    public static void main(String[] args) {
        BuyTicket station = new BuyTicket();

        new Thread(station,"我").start();
        new Thread(station,"你们").start();
        new Thread(station,"黄牛").start();
    }
}

class BuyTicket implements Runnable{

    private int ticketNums = 10;
    boolean flag = true;
    @Override
    public void run() {
        while (flag){
            try {
                buy();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    private void buy() throws InterruptedException {
        if(ticketNums<=0){
            flag = false;
            return;
        }
        Thread.sleep(100);
        System.out.println(Thread.currentThread().getName()+"拿到"+ticketNums--+"票");
    }
}

```

```java
public class UnSafeList {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        for (int i = 0; i < 10000; i++) {
            new Thread(()->{
                list.add(Thread.currentThread().getName());
            }).start();
        }
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(list.size());
    }
}
```

> 同步方法

`synchronized`  方法控制对“对象”的访问，每个对象对应一把锁，每个`synchronized`方法必须获得调用该方法的对象的锁才能执行，否则线程会阻塞。方法一旦执行，就独占该锁，直到方法返回才释放锁，后面被阻塞的线程才能获得这个锁，继续执行。

缺点：方法设置为synchronized会浪费大量的资源。

只需要锁方法里需要上锁的部分即可。

```java
 //这里锁的是this，调用这个方法的对象
    private synchronized void buy() throws InterruptedException {
        if(ticketNums<=0){
            flag = false;
            return;
        }
        Thread.sleep(100);
        System.out.println(Thread.currentThread().getName()+"拿到"+ticketNums--+"票");
    }
```

这里锁的是this，也就是当前的对象。

**如果要锁其他对象了?**  就需要锁一个块

```java
List<String> list = new ArrayList<>();
//这里需要锁要变化的对象，就是增删改查的那个对象
synchronized (list){
            for (int i = 0; i < 10000; i++) {
                new Thread(()->{
                    list.add(Thread.currentThread().getName());
                }).start();
            }
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
```

> 死锁

产生死锁的必要条件：

![image-20210318211129167](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210318211129.png)

==只要避免其中的一种情况，就不会出现死锁==

> Lock锁

显示定义同步锁

`ReentrantLock`(可重入锁)实现了Lock，拥有与synchronized相同的并发性和内存语义。

```java
import java.util.concurrent.locks.ReentrantLock;

public class TestLock {
    public static void main(String[] args) {
        BuyTick testLock = new BuyTick();

        new Thread(testLock,"A").start();
        new Thread(testLock,"B").start();
        new Thread(testLock,"C").start();
    }
}

class BuyTick implements Runnable{

    int tickNum = 10;

    //定义可重入锁
   private final ReentrantLock lock = new ReentrantLock();


    @Override
    public void run() {
        while(true){
            try {
                lock.lock();
                if (tickNum>0){
                    try {
                        Thread.sleep(100);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println(Thread.currentThread().getName()+tickNum--);
                }else
                    break;
            } finally {
                //解锁
               lock.unlock();
            }

        }
    }
}
```

> 线程协作

生产者消费者模式 （线程通信）

![image-20210318213002098](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210318213002.png)

- 解决线程通信问题：
  - ![image-20210318213039961](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210318213040.png)

---

管程法：弄一个缓冲区

信号灯法：需要一个标志位

信号的法代码：

```java
//测试生产者消费者问题，信号灯法：标志位解决
public class TestPC2 {
    public static void main(String[] args) {
        TV tv = new TV();
        new Player(tv).start();
        new Watcher(tv).start();
    }
}

//生产者--》演员
class Player extends Thread{
    TV tv;

    public Player(TV tv) {
        this.tv = tv;
    }

    @Override


    public void run() {
        for (int i = 0; i < 20; i++) {
            if(i%2==0){
                this.tv.paly("快乐大本营");
            }else {
                this.tv.paly("抖音");
            }
        }
    }
}

//消费者--》观众
class Watcher extends Thread{
    TV tv;

    public Watcher(TV tv) {
        this.tv = tv;
    }

    @Override
    public void run() {
        for (int i = 0; i < 20; i++) {
            this.tv.watch();
        }
    }
}

class TV{
    //演员表演，观众等待
    //观众观看，演员等待

    String voice;
    boolean flag = true;



    //表演
    public synchronized void paly(String voice){
        if (!flag)
        {
            try {
                this.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("演员表演 了"+voice);
//通知观众观看
        this.notifyAll();
        this.voice = voice;
        this.flag = !this.flag;

    }


    //观看

    public synchronized void watch(){
        if(flag){
            try {
                this.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("观看了"+voice);

        //通知演员表演
        this.notifyAll();
        this.flag = !this.flag;
    }
}
```

> 线程池

**背景**：经常创建和销毁使用量特别大的资源，比如并发情况下的线程，对性能的影响很大。

**思路**：提前创建好多个线程，放入线程池中，使用时直接获取，使用完放回池中。可以避免频繁创建销毁、实现重复利用。

**好处**：

- 提高响应速度
- 降低资源消耗
- 便于管理

![image-20210321212022227](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210321212022.png)

## JUC

#### 1、什么是JUC

java.util包下的几个并发库

![image-20210705104937386](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210705104937.png)

业务：普通的线程代码 Thread

Runnable创建线程的方式，没有返回值，效率比Callable低

#### 2、线程和进程

> 线程、进程

进程：一个程序，一个进程可以包含多个线程。

java默认有几个线程？ 2个 ，一个是main，一个是GC

> 并发、并行

并发：时间间隔内交替执行。

- CPU一核，模拟出多条线程

并行：同时进行

- CPU多核。线程池

并发编程的本质：**充分利用CPU的资源**

> 线程有几个状态

```java
 public enum State {
       
     // 新生
        NEW,
	// 运行
        RUNNABLE,

	//阻塞      
        BLOCKED,

    // 等待   
        WAITING,

     //超时等待，就是等一段约定的时间，过了就不等了。
        TIMED_WAITING,

       //终止
        TERMINATED;
    }
```

> wait/sleep的区别

- **来自不同的类**
  - wait ->Object
  - sleep ->Thread

- **关于锁的释放**
  - wait会释放锁
  - sleep是睡觉抱着锁，不会释放。

- **使用的范围不同**
  - wait必须在同步代码块
  - sleep可以在任何地方

#### 3、Lock锁(重点)

> 传统的synchronized

```java
//传统的线程创建
public class SaleTicketDemo1 {
    public static void main(String[] args) {
        new Thread(new MyThread()).start();
    }
}
class MyThread implements Runnable{
    @Override
    public void run() {
    }
}

/**
 * 真正的多线程开发，公司中的
 * 线程就是一个单独的资源类，没有任何附属的操作
 * 属性、方法
 */
public class SaleTicketDemo1 {
    public static void main(String[] args) {
        // 并发,多线程操作同一个资源类，把资源类丢入线程
        Ticket ticket = new Ticket();
        new Thread( ()->{ ticket.sale();} ).start();
    }
}

// 资源类OOP，不要让它继承类，变成一个不纯粹的
class Ticket{
    private  int num = 50;
    //执行的方法
    public  void sale(){
    }
}
```

==synchronized 本质就是排队==

```java
public class SaleTicketDemo1 {
    public static void main(String[] args) {
        Ticket ticket = new Ticket();
         new Thread(()->{ for (int i = 0; i < 60; i++)  ticket.sale(); },"A").start();
         new Thread(()->{ for (int i = 0; i < 60; i++)  ticket.sale(); },"B").start();
         new Thread(()->{ for (int i = 0; i < 60; i++)  ticket.sale(); },"C").start();
}

// 资源类OOP，不要让它继承类，变成一个不纯粹的
class Ticket{
    private  int num = 50;
    // synchronized 本质就是排队
    public synchronized void sale(){
        if(num>0){
            System.out.println(Thread.currentThread().getName()+"卖出了第"+num--+"张票,剩余的票数为"+num);
        }
    }
}
```

> Lock接口

![image-20210406110553184](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210406110600.png)



ReentratLock源码，可以设置是否选用公平锁

![image-20210406110902314](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210406110902.png)

公平锁：十分公平，先来后到

**非公平锁：十分不公平，可以插队,就是线程自己随机抢占资源   (java里默认的)**

非公平锁是公平的：  比如排队3s和排队3h的人，用公平锁，3h在前面的话，3s的人就要一直等待

```java
package com.xy.demo1;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * 真正的多线程开发，公司中的
 * 线程就是一个单独的资源类，没有任何附属的操作
 * 属性、方法
 */
public class SaleTicketDemo2 {
    public static void main(String[] args) {
        // 并发,多线程操作同一个资源类，把资源类丢入线程
        Ticket2 ticket = new Ticket2();
        new Thread(()->{ for (int i = 0; i < 60; i++)  ticket.sale(); },"A").start();
        new Thread(()->{ for (int i = 0; i < 60; i++)  ticket.sale(); },"B").start();
        new Thread(()->{ for (int i = 0; i < 60; i++)  ticket.sale(); },"C").start();
    }
}
// lock三部曲
class Ticket2{
    private  int num = 50;
    Lock lock = new ReentrantLock();
    public void sale(){
        // 加锁
        lock.lock();
        try {
            //业务代码
            if(num>0){
                System.out.println(Thread.currentThread().getName()+"卖出了第"+num--+"张票,剩余的票数为"+num);
            }
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            //解锁
            lock.unlock();
        }
    }
}
```

> Synchronized和Lock的区别

- Synchronized 是内置的java关键字，Lock是一个java类

- Synchronized无法判断获取锁的状态，Lock可以判断是否获取到了锁

- Synchronized会自动释放锁，lock必须要手动释放锁，如果不释放锁，就会导致死锁

- Synchronized 线程1如果(拿到锁，但是阻塞了)，线程2就要一直等待。Lock锁就不一定会等待下去

  - ```java
    lock.tryLock() //尝试获得锁
    ```

- Synchronized 可重入锁，不可以中断，非公平。Lock，可重入锁，可以判断锁，可以自己设置是公平锁还是非公平锁

- Synchronized 适合锁少量的代码块，Lock适合锁大量的同步代码

> 锁是什么，如何判断锁的是谁



#### 4、生产者和消费者

> 老版的synchronized, wait notify

```java
/**
 * 线程间通信问题，线程交替执行
 * A，B操作同一个变量
 */
public class A {
    public static void main(String[] args)  {
        Data data = new Data();
        new Thread(
                ()->{
                    for (int i = 0; i < 10; i++) {
                        try {
                            data.increment();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }

                }
        ,"A").start();
        
        new Thread(
                ()->{
                    for (int i = 0; i < 10; i++) {
                        try {
                            data.decrement();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
                ,"B").start();

        new Thread(
                ()->{
                    for (int i = 0; i < 10; i++) {
                        try {
                            data.increment();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
                ,"C").start();

        new Thread(
                ()->{
                    for (int i = 0; i < 10; i++) {
                        try {
                            data.decrement();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
                ,"D").start();
    }
}

// 等待 业务  通知
class Data{
    private int number = 0;

    public synchronized void increment() throws InterruptedException {
        if (number!=0){
            // 等待操作
            this.wait();
        }
        number++;
        System.out.println(Thread.currentThread().getName()+"==》" +number);
        this.notifyAll();
        // 通知其他线程，我+1完毕了
    }

    public synchronized void decrement() throws InterruptedException {
        if (number==0){
            // 等待操作
            this.wait();
        }
        number--;
        System.out.println(Thread.currentThread().getName()+"==》" +number);
        // 通知其他线程，我-1完毕了
        this.notifyAll();
    }
}

```

会有问题。。。。使用if。虚假唤醒  == 因为是if，就wait一次，之后不管有没有锁，就进入方法执行了

![image-20210406160610176](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210406160610.png)

> 如果A、B、C、D四个了

```java
package com.xy.product_Consumer;

/**
 * 线程间通信问题，线程交替执行
 * A，B操作同一个变量
 */

public class A {
    public static void main(String[] args)  {
        Data data = new Data();
        new Thread(
                ()->{
                    for (int i = 0; i < 10; i++) {
                        try {
                            data.increment();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }

                }
        ,"A").start();

        new Thread(
                ()->{
                    for (int i = 0; i < 10; i++) {
                        try {
                            data.decrement();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
                ,"B").start();

        new Thread(
                ()->{
                    for (int i = 0; i < 10; i++) {
                        try {
                            data.increment();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
                ,"C").start();

        new Thread(
                ()->{
                    for (int i = 0; i < 10; i++) {
                        try {
                            data.decrement();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
                ,"D").start();
    }
}
// 等待 业务  通知
class Data{
    private int number = 0;

    public synchronized void increment() throws InterruptedException {
        while (number!=0){
            // 等待操作
            this.wait();
        }
        number++;
        System.out.println(Thread.currentThread().getName()+"==》" +number);
        this.notifyAll();
        // 通知其他线程，我+1完毕了
    }

    public synchronized void decrement() throws InterruptedException {
        while (number==0){
            // 等待操作
            this.wait();
        }
        number--;
        System.out.println(Thread.currentThread().getName()+"==》" +number);
        // 通知其他线程，我-1完毕了
        this.notifyAll();
    }
}

```

> JUC版的生产者和消费者问题

![image-20210406161218969](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210406161219.png)

![image-20210406161237255](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210406161237.png)

```java
package com.xy.product_Consumer;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * 线程间通信问题，线程交替执行
 * A，B操作同一个变量
 */

public class B {
    public static void main(String[] args)  {
    // 同上ABCD
        ...
    }
}

// 等待 业务  通知
class Data2{
    private int number = 0;
    Lock lock = new ReentrantLock();
    Condition condition = lock.newCondition();

    public  void increment() throws InterruptedException {
        lock.lock();
        try {
            while (number!=0){
                // 等待操作
                condition.await();
            }
            number++;
            System.out.println(Thread.currentThread().getName()+"==》" +number);

            condition.signalAll();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }

    public  void decrement() throws InterruptedException {
        lock.lock();
        try {
            while (number==0){
                // 等待操作
                condition.await();
            }
            number--;
            System.out.println(Thread.currentThread().getName()+"==》" +number);
            // 通知其他线程，我-1完毕了
           condition.signalAll();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }
}

```

> condition

上面的代码虽然解决了通信的一个问题，但是不能按照ABCD的顺序执行。

```java
package com.xy.product_Consumer;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class C {
    public static void main(String[] args) {
        PP data = new PP();
        new Thread(()->{for (int i = 0; i < 10; i++)data.printA();},"A").start();
        new Thread(()->{for (int i = 0; i < 10; i++)data.printB();},"B").start();
        new Thread(()->{for (int i = 0; i < 10; i++)data.printC();},"C").start();
    }
}

class PP{
    Lock lock = new ReentrantLock();
    // 多个condition来精准通知
    Condition conditionA = lock.newCondition();
    Condition conditionB = lock.newCondition();
    Condition conditionC = lock.newCondition();

    private int num = 1; // 1A 2B 3C
    public void printA(){
        lock.lock();
        try {
            while (num!=1){
                conditionA.await();
            }
            System.out.println(Thread.currentThread().getName()+"打印了");
            num = 2;
            conditionB.signal();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }

    public void printB(){
        lock.lock();
        try {
            while (num!=2){
                conditionB.await();
            }
            System.out.println(Thread.currentThread().getName()+"打印了");
            num = 3;
            conditionC.signal();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }

    public void printC(){
        lock.lock();
        try {
            while (num!=3){
                conditionC.await();
            }
            System.out.println(Thread.currentThread().getName()+"打印了");
            num = 1;
            conditionA.signal();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }
}
```

#### 5、8锁现象

```java

/**
 * 8锁就是8个问题
 * 1.标准情况下，两个线程谁先打印出来？   发短信，先调用的获得锁了
 * 2.send 加延迟，两个线程谁先打印出来？  还是发短信，因为synchronized 锁的对象是方法的调用者，
 *         调用的方法两个用的是同一个对象，谁先拿到锁就先执行
 */
public class Test1 {
    public static void main(String[] args) throws InterruptedException {
        Phone phone = new Phone();
        new Thread(()->{phone.send();},"A").start();

        TimeUnit.SECONDS.sleep(1);
        new Thread(()->{phone.call();},"B").start();
    }

}

class Phone{
    // synchronized 锁的对象是方法的调用者
    // 两个方法用的是同一个锁
    public synchronized void send(){
        try {
            TimeUnit.SECONDS.sleep(3);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("发短信");
    }

    public synchronized void call(){
        System.out.println("打电话");
    }
}

```

```java


/**
 * 3.增加了一个普通方法后先发短信还是hello？  hello ，因为hello方法没有锁
 * 4.两个对象，两个同步方法，发短信还是打电话？  打电话，因为两个对象有两把锁，发短信被sleep了
 */

public class Test2 {
    public static void main(String[] args) throws InterruptedException {
        Phone2 phone = new Phone2();
        Phone2 phone2 = new Phone2();
        new Thread(()->{phone.send();},"A").start();

        TimeUnit.SECONDS.sleep(1);
        new Thread(()->{phone2.call();},"B").start();
    }
}

class Phone2 extends Phone{
    // 这里没有锁
    public void hello(){
        System.out.println("hello");
    }
}
```

```java


/**
 * 5.增加了两个静态的同步方法，只有一个对象，发短信还是打电话？  发短信
 * 6.如果是两个对象了?    答案是发短信
 */
public class Test3 {
    public static void main(String[] args) throws InterruptedException {
        Phone3 phone = new Phone3();
        new Thread(()->{phone.send();},"A").start();

        TimeUnit.SECONDS.sleep(1);
        new Thread(()->{phone.call();},"B").start();
    }
}

// phone3只有唯一的一个class对象
class Phone3{

    // static 静态方法
    // 类一加载就有了   class模板
    // 锁的是class
    public static synchronized void send(){
        try {
            TimeUnit.SECONDS.sleep(3);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("发短信");
    }

    public static synchronized void call(){
        System.out.println("打电话");
    }
}

```

```java

/**
 * 7. 一个是静态同步方法，一个是普通同步方法，先打电话还是先发短信？ 打电话
 */
public class Test4 {
    public static void main(String[] args) throws InterruptedException {
        Phone4 phone = new Phone4();
        new Thread(()->{phone.send();},"A").start();

        TimeUnit.SECONDS.sleep(1);
        new Thread(()->{phone.call();},"B").start();
    }
}

//两个方法锁的东西不是同一个，所以不需要等待
class Phone4{
    //这里锁的是class模板
    public static synchronized void send(){
        try {
            TimeUnit.SECONDS.sleep(3);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("发短信");
    }

    // 普通同步方法
    // 这里锁的是调用对象
    public  synchronized void call(){
        System.out.println("打电话");
    }
}
```

> 小结

普通同步方法锁的是 **类的实例**

static锁的是  **class**

两个是不一样的

#### 6、集合类不安全

> List不安全

```java
package com.xy.unsafe;

import java.util.*;
import java.util.concurrent.CopyOnWriteArrayList;


// java.util.ConcurrentModificationException 并发修改异常
public class ListTest {


    public static void main(String[] args) {
//    并发下ArrayList 不安全

        /**
         * 解决方案：
         * 1.  List<String> list = new Vector<>();
         * 2. List<String> list = Collections.synchronizedList(new ArrayList<>());
         * 3. List<String> list = new CopyOnWriteArrayList<>();
         */
        //  CopyOnWrite写入时复制    COW  计算机程序设计领域的一种优化策略
        // 多个线程调用的时候，list  读写的时候，固定的。  写入(覆盖)
        // 写入的时候，避免覆盖造成数据问题，先复制一份，再插入
       
        List<String> list = new CopyOnWriteArrayList<>();
        for (int i = 0; i < 10; i++) {
            new Thread(
                    ()->{
                        list.add(UUID.randomUUID().toString().substring(0,5));
                        System.out.println(list);
                    },String.valueOf(i)).start();
        }

    }
}
```

CopyOnWriteArrayList 比 Vector 好在哪里

- CopyOnWriteArrayList 使用的lock锁，Vector都是synchronized。效率比较低

> Set 不安全

```java
package com.xy.unsafe;

import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.UUID;
import java.util.concurrent.CopyOnWriteArraySet;

// java.util.ConcurrentModificationException
public class SetTest {
    public static void main(String[] args) {
        /**
         * 解决方法:
         * 1. Set<String> set = Collections.synchronizedSet(new HashSet<>());
         * 2. Set<String> set =new CopyOnWriteArraySet<>();
         */
        Set<String> set =new CopyOnWriteArraySet<>();

        for (int i = 0; i < 30; i++) {
            new Thread(
                    ()->{
                        set.add(UUID.randomUUID().toString().substring(0,5));
                        System.out.println(set);
                    },String.valueOf(i)).start();
        }
    }
}
```

Hashset底层是什么

```java
public HashSet() {
        map = new HashMap<>();
}

//add  本质就是map的key无法重复  PRESENT是一个不变的常量
public boolean add(E e) {
    return map.put(e, PRESENT)==null;
}

private static final Object PRESENT = new Object();
```

本质：利用map的key是不重复的(来存储数据)，value使用同一个值

> Map 不安全

和上面的一样

解决办法：

```java
Map<String, String> map = new ConcurrentHashMap();
```

看官方文档里面有讲解，concurrentHashMap的原理

#### 7、Callable

1、可以有返回值

2、可以抛出异常

3、方法不同，call()



```java
package com.xy.callable;

import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;

public class TestCallable {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        Mythread thread = new Mythread();
        // 适配类
        FutureTask futureTask = new FutureTask(thread);

        // thread 的参数只有Runnable，这时候需要让callable和Runnable搭上关系
        // 于是用到了Runnable的实现类futureTask，他可以传入callable进去(看源码就知道了)
        new Thread(futureTask,"A").start(); // 线程启动的方式只有1个
        new Thread(futureTask,"A").start();  // 如果运行两次会产生几个call()？  只有1个，有缓存

        String o =(String) futureTask.get(); // get方法可能会产生阻塞，把他放到最后
        System.out.println(o);
    }
}
class Mythread implements Callable<String>{

    @Override
    public String call() throws Exception {
        System.out.println("call()");
        return "123";
    }
}
```



#### 8、常用辅助类(必会)

> CountDownLatch  减法计数器 -- 倒计时

```java
package com.xy.add;

/**
    6个小孩在房间里，等人走完了才能锁上门
*/
import java.util.concurrent.CountDownLatch;

public class TestCountDownLatch {
    public static void main(String[] args) throws InterruptedException {
        CountDownLatch countDownLatch = new CountDownLatch(6); // 设置数量为6

        for (int i = 0; i < 6; i++) {
            new Thread(()->{
                System.out.println(Thread.currentThread().getName()+"go out");
                
                countDownLatch.countDown(); // 数量减1
            
            },String.valueOf(i)).start();
        }
        countDownLatch.await();  // 等待计数器归零，然后再向下执行
        System.out.println("door closed");
    }
}
```

> CyclicBarrier

加法计数器

```java
package com.xy.add;
import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;

public class TestCyclicBarrier {

    public static void main(String[] args) {
        /**
         * 集齐7颗龙珠召唤神龙
         */
        
        // 召唤神龙的线程
        CyclicBarrier cyclicBarrier = new CyclicBarrier(7,()->{
            System.out.println("召唤神龙成功");   // 当数量达到7的时候就启动该线程
        });
        
        for (int i = 1; i < 8; i++) {
            final int  temp = i;
            new Thread(()->{
                System.out.println(Thread.currentThread().getName()+"获得了"+temp+"个龙珠");
                try {
                    
                    cyclicBarrier.await();  //  其实就是等待，然后数量就加1
                
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }).start();
        }
    }
}
```

> Semaphore

```java
package jucLearn.add;

import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;

public class TestSemaphore {
    public static void main(String[] args) {
        // 线程数量：停车位，限流
        Semaphore semaphore = new Semaphore(3);

        for (int i = 0; i < 6; i++) {
            new Thread(()->{
                //acquire 得到
                
                try {
                    semaphore.acquire();
                    System.out.println(Thread.currentThread().getName()+"得到车位");
                    TimeUnit.SECONDS.sleep(2);
                    System.out.println(Thread.currentThread().getName()+"停车2s，离开车位");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }finally {
                    // release 释放
                    semaphore.release();
                }
            },String.valueOf(i)).start();
        }
    }
}
```

用来限流的。

`semaphore.acquire();` 获得，如果已经满了，就等待，等到别人被释放为止

`  semaphore.release();`释放，会将当前的信号了+1，然后唤醒等待的线程

作用：多个共享资源互斥的使用，并发限流

#### 9、读写锁

>ReadWriteLock

可以多个线程读，只能有一个线程写(为了提高效率)

```java
package jucLearn.rw;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

/**
 * 独占锁(写锁) 一次智能被1个线程占有
 * 共享锁(读锁)  多个线程可以同时占有
 * ReadWriteLock
 * 读-读      可以共存
 * 读-写      不可以共存
 * 写-写      不可以共存
 */
public class TestReadWriteLockDemo1 {
    public static void main(String[] args) {
        MyCacheLock myCache = new MyCacheLock();

        for (int i = 0; i < 5; i++) {
            final int temp = i;
            new Thread(() -> {
                myCache.put(temp + "", temp + "");
            }, String.valueOf(i)).start();
        }

        for (int i = 0; i < 5; i++) {
            final int temp = i;
            new Thread(() -> {
                myCache.get2(temp + "");
            }, String.valueOf(i)).start();
        }
    }
}

/**
 * 自定义缓存
 */

class MyCache {
    private volatile Map<String, Object> map = new HashMap<>();

    // 存，写
    public void put(String key, Object value) {
        System.out.println(Thread.currentThread().getName() + "写入" + key);
        map.put(key, value);
        System.out.println(Thread.currentThread().getName() + "写入完毕");
    }

    // 取，读
    public void get(String key) {
        System.out.println(Thread.currentThread().getName() + "读取" + key);
        Object o = map.get(key);
        System.out.println(Thread.currentThread().getName() + "读取完毕");
    }
}


/**
 * 加上读写锁之后的缓存
 */
class MyCacheLock {
    private volatile Map<String, Object> map = new HashMap<>();

    //读写锁,好处：更加细腻度的控制
    private ReadWriteLock lock = new ReentrantReadWriteLock();

    // 存，写
    //写入的时候只希望，同时只有一个线程往里面写
    public void put(String key, Object value) {
        lock.writeLock().lock();
        try {
            System.out.println(Thread.currentThread().getName() + "写入" + key);
//            TimeUnit.SECONDS.sleep(2);
            map.put(key, value);
            System.out.println(Thread.currentThread().getName() + "写入完毕");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            lock.writeLock().unlock();
        }


    }

    // 取，读
    //读的时候，可以有多个线程同时读
    public void get(String key) {
        lock.readLock().lock();
        try {
            System.out.println(Thread.currentThread().getName() + "读取" + key);
            Object o = map.get(key);
            System.out.println(Thread.currentThread().getName() + "读取完毕");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            lock.readLock().unlock();
        }


    }

    // 这里不加锁，写的时候就去读了
    public void get2(String key) {
        System.out.println(Thread.currentThread().getName() + "读取" + key);
        Object o = map.get(key);
        System.out.println(Thread.currentThread().getName() + "读取完毕");
    }
}
```

#### 10、阻塞队列

![image-20210408210636351](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210408210643.png)

什么情况下：我们使用阻塞队列？多线程并发处理，线程池

![image-20210408213051197](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210408213051.png)

学会使用队列：添加和移除

> 四组API



| 方式       | 抛出异常 | 有返回值，不抛异常 | 阻塞 等待 | 超时等待  |
| ---------- | -------- | ------------------ | --------- | --------- |
| 添加       | add      | offer              | put()     | offer(,,) |
| 移除       | remove   | poll               | take()    | poll(,,)  |
| 判断队列首 | element  | peek               |           |           |



1.抛出异常

2.不会抛出异常

3.阻塞 等待

4.超时等待

```java
package com.xy.bq;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.TimeUnit;

public class Test {
    // 设定队列的容量
   static ArrayBlockingQueue blockingQueue = new ArrayBlockingQueue<>(3);
    
    public static void main(String[] args) throws InterruptedException {
        test4();
    }
    // 抛出异常
    public static void test1(){
        //()里要写队列的大小

        System.out.println(blockingQueue.add('A'));
        System.out.println(blockingQueue.add('B'));
        System.out.println(blockingQueue.add('C'));

        System.out.println("对首"+blockingQueue.element());

        System.out.println(blockingQueue.remove());
        System.out.println(blockingQueue.remove());
        System.out.println(blockingQueue.remove());
        System.out.println(blockingQueue.remove());
    }

    // 不抛出异常，返回false
    public static void test2(){
        //()里要写队列的大小

        System.out.println(blockingQueue.offer('A'));
        System.out.println(blockingQueue.offer('B'));
        System.out.println(blockingQueue.offer('C'));
        System.out.println(blockingQueue.offer('D'));  // 返回值false

        System.out.println(blockingQueue.poll());
        System.out.println(blockingQueue.poll());
        System.out.println(blockingQueue.poll());
        System.out.println(blockingQueue.poll());  // 返回值null
    }

    // 一直阻塞,等待
    public static void test3() throws InterruptedException {
        blockingQueue.put("A");
        blockingQueue.put("B");
        blockingQueue.put("C");
//      blockingQueue.put("d");
        System.out.println(blockingQueue.take());
        System.out.println(blockingQueue.take());
        System.out.println(blockingQueue.take());
        System.out.println(blockingQueue.take());
    }
    // 等待设定的时间，就超时
    public static void test4() throws InterruptedException {
        System.out.println(blockingQueue.offer("a"));
        System.out.println(blockingQueue.offer("a"));
        System.out.println(blockingQueue.offer("a"));
        System.out.println(blockingQueue.offer("a", 2, TimeUnit.SECONDS));

        blockingQueue.poll(2,TimeUnit.SECONDS);
        blockingQueue.poll(2,TimeUnit.SECONDS);
        blockingQueue.poll(2,TimeUnit.SECONDS);
        blockingQueue.poll(2,TimeUnit.SECONDS);
    }

}
```



> SynchronousQueue

同步队列



#### 11、线程池(重点)

线程池：三大方法、7大参数、4种拒绝策略

> 池化技术

池化技术：事先准备好一些资源，有人要用，就来我这里拿，用完之后还给我。



线程池的好处：

- 降低资源的消耗
- 提高响应的速度(创建和销毁十分浪费资源)
- 方便管理

线程复用，控制最大并发数，管理线程。

##### 1、三大方法

```java
package com.xy.pool;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

//Executors工具类,三大方法
public class Demo1 {

    public static void main(String[] args) {
        //使用线程池创建线程
        ExecutorService threadPool = Executors.newSingleThreadExecutor();// 单个线程
        ExecutorService threadPool2 = Executors.newFixedThreadPool(5);// 创建一个固定的线程池的大小
        ExecutorService threadPool3 = Executors.newCachedThreadPool();//可伸缩的，遇强则强，遇弱则弱
        try {
            for (int i = 0; i < 100; i++) {
                threadPool3.execute(()->{
                    System.out.println(Thread.currentThread().getName()+" ok");
                });
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 线程池用完，关闭线程池
            threadPool3.shutdown();
        }
    }
}
```

 Executors.newSingleThreadExecutor()  只有一个线程跑

Executors.newFixedThreadPool(5); 有五个线程跑

Executors.newCachedThreadPool();电脑支持几个就有几个跑

##### 2、七大参数和四大策略

> 创建线程源码分析

```java
 public static ExecutorService newSingleThreadExecutor() {
        return new FinalizableDelegatedExecutorService
            (new ThreadPoolExecutor(1, 1,
                                    0L, TimeUnit.MILLISECONDS,
                                    new LinkedBlockingQueue<Runnable>()));
 	}


public static ExecutorService newFixedThreadPool(int nThreads) {
        return new ThreadPoolExecutor(nThreads, nThreads,
                                      0L, TimeUnit.MILLISECONDS,
                                      new LinkedBlockingQueue<Runnable>());
	}

public static ExecutorService newCachedThreadPool() {
        return new ThreadPoolExecutor(0, Integer.MAX_VALUE,
                                      60L, TimeUnit.SECONDS,
                                      new SynchronousQueue<Runnable>());
    }
```

==本质ThreadPoolExecutor()==

```java
  public ThreadPoolExecutor(int corePoolSize,  // 核心线程池大小
                              int maximumPoolSize,   //最大核心线程数大小
                              long keepAliveTime,   // 超时了，没有人调用就会释放
                              TimeUnit unit,   // 超时单位
                              BlockingQueue<Runnable> workQueue,  // 阻塞队列
                              ThreadFactory threadFactory,		// 线程工厂，创建线程的，一般不动
                              RejectedExecutionHandler handler// 拒绝策略) {  
        if (corePoolSize < 0 ||
            maximumPoolSize <= 0 ||
            maximumPoolSize < corePoolSize ||
            keepAliveTime < 0)
            throw new IllegalArgumentException();
        if (workQueue == null || threadFactory == null || handler == null)
            throw new NullPointerException();
        this.corePoolSize = corePoolSize;
        this.maximumPoolSize = maximumPoolSize;
        this.workQueue = workQueue;
        this.keepAliveTime = unit.toNanos(keepAliveTime);
        this.threadFactory = threadFactory;
        this.handler = handler;
    }
```

![image-20210412143805311](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210412143812.png)

**参数的解释**：

核心线程数： 1和2窗口，一直开着

最大线程数：1-5，3-5开始是不开着的，如果候客区(阻塞队列)满了，那么就必须来上班

超时的单位：设定单位

超时等待：如果业务都处理的差不多了，设置了1h，1h之后还是没人去3,4,5窗口，那么就下班了（释放）

阻塞队列：就是候客区的大小

线程工厂：使用默认的Executors.defaultThreadFactory()

拒绝策略：如果1-5窗口满了，候客区也满了，还有人进来，那么就要让他等待或者走开。 (RejectedExecutionHandler 有四种实现类，也就是四个拒绝策略)



> 手动创建一个线程池

```java
package com.xy.pool;

import java.util.concurrent.Executors;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

/**
 * 四种拒绝策略
 * 1.ThreadPoolExecutor.AbortPolicy()  超过了我们的服务数量，就抛出异常
 * 2.new ThreadPoolExecutor.CallerRunsPolicy()   哪来的去哪里，交给送进来的线程执行
 * 3.ThreadPoolExecutor.DiscardPolicy()   队列满了就丢掉任务，不会抛出异常
 * 4.ThreadPoolExecutor.DiscardOldestPolicy()  队列满了，尝试去和最早的竞争，也不会抛出异常
 */
public class Demo2 {
    public static void main(String[] args) {
       ThreadPoolExecutor threadPoll =  new ThreadPoolExecutor(2,5,
                3, TimeUnit.SECONDS,
                new LinkedBlockingQueue<>(3),
                Executors.defaultThreadFactory(),
                new ThreadPoolExecutor.DiscardOldestPolicy()

       );

        try {

            for (int i = 0; i < 20; i++) {
                Thread.sleep(2);
                threadPoll.execute(()->{
                    System.out.println(Thread.currentThread().getName()+"  ok");
                });
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            threadPoll.shutdown();
        }
    }
} 
```

> 拒绝策略

```java
/**
 * 四种拒绝策略
 * 1.ThreadPoolExecutor.AbortPolicy()  超过了我们的服务数量，就抛出异常
 * 2.new ThreadPoolExecutor.CallerRunsPolicy()   哪来的去哪里，交给送进来的线程执行
 * 3.ThreadPoolExecutor.DiscardPolicy()   队列满了就丢掉任务，不会抛出异常
 * 4.ThreadPoolExecutor.DiscardOldestPolicy()  队列满了，尝试去和最早的竞争，也不会抛出异常
 */
```

> CPU密集型和IO密集型

最大线程数该怎么定义：

1.CPU密集型： CPU是几核的，就设置是多少，这样CPU的效率最高

- ```java
  Runtime.getRuntime().availableProcessors();// 获取CPU的核数
  ```

2.IO密集型：判断程序中十分耗IO的线程有多少个，只要大于这个数就行，一般是两倍



#### 12、四大函数式接口(必须掌握)

新时代的程序员:lambda表达式，链式编程，函数式接口，Stream流式计算



> 函数式接口:只有一个方法的接口



![image-20210413100634770](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210413100634.png)

代码测试：

> Function

```java
package com.xy.functionInterface;

import java.util.function.Function;

/**
 * Function 函数式接口，有一个输入参数，一个输出
 * 只要是函数式接口就可以用lambda表达式简化
 */
public class Demo1 {
    public static void main(String[] args) {
        // 工具类，输出输入的值
//        Function<String, String> function = new Function<String, String>() {
//            @Override
//            public String apply(String s) {
//                return s;
//            }
//        };
        // lambda简化
        Function<String,String> function= str->{return str;};
        // apply方法
        System.out.println(function.apply("Hello"));
    }
}
```

>Predicate<String>

```java
package com.xy.functionInterface;
import java.util.function.Predicate;

/**
 * 断定性接口，有一个输入参数，返回值只能是布尔值
 */
public class Demo2 {
    public static void main(String[] args) {
//        new Predicate<>()

        //简化之后的
        Predicate<String> p = (str)->{
                return str.isEmpty();
        };
        //test方法
        System.out.println(p.test("123"));
    }
}
```

> Consumer消费型接口

```java
package com.xy.functionInterface;

import java.util.function.Consumer;

/**
 * 消费型接口：只有输入，没有返回值
 */
public class Demo3 {
    public static void main(String[] args) {
        Consumer consumer = (num)->{
            System.out.println(num);
        };
        
        consumer.accept("ioasdji");
    }
}
```

>supplier供给型接口

```java
package com.xy.functionInterface;

import java.util.function.Supplier;

/**
 * supplier:供给型接口,没有参数，只有返回值
 */
public class Demo4 {
    public static void main(String[] args) {
        Supplier<Integer> supplier = ()->{
            return 1024;
        };
        System.out.println(supplier.get());
    }
}
```

#### 13、Stream流式计算

> 什么是Stream流式计算

集合、mysql的本质是存储东西的。

计算应该都交给流来操作。

```java
package com.xy.stream;

import java.util.Arrays;
import java.util.List;

public class Test {
    public static void main(String[] args) {
        User user1 = new User(1, "a", 21);
        User user2 = new User(2, "b", 22);
        User user3 = new User(3, "c", 23);
        User user4 = new User(4, "d", 24);
        User user5 = new User(6, "e", 25);

        List<User> list = Arrays.asList(user1, user2, user3, user4, user5);
        list.stream()
                .filter((user)->{return user.getId()%2==0; })  // 过滤,
                .filter(u->{return u.getAge()>23;})         // filter(Predicate<? super T> predicate);
                .map((u)->{u.setName(u.getName().toUpperCase());return u;}) //map匹配  map(Function<? super T, ? extends R> mapper);
                .sorted((uu1,uu2)->{return uu2.getName().compareTo(uu1.getName());}) // 排序sorted(Comparator<? super T> comparator);
                .limit(1)  //输出数量
                .forEach(System.out::println);
    }
}
```

#### 14、ForkJoin

JDK1.7的东西，并行执行任务。提高效率，大数据量

大数据：MapReduce(把大任务拆分为小任务)

![image-20210413110458137](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210413110458.png)

> ForkJoin特点：工作窃取

A和B两个线程都在干活，B干完了，就去抢A的工作

里面维护的都是双端队列

#### 15、异步回调

这里的异步指的是，你这个线程也在跑，但是结果只有用get方法获取的时候才给你。比如下面这个例子

模拟了一个请求，等待3s才返回结果，这时候主线程提前休眠两秒，然后输出语句，等待1s之后，模拟的请求的就 输出了

> 无返回值

```java
package jucLearn;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;

public class Test {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        CompletableFuture completableFuture = CompletableFuture.runAsync(()->{
            try {
                TimeUnit.SECONDS.sleep(3);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        TimeUnit.SECONDS.sleep(2);
        System.out.println("等待2s了");
    
        System.out.println("1111");
        System.out.println(completableFuture.get());

    }
}
```

> 带返回值

```java
      CompletableFuture<Integer> completableFuture = CompletableFuture.supplyAsync(()->{
            System.out.println("completeTableFUture");
            int i = 10/0;  // 创造异常，让那边获取
            return 11;
        });

        //有点像js的语法
        System.out.println(completableFuture.whenComplete((t, u) -> {
            System.out.println("t-->>" + t);  // t代表正常的返回结果
            System.out.println("u-->>" + u);  // u是错误的返回信息
        }).exceptionally((e) -> {
            System.out.println(e.getMessage());
            return 233;
        }).get());
```



#### 16、JMM

>Volatile

Volatile是Java虚拟机提供**轻量级的同步机制**

1. 保证可见性 
   1. 可见性是指当多个线程访问同一个变量时，一个线程修改了这个变量的值，其他线程能够立即看得到修改的值。
2. 不保证原子性
3. 禁止指令重排



> 什么是JMM

jMM：java内存模型，不存在的东西。  这是一种约定

**关于JMM的一些同步的约定**：

- 线程解锁前，必须把共享变量立刻刷回主存
  - ![image-20210420104818992](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210420104826.png)
- 线程加锁前，必须读取主存中的最新值到工作内存中
- 加锁和解锁是同一把锁

> 8种操作

![image-20210420105822484](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210420105822.png)

可以去博客搜索一下，这八个操作的一些约定



有了问题，如果flag的值同时被两个线程读取了，在另外一个线程里面修改了flag的值，那另外一个读取的flag就是有问题的。



> 线程对主内存的变化不可知

```java
public class Demo01 {
    static int sum =0;
    public static void main(String[] args) throws InterruptedException {
        new Thread(() -> {
            while (sum==0){

            }
        }).start();

        TimeUnit.SECONDS.sleep(2);
        sum =1;
        System.out.println(sum);
    }
} // 这里的sum修改之后，线程并不会终止
```

#### 17、volatile

> 1、保证可见性

```java
public class Demo01 {
    static int sum =0;
    public static void main(String[] args) throws InterruptedException {
        new Thread(() -> {
            while (sum==0){

            }
        }).start();

        TimeUnit.SECONDS.sleep(2);
        sum =1;
        System.out.println(sum);
    }
} // 这里的sum修改之后，线程并不会终止
```

上面的代码会一直循环

```java
public class Demo01 {
    //使用volatile可以保证可见性
    static volatile int sum =0;

    public static void main(String[] args) throws InterruptedException {

        new Thread(() -> {
            while (sum==0){

            }
        }).start();

        TimeUnit.SECONDS.sleep(2);
        sum =1;
        System.out.println(sum);
    }
}
```

> 2、不保证原子性

```java
package com.xy.jmm;
public class Demo02 {

    private static volatile int num = 1;
    static void add(){
        num++; //不是一个原子性操作
    }
    public static void main(String[] args) {
        for (int j = 20; j > 0; j--) {
            new Thread(() -> {
                for (int i = 0; i < 1000; i++) {
                    add();
                }
            }).start();
        }
        while (Thread.activeCount()>2){
            //有两个线程 main 和gc一直在
        }
        System.out.println(num);
    }
}
```

最后输出的num不是20000

不用lock和synchronize怎么解决原子性的问题

使用**原子类**

![image-20210420112551645](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210420112551.png)

```java
package com.xy.jmm;

import java.util.concurrent.atomic.AtomicInteger;

public class Test03 {
    private static volatile AtomicInteger num = new AtomicInteger();
    static void add(){
        num.getAndIncrement();
    }
    public static void main(String[] args) {

        for (int j = 20; j > 0; j--) {
            new Thread(() -> {
                for (int i = 0; i < 1000; i++) {
                    add();
                }
            }).start();
        }
        while (Thread.activeCount()>2){
            //有两个线程 main 和gc一直在
        }
        System.out.println(num);
    }
}
```

这些类的底层都直接和操作系统挂钩，直接在内存中修改值。**Unsafe类**(里面都是native方法)

> 指令重排

你写的程序，计算机并不是按照你写的那样去执行的。

源代码--》编译器优化-》指令并行也可能会重排--》内存系统也会重排--》执行

**处理器在进行指令重排的时候，考虑：数据之间的依赖性。**

![image-20210420142742177](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210420142742.png)

**volatile可以避免指令重排：** **是内存屏障实现的。禁止上面的指令和下面的指令顺序交换**

内存屏障。CPU指令，作用：

- 保证特定的操作的执行顺序
- 可以保证某些变量的内存可见性，利用这些特性，volatile实现了可见性

![image-20210420143018218](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210420143018.png)

#### 17、单例模式

- 构造方法私有化
- 提供一个获得实例的方法



> 饿汉式               ----线程安全的。。浪费空间，效率低

```java
package com.xy.single;

//饿汉式单例
public class Hungry {

    // 缺点：浪费空间
    private Hungry(){}

    private final static Hungry HUNGRY = new Hungry();

    public static synchronized Hungry getInstance(){
        return HUNGRY;
    }
}

```

> 懒汉式   使用getInstance()的时候才创建，但是多线程可能会创建多个  --- 线程不安全的

```java
package com.xy.single;

//懒汉式
public class LazyMan {
    private LazyMan(){
        System.out.println(Thread.currentThread().getName()+"单例");
    }

    private static LazyMan lazyMan;

    public static LazyMan getInstance(){
        if(lazyMan==null){
            lazyMan = new LazyMan();
        }
        return lazyMan;
    }


    //多线程并发，会有问题
    public static void main(String[] args) {
        for (int i = 10; i > 0; i--) {
            new Thread(() -> {
                lazyMan.getInstance();
            }).start();
        }
    }
}

```

> DCL懒汉式   双重检测锁模式

```java
package com.xy.single;

//懒汉式
public class LazyManLock {
    private LazyManLock(){
        System.out.println(Thread.currentThread().getName()+"单例");
    }

    private volatile static LazyManLock lazyMan;

    //双重检测锁模式，懒汉式单例  DCL懒汉式
    public static LazyManLock getInstance(){
        if(lazyMan==null){
           synchronized (LazyMan.class){
               if(lazyMan==null){
                   lazyMan = new LazyManLock();
                   /**
                    * 1.分配内存空间
                    * 2.执行构造方法，初始化对象
                    * 3.把这个对象指向这个空间
                    *
                		指令重排可能会让这里出现一些问题
                    * 需要避免指令重排 ，在前面的加上关键词volatile
                    */
               }
           }
        }
        return lazyMan;
    }
    
    public static void main(String[] args) {
        for (int i = 10; i > 0; i--) {
            new Thread(() -> {
                lazyMan.getInstance();
            }).start();
        }
    }
}

```

> 静态内部类

```java
package com.xy.single;

public class Holder {

    private Holder(){

    }
    public static Holder getInstance(){
        return InnerClass.HOLDER;
    }

    public static class InnerClass{
        private static final Holder HOLDER = new Holder();
    }
}
```

反射可以破坏,都不安全

道高一尺魔高一丈

> 枚举

```java
package com.xy.single;

import java.lang.reflect.Constructor;

// enum 本身也是一个class类
public enum  EnumSingle {
    INSTANCE;
  /**  public EnumSingle getInstance(){
        return INSTANCE;
    }*/
}

//反射不能破坏枚举
class Test{
    public static void main(String[] args) throws Exception {
        EnumSingle instance1 = EnumSingle.INSTANCE;
        Constructor<EnumSingle> declaredConstructor = EnumSingle.class.getDeclaredConstructor(null);
        declaredConstructor.setAccessible(true);
        EnumSingle instance2 = declaredConstructor.newInstance();
        //报错 NoSuchMethodException: com.xy.single.EnumSingle.<init>()
        System.out.println(instance1);
        System.out.println(instance2);
    }
}
```

枚举是什么？

枚举类型的**最终反编译源码**，在idea里面和javap反编译出来的都有问题

![image-20210420155222245](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210420155222.png)

#### 18、深入理解CAS

> 什么是CAS

java层面的

```java
package com.xy.cas;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * CAS  : compareAndSet
 *
 */
public class CASDemo {

    public static void main(String[] args) {
        AtomicInteger atomicInteger = new AtomicInteger(20);
        // public final boolean compareAndSet(int expect, int update)
        // 期望的值是这个，那么就更新
        // CAS是CPU的并发原语
        System.out.println(atomicInteger.compareAndSet(20, 21));
        System.out.println(atomicInteger.get());

        System.out.println(atomicInteger.compareAndSet(20, 21));
    }
}
```

> 底层CAS

![image-20210420161221184](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210420161221.png)

![image-20210420161250470](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210420161250.png)



CAS:**比较当前工作内存中的值和主内存的值**，如果这个值是期望的，那么执行操作，如果不是就一直循环！

缺点：

- 循环会耗时
- 一次性只能保证一个共享变量的原子性
- ABA问题

> CAS:ABA问题(狸猫换太子)

就是一个数据A，被另外一个线程使用过，值先改变成B，后又改变会数据A了

这时候我们的线程并不知道这个数据被别人动过了

#### 19、原子引用

带版本号的数据

java.util.concurrent.atomic.**Atomic**Stamped**Reference**;

```java
package com.xy.cas;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicStampedReference;

public class CASDemo2 {
    public static void main(String[] args) {
        Integer yewu = new Integer(2020);
        AtomicStampedReference<Integer> atomicInteger = new AtomicStampedReference<>(yewu, 1);

        new Thread(() -> {
            int stamp = atomicInteger.getStamp(); // 获取版本号
            System.out.println("a1==>"+stamp);

            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println(atomicInteger.compareAndSet(yewu, 2021,
                    atomicInteger.getStamp(), atomicInteger.getStamp() + 1));
            System.out.println(atomicInteger.getStamp());

            System.out.println(atomicInteger.compareAndSet(2021, yewu,
                    atomicInteger.getStamp(), atomicInteger.getStamp() + 1));
            System.out.println(atomicInteger.getStamp());
        },"A").start();


        new Thread(() -> {
            int stamp = atomicInteger.getStamp(); // 获取版本号
            System.out.println("b==>"+stamp);

            try {
                TimeUnit.SECONDS.sleep(2);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }


            System.out.println(atomicInteger.compareAndSet(yewu, 2021,
                    stamp, stamp + 1));
            System.out.println(atomicInteger.getStamp());
        },"B").start();
    }
}

```

![image-20210421094220886](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210421094220.png)

#### 20、各种锁

##### 1、公平锁，非公平锁

默认都是非公平锁

##### 2、可重入锁

所有的锁都是可重入锁



可重入锁(递归锁)---   就是你有大门的钥匙，那么里面的小门的钥匙你就自动获得了

![image-20210421094627612](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210421094627.png)





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
- 养老区
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