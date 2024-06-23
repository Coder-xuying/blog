## Springboot

### 1.

### 2.自动配置的原理



> pom.xml

- 核心依赖在父工程里面
- 在写或者引入springBoot依赖的时候不需要指定版本，就是因为有这些版本仓库

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.5.0</version>
    <relativePath/> <!-- lookup parent from repository -->
</parent>

<!--spring-boot-starter-parent -->
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-dependencies</artifactId>
    <version>2.5.0</version>
</parent>

spring-boot-dependencies下是各种依赖

```

> 启动器：

- ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
  </dependency>
  ```

- 说白了就是springboot的启动场景

- springBoot将所有的功能场景都变成启动器

- 要使用什么功能，就找到对应的启动器



> 主程序

注解

```java
// springboot 的配置
@SpringBootConfiguration
   - @Configuration
   
@EnableAutoConfiguration
   	- @AutoConfigurationPackage   //自动配置
        - @Import(AutoConfigurationPackages.Registrar.class) // 自动配置，包注册
    - @Import(AutoConfigurationImportSelector.class)  // 
       
       
       
       
       
// 获取所有的配置
List<String> configurations = getCandidateConfigurations(annotationMetadata, attributes);
// 
```

```java
protected List<String> getCandidateConfigurations(AnnotationMetadata metadata, AnnotationAttributes attributes) {
    List<String> configurations = SpringFactoriesLoader.loadFactoryNames(getSpringFactoriesLoaderFactoryClass(),
                                                                         getBeanClassLoader());
    Assert.notEmpty(configurations, "No auto configuration classes found in META-INF/spring.factories. If you "
                    + "are using a custom packaging, make sure that file is correct.");
    return configurations;
}
```

### 3. springBoot 配置

springBoot 的配置有一个全局的配置文件，配置文件的名称是固定的，下面两个随便一个都可以,在文件中修改值就能够自动配置

- application.properties
- application.yaml

#### 3.1 yaml 语法

YAML是 "YAML Ain't a Markup Language" （YAML不是一种标记语言）的递归缩写。在开发的这种语言时，YAML 的意思其实是："Yet Another Markup Language"（仍是一种标记语言

- 空格不能省略
- 以缩进来控制层级关系，只要是左边对齐的一列数据都是同一个层级的。
- 属性和值的大小写都是十分敏感的。

##### 1  基础语法

```yaml
#  对空格的要求很高

#值的前面必须要有空格
server:
  port: 8081

#可以存放对象 Map ，student.name   student.age
student:
  name: xy
  age: 3
  
  
#行内写法
student: {name: xy,age: 3}

#数组
pets:
  - cat
  - dog
  - pig

#行内写法
pets: [cat,dog,pig]
```

##### 2 通过yaml 注入值

application.yml 中把需要注入的对象的值写好,person 相当于这个赋值的名字

```yaml
person:
  name: xuying
  age: 3
  happy: false
  Dog:
    name: 旺财
    age: 3
    
    
    
---
person2:
  name: xuying2
  age: 32
  happy: false
  Dog:
    name: 旺财2
    age: 32
```

**Person 类**

```java
#需要这个注解  使用prefix 指定person
#使用这个之后 会有红色错误出现在IDEA中,可导入下面的依赖
#参数 prefix = “person” : 将配置文件中的person下面的所有属性一一对应
@Component 注册bean到容器中去
@ConfigurationProperties(prefix = "person")
public class Person {
    private String name;
    private Integer age;
    private Boolean happy;
    private Dog dog;
}
```

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-configuration-processor</artifactId>
    <optional>true</optional>
</dependency>
```

#### 3.2 加载指定的配置文件

**@PropertySource ：**加载指定的配置文件；

**@configurationProperties**：默认从全局配置文件中获取值

```properties
#person.properties 文件
name=kuangshen
```

```java
@PropertySource(value = "classpath:person.properties")
# 此时这个类就可以使用person.properties文件的配置了
public class Person {
}
```

#### 3.3  比较

![image-20210610111030687](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210610111030.png)

##### 1 松散绑定

比如我的yml中写的last-name，这个和lastName是一样的， - 后面跟着的字母默认是大写的。这就是松散绑定。可以测试一下

```yaml
Dog:
  last-name: 小黄
  age: 3
