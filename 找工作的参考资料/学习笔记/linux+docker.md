## shell

### 1、变量

**变量名命名规范**

- 只能使用英文字母，数字和下划线，首个字符不能以数字开头。
- 中间不能有空格，可以使用下划线（_）
- 不能使用标点符号。
- 不能使用bash里的关键字

```
#使用变量需要加上$，也可使用{}把变量名包裹起来
your_name="qinjx"
echo $your_name
echo ${your_name}
```

**只读变量**

使用readonly将变量定义为只读变量，只读变量的值不能改变

`readonly xxx`

**删除变量**

`unset xxx`

**变量类型**

- 局部变量：局部变量在脚本或命令中定义，仅在当前shell实例中有效
- 环境变量：所有的程序，包括shell启动的程序，都能访问环境变量
- shell变量：shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量

### 2、shell字符串

> 单引号

```bash
str = "this is a string"
#单引号里的任何字符都会原样输出，不能有单独的一个单引号（即使使用转义符）
#单引号可以成对出现
```

> 双引号

```bash
#双引号里可以有变量
#双引号可以出现转义字符
your_name="runoob"
# 使用双引号拼接
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting  $greeting_1
# 使用单引号拼接
greeting_2='hello, '$your_name' !'
greeting_3='hello, ${your_name} !'
echo $greeting_2  $greeting_3

输出
hello, runoob ! hello, runoob !
hello, runoob ! hello, ${your_name} !
```

> 获取字符串长度

```bash
string="abcd"
echo ${#string} #输出 4
```

> 提取字符串

```bash
string="runoob is a great site"
echo ${string:1:4} # 输出 unoo  从1开始截取4位字符
```

### 3、数组

```bash
#数组名=（value1 value2 value3），使用空格分隔
array_name=(value0 value1 value2 value3)
or
array_name=(
value0
value1
value2
value3
)
```

==可以不使用连续的下标，而且下标的范围没有限制。==

> 读取数组

`${数组名[下标]}`，使用 **@** 或者*符号可以获取数组中的所有元素

```bash
echo ${array_name[@]}
```

> 获取数组的长度

```bash
# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}
# 取得数组单个元素的长度
lengthn=${#array_name[n]}
```

### 4、注释

```bash
#单行注释

:<<EOF
xx  多行注释
xx
EOF

:<<'
注释内容...
注释内容...
注释内容...
'

:<<!
注释内容...
注释内容...
注释内容...
!
```

==遇到大段断码需要临时注释，可以用花括号{} 括起来，定义成一个函数，然后其他的地方不调用这个函数，代码块就不会执行

### 5、传递参数

脚本内获取参数的格式为 ：`$n`

```bash
#test.sh
echo "Shell 传递参数实例！";
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";

./test.sh 1 2 3        传递三个参数进去，$n 相当于占位符
```

> 特殊字符

![image-20201019142335789](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20201019142335.png)

> `$@`和`$*`的区别

相同点：都是引用所有的参数

不同点：@ 相当于"1" "2" "3",   * 相当于 "1 2 3"(一个参数)

```bash
$ ./test.sh 1 2 3
-- $* 演示 ---
1 2 3
-- $@ 演示 ---
1
2
3
```

### 6、基本运算符

![image-20201019142356265](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20201019142356.png)

==运算符之间要空格==

> 关系运算符

![image-20201019142404408](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20201019142404.png)

> 布尔运算符

![image-20201019142420464](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20201019142420.png)

> 逻辑运算符

![image-20201019142428825](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20201019142428.png)

> 字符串运算符

![image-20201019142539616](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20201019142539.png)

>

![](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20201019142447.png)

### 7、echo命令

