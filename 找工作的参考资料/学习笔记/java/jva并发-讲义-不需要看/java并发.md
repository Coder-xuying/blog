## 并发

#### 3.进程线程

#### 1。线程运行

```bash
# linux里面查看进程
ps -ef | grep java

#java 提供查看进程id
jps

#查看java进程内线程信息的
top -H -p 进程ID

#java提供的查看线程的信息（更加详细），但是是以快照的形式，只抓取那一瞬间
jstack #进程ID
```



> jconsole



在运行的时候需要进行配置 `java -jar xxxxxxxx`

远程图形化监控服务 - 对java进程监控

![image-20211014182844272](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20211014182851.png)