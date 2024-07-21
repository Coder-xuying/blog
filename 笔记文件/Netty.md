

# Netty

Netty的异步不是异步IO而是 调用异步，使用IO多路复用，然后

#### 1.Netty是什么？

- netty是一个基于NIO的C/S框架，用它可以快速简单的开发网络应用程序
- 简化了TCP和UDP套接字服务器等网络编程，性能和安全性也更好
- 支持多种协议  - FTP、SMTP、HTTp等

#### 2.为什么用Netty

 Netty 具有下面这些优点

- 简单性能高
- 自带编码器解决TCP 沾包/拆包问题
- 安全性高
- 社区活跃，比较稳定
- 很多开源项目都用了，比如Dubbo、RocketMQ

#### 3.Netty 应用场景了解么？

- RPC框架的网络通信工具
- HTTp服务器
- 即使通讯系统
- 消息推送系统



#### 4、Netty的核心组件

- Channel：包含基本的IO操作，bind、connect、read、write。常用的实现类是NioServerSocketChannel （服务端）和 NioSocketChannel。分别对应 ServerSocket 以及 Socket
- EventLoop： 负责监听⽹络事件并调⽤**事件处理器(handler)**进⾏相关 I/O 操 作的处理,相当于反应器模式里面的reactor，EventLoop 负责处理注册到其上的 Channel
- ChannelFuture：Netty 是异步⾮阻塞的，所有的 I/O 操作都为异步的。你可以通过 ChannelFuture 接⼝的 addListener() ⽅法注册⼀个 ChannelFutureListener ，当操作执⾏成功或者失败时，监听就会⾃动触发返回结果。我们还可以通过 ChannelFuture 接⼝的 sync() ⽅法让异步的操作变成同步的。
- ChannelHandler 和 ChannelPipeline
  - ChannelHandler 是消息的具体处理器，负责处理读写操作、客户端连接等事情。
  - ChannelPipeline 为 ChannelHandler 的链，提供了⼀个容器并定义了⽤于沿着链传播⼊站和出站 事件流的 API 。通过 addLast() ⽅法添加⼀个或者多个 ChannelHandler ，因为⼀ 个数据或者事件可能会被多个 Handler 处理

#### 5、EventLoop中设置的线程数

```java
// 方法最后是运行的这个方法，可以看到当设置为0 的时候去找默认的 DEFAULT_EVENT_LOOP_THREADS 数量
protected MultithreadEventLoopGroup(int nThreads, Executor executor, Object... args) {
    super(nThreads == 0 ? DEFAULT_EVENT_LOOP_THREADS : nThreads, executor, args);
}  


private static final int DEFAULT_EVENT_LOOP_THREADS;
// 这个默认的数量在静态方法中设置为cpu核数的两倍，netty运行时获得
DEFAULT_EVENT_LOOP_THREADS = Math.max(1, SystemPropertyUtil.getInt(
                "io.netty.eventLoopThreads", NettyRuntime.availableProcessors() * 2));

```


