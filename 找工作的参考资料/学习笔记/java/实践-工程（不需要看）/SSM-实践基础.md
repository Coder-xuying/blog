## 1、Mybatis

### 1.简介

#### 1.1 什么是Mybatis

是一个优秀的持久层框架。

maven库

```xml
<!-- https://mvnrepository.com/artifact/org.mybatis/mybatis -->
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.5.2</version>
</dependency>
```

#### 1.2 为什么需要mybatis

- 方便，容易上手
- 传统的jdbc太复杂了。简化。框架，只用填一些东西就行

### 2.第一个Mybatis程序

思路：搭建环境-》导入Mybatis-》编写代码-》测试



1. 创建一个maven项目，删去src，变成一个空的项目(父项目)

2. 导入依赖的库.还有资源过滤的配置，也就是Build那块，必须要有否则后面会找不到配置文件

   ```xml
   <dependencies>
       <dependency>
           <groupId>org.mybatis</groupId>
           <artifactId>mybatis</artifactId>
           <version>3.5.2</version>
       </dependency>
       <dependency>
           <groupId>mysql</groupId>
           <artifactId>mysql-connector-java</artifactId>
           <version>8.0.21</version>
       </dependency>
   
       <dependency>
           <groupId>junit</groupId>
           <artifactId>junit</artifactId>
           <version>4.13.2</version>
       </dependency>
       
       <dependency>
           <groupId>org.projectlombok</groupId>
           <artifactId>lombok</artifactId>
           <version>1.18.20</version>
       </dependency>
   </dependencies>
   
   <build>
       <resources>
           <resource>
               <directory>src/main/java</directory>
               <includes>
                   <include>**/*.xml</include>
               </includes>
           </resource>
       </resources>
   </build>
   ```

3. 创建一个模块

   1. 编写配置文件mybatis-config.xml

      ```xml
      <?xml version="1.0" encoding="UTF-8" ?>
      <!DOCTYPE configuration
              PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
              "http://mybatis.org/dtd/mybatis-3-config.dtd">
      
      
      <!--核心配置文件-->
      <configuration>
          
          <properties resource="db.properties">
          </properties>
      
      
          <environments default="development">
              <environment id="development">
                  <transactionManager type="JDBC"/>
      
                  <dataSource type="POOLED" >
                      <property name="driver" value="${driver}"/>
                      <property name="url" value="${url}"/>
                      <property name="username" value="${username}"/>
                      <property name="password" value="${password}"/>
                  </dataSource>
              </environment>
          </environments>
      
      
          <mappers>
              <mapper resource="com/xy/dao/userMapper.xml" />
          </mappers>
      </configuration>
      ```

   2. dp.properties

      ```properties
      #db.properties文件的内容
      driver=com.mysql.cj.jdbc.Driver
      url=jdbc:mysql://localhost:3306/mybatis?serverTimezone=UTC&useSSL=true&useUnicode=true&characterEncoding=UTF-8
      username=root
      password=root
      ```

   3. 创建实体类User

      ```java
      package com.xy.pojo;
      
      import lombok.AllArgsConstructor;
      import lombok.Data;
      import lombok.NoArgsConstructor;
      
      @Data
      @NoArgsConstructor
      @AllArgsConstructor
      public class User {
          private int id;
          private String name;
          private String pwd;
      }
      ```

   4. 创建mybatis工具类MybatisUtil.java

      ```java
      package com.xy.utils;
      
      import org.apache.ibatis.io.Resources;
      import org.apache.ibatis.session.SqlSession;
      import org.apache.ibatis.session.SqlSessionFactory;
      import org.apache.ibatis.session.SqlSessionFactoryBuilder;
      
      import java.io.IOException;
      import java.io.InputStream;
      
      public class MybatisUtil {
          private static SqlSessionFactory sqlSessionFactory;
      
      
          static{
              try {
                  //使用Mybatis第一步：获取sqlSessionFactory对象
                  String resource = "mybatis-config.xml";
                  InputStream inputStream = Resources.getResourceAsStream(resource);
                  sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
              } catch (IOException e) {
                  e.printStackTrace();
              }
      
          }
      
          //既然有了 SqlSessionFactory，顾名思义，我们就可以从中获得 SqlSession 的实例了。
          // SqlSession 完全包含了面向数据库执行 SQL 命令所需的所有方法。
          public static SqlSession getSqlSession(){
              return sqlSessionFactory.openSession();
          }
      }
      ```

   5. Dao接口

      ```java
      public interface UserDao {
          List<User> getUserList();
      }
      ```

   6. userMapper.xml 实现接口

      ```xml
      <?xml version="1.0" encoding="UTF-8" ?>
      <!DOCTYPE mapper
              PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
              "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
      <!--namespace=绑定一个对应的Dao/Mapper接口-->
      <mapper namespace="com.xy.dao.UserDao">
      
          <!--select查询语句,这里的id就相当于impl实现的方法-->
          <select id="getUserList" resultType="com.xy.pojo.User">
             select * from mybatis.user
         </select>
      
      </mapper>
      ```

4. 编写代码测试

   ```java
   package com.xy.dao;
   
   import com.xy.pojo.User;
   import com.xy.utils.MybatisUtil;
   import org.apache.ibatis.session.SqlSession;
   import org.junit.Test;
   
   import java.util.List;
   
   public class UserDaoTest {
       private static SqlSession sqlSession = MybatisUtil.getSqlSession();
   
       @Test
       public void test(){
           UserDao mapper = sqlSession.getMapper(UserDao.class);
           List<User> userList = mapper.getUserList();
           for (User user : userList) {
               System.out.println(user);
           }
   
           sqlSession.close();
       }
   }
   ```

### 3、CURD

#### 1、select

选择，查询语句

- id就是:namespace中的方法名
- resultType：sql语句执行的返回
- 

#### 4、Map

```java
//万能的Map
int addUser2(Map<String,Object> map);
```

```xml
<!--对象中的属性，可以直接取出来    传递map的key-->
<insert id="addUser" parameterType="map">
    insert into mybatis.user (id, pwd) values (#{userid},#{passWord});
</insert>
```

```java
@Test
public void addUser2(){
    SqlSession sqlSession = MybatisUtils.getSqlSession();

    UserMapper mapper = sqlSession.getMapper(UserMapper.class);

    Map<String, Object> map = new HashMap<String, Object>();

    map.put("userid",5);
    map.put("passWord","2222333");

    mapper.addUser2(map);

    sqlSession.close();
}
```

Map传递参数，直接在sql中取出key即可！    【parameterType="map"】

对象传递参数，直接在sql中取对象的属性即可！【parameterType="对象的类"】

只有一个基本类型参数的情况下，可以直接在sql中取到！

多个参数用Map，或者注解！

### 4、配置解析

#### 1.核心配置文件

mybatis-config.xml  里面的标签页需要**按照**下面这个**顺序**写，不然会报错