```

```java
class Dog{
    private String lastName;
    private int age;
}
```

==可以在yaml中使用 xx-xx 给类里面使用驼峰的属性赋值==



##### 2 JSR303数据校验

导入依赖

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```

我们可以在字段是增加一层过滤器验证 ， 可以保证数据的合法性

```java
@Data
@AllArgsConstructor
@NoArgsConstructor
@Component
@ConfigurationProperties(prefix = "emails111")
// 开启数据校验
@Validated
public class EmailTest {
    @Email(message = "邮箱格式错误")
    private String url ;
}
```

```yml
emails111:
  url: 19082ioj
```

> **JSR303常见参数**

```java
# Bean Validation 中内置的 constraint
@Null	被注释的元素必须为 null
@NotNull	被注释的元素必须不为 null
@AssertTrue	被注释的元素必须为 true
@AssertFalse	被注释的元素必须为 false
@Min(value)	被注释的元素必须是一个数字，其值必须大于等于指定的最小值
@Max(value)	被注释的元素必须是一个数字，其值必须小于等于指定的最大值
@DecimalMin(value)	被注释的元素必须是一个数字，其值必须大于等于指定的最小值
@DecimalMax(value)	被注释的元素必须是一个数字，其值必须小于等于指定的最大值
@Size(max, min)	被注释的元素的大小必须在指定的范围内
@Digits (integer, fraction)	被注释的元素必须是一个数字，其值必须在可接受的范围内
@Past	被注释的元素必须是一个过去的日期
@Future	被注释的元素必须是一个将来的日期
@Pattern(value)	被注释的元素必须符合指定的正则表达式

# Hibernate Validator 附加的 constraint

Constraint	详细信息
@Email	被注释的元素必须是电子邮箱地址
@Length	被注释的字符串的大小必须在指定的范围内
@NotEmpty	被注释的字符串的必须非空
@Range	被注释的元素必须在合适的范围内
```

#### 3.4  配置文件位置

##### 1.配置文件位置、优先级

**官方参考**：

classpath:表示的是resources这个文件夹

file：指的是这个项目的第一个文件夹。

![image-20210610111038990](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210610111039.png)

```java
//优先级由高到底，高优先级的配置会覆盖低优先级的配置；
//SpringBoot会从这四个位置全部加载主配置文件；互补配置
优先级1：项目路径下的config文件夹配置文件  
优先级2：项目路径下配置文件
优先级3：资源路径下的config文件夹配置文件
优先级4：资源路径下配置文件
```

```properties
#配置项目的访问路径
server.servlet.context-path= /kuang
```



##### 2.多环境配置切换

> 多个配置文件

```properties
#properties配置，需要写多个配置文件
application-test.properties 代表测试环境配置
application-dev.properties 代表开发环境配置

#application.properties中切换
spring.profiles.active = dev
```

> 一个yml文件配置多环境

```yaml
#yaml 配置  ，则可以在一个文件中用 --- 隔开多个配置， spring.profies 附一个名字
spring:
  profiles:
    active: test
---
server:
  port: 8081
spring:
  profiles: dev

---
server:
  port: 8085
spring:
  profiles: test
```

**注意：如果yml和properties同时都配置了端口，并且没有激活其他环境 ， 默认会使用properties配置文件的！**



### 4、SpringBoot Web开发

#### 1.静态资源

路径

```java
private static final String[] CLASSPATH_RESOURCE_LOCATIONS = { 
    "classpath:/META-INF/resources/",   // webjar里的路径
	"classpath:/resources/",       // ①
    "classpath:/static/",       // ②
    "classpath:/public/" };   // ③


private String staticPathPattern = "/**";
```

优先级：① > ② > ③

#### 2.首页和图标定制

定制一个index.html 就行

放在static目录下

#### 3.Thymeleaf

```html
#{}  //  国际化取值
@{}  //  链接

th:fragment="bar"
~{页面名::bar}  : // 搭配th:replace使用


${}  // 取传过来的数据

// 条件判断
${name=='xy'? true:false} 

// 循环
th:each="emp:${emps}"
```



![image-20210618150335351](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210618150335.png)



RestFul

![image-20210618150908626](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210618150908.png)

![image-20210618150859237](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210618150859.png)







==security的没看==

