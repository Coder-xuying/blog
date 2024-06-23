### java的IO演进

#### 1、BIO(同步并阻塞)

服务器实现模式是一个连接一个线程，客户端有连接请求时，服务端就要启动一个线程进行处理，这个连接不作任何事情，就会有不必要的线程开销

![image-20210728094036126](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210728094036.png)

即使啥都不干，线程还是要阻塞在那里

#### 2.NIO(同步非阻塞)

服务器实现模式是**一个线程处理多个请求**，客户端发送的连接请求都会注册到多路复用器上,多路复用器**轮询**到连接有I/O请求就进行处理   **Selector选择器就是多路复用器**。 当通道没数据的时候，就切换到下一个，不等待

![image-20210728094340450](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210728094340.png)

#### 3.AIO 异步非阻塞

![image-20210728094520609](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210728094520.png)

#### 4、适用场景

![image-20210728094756113](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210728094756.png)

### 2.BIO深入





### IO多路复用

阻塞+可以监听

![image-20210806201514224](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210806201514.png)



![image-20210806201701416](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210806201701.png)

epoll 比select能接收的快递多得多

![image-20210806201855440](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210806201855.png)







### 4、零拷贝

#### linux的IO原理

##### 1.物理内存和虚拟内存

物理内存是实际的内存，虚拟内存是计算机系统内存管理的技术，给每一个进程分配一个内存映射表，用来把不连续的物理内存碎片让进程看起来是连续的，可以进行虚拟内存到物理内存的一个映射

##### 2.内核空间和用户空间

操作系统将虚拟空间划分成了两部分，一部分是内核空间，一部分是用户空间。内核空间对应的进程处于内核态的。

内核进程和用户进程占有的虚拟内存比例是1:3、加入是4g的寻址空间，那么内核空间是最高的1G字节。其余的是用户空间

![image-20210811141306527](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811141306.png)



内核态可以执行任意命令，调用系统的一切资源，而用户态只能执行简单的运算，不能直接调用系统资源。用户态必须通过系统接口（System Call），才能向内核发出指令。



当用户进程启动一个 bash 时，它会通过 getpid() 对内核的 pid 服务发起系统调用，获取当前用户进程的 ID；

当用户进程通过 cat 命令查看主机配置时，它会对内核的文件子系统发起系统调用。



#### Linux IO读写的方式

##### IO中断技术

在DMA技术之前，应用程序和磁盘之间的IO都是通过CPU的中断完成的，然后发起 I/O 请求等待数据读取和拷贝完成，**每次的 I/O 中断都导致 CPU 的上下文切换。**

![image-20210811141652681](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811141652.png)

- 用户进程向CPU发起read()系统调用，会进行中断，用户态切换为内核态，然后一直阻塞等待数据的返回。
- CPU收到命令后就发起IO请求，将磁盘数据准备到磁盘控制器缓冲区
- 数据准备完成以后，磁盘向 CPU 发起 I/O 中断。
- CPU 收到 I/O 中断以后将**磁盘缓冲区中的数据拷贝到内核缓冲区**，然后再**从内核缓冲区拷贝到用户缓冲区**
- 用户进程由内核态切换回用户态，解除阻塞状态，然后等待 CPU 的下一个执行时间钟。

##### DMA传输原理

DMA 的全称叫直接内存存取（Direct Memory Access），就是可以让外围设备直接访问系统主内存

![image-20210811142009686](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811142009.png)

这时候进行请求就变成下面这样了

![image-20210811142033879](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811142034.png)

CPU在发起IO请求之后，CPU 从繁重的 I/O 操作中解脱，CPU发送IO之后，可以去干别的事情，让DMA和磁盘进行数据准备和数据拷贝到内核缓冲区，然后再通知CPU，进行数据从内核缓冲区拷贝到用户缓存区中。



##### 传统IO方式

在 Linux 系统中，传统的访问方式是通过 write() 和 read() 两个系统调用实现的，通过 read() 函数读取文件到到缓存区中，然后通过 write() 方法把缓存中的数据输出到网络端口



读取流程如下，会涉及到4次上下文切换(每次系统调用和返回都要进行上下文切换，read和write就需要四次)，两次CPU拷贝，两次DMA拷贝。

#### 零拷贝方式



在 Linux 中零拷贝技术主要有 3 个实现思路：用户态直接 I/O、减少数据拷贝次数以及写时复制技术。

##### 1.用户态直接IO

![image-20210811142641179](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811142641.png)

用户态直接进行IO，跨过内核进行传输，极大的提高了性能。

用户态直接 I/O 只能**适用于不需要内核缓冲区处理的应用程序**(数据没有处理直接拿过去用了)，这些应用程序通常在进程地址空间有自己的数据缓存机制，称为自缓存应用程序，如数据库管理系统就是一个代表。

这种零拷贝机制会直接操作磁盘 I/O，由于 CPU 和磁盘 I/O 之间的执行时间差距，会造成大量资源的浪费，**解决方案是配合异步 I/O 使用**。