- **properties（属性）**
  **settings（设置）**
  **typeAliases（类型别名）**
  typeHandlers（类型处理器）
  objectFactory（对象工厂）
  plugins（插件）
  **environments（环境配置）**
  **environment（环境变量）**
  transactionManager（事务管理器）
  dataSource（数据源）
  databaseIdProvider（数据库厂商标识）
  **mappers（映射器）**

> properties

```xml
<!--引入外部配置文件-->
<properties resource="db.properties">
    <property name="username" value="root"/>
    <property name="pwd" value="11111"/>
</properties>
```

- 可以直接引入外部文件
- 可以在其中增加一些属性配置
- 如果存在同一个字段，**优先使用外部配置文件的**！

> typeAliases

- 类型别名是为 Java 类型设置一个短的名字。

- 于用来减少类完全限定名的冗余。

- 方式一--给每个类都取一个别名，这可以自己定制别名

  ```xml
  <!--可以给实体类起别名-->
  <typeAliases>
      <!--引入外部配置文件-->
      <typeAlias type="com.kuang.pojo.User" alias="User"/>
  </typeAliases>
  ```

- 方式二-----扫描一个包。默认别名就为**这个类的类名，首字母小写**

  ```xml
  <!--可以给实体类起别名-->
  <typeAliases>
      <package name="com.kuang.pojo"/>
  </typeAliases>
  ```

- 类比较多的话，使用第二种比较方便

- 也可以使用注解指定别名    ==这里用的也是方式2，==可以自己**定制别名**

  ```java
  @Alias("user")
  public class User {
    
  }
  ```

> settings

这是 MyBatis 中极为重要的调整设置，它们会改变 MyBatis 的运行时行为

里面有很多，记一些比较重要的就行。

![image-20210527161455479](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210527161455.png)

```xml
<settings>
    <setting name="logImpl" value="LOG4J"/>
</settings>
```

> mappers

方法1 对每一个Mapper.xml进行注册

```xml
<mappers>
    <mapper resource="com/kuang/dao/UserMapper.xml"/>
</mappers>
```

方法2： 使用class文件绑定注册

```xml
<!--每一个Mapper.XML都需要在Mybatis核心配置文件中注册！-->
<mappers>
    <mapper class="com.kuang.dao.UserMapper"/>
</mappers>
```

注意点：

- **接口和他的Mapper配置文件必须同名！**   
- 接口和他的Mapper配置文件必须在同一个包下！

方式三：使用扫描包进行注入绑定

```xml
<!--每一个Mapper.XML都需要在Mybatis核心配置文件中注册！-->
<mappers>
    <package name="com.kuang.dao"/>
</mappers>
```

注意点：

- 接口和他的Mapper配置文件必须同名！
- 接口和他的Mapper配置文件必须在同一个包下！

**推荐使用第一种方式**，没有任何限制



> environments



#### 2.生命周期和作用域

生命周期，和作用域，是至关重要的，因为错误的使用会导致非常严重的**并发问题**。

>SqlSessionFactoryBuilder

- 一旦创建了 SqlSessionFactory，就不再需要它了
- 局部变量

>SqlSessionFactory

- 说白了就是可以想象为 ：数据库连接池
- SqlSessionFactory 一旦被创建就应该在应用的运行期间一直存在，**没有任何理由丢弃它或重新创建另一个实例。** 
- SqlSessionFactory 的最佳作用域是应用作用域。 程序开始就开始，程序结束就结束
- 使用**单例模式**或者静态单例模式。 
- 可以多次创建，但是浪费资源。

> SqlSeesion

- 每个线程都应该有它自己的 SqlSession 实例。
- SqlSession 的实例不是线程安全的，因此是不能被共享的，所以它的最佳的作用域是请求或方法作用域。 
- 绝对不能将 SqlSession 实例的引用放在一个类的静态域，甚至一个类的实例变量也不行。 
- 用完之后，**就关闭它**。

![image-20210527202153758](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210527202153.png)

### 5、ResultMap(字段不一致问题)

问题出现的测试

```java
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    private int id;
    private String name;
    private String password;  //实体类是password
}
```

![image-20210527202919740](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210527202919.png)

![image-20210527202933901](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210527202933.png)

查询之后password是null

> 原因

```xml
 <select id="getUserById" resultType="com.xy.pojo.User" parameterType="int">
    select * from mybatis.user where id = #{id}
</select>
```

这是我们的查询语句，相当于 `select id,name,password from user where xxxx`

可以看出来这里是mybatis自动进行了一个上述的转换工作，但是因为数据库里的数据是pwd和这里的字段名不一致，就显示为null。一个解决办法就是sql语句起别名`select id,name,password as pwd`就解决了

> ResultMap解决上述问题

```xml
<!--结果集映射   ，解决数据库和实体类名称不匹配-->
<resultMap id="UserMap" type="User">
    <!--column是数据库中的字段，property对应实体类中的属性-->
    <result column="id" property="id"/>
    <result column="name" property="name"/>
    <result column="pwd" property="password"/>
</resultMap>
```

==column是数据库中的字段，property对应实体类中的属性== 就能将数据库中查询出来的操作映射到实体类中的属性

- `resultMap` 元素是 MyBatis 中最重要最强大的元素
- ResultMap 的设计思想是，对于简单的语句根本不需要配置显式的结果映射，**而对于复杂一点的语句只需要描述它们的关系就行了。（后述会讲）**
- `ResultMap` 最优秀的地方在于，虽然你已经对它相当了解了，但是根本就不需要显式地用到他们。(只需要在需要映射的地方使用)

### 6、日志

#### 1.日志工厂

如果一个数据库操作出现异常，需要排错，使用日志来当助手。

之前都是使用sout输出，现在可以使用日志来实现。

- LOG4J  【掌握】
- LOG4J2
- JDK_LOGGING
- STDOUT_LOGGING   【掌握】
- NO_LOGGING

#### 2. STDOUT_LOGGING   

mybatis-config.xml

```xml
<settings>
    <setting name="logImpl" value="STDOUT_LOGGING"/>
</settings>
```

上面的设置一点也不能错，空格、大小写不能错

这是标准日志，不需要导

> 加了STDOUT_LOGGING日志之后，就多了一些内容

这些就是我们对数据库的操作

![image-20210528143802911](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210528143803.png)

![image-20210528143809298](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210528143809.png)

#### 3.LOG4J

导入包

```xml
<dependency>
    <groupId>log4j</groupId>
    <artifactId>log4j</artifactId>
    <version>1.2.17</version>
</dependency>
```

配置

```xml
<settings>
    <setting name="logImpl" value="LOG4J"/>
</settings>
```

log4j可以通过添加一个**配置文件**，来控制日志的格式和定义日志信息的级别

`log4j.properties`如下，这个值要在resources中添加进去就可以用了