### 5、分布式Dubbo + Zookeper

#### 1.RPC

HTTP协议，RPC协议

进行网络通信的

RPC的两个核心模块：通讯、序列化

序列化：数据传输需要转换

#### 2.Dubbo 

基于java的RPC框架

> Zookper

Zookper  服务中心  == nacos



下载Zookper，解压 之后弄配置文件

然后运行



### 6.Dubbo+Zookeeper实战小Demo(补充狂神说新版Dubbo)

> 不浪费时间阅读版 - 2.7.8版本的dubbo

下面两个改变：

- 新版注解

```java
@DubboService
@DubboReference
```

- 依赖    -- 替换zkclient

```xml
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-framework</artifactId>
    <version>2.12.0</version>
</dependency>
```

> 依赖

```xml
<dependency>
    <groupId>org.apache.dubbo</groupId>
    <artifactId>dubbo-spring-boot-starter</artifactId>
    <version>2.7.8</version>
</dependency>

<!-- https://mvnrepository.com/artifact/com.github.sgroschupf/zkclient -->
<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-framework</artifactId>
    <version>2.12.0</version>
</dependency>


<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-recipes</artifactId>
    <version>2.12.0</version>
</dependency>
<dependency>
    <groupId>org.apache.zookeeper</groupId>
    <artifactId>zookeeper</artifactId>
    <version>3.4.14</version>
    <!--排除这个slf4j-log4j12-->
    <exclusions>
        <exclusion>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-log4j12</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

我用的是2.7.8版本的dubbo.查了一下别人的博客，说

- dubbo 2.6以前的版本，引入zkclient操作zookeeper
- dubbo 2.6及以后的版本，引入curator操作zookeeper

```xml
<dependency>
    <groupId>com.101tec</groupId>
    <artifactId>zkclient</artifactId>
    <version>0.10</version>
</dependency>


<dependency>
    <groupId>org.apache.curator</groupId>
    <artifactId>curator-framework</artifactId>
    <version>2.12.0</version>
</dependency>
```

所以需要用curator依赖替换掉zkclient

> provider-server

`TicketService.java`

```java
public interface TicketService {
    String buy();
}
```

`TicketServiceImpl.java`

新版Dubbo里面的`@Service`过时了，去包里看了一下，换成新注解`@DubboService `。所以这里我们也可以用Spring的`@Service`和`@DubboService `组合。

```java
import org.apache.dubbo.config.annotation.DubboService;
import org.springframework.stereotype.Component;

@Component
@DubboService   
public class TicketServiceImpl implements TicketService {
    @Override
    public String buy() {
        return "买买买";
    }
}
```

`application.properties`

```properties
server.port=8081
#服务应用的名字
dubbo.application.name=provider-server
#注册中心地址
dubbo.registry.address=zookeeper://127.0.0.1:2181
#哪些服务要被注册，服务所在的包名
dubbo.scan.base-packages=com.xy.service 
```

> Consumer-server

调用远程服务

`UserService`  

```java
public class UserService {

    @DubboReference //引用
    //1.定义路径相同的接口名
    TicketService TICKET_SERVICE;

    public void buyTicket(){
        String buy = TICKET_SERVICE.buy();
        System.out.println(buy);
    }
}
```

TicketService没有，狂神提出的第一种办法就是在同一路径下创建TicketService.java 的接口。第二种办法他没讲

新版的`    @Reference` 也是过期了，换成了`    @DubboReference`

`application.properties`

```properties
server.port=8082
#消费者去哪里拿，暴露自己的名字
dubbo.application.name=consumer-server
#注册中心的地址
dubbo.registry.address=zookeeper://127.0.0.1:2181
```

测试：

```java
@SpringBootTest
class ConsumerServerApplicationTests {

    @Autowired
    UserService userService;

    @Test
    void contextLoads() {
        userService.buyTicket();
    }
}
```



## 实战总结



### 1.springboot整合 mybatis+druid+log4j日志

#### 0.简介

springboot默认的应该是`**HikariDataSource**` ，这个号称是最快的。

这里的整合是使用druid做为数据源



#### 1.导入依赖

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.12</version>
</dependency>

<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>2.1.1</version>
</dependency>

<!--数据库驱动，这里使用了druid-->
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.47</version>
</dependency>

<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid</artifactId>
    <version>1.1.21</version>
</dependency>

<!--        #开启日志功能需要用到-->
<dependency>
    <groupId>log4j</groupId>
    <artifactId>log4j</artifactId>
    <version>1.2.17</version>
</dependency>
```

