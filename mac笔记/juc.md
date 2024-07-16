### 基础知识

#### sleep 和yield

> sleep

- 线程会休眠，线程状态running= > timed waitting (阻塞状态)

- 在sleep的时候，调用interrupt方法（唤醒线程），这个时候线程会抛InterruptedExcption
- 睡眠结束后线程不一定会立刻得到执行
- 建议使用TimeUnit的sleep方法（使用工具类，这个有时间单位，更清晰）

> yield

- 调用yield，会让当前线程从running进入Runnable 状态，
- 这个线程还是会和其他线程一起抢cpu的时间片                                                                                                                                                                                                                                                                                                  

> Join

等待线程执行完成

> interrupt

打断线程

```java
// 获取打断标记，true和false
thread.isInterrupted() 
```

打断sleep、wait、join的线程，会清空打断标记，并抛出InterruptedException 的异常

但是对正常执行的线程，不会阻塞执行，只是把打断标记 置为true



interrupt 可以优雅的停止线程

##### 两阶段中止模式

一个线程t1怎么优雅终止线程t2

> 错误思路

1、使用线程对象的stop方法： 会杀死线程，如果线程锁住了共享资源，杀死后就没机会释放锁，其他线程永远无法获得锁

2、System.exit()方法：会让整个程序都停止