```properties
#将等级为DEBUG的日志信息输出到console和file这两个目的地，console和file的定义在下面的代码
log4j.rootLogger=DEBUG,console,file

#控制台输出的相关设置
log4j.appender.console = org.apache.log4j.ConsoleAppender
log4j.appender.console.Target = System.out
log4j.appender.console.Threshold=DEBUG
log4j.appender.console.layout = org.apache.log4j.PatternLayout
log4j.appender.console.layout.ConversionPattern=[%c]-%m%n

#文件输出的相关设置
log4j.appender.file = org.apache.log4j.RollingFileAppender
log4j.appender.file.File=./log/kuang.log
log4j.appender.file.MaxFileSize=10mb
log4j.appender.file.Threshold=DEBUG
log4j.appender.file.layout=org.apache.log4j.PatternLayout
log4j.appender.file.layout.ConversionPattern=[%p][%d{yy-MM-dd}][%c]%m%n

#日志输出级别
log4j.logger.org.mybatis=DEBUG
log4j.logger.java.sql=DEBUG
log4j.logger.java.sql.Statement=DEBUG
log4j.logger.java.sql.ResultSet=DEBUG
log4j.logger.java.sql.PreparedStatement=DEBUG
```

然后可以直接使用了，、

>

**简单使用**

1. 在要使用Log4j 的类中，导入包  import org.apache.log4j.Logger;

2. 日志对象，参数为当前类的class

   ```java
   static Logger logger = Logger.getLogger(UserDaoTest.class);
   ```

3. 日志级别

   ```java
   logger.info("info:进入了testLog4j");
   logger.debug("debug:进入了testLog4j");
   logger.error("error:进入了testLog4j");
   ```

### 7、分页

为什么要分页？  **减少数据的处理量**

#### 1.Mybatis实现分页

```sql
SELECT * from user limit startIndex,pageSize;
SELECT * from user limit 0,3; // 从0开始，显示三个数据
```

1. 接口

   ```java
   //分页
   List<User> getUserByLimit(Map<String,Integer> map);
   ```

2. Mapper.xml

   ```xml
   <!--//分页-->
   <select id="getUserByLimit" parameterType="map" resultType="user">
       select * from  mybatis.user limit #{startIndex},#{pageSize}
   </select>
   ```

3. 测试

   ```java
   @Test
   public void getUserByLimit(){
       // mapper通过之前的mybatis工具类得到的
   	HashMap<String, Integer> map = new HashMap<String, Integer>();
       map.put("startIndex",1);
       map.put("pageSize",2);
   
       List<User> userList =  mapper.getUserByLimit(map);
       for (User user : userList) {
       System.out.println(user);
       }
       sqlSession.close();
   }
   ```

   

### 8、使用注解开发

#### 1、使用注解开发

```java
@Select("select * from user")
List<User> getUsers();
```

绑定配置文件

```xml
<!--绑定接口-->
<mappers>
    <mapper class="com.kuang.dao.UserMapper"/>
</mappers>
```

测试即可

#### 2、CURD

我们可以在工具类创建的时候实现自动提交事务！

```java
public static SqlSession  getSqlSession(){
    return sqlSessionFactory.openSession(true);
}
```

```java
public interface UserMapper {

    @Select("select * from user")
    List<User> getUsers();

    // 方法存在多个参数，所有的参数前面必须加上 @Param("id")注解
    @Select("select * from user where id = #{id}")
    User getUserByID(@Param("id") int id);


    @Insert("insert into user(id,name,pwd) values (#{id},#{name},#{password})")
    int addUser(User user);

    
    @Update("update user set name=#{name},pwd=#{password} where id = #{id}")
    int updateUser(User user);

    //@Param("uid")  sql语句里取的值是从这里的名字
    @Delete("delete from user where id = #{uid}")
    int deleteUser(@Param("uid") int id);
}
```

**关于@Param() 注解**

- 基本类型的参数或者String类型，需要加上
- 引用类型不需要加
- 如果只有一个基本类型的话，可以忽略，但是建议大家都加上！
- 我们在SQL中引用的就是我们这里的 @Param() 中设定的属性名！



> **#{}     ${} 区别**

默认情况下,使用#{}语法,MyBatis会产生PreparedStatement语句中，并且安全的设置PreparedStatement参数，这个过程中MyBatis会进行必要的安全检查和转义。

说明：

1. `#`将传入的数据都当成一个字符串，**会对自动传入的数据加一个双引号**。如：order by #{user_id}，如果传入的值是 name , 那么解析成sql时的值为order by “name”, 如果传入的值是id，则解析成的sql为order by “id”.
2. `$`  将传入的数据**直接显示生成在sql中**。如：order by ${user_id}，如果传入的值是name, 那么解析成sql时的值为order by name, 如果传入的值是id，则解析成的sql为order by id.

综上所述,`$ {}`方式会引发SQL注入的问题、同时也会影响SQL语句的预编译，所以从安全性和性能的角度出发，能使用`#{}`的情况下就不要使用 `${}`。

### 9、复杂关系查询

#### 1.多对一

多个学生对应一个老师的例子

- 对于学生而言，**关联**，多个学生关联一个老师
- 对于老师而言是**集合**，一个老师有很多学生

创建环境

**学生表** （这里我用的是User）和**老师表**  学生里用tid关联teacher

> 实体类

```java
package com.xy.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor

public class User {
    private int id;
    private String name;
    private String password;
    //关联老师
    private Teacher teacher;
}
```

```java
package com.xy.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Teacher {
    private int id;
    private String name;
}
```

> mapper

`UserMapper.java`

```java
package com.xy.dao;

import com.xy.pojo.User;
import org.apache.ibatis.annotations.Select;

import java.util.List;
import java.util.Map;

public interface UserMapper {
    List<User> getStudent();
}

```



`UserMapper.xml `两种写法

- 1.按照查询嵌套

  ```xml
  <!--
      思路:
          1. 查询所有的学生信息
          2. 根据查询出来的学生的tid，寻找对应的老师！  子查询
   -->
  <select id="getStudent" resultMap="StudentTeacher">
      select * from user
  </select>
  
  <resultMap id="StudentTeacher" type="Student">
      <result property="id" column="id"/>
      <result property="name" column="name"/>
      <!--复杂的属性，我们需要单独处理 对象： association 集合： collection -->
      <association property="teacher" column="tid" javaType="teacher" select="getTeacher"/>
  </resultMap>
  
  <select id="getTeacher" resultType="Teacher">
      select * from teacher where id = #{id}
  </select>  
  ```

- 2、按照结果嵌套查询

  ```xml
  <?xml version="1.0" encoding="UTF-8" ?>
  <!DOCTYPE mapper
          PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
          "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
  <mapper namespace="com.xy.dao.UserMapper">
      
      <resultMap id="StudentByTeacher" type="user">
          <result property="id" column="sid"/>
          <result property="name" column="sname"/>
          <result property="password" column="pwd"/>
          <association property="teacher"  javaType="teacher">
              <result property="id" column="tid"/>
              <result property="name" column="tname"/>
          </association>
      </resultMap>
  
      <select id="getStudent" resultMap="StudentByTeacher">
          select s.id sid,s.name sname,pwd,t.id tid,t.name tname  from user s,teacher t where s.tid = t.id
      </select>
  </mapper>
  ```

