

存储和中间件

- mysql
  - **85%**
  - 事务、隔离级别、mvcc、log
  - 索引、如何设计、如何优化、索引失效
  - 锁、间隙锁、读写锁等
  - 分库分表、高可用、多集群、读写分离 数据同步
  - sql语法、内外连接、sql注入
  - zebra设计
    - 参考：https://github.com/Meituan-Dianping/Zebra/wiki/Zebra%E6%80%BB%E4%BD%93%E8%AE%BE%E8%AE%A1 （zebra ）
- redis
  - **90%**
  - 分布式锁、缓存方案（缓存击穿等）、一致性
  - 底层数据结构、zset 和跳表
  - 持久化、高可用集群（主从、哨兵、集群）
  - redis单线程为什么快、过期机制、内存淘汰 
  - 线程模型、通信模型、底层架构、bat、bat2架构区别
- kafka 
  - **70%**
- hbase
  - **60%**
- zk
  - **60%**
-  本地缓存caffeine
  - **40%**

java相关

- jvm
  - 判断对象、垃圾回收GC、内存模型、GC调优
  - 类加载、G1、CMS、双亲委派、内存溢出
- 多线程
  - 锁、Synchronized、volatile、线程池、CAS、Java 锁升级、AQS
  - ReetrantLock、线程安全的结构
- spring
  - aop、IOC、bean的生命周期、动态代理、循环依赖
  - Spring MVC 的原理和流程
  - dubbo服务调用过程、
- 集合框架
  - hashMap、ConcurrentHashMap、 ArrayList 与 LinkedList 

- 基础语法
  - 反射、**ThreadLocal**、sleep() 与 wait() 的区别、内存泄漏
  - 深浅拷贝、封装、继承、多态、netty
  - MyBatis、 ORM 映射

夯实

- 操作系统
  - **50%**
  - 进程和线程、通信方式、 Linux 进程调度、linux的命令和功能、copyOnWrite
  - 内存管理、零拷贝
  - IO模型、BIO、NIO、select, poll, epoll
- 计算机网络
  - TCP机制、粘包和拆包，三次握手、四次、 https和http、输入url的过程
  - cookie和session、加密对称和非对称、DDOS攻击、tcp长短连接、RPC调用、序列化相关
  - http1.0、2.0、3.0

- 链路追踪 

- 系统设计
  - 研究4-6个系统设计的题目
  - 电商秒杀
  - 短链生成
  - 限流
  - feed 流
- 算法
  - leetcode 100 刷完
- 设计模式
  - 常用的掌握6-8种
  - 单例模式、
- 版本控制git、构建工具gradle
  - **0-30%**



优先级排名：

- 第一档：mysql、**redis**、**jvm**、多线程、算法（必考）、**kafka**、**系统设计**
- 第二档：spring、java集合和基础知识、hbase、分布式理论、zk
- 第三档：计算机网络、操作系统
- 第四档：本地缓存caffeine、链路追踪cat、版本控制git、构建工具gradle

掌握能力：mysql