```bash
echo "it is a test"
it is a test


#转义字符
echo "\"it is a test\""
"it is a test"

#!/bin/sh
read name 
echo "$name It is a test"

#显示换行

echo -e "OK!" # -e 开启转义
echo "It is a test"

OK!
It is a test

#显示不换行
echo -e "OK! \c" # -e 开启转义 \c 不换行
echo "It is a test"

#显示结果输出到文件
echo "It is a test" > myfile

#用单引号，原样输出字符串
echo '$name\"'

#显示命令执行结果，使用的是反引号 `
echo `date`
```



## linux



==linux中没有输出，就代表成功==

```  
sync   # 将数据同步到硬盘中
shutdown    #关机
reboot    #重启
halt #关闭系统
```

### 1、系统目录结构

![image-20201019142242450](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20201019142242.png)

### 2、常用的基本命令

#### 2.1 目录管理

```
cd      #切换目录命令
./      #当前目录
..      #上一级目录
```

```
ls     
-a   #查看所有的文件，包括隐藏文件
-l   #列出所有文件，包含文件的属性和权限，没有隐藏文件
#所有的可以组合使用

pwd  #显示当前所在的目录
mkdir  #创建一个目录

mkdir -p xx/xx/xx    #加上-p之后才能创建  xx/xx/xx这种
```

```
rmdir xx    #删除目录，不能直接删除非空文件夹
rmdir  -p  xx/xx/xx  递归删除多个目录  
```

```
cp filename  path  #复制文件到path
rm                 #移除文件
   -f     强制删除，不会出现警告
   -r     递归删除目录
   -i     互动，删除询问是否删除
   
   
mv    #移动
	-f      强制
	-u 		只替换已经更新过的
	
mv  xxx  xxx1   #把xxx重命名为xxx1
```

#### 2.2 基本属性

![image-20201019142255859](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20201019142256.png)

Linux中的第一个属性：

- 为d是目录
- 为- 是文件
- 为l则表示链接文档
- ...

![image-20201019142306306](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20201019142306.png)

> 修改文件属性

```
chgrp -R  xxx1   文件名     # xxx1修改后，修改前     更改文件属组
chown -R  xxx1   文件名     # xxx1修改后，修改前     更改文件属主
chown -R  xxx1：xxx2   文件名   #   xxx1：属主名  xxx2：属组名
```

> chmod   更改9个属性

- r:4  
- w:2 
- x:1
- -: 0

rwx = 4+2+1 = 7 

`chmod -R xyz 文件名或目录`  比如 ：chmod -R 777  xxx

> 文件内容查看

- cat  由第一行显示文件内容
- tac  由最后一行显示文件内容
- nl     显示行号
- more   只显示部分，其余的用more显示，按空格翻页，enter向下一行，:f 行号
- less  和more 差不多，不过它可以往前翻
- head  只看头几行     `head -n number xx文件`   -n控制显示number行
- tail   看尾部几行，和head用法相同

```
/xx   向下查找 xx  
?xx   向上查找 xx
n     向下下一个
N	  向上下一个
q	  推出
```

> 扩展

linux 的链接：

- 硬链接    B硬链接A之后，即使删除A也能够通过B访问到A
- 软连接    相当于win的快捷方式，删除之后就用不了了

```
ln 命令创建链接

ln A  B     #B->A   硬链接
ln -s A B   #软连接  又叫符号链接

touch 创建文件
echo  输入字符串

```





### 3、Vim编辑器

#### 3.1 命令模式

- **i**切换到输入模式
- **x** 删除当前光标所在处的字符
- ：切换到底线命令模式，在最底一行输入命令
- 数字 加空格，向右移动xx位
- 数字 加Enter，向下移动xx位

#### 3.2 输入模式

可以使用一下按键：

- backspace 删除光标前一个字符
- del 删除光标后一个字符
- HOME/END  移动光标到行首/行尾
- page down/up  上下翻页
- insert  切换光标为输入/替换模式 ， 看光标的样子

#### 3.3 底线命令模式

基本的命令：

- q  退出程序
- w  保存程序
- wq  保存退出
- set nu   显示行号

==狂神说公众号里面有各种命令==



### 4、账号管理

> useradd 添加用户

`useradd -选项  用户名`

- -m: 自动创建这个用户的主目录  /home/xxx

> userdel 删除用户

`userdel -r xxx`：-r  删除用户之后，将目录也删掉

>usermod 修改用户

`usermod `

> 用户密码设置

创建用户的时候配置密码

### 5、磁盘管理

> df(列出文件系统整体的磁盘使用量) du（检查磁盘空间的使用量）

df  -h ：把字节换算成M、G

![image-20200613195732497](C:\Users\xuying\AppData\Roaming\Typora\typora-user-images\image-20200613195732497.png)

> mount挂载  umount

### 6、进程管理

> 命令

ps  查看当前系统正在执行的各种进程的信息

ps -xx:

- -a 显示当前终端运行的所有的进程信息
- -u 以用户的信息显示进程
- -x 显示后台运行进程的参数   

```bash
ps -aux|grep  mysql   #查看mysql的进程