#### 2.配置文件

> application.yml

```yml
spring:
# 数据库连接
  datasource:
    username: root
    url: jdbc:mysql://localhost:3306/mybatis
    driver-class-name: com.mysql.jdbc.Driver
    password: root
    
    #使用type将数据源设置为Druid
    type: com.alibaba.druid.pool.DruidDataSource


	#druid 数据源专有配置
	
    #Spring Boot 默认是不注入这些属性值的，需要自己绑定
    initialSize: 5
    minIdle: 5
    maxActive: 20
    maxWait: 60000
    timeBetweenEvictionRunsMillis: 60000
    minEvictableIdleTimeMillis: 300000
    validationQuery: SELECT 1 FROM DUAL
    testWhileIdle: true
    testOnBorrow: false
    testOnReturn: false
    poolPreparedStatements: true


	#Druid的日志功能-使用log4j

    #配置监控统计拦截的filters，stat:监控统计、log4j：日志记录、wall：防御sql注入
    #如果允许时报错  java.lang.ClassNotFoundException: org.apache.log4j.Priority
    #则导入 log4j 依赖即可，Maven 地址：https://mvnrepository.com/artifact/log4j/log4j
    filters: stat,wall,log4j
    maxPoolPreparedStatementPerConnectionSize: 20
    useGlobalDataSourceStat: true
    connectionProperties: druid.stat.mergeSql=true;druid.stat.slowSqlMillis=500


#配置mybatis的配置
mybatis:
  type-aliases-package: com.xy.pojo
  mapper-locations: classpath:mapper/*.xml
```

> 配置druid的config加入到springboot

```java
package com.xy.config;
import com.alibaba.druid.pool.DruidDataSource;
import com.alibaba.druid.support.http.StatViewServlet;
import com.alibaba.druid.support.http.WebStatFilter;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.boot.web.servlet.ServletRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import javax.sql.DataSource;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

@Configuration
public class DruidConfig {
    //将自定义的 Druid数据源添加到容器中，不再让 Spring Boot 自动创建
    // @ConfigurationProperties(prefix = "spring.datasource")：作用就是将 全局配置文件中
    // 前缀为 spring.datasource的属性值注入到 com.alibaba.druid.pool.DruidDataSource 的同名参数中
    @ConfigurationProperties(prefix = "spring.datasource")
    @Bean
    public DataSource druidDataSource(){
        return new DruidDataSource();
    }

    //  配置Druid的后台监控  ，一些固定形式
    @Bean
    public ServletRegistrationBean statViewServlet(){

	//  这个也是固定的
        ServletRegistrationBean<StatViewServlet> bean =
                new ServletRegistrationBean<>(new StatViewServlet(), "/druid/*");
        //后台需要有人登陆，账号密码配置
        HashMap<String, String> initParams = new HashMap<>();

        //key 是固定的 loginUsername  loginPassword
        initParams.put("loginUsername", "admin");
        initParams.put("loginPassword", "123456");

        //允许谁可以访问
        //initParams.put("kuangshen", "192.168.1.20");表示禁止此ip访问
        //initParams.put("allow", "localhost")：表示只有本机可以访问
        initParams.put("allow", "");  //参数为空 所有人都能访问

        bean.setInitParameters(initParams);
        return bean;
    }

    //配置 Druid 监控 之  web 监控的 filter
//WebStatFilter：用于配置Web和Druid数据源之间的管理关联监控统计
    @Bean
    public FilterRegistrationBean webStatFilter() {
        FilterRegistrationBean bean = new FilterRegistrationBean();
        bean.setFilter(new WebStatFilter());

        //exclusions：设置哪些请求进行过滤排除掉，从而不进行统计
        Map<String, String> initParams = new HashMap<>();
        initParams.put("exclusions", "*.js,*.css,/druid/*,/jdbc/*");
        bean.setInitParameters(initParams);

        //"/*" 表示过滤所有请求
        bean.setUrlPatterns(Arrays.asList("/*"));
        return bean;
    }
}
```

