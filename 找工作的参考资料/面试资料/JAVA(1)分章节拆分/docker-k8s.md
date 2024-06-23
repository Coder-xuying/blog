# 二：Docker&K8S篇

> chroot 是在 Unix 和 Linux 系统的一个操作，针对正在运作的软件行程和它的子进程，改变它外显的根目录。一个运行在这个环境下，经由 chroot 设置根目录的程序，它不能够对这个指定根目录之外的文件进行访问动作，不能读取，也不能更改它的内容。

**虚拟化技术_VMware 、VirtualBox、KVM**

虚拟化技术就是在操作系统上多加了一个虚拟化层（Hypervisor），可以将物理机的CPU、内存、硬盘、网络等资源进行虚拟化，再通过虚拟化出来的空间上安装操作系统，构建虚拟的应用程序执行环境。这就是我们通常说的虚拟机。

虚拟机的优点：

- 提升IT效率、降低运维成本
- 更快地部署工作负责
- 提高服务器可用性

虚拟机的缺点：

- 占用资源较多、性能较差
- 扩展、迁移能力较差



### Why Docker

**场景**

- 开发人员在本地编写代码，并使用Docker容器与其他同事共享劳动成果。
- 使用Docker将应用程序推送到测试环境中，并执行自动和手动测试。
- 开发人员可以在开发环境中对其进行修复，然后将其重新部署到测试环境中以进行测试和验证。
- 测试完成后，将修补程序推送给生产环境就像将更新的镜像推送到生产环境一样简单。

**需求**

> 快速，一致地交付应用程序、镜像打包环境，避免了环境不一致的问题，简化开发的生命周期，适合于快速迭代敏捷开发的场景

<img src="https://i.loli.net/2021/02/20/7hx2RcvUPKgXpma.png" alt="image-20210220140837929" style="zoom: 50%;" />



### 核心概念

**Docker引擎-守护进程**

​	Docker使用C / S架构 ：用户通过**Docker客户端**与Docker守护进程（Docker引擎）通过Unix套接字或者RESTAPI进行通信，**Docker引擎**完成了构建，运行和分发Docker容器的繁重工作



**Docker镜像-Dockerfile**

​	Docker镜像类似于虚拟机镜像，是一个只读的模板，是创建Docker容器的基础

​	镜像是基于联合（Union）文件系统的一种层式的结构，由一系列指令一步一步构建出来。

​	比如：拷贝文件、执行命令



**Docker仓库-Hub**

Docker仓库可以分为**公开仓库 （Public）**和**私有仓库（Private）**两种形式。

最大的公开仓库是官方提供的**Docker Hub**，其中存放了数量庞大的镜像供用户下载。



### 基本操作

**镜像**

```dockerfile
[root@localhost ~]# docker pull mysql:5.7.30
5.7.30: Pulling from library/mysql ……
[root@localhost ~]# docker images 
REPOSITORY TAG IMAGE ID CREATED SIZE 
mysql 5.7.30 9cfcce23593a 6 weeks ago 448MB
[root@localhost ~]# docker tag mysql:5.7.30 mysql5 
[root@localhost ~]# docker images 
REPOSITORY TAG IMAGE ID CREATED SIZE 
mysql5 latest 9cfcce23593a 6 weeks ago 448MB 
mysql 5.7.30 9cfcce23593a 6 weeks ago 448MB
[root@localhost ~]# docker inspect mysql:5.7.30 
[{显示docker 详细信息}]
[root@localhost ~]# docker search mysql
[root@localhost ~]# docker rmi mysql:5.7.30
[root@localhost ~]# docker push mysql[:TAG]
```

**容器**

```dockerfile
[root@localhost ~]# docker create -it nginx
[root@localhost ~]# docker start 9cfcce23593a

#查看运行的容器 
[root@localhost ~]# docker ps 
#查看所有容器 
[root@localhost ~]# docker ps -a
#新建并启动容器
[root@localhost ~]# docker run -it --rm --network host tomcat:8.5.56-jdk8-openjdk
```



### 实战

1. 创建一个卷，待后边使用

   ```dockerfile
   docker volume create test_volume
   ```

   

2. 分别启动2个容器挂在上卷,

   ```dockerfile
   在2个终端窗口启动2个容器 
   docker run -it --rm -v test_volume:/test nginx:latest /bin/bash
   docker run -it --rm -v test_volume:/test nginx:latest /bin/bash 
   cd /test; 
   touch a.txt 
   ls /test # 在两个容器中我们均可以看到我们创建的文件，shixian在多个容器之间实现数据共享
   ```

   

挂载在容器 /test 目录内创建。 Docker **不支持容器内安装点的相对路径**。 多个容器可以在同一时间段内使用相同的卷。如果两个容器需要访问共享数据，例如，如果一个容器写入而另一个容器读取数据。 卷名 在驱动程序test必须唯一。这意味着不能将**相同的卷名**与两个不同的驱动程序一起使用。 如果我们指定了当前test_volume程序上已在使用的卷名，则Docker会假定我们要重用现有卷，并且不会返回错误。如果开始无 test_volume 则会创建这个卷当然除了使用卷，也可以使用将宿主机的文件映射到容器的卷，命令类似，只不过不用提前创建卷，而且数据会映射到宿主机上注意如果宿主机上的目录可以不存在，会在启动容器的时候创建