对应mysql的两种查询

- 子查询 -- 方法1
- 连表查询 -- 方法2

#### 2.一对多

```xml
<resultMap id="teacher_student" type="teacher">
    <result property="id" column="tid"/>
    <result property="name" column="tname"/>
    <!--        学生是一个集合-->
    <collection property="students" ofType="user">
        <result property="id" column="sid"/>
        <result property="name" column="sname"/>
        <result property="tid" column="tid"/>
        <result property="password" column="pwd"/>
    </collection>
</resultMap>

<!--    查询指定id的老师的学生-->
<select id="getTeacher" resultMap="teacher_student">
    select  s.id sid,s.name sname,s.tid ,pwd , t.id tid ,t.name tname from user s,teacher t where s.tid = tid and tid =#{id}
</select>
```

#### 3 总结

- 关联 association
- 集合 collection
- javaType 指定实体类中属性的类型
- ofType 指定映射到List里的类型。

### 10、动态SQL(跳过，之后可以回看)

#### 11、缓存

查询，**连接数据库耗费资源**

 一次查询的结果，暂存在一个可以直接取到的地方--**内存**

再次相同数据的时候，直接走缓存，不走数据



1. 为什么使用缓存？

   - 减少和数据库的交互次数，减少系统开销，提高系统效率。解决了高并发系统的性能问题。
2. 什么样的数据能使用缓存？

   - 经常查询并且不经常改变的数据。【可以使用缓存】



MyBatis系统中默认定义了两级缓存：**一级缓存**和**二级缓存**

- 默认情况下，开启一级缓存。（SqlSession级别的缓存，也称为本地缓存）

- 二级缓存需要手动开启和配置，他是基于namespace级别的缓存。

- 为了提高扩展性，MyBatis定义了缓存接口Cache。我们可以通过实现Cache接口来自定义二级缓存

##### 1.一级缓存

一级缓存也叫本地缓存：  SqlSession

- 与数据库同一次会话期间查询到的数据会放在本地缓存中。
- 以后如果需要获取相同的数据，直接从缓存中拿，没必须再去查询数据库；

> 测试

需要开启日志  

测试代码

```java
public class test {

   static SqlSession sqlSession = MybatisUtil.getSqlSession();
   static UserMapper userMapper = sqlSession.getMapper(UserMapper.class);

    @Test
    public void test(){
        User user = userMapper.getUserById(1);
        System.out.println(user);
        System.out.println( "=========================");
        
        User user2 = userMapper.getUserById(1);
        System.out.println(user2);
        sqlSession.close();
    }
}
```

运行结果

![image-20210530195209438](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210530195209.png)

可以看到只查询了一次

>缓存失效的情况

- 1、查询不同的东西

```java
public class test {

   static SqlSession sqlSession = MybatisUtil.getSqlSession();
   static UserMapper userMapper = sqlSession.getMapper(UserMapper.class);

    @Test
    public void test(){
        User user = userMapper.getUserById(1);
        System.out.println(user);
        System.out.println( "=========================");
        
        User user2 = userMapper.getUserById(2);
        System.out.println(user2);
        sqlSession.close();
    }
}
```

![image-20210530195313666](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210530195313.png)

- 2、增删改操作，可能会改变原来的数据，所以必定会刷新缓存！

  ![image-20210530195644320](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210530195644.png)

- 3、查询不同的Mapper.xml

- 4、手动清理缓存！

  ```java
   User user = userMapper.getUserById(1);
          System.out.println(user);
          
          sqlSession.clearCache();
          System.out.println( "=========================");
  
          User user2 = userMapper.getUserById(1);
          System.out.println(user2);
          sqlSession.close();
  ```

  ![image-20210530195815902](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210530195816.png)

> 小结

**一级缓存默认是开启的,无法关闭**，只在一次SqlSession中有效，也就是拿到连接到关闭连接这个区间段！

**一级缓存就是一个Map。**

##### 2.二级缓存

- 二级缓存也叫全局缓存，一级缓存作用域太低了，所以诞生了二级缓存
- 基于namespace级别的缓存，一个名称空间，对应一个二级缓存；
- 工作机制
  - 一个会话查询一条数据，这个数据就会被放在当前会话的一级缓存中；
  - 如果当前会话关闭了，这个会话对应的一级缓存就没了；但是我们想要的是，会话关闭了，一级缓存中的数据被保存到二级缓存中；
  - 新的会话查询信息，就可以从二级缓存中获取内容；
  - 不同的mapper查出的数据会放在自己对应的缓存（map）中；

> 步骤

1.开启缓存

```xml
<!--显示的开启全局缓存-->
<setting name="cacheEnabled" value="true"/>
```

2.在需要使用二级缓存的Mapper中开启

```xml
<!--在当前Mapper.xml中使用二级缓存-->
<cache/>
```

也可以自定义一些参数，如下图

![image-20210530202218473](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210530202218.png)

3.测试

1. 问题

   如果没有下面的readOnly就会报错-- **需要序列化对象**

   `Caused by: java.io.NotSerializableException: com.kuang.pojo.User`

   ```xml
    <cache readOnly="true"/>
   ```

   

> 小结

小结：

- 只要开启了二级缓存，在同一个Mapper下就有效
- 所有的数据都会先放在一级缓存中；
- 只有当会话提交，或者关闭的时候，才会提交到二级缓冲中！

![image-20210530203543964](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210530203544.png)

一级缓存关闭的时候，就把数据保存在二级缓存了。

查询顺序- 》先看二级缓存有没有，再看一级缓存，最后看数据库

##### 3.自定义缓存

Ehcache是一种广泛使用的开源Java**分布式缓存**。主要面向通用缓存

> 使用

导包

```xml
<!-- https://mvnrepository.com/artifact/org.mybatis.caches/mybatis-ehcache -->
<dependency>
    <groupId>org.mybatis.caches</groupId>
    <artifactId>mybatis-ehcache</artifactId>
    <version>1.1.0</version>
</dependency>
```

mapper中指定我们的ehcache

```xml
<!--在当前Mapper.xml中使用二级缓存-->
<cache type="org.mybatis.caches.ehcache.EhcacheCache"/>
```