之后可以通过http://localhost:8080/druid/login.html后台检测查询的一些过程

#### 3.测试

> 用户类

```java
package com.xy.pojo;
@Data
@AllArgsConstructor
@NoArgsConstructor
public class User {
    private int id;
    private String name;
    private String pwd;
}
```

> UserMapper.java

```java
@Mapper
@Component
public interface UserMapper {
     User queryUserByName(String name);
}
```

> UserMapper.xml   -- xml配置

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Confg 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.xy.mapper.UserMapper">

    <select id="queryUserByName" parameterType="String" resultType="User">
           select * from user where name = #{name}
    </select>

</mapper>
```

> UserService

```java
@Service
public interface UserService {
    User queryUserByName(String name);
}
```

> UserServiceImpl

```java
@Service
public class UserServiceImpl implements UserService{
    @Autowired
    UserMapper userMapper;

    @Override
    public User queryUserByName(String name) {
        return userMapper.queryUserByName(name);
    }
}
```

---

test里面测试一下

```java
@Autowired
UserServiceImpl userService;

@Test
void contextLoads() {
    System.out.println(userService.queryUserByName("张三"));
}
```

### 2.上面的基础上整合Shiro权限认证

#### 1.导入依赖

```xml
<dependency>
    <groupId>com.stormpath.shiro</groupId>
    <artifactId>shiro-spring-boot-starter</artifactId>
    <version>0.7.2</version>
</dependency>
```

#### 2.shiro的配置类

> UserRealm.java

```java
package com.xy.config;

import com.xy.pojo.User;
import com.xy.service.UserServiceImpl;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.*;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.authz.SimpleAuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;
import org.springframework.beans.factory.annotation.Autowired;

public class UserRealm  extends AuthorizingRealm {

 
    @Autowired
    UserServiceImpl userService;


    @Override
    // 授权
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        // 用户在经过需要权限的请求时，会自己进来的
        SimpleAuthorizationInfo info = new SimpleAuthorizationInfo();
        // 在数据库里面取这个用户的权限
        User user = (User) SecurityUtils.getSubject().getPrincipal();

         // 设置用户的权限
		// 如果数据库里面的字段有权限字段，加入是perm
         // 这里就是info.addStringPermission(user.getperm());
        info.addStringPermission("user:add");
        //这个是集合info.addStringPermissions();
       
        return info;
    }

    @Override
    // 认证  -- 认证就是这个用户是我们的用户，但是有什么权限，需要到授权里面去获得
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken token) throws AuthenticationException {
        UsernamePasswordToken uToken = (UsernamePasswordToken) token;
        User user = userService.queryUserByName(uToken.getUsername());
        if(user==null){
            // 返回null就代表认证失败
            return null;
        }
        // 第一个是priciple，用来传递给上面方法的，存在subject里面
       return new SimpleAuthenticationInfo(user,user.getPwd(),"");
    }
}

```

```java
package com.xy.config;

import org.apache.catalina.User;
import org.apache.shiro.spring.web.ShiroFilterFactoryBean;
import org.apache.shiro.web.mgt.DefaultWebSecurityManager;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import sun.security.krb5.Realm;

import java.util.HashMap;
import java.util.Map;

@Configuration
public class ShiroConfig {// 三大对象爱你
    // shiroFilterFactoryBean
    @Bean
    public ShiroFilterFactoryBean shiroFilterFactoryBean(DefaultWebSecurityManager securityManager){
        ShiroFilterFactoryBean bean = new ShiroFilterFactoryBean();
        // 设置安全管理器
        bean.setSecurityManager(securityManager);

        /**
         * 添加内置过滤器
         * anon :无需认证
         * authc: 必须认证才能访问
         * user : 必须拥有记住我权限 才能访问
         * perms: 拥有对某个资源的权限才能访问
         * role:  必须拥有个角色才行
         */
        // 添加shiro的内置过滤器，就是制定一些规则
        Map<String, String> filterMap = new HashMap();
        filterMap.put("/user/add", "perms[user:add]");
        filterMap.put("/user/update", "perms[user:update]");
        
        //设置未认证跳转的位置
        bean.setLoginUrl("/toLogin");
       
        // 设置未授权跳转的位置 bean.setUnauthorizedUrl("/noauth");

        // 添加到工厂里面
        bean.setFilterChainDefinitionMap(filterMap);
        return bean;
    }