#  |  叫做管道符   A|B  把A得到的结果  用在B中
# grep  查找文件中符合条件的字符串

ps -ef|grep mysql   # -ef 可以看到父进程的信息

# 一般通过目录树的结构来看父进程

pstree -pu
  -p  显示父 id
  -u  显示用户组
```

结束进程：

```bash
kill -9 进程id
```

### 7、环境安装

#### 7.1 JDK安装

```bash
#rpm安装的
rpm -ivh jdkxxx.rpm

#rpm卸载
rpm -qa|grep jdk   #检测jDk版本信息
rpm -e --nodeps jdkxxxx  #上面查出来的

#配置环境变量
#编辑  /etc/profile  文件
source /etc/profile #让这个文件生效
```

```bash
#开启防火墙端口
firewall -cmd --zone=public --add-port=xxxx/tcp --permanent

#重启防火墙
systemctl restart firewalld.service 

#查看所有开启的端口
firewall-cmd --list-ports
```

#### 7.2 Tomcat安装  

1. 下载tomcat文件

2. 解压 

   ```bash
   tar -zxvf xxxx
   ```

3. 启动tomcat 测试  `./ xx.sh`

   ```bash
   ./startup.sh
   ./shutdown.sh
   ```

4. 确保防火墙的端口是打开的

   ```bash
   # 查看firewall服务状态
   systemctl status firewalld
   
   # 开启、重启、关闭、firewalld.service服务
   # 开启
   service firewalld start
   # 重启
   service firewalld restart
   # 关闭
   service firewalld stop
   
   # 查看防火墙规则
   firewall-cmd --list-all    # 查看全部信息
   firewall-cmd --list-ports  # 只看端口信息
   
   # 开启端口
   开端口命令：firewall-cmd --zone=public --add-port=80/tcp --permanent
   重启防火墙：systemctl restart firewalld.service
   
   命令含义：
   --zone #作用域
   --add-port=80/tcp  #添加端口，格式为：端口/通讯协议
   --permanent   #永久生效，没有此参数重启后失效
   ```

   

#### 7.3 docker安装 （yum安装）

```bash
检查centOS的版本
[root@xuying bin]# cat /etc/redhat-release
CentOS Linux release 7.3.1611 (Core)
```

2、安装我们的准备环境

```bash
yum -y install 包名   #-y 所有的提示都为y


yum -y install gcc
yum -y install gcc-c++


yum remove docker \xx
```

3、清除以前的docker

```bash
yum remove docker \
          docker-client \
          docker-client-latest \
          docker-common \
          docker-latest \
          docker-latest-logrotate \
          docker-logrotate \
          docker-engine
```



4、安装需要的软件包

```bash
yum install -y yum-utils device-mapper-persistent-data lvm2
```

5、设置阿里云的景象

```bash
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

6、更新yum软件包的索引

```bash
yum makecache fast
```

7、安装Docker CE

```bash
yum -y install docker-ce docker-ce-cli containerd.io
```

8、启动测试

```bash
systemctl start docker
docker version
docker run hello-world
```



### linux安装mysql

#### 一、下载mysql的包

`wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.22-linux-glibc2.12-x86_64.tar.gz`

#### 二、解压