**牛逼之处 **  ehcache.xml  可以定义配置文件，自定义策略，功能更强

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ehcache xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="http://ehcache.org/ehcache.xsd"
         updateCheck="false">
    <!--
       diskStore：为缓存路径，ehcache分为内存和磁盘两级，此属性定义磁盘的缓存位置。参数解释如下：
       user.home – 用户主目录
       user.dir  – 用户当前工作目录
       java.io.tmpdir – 默认临时文件路径
     -->
    <diskStore path="./tmpdir/Tmp_EhCache"/>
    
    <defaultCache
            eternal="false"
            maxElementsInMemory="10000"
            overflowToDisk="false"
            diskPersistent="false"
            timeToIdleSeconds="1800"
            timeToLiveSeconds="259200"
            memoryStoreEvictionPolicy="LRU"/>
 
    <cache
            name="cloud_user"
            eternal="false"
            maxElementsInMemory="5000"
            overflowToDisk="false"
            diskPersistent="false"
            timeToIdleSeconds="1800"
            timeToLiveSeconds="1800"
            memoryStoreEvictionPolicy="LRU"/>
    <!--
       defaultCache：默认缓存策略，当ehcache找不到定义的缓存时，则使用这个缓存策略。只能定义一个。
     -->
    <!--
      name:缓存名称。
      maxElementsInMemory:缓存最大数目
      maxElementsOnDisk：硬盘最大缓存个数。
      eternal:对象是否永久有效，一但设置了，timeout将不起作用。
      overflowToDisk:是否保存到磁盘，当系统当机时
      timeToIdleSeconds:设置对象在失效前的允许闲置时间（单位：秒）。仅当eternal=false对象不是永久有效时使用，可选属性，默认值是0，也就是可闲置时间无穷大。
      timeToLiveSeconds:设置对象在失效前允许存活时间（单位：秒）。最大时间介于创建时间和失效时间之间。仅当eternal=false对象不是永久有效时使用，默认是0.，也就是对象存活时间无穷大。
      diskPersistent：是否缓存虚拟机重启期数据 Whether the disk store persists between restarts of the Virtual Machine. The default value is false.
      diskSpoolBufferSizeMB：这个参数设置DiskStore（磁盘缓存）的缓存区大小。默认是30MB。每个Cache都应该有自己的一个缓冲区。
      diskExpiryThreadIntervalSeconds：磁盘失效线程运行时间间隔，默认是120秒。
      memoryStoreEvictionPolicy：当达到maxElementsInMemory限制时，Ehcache将会根据指定的策略去清理内存。默认策略是LRU（最近最少使用）。你可以设置为FIFO（先进先出）或是LFU（较少使用）。
      clearOnFlush：内存数量最大时是否清除。
      memoryStoreEvictionPolicy:可选策略有：LRU（最近最少使用，默认策略）、FIFO（先进先出）、LFU（最少访问次数）。
      FIFO，first in first out，这个是大家最熟的，先进先出。
      LFU， Less Frequently Used，就是上面例子中使用的策略，直白一点就是讲一直以来最少被使用的。如上面所讲，缓存的元素有一个hit属性，hit值最小的将会被清出缓存。
      LRU，Least Recently Used，最近最少使用的，缓存的元素有一个时间戳，当缓存容量满了，而又需要腾出地方来缓存新的元素的时候，那么现有缓存元素中时间戳离当前时间最远的元素将被清出缓存。
   -->

</ehcache>

```

==自己也可以写缓存内==  只要继承Cache类就行

```java
package com.xy.utils;
import org.apache.ibatis.cache.Cache;

public class MyCache implements Cache {
    public String getId() {
        return null;
    }
    public void putObject(Object o, Object o1) {
    }
    public Object getObject(Object o) {
        return null;
    }
    public Object removeObject(Object o) {
        return null;
    }
    public void clear() {
    }
    public int getSize() {
        return 0;
    }
}
```



## 2、Spring

### 1.Spring概述

#### 1.1 Spring概述

1. Spring是一个开源框架 

2. Spring是一个**IOC**(DI)和**AOP**容器框架。

3. 支持事务的处理，对框架整合的支持。

4. Spring的优良特性

   1.  **非侵入式**：基于Spring开发的应用中的对象可以不依赖于Spring的API
   2.  **依赖注入**：DI——Dependency Injection，反转控制(IOC)最经典的实现。
   3.  **面向切面编程**：Aspect Oriented Programming——AOP
   4.  **容器**：Spring是一个容器，因为它包含并且管理应用对象的生命周期
   5.  **组件化**：Spring实现了使用简单的组件配置组合成一个复杂的应用。在 Spring 中可以使用XML和Java注解组合这些对象。

5. Spring模块

   > 每个模块的功能如下：

   - **核心容器**：核心容器提供 Spring 框架的基本功能。核心容器的主要组件是BeanFactory，它是工厂模式的实现。BeanFactory 使用*控制反转*（IOC） 模式将应用程序的配置和依赖性规范与实际的应用程序代码分开。
   - **Spring 上下文**：Spring 上下文是一个配置文件，向 Spring 框架提供上下文信息。Spring 上下文包括企业服务，例如 JNDI、EJB、电子邮件、国际化、校验和调度功能。
   - **Spring AOP**：通过配置管理特性，Spring AOP 模块直接将面向切面的编程功能 , 集成到了 Spring 框架中。所以，可以很容易地使 Spring 框架管理任何支持 AOP的对象。Spring AOP 模块为基于 Spring 的应用程序中的对象提供了事务管理服务。通过使用 Spring AOP，不用依赖组件，就可以将声明性事务管理集成到应用程序中。
   - **Spring DAO**：JDBC DAO 抽象层提供了有意义的异常层次结构，可用该结构来管理异常处理和不同数据库供应商抛出的错误消息。异常层次结构简化了错误处理，并且极大地降低了需要编写的异常代码数量（例如打开和关闭连接）。Spring DAO 的面向 JDBC 的异常遵从通用的 DAO 异常层次结构。
   - **Spring ORM**：Spring 框架插入了若干个 ORM 框架，从而提供了 ORM 的对象关系工具，其中包括 JDO、Hibernate 和 iBatis SQL Map。所有这些都遵从 Spring 的通用事务和 DAO 异常层次结构。
   - **Spring Web 模块**：Web 上下文模块建立在应用程序上下文模块之上，为基于 Web 的应用程序提供了上下文。所以，Spring 框架支持与 Jakarta Struts 的集成。Web 模块还简化了处理多部分请求以及将请求参数绑定到域对象的工作。
   - **Spring MVC 框架**：MVC 框架是一个全功能的构建 Web 应用程序的 MVC 实现。通过策略接口，MVC 框架变成为高度可配置的，MVC 容纳了大量视图技术，其中包括 JSP、Velocity、Tiles、iText 和 POI。

- spring Boot
  - 一个快速开发的脚手架
  - 基于SpringBoot可以快速的开发单个微服务
  - 约定大于配置
- Spring cloud
  - SpringCLoud是基于SpringBoot实现的

现在大多数公司使用SpringBoot进行快速开发。Spring和SpringMVC是SpringBoot的基础。

### 2.IOC

#### 2.1.原型

改需求之后，影响了之前的代码，需要修改代码。如果程序代码量十分大，修改一次的成本代价十分昂贵



我们可以使用一个Set接口实现，

最开始的Dao是自己new的对象 `private UserDao userDao  = new UserDaoImpl();`每次Impl一个新的类，就要改源代码了。

![image-20210601154216992](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210601154217.png)

程序员不用管理对象的创建了，系统的耦合性降低，

#### 2.2 IOC的本质



#### 2.3 IOC创建Bean

> 默认创建方式

通过Bean的**无参构造器**创造，使用属性的set方法进行注入的。

Bean在导入配置文件xxx.xml的时候创建的

> 通过有参构造创建

1.通过下标

```xml
<bean id="hello" class="com.xy.pojo.Hello">
    <constructor-arg index="0" value="无参构造index"/>
