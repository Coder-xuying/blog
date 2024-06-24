

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