```bash
tar -xvf mysql-5.7.22-linux-glibc2.12-x86_64.tar.gz 

//移动到 usr/local 下
mv -v mysql-5.7.22-linux-glibc2.12-x86_64 /usr/lcoal

```

==修改文件夹的名字为mysql==

再创建用户和用户组

```bash
groupadd mysql

useradd -r -g mysql mysql

在mysql目录下创建data文件夹
mkdir data
```

#### 三、初始化

```bash
yum -y install numactl
yum install libaio

/usr/local/mysql/bin/mysqld --user=mysql --basedir=/usr/local/mysql/ --datadir=/usr/local/mysql/data --initialize
```

完成初始化后编辑配置文件 /etc/my.cnf

```bash
[mysqld]
datadir=/usr/local/mysql/data
basedir=/usr/local/mysql
socket=/tmp/mysql.sock
user=mysql
port=3306
character-set-server=utf8
# 取消密码验证
skip-grant-tables
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0
# skip-grant-tables
[mysqld_safe]
log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid
```

将mysql加入到服务

```bash
cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysql

#开机启动
chkconfig mysql on

#启动mysql
service mysql start
```

#### 四、设置mysql密码

```bash
#配置环境变量
export PATH=$PATH:/usr/local/mysql/bin

mysql -u root -p  直接回车进入，不需要输入密码

use mysql;

update user set authentication_string=password('你的密码') where user='root';

flush privileges;

exit

###将 /etc/my.cnf 中skip-grant-tables删除或注释掉


如果提示不能操作数据库，就再修改一次密码
#mysql -u root -p
#alter user 'root'@'localhost' identified by'修改后的密码';
#exit
```

#### 五、设置可以远程连接

```bash
mysql -u root -p
use mysql;
update user set host='%' where user = 'root';
flush privileges;
exit
```





#### 附录

##### 1、防火墙

```bash
firewall-cmd --state  	#查看防火墙状态
systemctl start firewalld.service     #开启防火墙

systemctl enable firewalld.service    #设置开机自启
systemctl restart firewalld.service	  #重启防火墙
systemctl stop firewalld.service      #关闭防火墙
#开端口命令

firewall-cmd --zone=public --add-port=80/tcp --permanent			#单个端口
firewall-cmd --zone=public --add-port=20000-29999/tcp --permanent		#多个端口

firewall-cmd --list-ports		#查看开启端口
firewall-cmd --zone= public --remove-port=80/tcp --permanent  #关闭端口
firewall-cmd --zone= public --query-port=80/tcp		#查看端口是否打开
```





```
ifconfig 

 netstat -anp | grep xxx   查看端口号
```

##### 2.分区

> df

分区的使用空间

df -h 会换成M、G的单位  

![image-20210706211709327](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210706211709.png)



##### 3.删除

> 删除命令

vm -f

-r 就是向下递归，不管有多少级目录，一并删除
-f 就是直接强行删除，不作任何提示的意思







## Docker

### 1、Docker是什么？

Docker是世界上领先的软件集装箱化平台。它灵活、可移植、安全、节省成本。

Container是一个标准化的软件单元。

> Container

一个容器镜像是一个轻量级的、独立的、可以执行的软件包，其中包含运行这个软件所必须的：代码、运行时环境、系统工具、系统库、设置等待。所以这个应用无论在哪个系统上都能运行起来，减少冲突

>Containers And VMs

Container 虚拟化的是操作系统，VM虚拟化的是硬件

- 容器是app层面的抽象，它把代码和它们的依赖一起打包。一台机器上可以运行多个容器，并且它们共享操作系统内核，而且在不同的用户空间被隔离。容器比虚拟机花费更少的空间（容器镜像通常只有几十MBs），而且启动非常快。

- 虚拟机是物理硬件层面的抽象，它的目标是把一个服务器转成多个服务器。一台物理机上可以运行多个虚拟机。每个虚拟机都包含一个操作系统的完全复制，已经一个或多个应用和它们所需的库。通常一个虚拟机几十GBs。虚拟机启动比较慢。

 Docker是平台，Container是这个平台中的一个标准的单元。

### 2、Docker快速开始