</bean>
```

2.通过类型创建

如果有两个一样类型的，会有问题

不推荐使用

```xml
<bean id="hello" class="com.xy.pojo.Hello">
    <constructor-arg type="java.lang.String" value="无参构造index"/>
</bean>
```

3.通过参数名的方式

```xml
 <bean id="hello" class="com.xy.pojo.Hello">
       <constructor-arg name="name" value="无参构造index"/>
    </bean>
```

### 3.Spring配置

#### 3.1 别名

```xml
<bean id="hello" class="com.xy.pojo.Hello">
    <constructor-arg name="name" value="hello Xy"/>
</bean>
上面的hello，取了个别的名字，可以在applicationContext中取出来
<alias name="hello" alias="你好"/>
```

```java
ApplicationContext applicationContext = new ClassPathXmlApplicationContext("beans.xml");
Hello hello = applicationContext.getBean("你好", Hello.class);
System.out.println(hello.getName());
```

#### 3.2 Bean配置

```xml
<!--
    id: bean的唯一标识符，就是创建类的名字
    class：包名+类名
    name:别名，比alias更厉害，可以取多个name="u1,u2"，也可以通过空格分割
//还有一个scope ，默认为单例模式，就是只创建这一次
-->
    <bean id="hello" class="com.xy.pojo.Hello" name="u1,u2">
       <constructor-arg name="name" value="无参构造index"/>
    </bean>
```

#### 3.3 import

用于团队开发使用，导入其他的配置文件

`applicationContext.xml`

有beans.xml 、beans2.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <import resource="beans.xml"/>
    <import resource="beans2.xml"/>
</beans>
```



### 4、依赖注入

#### 4.1 构造器注入

之前讲了

#### 4.2 set方式注入(重点)

依赖注入：

- 依赖：bean对象的创建依赖于容器
- 注入：bean对象的注入都

> 各种注入

```java
// Address 类
public class Address {
    private String address;
}

// 学生类
public class Student {
    private String name;
    private Address address;
    private String[] books;
    private List<Object> hobbies;
    private Map<String,String>  card;
    private Set<String> games;
    private String wife;
    private Properties info;
}

```

注入的xml配置

```xml
<bean id="address" class="com.xy.pojo.Address">
    <property name="address" value="湖北随州"/>
</bean>


<bean id="student" class="com.xy.pojo.Student">
    <property name="name" value="xy"/>

    <!--        数组-->
    <property name="books">
        <array>
            <value>红楼梦</value>
            <value>西游记</value>
            <value>三国演义</value>
        </array>
    </property>

    <!--list-->
    <property name="hobbies">
        <list>
            <value>听歌</value>
            <value>打篮球</value>
        </list>
    </property>

    <!-- Map-->
    <property name="card">
        <map>
            <entry key="xuying" value="12345"/>
            <entry key="身份证" value="249032i509590530"/>
        </map>
    </property>

    <!--Set-->
    <property name="games">
        <set>
            <value>LOL</value>
            <value>DNF</value>
        </set>
    </property>
    <!--复杂类型  依赖的实体类-->  
    <property name="address" ref="address"/>

    <!--  <property name="wife" value=""> 这是设置空字符串 --> 
    <!--null --> 
    <property name="wife">
        <null/>
    </property>

    <!--Properties-->
    <property name="info">
        <props>
            <prop key="学号">19S0529017</prop>
            <prop key="姓名">xx</prop>
        </props>
    </property>

</bean>
```

#### 4.3 c命名空间和p命名空间注入

- p命名空间对应之前的属性注入，需要有set方法和无参构造器
- c命名空间对应之前的构造器注入，需要有有参构造器，否则会报错

xml 配置

```xml
<!--  需要在beans里面加上
xmlns:p="http://www.springframework.org/schema/p"
xmlns:c="http://www.springframework.org/schema/c"
-->


<!--    p命名空间对应之前的属性注入，需要有set方法和无参构造器-->
<bean id="user" class="com.xy.pojo.User" p:name="xuying" />

<!--    c命名空间对应之前的构造器注入，需要有有参构造器，否则会报错-->
<bean id="user2" class="com.xy.pojo.User" c:age="18"/>
```

#### 4.4 bean作用域

1.单例模式

2.原型模式：每次从容器中get的时候，都会产生一个新对象！

3.其余的



### 5、自动装配

- 自动装配式spring满足bean依赖的i一种方式
- spring会在上下文中自动寻找，并自动给bean装配属性

在spring中有三种装配方式

1. 在xml中显示的装配
2. 在java中显示装配
3. 隐式的自动装配

#### 5.1 byName自动装配

```java
public class User {
   private Cat cat;
   private Dog dog;
   private String str;
}

public class Dog {
    public void shout() {
        System.out.println("wang~");
    }
}

public class Dog {
    public void shout() {
        System.out.println("wang~");
    }
}
```

<!--    autowire="byName"   会自动去找set后面对应的名称的id ,如果名字错了，就会报错，比如上面的id="dog1"，就错-->

```xml
<bean id="dog" class="com.kuang.pojo.Dog"/>
<bean id="cat" class="com.kuang.pojo.Cat"/>
<!--    autowire="byName"   会自动去找set后面对应的名称的id ,如果名字错了，就会报错，比如上面的id="dog1"，就错-->

<bean id="people" class="com.xy.pojo.People" autowire="byName">
    <property name="name" value="xy"/>
</bean>
```

#### 5.2 byType

```xml
<!--    autowire="byName"   会自动去找和自己类型一样的bean 
 类型还要是在spring容器中唯一，否则会报错-->
<bean id="people2" class="com.xy.pojo.People" autowire="byType">
    <property name="name" value="xy"/>
</bean>
```

#### 5.3使用注解完成自动装配

jdk1.5 支持的注解，spring2.5支持的注解

使用注解须知：

- 导入约束