    /*
    下面这是固定的套路
    */
    @Bean
    //DefaultWbeSecurityManager
    public DefaultWebSecurityManager defaultWebSecurityManager(@Qualifier("userRealm") UserRealm userRealm){
        DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager();
        securityManager.setRealm(userRealm);
        return securityManager;
    }

    //realm
    @Bean
    public UserRealm userRealm(){
        return new UserRealm();
    }
}
```

#### 3.请求

```java
// 这是一个简单的登录请求
@RequestMapping("/login")
public String Login(@RequestParam("user") String username, String password, Model model){
    // 获取到subject对象，全局的
    Subject subject = SecurityUtils.getSubject();
    // 把登录的用户制作成一个token
    UsernamePasswordToken token = new UsernamePasswordToken(username, password);
    //登录用户
    try{
        //login方法登录这个token
        subject.login(token);
        return "index";
    }// 这里有很多异常,可以根据需求捕获
    catch (Exception e) {
        model.addAttribute("msg", "登录失败");
        return "login";
    }
}
```

#### 4.shiro加密

我们这里用的是二次salt加密

> 数据库里面增加字段salt

alter table user add (salt varchar(100) )

password的长度增大，免得超出长度了

> 修改

insert请求

```java
@RequestMapping("/add2")
@ResponseBody
public String create(@RequestParam("user") String username, String password, Model model){
    //盐量随机
    String salt = new SecureRandomNumberGenerator().nextBytes().toString(); 
    // md5二次盐值加密
    String encodedPassword= new SimpleHash("md5",password,salt,2).toString();
    User user = new User(10, username, encodedPassword, salt);
    userMapper.insertUser(user);
    return "创建用户成功";
}
```

`UserRealm.java类`

realme里面认证部分需要修改

```java
 @Override
    // 认证  -- 认证就是这个用户是我们的用户，但是有什么权限，需要到授权里面去获得
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken token) throws AuthenticationException {
        UsernamePasswordToken uToken = (UsernamePasswordToken) token;
        String password = new String(uToken.getPassword());
        User user = userService.queryUserByName(uToken.getUsername());
        if(user==null){
            return null;
        }
        /*
        	主要改的是这里，获取盐，对token传过来的password进行md5处理，之后进行字符串比较
        */
        String salt = user.getSalt();
        String passwordEncoded = new SimpleHash("md5",password,salt,2).toString();

        System.out.println("生成加密之后的"+passwordEncoded);
        if(passwordEncoded.equals(user.getPwd())){
            // 第一个是priciple，用来传递给上面方法的，存在subject里面，第二个还是用token里面的password
            return new SimpleAuthenticationInfo(user,password,"");
        }
        return null;
    }