> 概念

容器的特点：

- 灵活性：即使是最复杂的应用程序也可以被容器化
- 轻量级：容器利用并共享主机内核
- 可互换的：你可以实时部署更新和升级
- 可移植性：你可以在本地构建、部署到云，并在任何地方运行
- 可伸缩：你可以增加并自动分发容器副本
- 可叠加：你可以垂直地、动态地叠加服务

>  镜像、容器和仓库

image：镜像，一个镜像是一个可执行包，它包含运行应用程序所需的所有内容，包括代码、运行时环境、库、环境变量、配置文件。通过运行镜像类启动一个容器。

container：容器，容器是镜像的运行时实例。你可以使用`docker ps`命令看到正在运行的容器列表，就像在Linux中一样。

repository：仓库，存放镜像的地方 

- 公有仓库
- 私有仓库

> 安装

```bash
1、卸载旧版本
$ sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
  
  
2、需要的安装包
$ sudo yum install -y yum-utils

3、设置镜像的仓库
$ sudo yum-config-manager \
    --add-repo \
    http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    
4、安装docker
$ sudo yum install docker-ce docker-ce-cli containerd.io

5、启动docker
$ sudo systemctl start docker

6、hello
sudo docker run hello-world
```

`docker images`  #查看下载的镜像

==卸载==

```bash
1、卸载依赖
sudo yum remove docker-ce docker-ce-cli containerd.io
2、删除资源   #/var/lib/docker  docker的默认路径
sudo rm -rf /var/lib/docker
```

**阿里云镜像加速**

登录阿里云，找到容器镜像服务

![image-20210313143410885](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210313143411.png)

![image-20210313143421385](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210313143421.png)

```bash
#配置加速
sudo mkdir -p /etc/docker

sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://6ub68k8t.mirror.aliyuncs.com"]
}
EOF

sudo systemctl daemon-reload

sudo systemctl restart docker
```



### 3.run的流程和Docker的原理

#### 1.run的过程

![image-20210712205120137](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210712205120.png)

#### 2.底层原理

Docker是怎么工作的。

Docker是一个Client-Server结构的系统，Docker的守护进程运行在主机上，通过Socket从客户端访问。

Docker-Server接受到Docker-Client的指令，就会执行命令

![image-20210712205803966](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210712205804.png)



> Docker为什么比VM快?

1.Docker有着比虚拟机更少的抽象层

![image-20210712205909960](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210712205910.png)

2.docker利用的宿主机的内核，VM需要Guest OS

docker启动不需要加载一个操作系统的内核直接利用宿主机的操作系统，启动很快，虚拟机启动需要先加载GuestOS，很慢



### 3.常用命令

#### 1.帮助命令

```bash
docker version   #版本信息
docker info     #更详细的信息
docker --help    #查看docker所有的命令
docker 命令 --help
```

#### 2.生命周期

```bash
systemctl stop docker.service
systemctl start docker.service
systemctl restart docker.service
systemctl status docker.service



docker pull xxx   #拉取镜像

docker tag [image id] [name]:[版本]   #给指定版本号的镜像修改名字和版本名。image id  通过docker image查询的
sudo docker run hello-world
```

> docker run命令详解

```bash
docker run -dit --privileged -p21:21 -p80:80 -p8080:8080 -p30000-30010:30000-30010 --name how2jtmall how2j/tmall:latest /usr/sbin/init
```

- docker run 运行一个镜像
- `-dit` 是 -d -i -t 缩写  ，
  - -d表示detach 后台运行 
  - -i表示提供交互的接口。 
  - -t表示提供一个tty 伪终端 与 -i配合。就可以通过 ssh 工具连接到 这个容器