- 配置注解的支持

  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <beans xmlns="http://www.springframework.org/schema/beans"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns:context="http://www.springframework.org/schema/context"
         xsi:schemaLocation="http://www.springframework.org/schema/beans
         http://www.springframework.org/schema/beans/spring-beans.xsd
         http://www.springframework.org/schema/context
         http://www.springframework.org/schema/context/spring-context.xsd">
  
  这里是开启注解
  <context:annotation-config/>
      
  </beans>
  ```

  **@Autowired**

  - 在属性上使用，也可以在set方式上使用

  - 使用Autowired可以不写Set方法了，前提是你自动装配的属性在spring容器中存在

  - **查找的方式是byName 和 byTypre 两个一起**

  - 如果有两个同类型的bean，id不一样，需要下面搭配`@Qualifier`

    ```java
    #搭配这个注解使定位更具体   这个是指定id 
    @Qualifier("dog1")
    ```

  - @Autowired(required=false)  

    ```java
    //如果允许装配的对象为null，设置required = false,默认为true
    //否则的话，就会在装在bean的时候报错
    @Autowired(required = false)
    private Cat cat;
    ```






> **@Resource**和**@Autowired**比较

**@Resource**和**@Autowired**比较：

- @Resource

  - 先通过name，如果找不到就通过Type

  - 不允许找不到bean的情况

  - 指定name的方式：

    ```java
    @Resource("baseDao")
    ```

  - Resource是JDK提供的

- @Autowired

  - 而Autowired先通过type查找，再通过name查找

  - Autowired允许找不到Bean（`@Autowired(required = false)`）

  - 指定name的方式：

    ```java
    @Autowired()
    @Qualifier("baseDao")
    xxxx
    ```

  - Autowired是Spring提供的

### 6、使用注解开发

在spring4之后，使用 注解必须导入aop的包

1.配置扫描注解包

```xml
<!--指定注解扫描包-->
<context:component-scan base-package="com.xy.pojo"/>
<context:annotation-config/>  
```

2. 指定包下编写类

```java
// 相当于配置文件中 <bean id="user" class="当前注解的类"/>
@Component("user")
public class User {
    //给属性赋值 ，也可以用在Set方法上
    @Value("xuYing")
    public String name; 
}
```

> @Component衍生注解：

功能都一样

- 按照mvc三层架构衍生出来的
  - Dao   ：`@Repository`
  - Controller:`@Controller`
  - Service :`@Service`
- 上面四个注解的功能是一样的，都是代表将某个类注册到Spring容器中

**@Scope("singleton")**    ==bean的作用域里的==  使用注解就相当于简化xml

> 配置类--去掉xml文件

1. 编写实体类

   ```java
   @Component  //将这个类标注为Spring的一个组件，放到容器中！
   public class Dog {
      public String name = "dog";
   }
   ```

2. MyConfig配置类

   ```java
   @Configuration  //代表这是一个配置类
   public class MyConfig {
   
      @Bean //通过方法注册一个bean，这里的返回值就Bean的类型，方法名就是bean的id！
      public Dog dog(){
          return new Dog();
     }
   
   }
   ```

3. 测试

   ```java
   @Test
   public void test2(){
       //跟xml不同的地方
      ApplicationContext applicationContext =
              new AnnotationConfigApplicationContext(MyConfig.class);
      Dog dog = (Dog) applicationContext.getBean("dog");
      System.out.println(dog.name);
   }
   ```

4. 可以导入其他的配置类

   ```java
   @Configuration  //代表这是一个配置类
   public class MyConfig2 {
   }
   ```

   ```java
   @Configuration
   @Import(MyConfig2.class)  //导入合并其他配置类，类似于配置文件中的 inculde 标签
   public class MyConfig {
   
      @Bean
      public Dog dog(){
          return new Dog();
     }
   
   }
   ```

   

### 7、代理模式

代理模式是SpringAOP的底层   。     **【SpringAOP和SpringMVC】面试必问**

代理模式的分类：

- 静态代理
- 动态代理

##### 静态代理

角色分析：

- 抽象角色：一般会使用接口或者抽象类来解决
- 真实角色：被代理的角色
- 代理角色：代理真实角色，代理真实角色后，一般会做一些附属操作
- 客户：访问代理对象的人！

##### 动态代理

- 动态代理的代理是动态生成的
- 动态代理分为两大类：
  - 基于接口  -- JDK动态代理
  - 基于类   cglib
  - java字节码实现：javasist

需要了解两个类：反射下的`Proxy.java` 代理。  `InvocationHandler.java` ：调用处理程序

动态代理的好处：

- 使真实角色更加纯粹
- 一个动态代理可以代理多个类，只要实现了同一个接口接口即可

> 动态代理实现

`ProxyInvocationHandler.java`

```java
package com.xy.proxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

public class ProxyInvocationHandler implements InvocationHandler {
    private Object target ;

    public void setTarget(Object target) {
        this.target = target;
    }
    //生成得到的代理类
    public Object getProxy(){

      return  Proxy.newProxyInstance(target.getClass().getClassLoader(),target.getClass().getInterfaces(),this);
    }

    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        // 使用invoke执行代理类的方法
        Object result = method.invoke(target, args);
        return result;
    }
}
```

`UserService.java`

```java
package com.xy.proxy;

public interface UserService {
    void add();
    void update();
}
```

`UserServiceImpl.java`

```java
package com.xy.proxy;

public class UserServiceImpl implements UserService{

    public void add() {
        System.out.println("add");
    }

    public void update() {
        System.out.println("update");
    }
}
```

`Client.java`

```java
package com.xy.proxy;

public class Client {
    public static void main(String[] args) {
        UserServiceImpl userService = new UserServiceImpl();
        ProxyInvocationHandler pih = new ProxyInvocationHandler();
        pih.setTarget(userService);
        UserService proxy = (UserService) pih.getProxy();
        proxy.add();
    }
}
```



### 8、AOP

> 名词

![image-20210604154134845](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210604154135.png)

#### 1.Aop的实现

导入需要的依赖包

```xml
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.4</version>
</dependency>
```

> 方式一: 使用Spring的AOP接口

`Log` 继承MethodBeforeAdvice实现

```java
@Component
public class Log  implements MethodBeforeAdvice {
    public void before(Method method, Object[] objects, Object target) throws Throwable {
        System.out.println(target.getClass()+"的"+method.getName()+"被执行了");
    }
}
```

`applicationContext.xml`   xml文件配置aop

```xml
<!--    配置aop-->
    <aop:config>
<!--        切入点  expression表达式:execution()-->
        <aop:pointcut id="pointcut" expression="execution(* com.xy.service.UserServiceImpl.*(..))"/>
<!--        将log类切入到切入点-->
        <aop:advisor advice-ref="log" pointcut-ref="pointcut"/>
    </aop:config>
```



> 方法二：自定义类实现AOP

```java
package com.xy.diy;


import org.springframework.stereotype.Component;

@Component("diy")
public class DiyPointCut {

    public void before(){
        System.out.println("方法执行前");
    }

    public void after(){
        System.out.println("方法执行后");
    }
}

```



```xml
<!--    方式二-->
    <aop:config>
<!--        自定义切面 -->
        <aop:aspect ref="diy">
            <aop:pointcut id="pointcut" expression="execution(* com.xy.service.UserServiceImpl.*(..))"/>
            <aop:before method="after" pointcut-ref="pointcut"/>
            <aop:after method="after" pointcut-ref="pointcut"/>
         </aop:aspect>
    </aop:config>
```

> 方法三：注解实现

**切面**

```java
package com.xy.diy;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

@Aspect  // 标注这个类是一个切面
public class AnnotationPointCut {
    @Before("execution(* com.xy.service.UserServiceImpl.*(..))")
    public void before(){
        System.out.println("在什么之前");
    }
    
