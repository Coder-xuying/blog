# Zookeeper

### 1.基础

#### 1.Zookeeper的特点

![image-20210811154037264](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811154037.png)



leader进行写，follower读。

为什么适合奇数，因为5台挂了三台就不能用，6台集群也是挂三台就不能用，浪费了一台。所以更适合奇数台



#### 2.数据结构

![image-20210811154935005](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811154935.png)

#### 3.应用场景

![image-20210811155015293](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811155015.png)



> 统一命名服务

![image-20210811155152942](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811155153.png)

> 统一配置管理

![image-20210811155301909](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811155302.png)



> 统一集群管理

![image-20210811155413689](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811155413.png)

管理集群的状态。

> 软负载均衡

![image-20210811185348597](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811185348.png)







### 4、源码分析

#### 1.算法基础

##### 1.1 拜占庭将军问题

将军们必须全体一致是否攻击某一支敌军，然后各个将军的部队都是分离的，里面有叛徒。必须所有的将军都同意，才能做出决定。

##### 1.2 Paxos算法

![image-20210813205226484](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210813205226.png)

##### ZAB协议

在Paxos算法上改进的协议，Zookeeper用的是这个  ==两阶段提交==



![image-20210813210403079](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210813210403.png)

![image-20210813210438539](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210813210438.png)



> 崩溃恢复-异常假设

两种情况：

- leader在commit发出去之后，挂了，所有的follower必须提交
- leader在commit还没有发就挂了，那么提案就丢掉

> 崩溃恢复 - leader选举

![image-20210813210828824](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210813210828.png)



> 数据恢复

![image-20210813210952128](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210813210952.png)

### CAP理论

#### 1.ZooKeeper 是什么？

ZooKeeper 是一个分布式协调服务，它是集群的管理者，监视着集群中各个节点的状态根据节点提交的反馈进行下一步合理操作。最终，将简单易用的接口和性能高效、功能稳定的系统提供给用户。
ZooKeeper 为我们提供了高可用、高性能、稳定的分布式数据一致性解决方案，通常被用于实现诸如数据发布/订阅、负载均衡、命名服务、分布式协调/通知、集群管理、Master 选举、分布式锁和分布式队列等功能。**ZooKeeper 将数据保存在内存中，性能是非常棒的。**

客户端的读请求可以被集群中的任意一台机器处理，对于写请求，这些请求会同时发给其他 zookeeper 机器并且达成一致后，请求才会返回成功。因此，随着 zookeeper 的集群机器增多，读请求的吞吐会提高但是写请求的吞吐会下降。



有序性是 zookeeper 中非常重要的一个特性，所有的更新都是全局有序的，每个更新都有一个唯一的时间戳，这个时间戳称为 zxid（Zookeeper Transaction Id）

#### Zookeeper特点

- **顺序一致性：** 从同一客户端发起的事务请求，最终将会严格地按照顺序被应用到 ZooKeeper 中去。
- **原子性：** 所有事务请求的处理结果在整个集群中所有机器上的应用情况是一致的，也就是说，要么整个集群中所有的机器都成功应用了某一个事务，要么都没有应用。
- **单一系统映像 ：** 无论客户端连到哪一个 ZooKeeper 服务器上，其看到的服务端数据模型都是一致的。
- **可靠性：** 一旦一次更改请求被应用，更改的结果就会被持久化，直到被下一次更改覆盖。

#### 2.zookeeper的文件系统

Zookeeper 提供一个多层级的节点命名空间（节点称为 znode）。与文件系统不同的是，**这些节点都可以设置关联的数据**，而文件系统中只有文件节点可以存放数据而目录节点不行。Zookeeper 为了保证高吞吐和低延迟，在内存中维护了这个树状的目录结构，所以Zookeeper 不能用于存放大量的数据，每个节点的存放数据上限为1M。

#### zookeeper应用场景

- 分布式锁：创建唯一节点获得分布式锁，当获得锁的一方执行完相关代码或者是挂掉之后就释放锁。
- **命名服务** ：可以通过 ZooKeeper 的顺序节点生成全局唯一 ID
- **数据发布/订阅** ：通过 **Watcher 机制** 可以很方便地实现数据发布/订阅。当你将数据发布到 ZooKeeper 被监听的节点上，其他机器可通过监听 ZooKeeper 上节点的变化来实现配置的动态更新。

### 基本概念



#### 数据模型

ZooKeeper 数据模型采用层次化的多叉树形结构，每个节点上都可以存储数据，这些数据可以是数字、字符串或者是二级制序列。每个node可以存1M

![image-20210822130851841](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210822130858.png)

#### 数据节点

> Znode四种类型

- **持久（PERSISTENT）节点** ：一旦创建就一直存在即使 ZooKeeper 集群宕机，直到将其删除。
- **临时（EPHEMERAL）节点** ：临时节点的生命周期是与 **客户端会话（session）** 绑定的，**会话消失则节点消失** 。并且，**临时节点只能做叶子节点** ，不能创建子节点。
- **持久顺序（PERSISTENT_SEQUENTIAL）节点** ：除了具有持久（PERSISTENT）节点的特性之外， 子节点的名称还具有顺序性。比如 `/node1/app0000000001` 、`/node1/app0000000002` 。
- **临时顺序（EPHEMERAL_SEQUENTIAL）节点** ：除了具备临时（EPHEMERAL）节点的特性之外，子节点的名称还具有顺序性。

> znode数据结构

每个 znode 由 2 部分组成:

- **stat** ：状态信息
  - cZxid	create ZXID，即该数据节点被创建时的事务 id
  - mZxid	modified ZXID，即该节点最终一次更新时的事务 id
  - aclVersion	节点的 ACL 版本号，表示该节点 ACL 信息变更次数
- **data** ： 节点存放的数据的具体内容

> ACL (权限控制)

对于 znode 操作的权限，ZooKeeper 提供了以下 5 种：

- **CREATE** : 能创建子节点
- **READ** ：能获取节点数据和列出其子节点
- **WRITE** : 能设置/更新节点数据
- **DELETE** : 能删除子节点
- **ADMIN** : 能设置节点 ACL 的权限



### 1.Zookeeper的选举制度

> 第一次初始化的时候

假设有五台机器，需要上线三台才能选举成功

- 首先，第一台服务器上线，投票给自己，未到半数以上
- 然后第二台上线，都投给自己，并交换选票的信息，此时第一台服务器发现另外一台的myid大于自己的，就把选票给了第二台服务器
- 第三台服务器上线，投给了自己，交换选票信息，第二台发现第三台的myid大于自己的，就把选票给第三台了，此时选票数大于半数，leader选举成功。
- 此时如果有第四台上线，投给自己，因为第三台的票数》第四台的，直接成为follower，并把选票给leader

> 非第一次启动的情况

无服务运行期间无法和leader保持连接： 两种情况

- 集群中有leader但是连接不上
  - 想去选举的话，其他机器会告诉他leader还在，你要去继续尝试连接
- 集群中的leader挂掉了



![image-20210811192916829](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811192916.png)

字段的意思：

- SID，服务器的ID，用来标识集群中的机器
- ZXID，事务ID，就是标识这个服务器状态变更的次数，比如做了一次操作就加1
- Epoch，投票的次数，比如初始化之后，他们就是1，第二次投票就变成2了

leader挂掉按照下面的步骤选取：

假设有五台机器，SID分别是1,2,3,4,5 ，ZXID分别是8,8,8,7,7. 然后SID为3的机器是Leader，此时，3和5号机器挂掉了，开始进行Leader选举

![image-20210811193130016](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210811193130.png)

EPOCH越大代表他存在的时间越长，