- `--privileged` 启动容器的时候，把权限带进去。 这样才可以在容器里进行完整的操作
- `-p21:21` 第一个21，表示在CentOS 上开放21端口。 第二个21 表示在容器里开放21端口
- -p80:80 和 21一个道理  http
- -p8080:8080 和21 一个道理，8080是 CentOS 的端口，但是通过-p8080:8080 这么一映射，就访问到容器里的8080端口上的 tomcat了  ==》可以改成其他端口
- -p30000-30010 和21也是一个道理，这个是ftp用来传输数据的
- `--name` how2jtmall 给容器取了个名字，叫做 how2jtmall，方便后续管理
- how2j/tmall:latest                      `how2j/tmall`就是镜像的名称。 latest是版本号
- /usr/sbin/init:       表示启动后运行的程序，即通过这个命令做初始化

> 启动容器之后，就能进入容器

```bash
docker exec -it how2jtmall /bin/bash
```

然后就能在容器里面像linux一样操作了

仓库： 别人做好的现成的镜像，都放在仓库里
镜像： 自己要用哪个镜像，就先拉到本地来。镜像就相当于还没激活的容器。
容器： 容器就是跑起来的镜像，就是一个完整的工作环境



#### 2.镜像命令

```bash
docker images  #查看下载到本地的镜像
	#可选项
	-a #列出所有的镜像
	-q #只显示镜像的id

docker search  xx   #在docker的仓库中找到xx镜像
	-filter=stars=3000  #查找stars大于3000的，其他的被过滤了

#：8.0是指定了版本
docker pull tomcat:8.0    #拉取镜像，下载
docker push     #把镜像提交到仓库

#运行  ，--rm指的是如果容器已经存在了，自动删除
docker run -it --rm -p 8888:8080 tomcat:8.0


#删除镜像，但是必须先删除容器之后才能删除镜像 rmi：remove image
docker rmi docker.io/tomcat:8.0
#删除所有镜像
docker rmi $(docker images -q)


#对镜像进行标记
docker tag docker.io/tomcat:8.0 docker.io/mytomcat:8.0
```

![image-20210712211217514](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210712211217.png)

#### 3.容器管理

```bash
docker run     #运行容器，前面有讲参数配置
docker run -it  xxx /bin/bash  #运行并进入容器 
#退出容器，关闭运行
exit
#退出容器，容器不停止运行
ctrl + P + Q
#进入容器，后面的是容器ID，用docker ps查出来 ,
docker attach c0d5cf1f16ff
docker exec -it how2jtmall或者容器id /bin/bash   #进入容器


--- attach进入容器正在执行的终端
--- exec 是进入容器之后打开一个新的中断，就跟ssh一样


docker commit how2jtmall how2j/tmall:now  #把容器变成镜像



------容器的生命周期管理 ---
暂停：docker pause
恢复：docker unpause
停止：docker stop
开始：docker start
杀死：docker kill
------


docker ps -a    #查询所有的容器
  		-n=?    #显示最近创建的容器
  		-q		#只显示容器的编号
  		
docker ps    #查询 run 状态的和 pause 状态的，stop的不会出现
docker inspect how2jtmall  #检查容器里面的信息
docker rm how2jtmall   #删除容器，但是在运行中的容器是不能删除的，要先stop,然后再删除。
docker rm `docker ps -a -q` -f   #删除所有容器
```

#### 4.常用其他命令

![image-20210712213035667](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210712213035.png)

![image-20210712215356391](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210712215356.png)



> 查看容器中进程信息

```bash
docker top  容器id
```

>查看镜像的元数据

```bash
docker inspect 容器ID
```

> 容器拷贝文件到主机

```bash
#在容器的home 文件夹下面创建test.java文件

#在主机运行
docker cp c0d5cf1f16ff:/home/test.java /home

#就可以拷贝文件出来了
```

### 4、作业联系

#### 1.安装nginx

1.下载nginx的镜像

```bash
docker pull nginx
docker run -d --name nginx01 -p 3344:80 nginx
```

端口映射将外网的3344端口，映射到容器里面的80端口

测试：  `服务器ip:3344`

#### 2.tomcat

```bash
docker run -it --rm  tomcat:9.0   #--rm 用完镜像就删除了，测试用的

docker pull tomcat:9.0

docker run -d -p 8081:8080 --name tomcat01 tomcat:9.0  

#有问题
这个tomcat里面是最小的能运行的，所以网页都没有
```