```

#### 5.官方方法例子--看方法用的

```java
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.*;
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.session.Session;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.Factory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class Quickstart {

    private static final transient Logger log = LoggerFactory.getLogger(Quickstart.class);


    public static void main(String[] args) {


        // 用工厂可以获得SecurityManager的实例
        Factory<SecurityManager> factory = new IniSecurityManagerFactory("classpath:shiro.ini");
        SecurityManager securityManager = factory.getInstance();
        SecurityUtils.setSecurityManager(securityManager);

      

        // get the currently executing user:
        Subject currentUser = SecurityUtils.getSubject();

        // 通过当前用户拿到session
        Session session = currentUser.getSession();
        session.setAttribute("someKey", "aValue");
        
        
        String value = (String) session.getAttribute("someKey");
        if (value.equals("aValue")) {
            log.info("Retrieved the correct value! [" + value + "]");
        }

        //判断当前的用户是否被认证
        if (!currentUser.isAuthenticated()) {
            // 认证之后，就能拿到一个令牌
            UsernamePasswordToken token = new UsernamePasswordToken("lonestarr", "vespa");
            // remember me
            token.setRememberMe(true);
            try {
                currentUser.login(token);
            } catch (UnknownAccountException uae) {
                log.info("There is no user with username of " + token.getPrincipal());
            } catch (IncorrectCredentialsException ice) {
                log.info("Password for account " + token.getPrincipal() + " was incorrect!");
            } catch (LockedAccountException lae) {
                log.info("The account for username " + token.getPrincipal() + " is locked.  " +
                        "Please contact your administrator to unlock it.");
            }
            // ... catch more exceptions here (maybe custom ones specific to your application?
            catch (AuthenticationException ae) {
                //unexpected condition?  error?
            }
        }

        //say who they are:
        // 用户的信息 currentUser.getPrincipal()
        log.info("User [" + currentUser.getPrincipal() + "] logged in successfully.");

        //test a role:
        if (currentUser.hasRole("schwartz")) {
            log.info("May the Schwartz be with you!");
        } else {
            log.info("Hello, mere mortal.");
        }

        //test a typed permission (not instance-level)
        if (currentUser.isPermitted("lightsaber:wield")) {
            log.info("You may use a lightsaber ring.  Use it wisely.");
        } else {
            log.info("Sorry, lightsaber rings are for schwartz masters only.");
        }

        //a (very powerful) Instance Level permission:
        if (currentUser.isPermitted("winnebago:drive1:eagle5")) {
            log.info("You are permitted to 'drive' the winnebago with license plate (id) 'eagle5'.  " +
                    "Here are the keys - have fun!");
        } else {
            log.info("Sorry, you aren't allowed to drive the 'eagle5' winnebago!");
        }

        //all done - log out!
        currentUser.logout();

        System.exit(0);
    }
}
```

> 主要的

```java
Subject currentUser = SecurityUtils.getSubject();
Session session = currentUser.getSession();
session.setAttribute("someKey", "aValue");
currentUser.isAuthenticated();
currentUser.hasRole("schwartz");
currentUser.isPermitted();        
currentUser.logout();
```

异常

```java
try {
    currentUser.login(token);
} catch (UnknownAccountException uae) {
    log.info("There is no user with username of " + token.getPrincipal());
} catch (IncorrectCredentialsException ice) {
    log.info("Password for account " + token.getPrincipal() + " was incorrect!");
} catch (LockedAccountException lae) {
    log.info("The account for username " + token.getPrincipal() + " is locked.  " +
             "Please contact your administrator to unlock it.");
}
// ... catch more exceptions here (maybe custom ones specific to your application?
catch (AuthenticationException ae) {
    //unexpected condition?  error?
}
```



### 3、springboot解决跨域问题

实现一个类

```java
package com.xy.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

/**
 * 解决跨域问题
 */
@Configuration
public class CorsConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
                .allowedOriginPatterns("*")
                .allowedMethods("GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS")
                .allowCredentials(true)
                .maxAge(3600)
                .allowedHeaders("*");
    }
}
```

在拦截器前加上一个预处理方法  ==预处理操作

```java
  /**
     * 进入filter之前的解决跨域问题
     * @param request
     * @param response
     * @return
     * @throws Exception
     */
    @Override
    protected boolean preHandle(ServletRequest request, ServletResponse response) throws Exception {

        HttpServletRequest httpServletRequest = WebUtils.toHttp(request);
        HttpServletResponse httpServletResponse = WebUtils.toHttp(response);
        httpServletResponse.setHeader("Access-control-Allow-Origin", httpServletRequest.getHeader("Origin"));
        httpServletResponse.setHeader("Access-Control-Allow-Methods", "GET,POST,OPTIONS,PUT,DELETE");
        httpServletResponse.setHeader("Access-Control-Allow-Headers", httpServletRequest.getHeader("Access-Control-Request-Headers"));
        // 跨域时会首先发送一个OPTIONS请求，这里我们给OPTIONS请求直接返回正常状态
        if (httpServletRequest.getMethod().equals(RequestMethod.OPTIONS.name())) {
            httpServletResponse.setStatus(org.springframework.http.HttpStatus.OK.value());
            return false;
        }
        return super.preHandle(request, response);
    }
```





![image-20210704151530645](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210704151530.png)

传递实体的时候，要加上`@RequestBody`



### 4、springboot+MybatisPlus代码自动生成

#### 1.导入依赖包

```xml
  <!--mp代码生成器-->
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-generator</artifactId>
    <version>3.2.0</version>
</dependency>

  <!--模板-->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-freemarker</artifactId>
</dependency>
```

#### 2.生成方法

```java

package com.xy;