     // 环绕
    @Around("execution(* com.xy.service.UserServiceImpl.*(..))")
    public void around(ProceedingJoinPoint jp) throws Throwable {
        System.out.println("环绕前");
        jp.proceed();  //这里是执行我们本来要执行的方法，jp也可以获得方法的信息
        System.out.println("环绕后");
    }
}
```

xml配置

```xml
<!--    自动代理，，注解用这个就可以了-->
<aop:aspectj-autoproxy/>
```

**注解：**

```java
@Around()
@After()
@Before()
@AfterReturning()
```

### 9、整合mybatis

导入依赖的包

```xml
 <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-webmvc</artifactId>
            <version>5.2.4.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-jdbc</artifactId>
            <version>5.2.4.RELEASE</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.aspectj/aspectjweaver -->
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjweaver</artifactId>
            <version>1.9.4</version>
        </dependency>

        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.5.2</version>
        </dependency>
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis-spring</artifactId>
            <version>2.0.2</version>
        </dependency>
        <!--数据库驱动-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.21</version>
        </dependency>

        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.20</version>
        </dependency>
```



#### 1.方法一

步骤：

- 数据源注册到Spring
- sqlSessionFactory 注册到Spring
- sqlSessionTemplate（== sqlSession） 注册到Spring
- 给接口实现类，并注册到Spring
- 测试

> db.properties

```properties
#db.properties文件的内容
driver=com.mysql.cj.jdbc.Driver
url=jdbc:mysql://localhost:3306/mybatis?serverTimezone=UTC&useUnicode=true&characterEncoding=UTF-8
name=root
password=root
```

> mybatis-spring.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:util="http://www.springframework.org/schema/util"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/util https://www.springframework.org/schema/util/spring-util.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">

    <context:property-placeholder location="classpath:db.properties"/>

    <bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
        <property name="driverClassName" value="${driver}"/>
        <property name="url" value="${url}"/>
        <property name="username" value="${name}"/>
        <property name="password" value="${password}"/>

    </bean>

    <!--        sqlSessionFactory-->
    <bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
        <property name="dataSource" ref="dataSource"/>
        <!--      这里这个可以指定一个mybatis的xml在里面进行一些设置，可以不需要这个文件
          <property name="configLocation" value="classpath:mybatis-config.xml"/>   -->
        <property name="mapperLocations" value="classpath*:com/xy/mapper/*.xml"/>
    </bean>

    <!--    这个SqlSessionTemplate 就是sqlSession  因为没有无参构造，所以用构造方法注入-->
    <bean id="sqlSessionTemplate" class="org.mybatis.spring.SqlSessionTemplate">
        <constructor-arg name="sqlSessionFactory"  ref="sqlSessionFactory">
        </constructor-arg>
    </bean>

</beans>

```

> applicationContext.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/context
       http://www.springframework.org/schema/context/spring-context.xsd">

    <import resource="mybatis-spring.xml"/>

<!--    指定要扫描的包，这个包下的注解就会生效-->
    <context:component-scan base-package="com.xy"/>
    <context:annotation-config/>

</beans>
```



> UserMapper.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<!--namespace=绑定一个对应的Dao/Mapper接口-->
<mapper namespace="com.xy.mapper.UserMapper">

    <!--select查询语句,这里的id就相当于impl实现的方法-->
    <select id="userList" resultType="com.xy.pojo.User">
       select * from mybatis.user
   </select>

</mapper>
```

> UserMapper

```java
package com.xy.mapper;
import com.xy.pojo.User;
import java.util.List;

public interface UserMapper {
    List<User> userList();
}
```

`userMapperImpl.java`

```java
package com.xy.mapper;
import com.xy.pojo.User;
import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service("userMapperImpl")
public class UserMapperImpl implements UserMapper {

    @Autowired
    private SqlSessionTemplate sqlSession;

    @Override
    public List<User> userList() {
        UserMapper mapper = sqlSession.getMapper(UserMapper.class);
        //直接return这个方法
        return mapper.userList();
    }
}
```

> 问题

1.pom.xml 必须配置静态资源过滤

```xml
<build>
    <resources>
        <resource>
            <directory>src/main/java</directory>
            <includes>
                <include>**/*.xml</include>
            </includes>
        </resource>
    </resources>
</build>
```

----

2.db.properties读取的问题

![image-20210604214030922](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210604214031.png)

在spring的配置文件中，加载数据库的properties文件，利用${username} 获取数据库用户名时，会得到系统当前的用户名；

这是因为 **spring默认会优先加载系统环境变量，此时获取到的username的值实际上指的是当前计算机的用户名。而不是properties配置文件中指定的username的值。**

#### 2.方法二

简化MapperImpl

> UserDaoImpl.java

```java
package com.xy.mapper;

import com.xy.pojo.User;
import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.support.SqlSessionDaoSupport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service("userMapperImpl")
public class UserDaoImpl extends SqlSessionDaoSupport implements UserMapper {

    @Autowired
    public void setSqlSessionFactory(SqlSessionFactory sqlSessionFactory) {
        super.setSqlSessionFactory(sqlSessionFactory);
    }

    @Override
    public List<User> userList() {
        return getSqlSession().selectList("com.xy.mapper.UserMapper.userList");
    }
}
```

其他配置同上，这里可以不用配置sqlSessionTemplate。只需要将sqlSessionFactory的依赖注入到上面的类就行.

### 10、声明式事务

ACID原则



事务分类：

- 声明式事务
- 编程式事务

```xml
    
<!--    配置声明式事务-->
    <bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
        <property name="dataSource" ref="datasource"/>
    </bean>
<!--    结合aop+-->
    <tx:advice id="txAdvice" transaction-manager="transactionManager">
        <tx:attributes>
       <!--    哪个方法中使用事务-->     
            <tx:method name="add" propagation="REQUIRED"/>
        </tx:attributes>
    </tx:advice>
    
    <aop:config>
        <aop:pointcut id="txPointCut" expression="execution(* com.xy.mapper.*.*(..))"/>
        <aop:advisor advice-ref="txAdvice" pointcut-ref="txPointCut"/>
    </aop:config>
```







![image-20210604221201864](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210604221201.png)

## 3、SpringMvc

### 1.概述

### 2.注解

`@Controller` `@RequestMapping` 

`@RestController` ：标记的类不会被视图解析器解析

```java
@Controller
public class HelloController {

    @RequestMapping("hello")
    public String hello(Model model) throws Exception {
        model.addAttribute("msg","huan");
        return "test";
    }
}
```



### 5、json

> 前端自带JSON类

```html
<script type="text/javascript">
    var user ={
        name : "xuying",
        age : 1,
        set: "男"
    }
    // 将对象转化成json格式字符串
    var json = JSON.stringify(user);
    console.log(json)
    console.log(user)
    // 将json格式字符串解析为对象
    var obj = JSON.parse(json);
    console.log(obj)
</script>
```

### 6、整合mybatis