#### 3.其他

```bash
docker stats   #查看容器占用内存的大小

#修改配置文件，增加内存限制


```

### 5、可视化

- portainer  
- Rancher(CI/CD用)

#### 1.portainer  

Docker的图形化界面管理工具！提供后台面板给我们这操作

```bash
docker pull docker.io/portainer/portainer


docker run -d -p 9000:9000 \
--restart=always \
-v /var/run/docker.sock:/var/run/docker.sock \
--name prtainer-test \
docker.io/portainer/portainer
```

### 6、Docker镜像讲解

#### 1.镜像是什么

![image-20210713102345042](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210713102345.png)

#### 2.镜像加载原理

> 联合文件系统Union FS



> Docker 镜像加载原理

![image-20210713102737975](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210713102738.png)

#### 3.分层原理

自己去看网上的 讲解



#### 4.commit镜像

```bash
docker commit   #提交容器
docker commit -m="提交的信息"  -a="作者" 容器ID  目标镜像名:[TAG]


#这个容器tomcat 修改了，
docker commit -a="xuying" -m="add webapps" 5b08614d4809 tomcat-xy:1.0

docker images #发现多了一个镜像

```

![image-20210713141301520](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210713141301.png)

### 7、容器数据卷

#### 1.是什么？

容器之间的数据共享技术。  镜像容器被删了，数据就没了 - -》 但是数据我们不能丢失比如数据库里的数据。



数据共享技术，将Docker容器产生的数据，同步到本地，卷技术，目录的挂载（将容器的目录，挂载到Linux上面）

**容器的持久化和同步操作！容器间也可以数据共享**

#### 2.如何使用

> 直接使用命令挂载 -v

```bash
docker run -it -v 本地目录:容器目录

docker run -d -v /home/test:/home --name tomcat03 tomcat:9.0


```

挂载之后，在容器内部home 目录下，删除添加文件，本地/home/test下会进行同步操作

反过来，本地/home/test添加删除，容器里面的home也是进行同步操作

#### 3.mysql挂载

```bash
docker pull mysql
docker run -d -p 8811:3306 -v /home/mysql/conf:/etc/mysql/conf.d -v /home/mysql/data:/var/lib/mysql  -e MYSQL_ROOT_PASSWORD=admin --name mysql01 mysql:5.7
```

`-e` 配置环境，这里配置的是密码

#### 4.具名挂载和匿名挂载

```bash
#匿名挂载
-v  容器目录   #不指定主机目录

docker volume ls 

#具名
-v  挂载的名字(这里是名字不是主机的目录):容器目录


docker volume inspect 卷的名字  # 就能知道位置
```

![image-20210713151101670](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210713151101.png)

#### 5、初识DockerFile

dockerfile 用来构建docker镜像的构建文件，命令脚本。

通过脚本可以生成镜像，镜像是一层一层的，脚本一个一个

```dockerfile
FROM centos                   
VOLUME ["/volume01","/volume02"]   #挂载
CMD echo "----------end------"
CMD /bin/bash
```



```bash
docker build -f dockerfile1 -t xuying-centos:1.0 . # .表示当前目录下
```

![image-20210714093134933](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210714093135.png)



```bash
docker run --name xuyingtest2  -it xuying-centos:1.0
```





![image-20210714095311546](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210714095311.png)



![image-20210714095250559](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210714095250.png)

#### 6、容器数据卷

多个容器数据同步

![image-20210714100108954](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210714100109.png)





```bash
docker run -it --name xuying01   镜像ID

docker run -it --name xuying02 --volumes-from xuying01   镜像ID
```

这里的两个容器都挂载到宿主机的同一位置。然后修改目录的文件**，另一个容器也同步修改**

删除其中一个容器，另一个容器的数据不受影响

**硬链接**？？？

数据卷的生命周期，一直持续到没有容器使用为止(就是没有容器使用了，就删除了)

如果使用-v 挂载到本地，即使删除容器，数据也不会被删除