##### 2. mmap + write

mmap 是 Linux 提供的一种内存映射文件方法，mmap 的目的是将内核中读缓冲区（read buffer）的地址与用户空间的缓冲区（user buffer）进行映射，从而实现内核缓冲区与应用程序内存的共享 。  (这样就减少了一次CPU拷贝)

![image-20210811143224852](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811143224.png)

mmap 主要的用处是提高 I/O 性能，特别是针对大文件。

mmap 的拷贝虽然减少了 1 次拷贝，提升了效率，但也存在一些隐藏的问题。当 mmap 一个文件时，如果这个文件被另一个进程所截获，那么 write 系统调用会因为访问非法地址被 SIGBUS 信号终止，服务器可能因此被终止。

##### 3.sendfile

通过 sendfile 系统调用，数据可以直接在内核空间内部进行 I/O 传输，从而省去了数据在用户空间和内核空间之间的来回拷贝。

也就是数据不经过用户缓存区了，直接在内核缓冲区进行CPU拷贝到Socket的缓冲区，这可以减少两次上下文切换和一次CPU拷贝。

**sendfile 存在的问题是用户程序不能对数据进行修改，而只是单纯地完成了一次数据传输过程。**

![image-20210811143404121](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811143404.png)

##### 4. sendfile + DMA gather copy

![image-20210811143635681](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811143635.png)

少了从内核缓冲区-》socket缓冲区的拷贝过程，直接进行DMA Gather Copy拷贝到网卡

这个方式需要硬件的支持，用户不能对数据进行修改，它只适用于将数据从文件拷贝到 socket 套接字上的传输过程。

##### 5. splice

splice 系统调用可以在内核空间的读缓冲区（read buffer）和网络缓冲区（socket buffer）之间建立管道（pipeline），从而避免了两者之间的 CPU 拷贝操作

![image-20210811143808451](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811143808.png)

splice 拷贝方式也同样存在用户程序不能对数据进行修改的问题。



#### java中NIO零拷贝的实现

javaNIO中的通道(Channel)相当于OS里面的内核空间缓冲区，缓冲区(Buffer)对应OS里的用户空间的用户缓冲区

- 通道（Channel）是半双工的，它既可能是读缓冲区（read buffer），也可能是网络缓冲区（socket buffer）。
- 缓冲区（Buffer）分为堆内存（HeapBuffer）和堆外内存（DirectBuffer），这是通过 malloc() 分配出来的用户态内存。

堆外内存（DirectBuffer）在使用后需要应用程序手动回收，而堆内存（HeapBuffer）的数据在 GC 时可能会被自动回收。

在使用 HeapBuffer 读写数据时，为了避免缓冲区数据因为 GC 而丢失，NIO 会先把 HeapBuffer 内部的数据拷贝到一个临时的 DirectBuffer 中的本地内存

##### 1. MappedByteBuffer

MappedByteBuffer 是 NIO 基于内存映射（mmap）这种零拷贝方式的提供的一种实现

MappedByteBuffer 使用是堆外的虚拟内存，因此分配（map）的内存大小不受 JVM 的 -Xmx 参数限制，但是也是有大小限制的。

MappedByteBuffer 在处理大文件时性能的确很高，但也存内存占用、文件关闭不确定等问题，

##### 2. DirectByteBuffer

DirectByteBuffer 的对象引用位于 Java 内存模型的堆里面，JVM 可以对 DirectByteBuffer 的对象进行内存分配和回收管理，一般使用 DirectByteBuffer 的静态方法 allocateDirect() 创建 DirectByteBuffer 实例并分配内存。



##### 3. FileChannel

FileChannel 是一个用于文件读写、映射和操作的通道，同时它在并发环境下是线程安全的

FileChannel 定义了 transferFrom() 和 transferTo() 两个抽象方法，它通过在通道和通道之间建立连接实现数据传输的。



TransferTO()执行的过程

以 sendfile 的零拷贝方式尝试数据拷贝。如果系统内核不支持 sendfile，以 mmap 的零拷贝方式进行内存映射，这种情况下目的通道必须是 FileChannelImpl 或者 SelChImpl 类型。如果以上两步都失败了，则执行 transferToArbitraryChannel() 方法，基于传统的 I/O 方式完成读写





#### Netty零拷贝

 我们所说的 Netty 零拷贝完全是基于（Java 层面）用户态的，它的更多的是偏向于数据操作优化这样的概念



####  RocketMQ和Kafka对比

RocketMQ 选择了 mmap + write 这种零拷贝方式，适用于业务级消息这种小块文件的数据持久化和传输；而 Kafka 采用的是 sendfile 这种零拷贝方式，适用于系统日志消息这种高吞吐量的大块文件的数据持久化和传输。但是值得注意的一点是，Kafka 的索引文件使用的是 mmap + write 方式，数据文件使用的是 sendfile 方式。