import com.baomidou.mybatisplus.core.exceptions.MybatisPlusException;
import com.baomidou.mybatisplus.core.toolkit.StringPool;
import com.baomidou.mybatisplus.core.toolkit.StringUtils;
import com.baomidou.mybatisplus.generator.AutoGenerator;
import com.baomidou.mybatisplus.generator.InjectionConfig;
import com.baomidou.mybatisplus.generator.config.*;
import com.baomidou.mybatisplus.generator.config.po.TableInfo;
import com.baomidou.mybatisplus.generator.config.rules.NamingStrategy;
import com.baomidou.mybatisplus.generator.engine.FreemarkerTemplateEngine;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// 演示例子，执行 main 方法控制台输入模块表名回车自动生成对应项目目录中
public class CodeGenerator {
    public static String scanner(String tip) {
        Scanner scanner = new Scanner(System.in);
        StringBuilder help = new StringBuilder();
        help.append("请输入" + tip + "：");
        System.out.println(help.toString());
        if (scanner.hasNext()) {
            String ipt = scanner.next();
            if (StringUtils.isNotEmpty(ipt)) {
                return ipt;
            }
        }
        throw new MybatisPlusException("请输入正确的" + tip + "！");
    }

    public static void main(String[] args) {
        // 代码生成器
        AutoGenerator mpg = new AutoGenerator();

        // 全局配置
        GlobalConfig gc = new GlobalConfig();
        String projectPath = System.getProperty("user.dir");
        gc.setOutputDir(projectPath + "/src/main/java");

        gc.setAuthor("xuying");
        gc.setOpen(false);
        // gc.setSwagger2(true); 实体属性 Swagger2 注解
        gc.setServiceName("%sService");
        mpg.setGlobalConfig(gc);

        // 数据源配置
        DataSourceConfig dsc = new DataSourceConfig();
        dsc.setUrl("jdbc:mysql://localhost:3306/vueblog?useUnicode=true&useSSL=false&characterEncoding=utf8&serverTimezone=UTC");
        dsc.setDriverName("com.mysql.cj.jdbc.Driver");
        dsc.setUsername("root");
        dsc.setPassword("root");
        mpg.setDataSource(dsc);

        
        // 包配置
        PackageConfig pc = new PackageConfig();
        pc.setModuleName(null);
        // 包目录
        pc.setParent("com.xy");
        mpg.setPackageInfo(pc);

        // 自定义配置
        InjectionConfig cfg = new InjectionConfig() {
            @Override
            public void initMap() {
                // to do nothing
            }
        };

//         如果模板引擎是 freemarker
        String templatePath = "/templates/mapper.xml.ftl";
//         如果模板引擎是 velocity
//         String templatePath = "/templates/mapper.xml.vm";

        
        // 自定义输出配置
        List<FileOutConfig> focList = new ArrayList<>();
        // 自定义配置会被优先输出
        focList.add(new FileOutConfig(templatePath) {
            @Override
            public String outputFile(TableInfo tableInfo) {
                // 自定义输出文件名 ， 如果你 Entity 设置了前后缀、此处注意 xml 的名称会跟着发生变化！！
                return projectPath + "/src/main/resources/mapper/"
                        + "/" + tableInfo.getEntityName() + "Mapper" + StringPool.DOT_XML;
            }
        });

        cfg.setFileOutConfigList(focList);
        mpg.setCfg(cfg);

        // 配置模板
        TemplateConfig templateConfig = new TemplateConfig();

        templateConfig.setXml(null);
        mpg.setTemplate(templateConfig);

        // 策略配置
        StrategyConfig strategy = new StrategyConfig();
        strategy.setNaming(NamingStrategy.underline_to_camel);
        strategy.setColumnNaming(NamingStrategy.underline_to_camel);
        strategy.setEntityLombokModel(true);
        strategy.setRestControllerStyle(true);
        strategy.setInclude(scanner("表名，多个英文逗号分割").split(","));
        strategy.setControllerMappingHyphenStyle(true);
        // 设置前缀，生成的文件名就不回带上这个
        strategy.setTablePrefix("m_");
        mpg.setStrategy(strategy);
        mpg.setTemplateEngine(new FreemarkerTemplateEngine());
        mpg.execute();
    }
}
```

运行的时候输入数据库里面的表面就可以自动生成了