### 8、Dockerfile

![image-20210714102748955](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210714102749.png)

官方的镜像很多都是基础包，很多功能都没有。我们通常构建自己的镜像

#### 1.构建过程

![image-20210714103204944](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210714103205.png)

docker镜像成了企业交付的标准



dockerFile：构建文件，定义了一切步骤，源文件

dockerImage：dockerfile构建的镜像，最终发布和运行的产品

docker容器：容器就是镜像运行起来的服务器

#### 2.dockerfile指令

![image-20210714103442527](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210714103442.png)



```shell
FROM    	#基础镜像
MAINTAINER	#镜像谁写的，姓名+邮箱
RUN			#镜像构建的时候需要运行的命令
ADD			#步骤,tomcat镜像 ，加进去。tocat的压缩包
WORKDIR     #镜像的工作目录
VOLUME		#挂载的目录
EXPOSE		#暴露端口配置  -p
CMD 		#指定容器启动要运行的命令,只有最后一个生效，可以被替代
ENTRYPOINT	#指定容器启动运行的命令，可以追加
ONBUILD     #看下文
COPY  	 	#文件拷贝到镜像中
ENV			#构建的时候设置环境变量
```

> ONBUILD

```dockerfile
#test先写一个dockerfile
FROM ubuntu
MAINTAINER hello
ONBUILD RUN mkdir mydir

#把上面的build 名字叫image，不会触发ONBUILD指令，也就是没有目录


---
#第二个dockerfile
FROM image   # 这里继承了上面的构建镜像
MAINTAINER hello

#build第二个dockerfile，就会在最开始执行 ONBUILD指令，创建mydir目录
```

#### 3、练习

在基础centos中，增加功能

![image-20210714105449382](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210714105449.png)



```bash
docker history  #查看构建日志
```



> CMD 和 ENTRYPOINT的区别

dockerfile

```dockerfile
FROM centos
CMD echo "hello,word"
CMD ["ls","-1"]
```

```
docker build -f dockerEntryPoint（dockerfile文件） -t testentrypoint .
```





打包运行

第一个测试CMD只运行了最后一次的

![image-20210715091518276](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715091518.png)

第二个测试加参数，-l替换了CMD

![image-20210715091551330](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715091551.png)





entryPoint

```dockerfile
FROM centos
ENTRYPOINT ["echo","hello"]
ENTRYPOINT ["ls","-a"]
```

运行结果如下，加上-l之后变成参数了  。。==覆盖这个没测试好==



![image-20210715092528873](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715092528.png)

#### 4、Tomcat镜像



dockerfile文件命名：Dockerfile (官方的)  就可以不用指定-f文件，会自动在当前目录下查找这个文件



1.准备镜像文件：tomcat 压缩包，jdk压缩包





![image-20210715093659796](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715093659.png)



#### 5、提交

先login in  自己的账号









![image-20210715100152852](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715100152.png)

#### 6、小结

全流程

![image-20210715100458550](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210715100458.png)





## Docker配置环境



#### 1.mysql

```bash
docker run --name mysql-xy -e MYSQL_ROOT_PASSWORD=x.com520 -d  -p 8200:3306 09361feeb475(镜像id)
```

#### 2、RabbitMQ



端口号： 8300 是管理器的

8301：是rabbitmq的

然后虚拟容器是：my_vhost

```bash
docker search rabbitmq:management #需要拉这个镜像
```



```bash
docker run -d --name rabbitmq-xy -p 8301:5672 -p 8300:15672 -v `pwd`/data:/var/lib/rabbitmq --hostname myRabbit -e RABBITMQ_DEFAULT_VHOST=my_vhost  -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=admin df80af9ca0c9
```

`无挂载卷`

```bash
docker run -d --name rabbitmq-xy -p 8301:5672 -p 8300:15672  --hostname myRabbit -e RABBITMQ_DEFAULT_VHOST=my_vhost  -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=admin df80af9ca0c9
```



#### 3.Zookeeper

```java
docker run -d -p 8400:2181  --name zookeeper xxx
```

