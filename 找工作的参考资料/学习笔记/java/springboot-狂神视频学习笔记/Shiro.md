### Shiro

![image-20210703141912318](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210703141912.png)



realm相当于数据层

#### 一、简单使用

1. 导入依赖

   ```xml
   <dependency>
   <groupId>org.apache.shiro</groupId>
       <artifactId>shiro-core</artifactId>
       <version>1.5.3</version>
   </dependency>
   
   <!-- configure logging -->
   <dependency>
       <groupId>org.slf4j</groupId>
       <artifactId>jcl-over-slf4j</artifactId>
       <version>1.7.21</version>
   </dependency>
   
   <dependency>
       <groupId>org.slf4j</groupId>
       <artifactId>slf4j-log4j12</artifactId>
       <version>1.7.21</version>
   </dependency>
   
   <dependency>
       <groupId>log4j</groupId>
       <artifactId>log4j</artifactId>
       <version>1.2.17</version>
   </dependency>
   ```

2. 配置文件

   1. `log4j.properties`

      ```properties
      
      log4j.rootLogger=INFO, stdout
      
      log4j.appender.stdout=org.apache.log4j.ConsoleAppender
      log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
      log4j.appender.stdout.layout.ConversionPattern=%d %p [%c] - %m %n
      
      # General Apache libraries
      log4j.logger.org.apache=WARN
      
      # Spring
      log4j.logger.org.springframework=WARN
      
      # Default Shiro logging
      log4j.logger.org.apache.shiro=INFO
      
      # Disable verbose logging
      log4j.logger.org.apache.shiro.util.ThreadContext=WARN
      log4j.logger.org.apache.shiro.cache.ehcache.EhCache=WARN
      ```
      
   2. `shiro.ini`
   
      ```ini
      
      [users]
      # user 'root' with password 'secret' and the 'admin' role
      root = secret, admin
      # user 'guest' with the password 'guest' and the 'guest' role
      guest = guest, guest
      # user 'presidentskroob' with password '12345' ("That's the same combination on
      # my luggage!!!" ;)), and role 'president'
      presidentskroob = 12345, president
      # user 'darkhelmet' with password 'ludicrousspeed' and roles 'darklord' and 'schwartz'
      darkhelmet = ludicrousspeed, darklord, schwartz
      # user 'lonestarr' with password 'vespa' and roles 'goodguy' and 'schwartz'
      lonestarr = vespa, goodguy, schwartz
   
      # -----------------------------------------------------------------------------
   # Roles with assigned permissions
      #
      # Each line conforms to the format defined in the
      # org.apache.shiro.realm.text.TextConfigurationRealm#setRoleDefinitions JavaDoc
      # -----------------------------------------------------------------------------
      [roles]
      # 'admin' role has all permissions, indicated by the wildcard '*'
      admin = *
      # The 'schwartz' role can do anything (*) with any lightsaber:
      schwartz = lightsaber:*
      # The 'goodguy' role is allowed to 'drive' (action) the winnebago (type) with
      # license plate 'eagle5' (instance specific id)
      goodguy = winnebago:drive:eagle5
      ```
      
      
   
3. HelloWorld

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

   

```java
Subject currentUser = SecurityUtils.getSubject();
Session session = currentUser.getSession();
session.setAttribute("someKey", "aValue");
currentUser.isAuthenticated();
currentUser.hasRole("schwartz");
currentUser.isPermitted();        
currentUser.logout();
```

#### 二、springboot集成

创建的boot项目需要导入thymeleaf和web模块

##### 1、整合shiro

> 依赖

```xml
<dependency>
    <groupId>com.stormpath.shiro</groupId>
    <artifactId>shiro-spring-boot-starter</artifactId>
    <version>0.7.2</version>
</dependency>
```

> shiro配置

`UserRealm.java`

```java
public class UserRealm extends AuthorizingRealm {

    
    //这是整合mybatis之后的
    @Autowired
    UserService userService;
  
    //授权


    @Override
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {

        SimpleAuthorizationInfo info = new SimpleAuthorizationInfo();

        //获取当前对象
        Subject subject = SecurityUtils.getSubject();
        
        
        User user = (User) subject.getPrincipal();
		//授予权力  user.getPerms() 从数据库里面取出来的
        info.addStringPermission(user.getPerms());
        return info;
    }
    
    //认证

    @Override
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {

		//获得token
        UsernamePasswordToken token = (UsernamePasswordToken) authenticationToken;

        // 查询数据库的对象表
        User user = userService.queryUserByName(token.getUsername());
        if(null == user){
            return null;   //相当于抛出了用户名不存在的异常，
        }
	
        return new SimpleAuthenticationInfo(user,user.getPwd(),"");  //直接在这匹配了密码，shiro自己做的
    }
}

```



>shiroConfig.java



```js
// 1. 创建Realm
@Bean
public UserRealm userRealm(){
    return new UserRealm();
}
```

```java
// 2. 创建DefaultWebSecurityManager
@Bean(name = "manager")
public DefaultWebSecurityManager getDefaultWebSecurityManager(@Qualifier("userRealm") UserRealm userRealm){
    DefaultWebSecurityManager manager = new DefaultWebSecurityManager();
    manager.setRealm(userRealm);
    return manager;
}
```

```java
// 3.创建ShiroFilterFactoryBean 
@Bean
public ShiroFilterFactoryBean getShiroFilterFactoryBean(@Qualifier("manager") DefaultWebSecurityManager manager){
    ShiroFilterFactoryBean bean = new ShiroFilterFactoryBean();

    bean.setSecurityManager(manager);

    /**
         * 添加内置过滤器
         * anon :无需认证
         * authc: 必须认证才能访问
         * user : 必须拥有记住我权限 才能访问
         * perms: 拥有对某个资源的权限才能访问
         * role:  必须拥有个角色才行
         */

    Map<String, String> filterMap = new HashMap<>();
	 //给路径添加规则
    filterMap.put("/user/add", "perms[user:add]");
    filterMap.put("/user/update", "perms[user:update]");
    
    //规则放入
    bean.setFilterChainDefinitionMap(filterMap);
	
    //设置未授权的跳转路径
    bean.setUnauthorizedUrl("/unAuthor");
    //设置登录的跳转路径  
    bean.setLoginUrl("/toLogin");
    return bean;
}
```

最终的代码

```java
@Configuration
public class ShiroConfig {
    //ShiroFilterFactoryBean
    @Bean
    public ShiroFilterFactoryBean getShiroFilterFactoryBean(@Qualifier("manager") DefaultWebSecurityManager manager){
        ShiroFilterFactoryBean bean = new ShiroFilterFactoryBean();

        bean.setSecurityManager(manager); 

        Map<String, String> filterMap = new HashMap<>();
        filterMap.put("/user/add", "perms[user:add]");
        filterMap.put("/user/update", "perms[user:update]");
        bean.setFilterChainDefinitionMap(filterMap);

        bean.setUnauthorizedUrl("/unAuthor");
        bean.setLoginUrl("/toLogin");
        return bean;
    }

    //DefaultWevSecurityManager
    @Bean(name = "manager")
    public DefaultWebSecurityManager getDefaultWebSecurityManager(@Qualifier("userRealm") UserRealm userRealm){
        DefaultWebSecurityManager manager = new DefaultWebSecurityManager();
        manager.setRealm(userRealm);
        return manager;
    }


    //创建realm对象   ==第一步==
    @Bean
    public UserRealm userRealm(){
        return new UserRealm();
    }

}
```

controller

```java
 @RequestMapping({"/login","/login.jsp"})
    public String Login(String username,String password ,Model model){

        Subject currentUser = SecurityUtils.getSubject();
        UsernamePasswordToken token = new UsernamePasswordToken(username, password);
        
        
        try {
            //这里和shiro 结合起来了
            currentUser.login(token);
            return "index";
        } catch (UnknownAccountException e) {
           model.addAttribute("msg", "用户名错误");
           return "login";
        }catch (IncorrectCredentialsException e){
            model.addAttribute("msg", "密码");
            return "login";
        }
    }
```

##### 2、shiro整合thymeleaf

> 依赖

```xml
<dependency>
    <groupId>com.github.theborakompanioni</groupId>
    <artifactId>thymeleaf-extras-shiro</artifactId>
    <version>2.0.0</version>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

> ShiroConfig

```java
 //整合shiroDialect
@Bean
public ShiroDialect getshiroDialect(){
    return new ShiroDialect();
}
```

html

```html

<!DOCTYPE html>
<!--命名空间-->
<html lang="en"  xmlns:th="http://www.thymeleaf.org"
      xmlns:shiro="http://www.pollix.at/thymeleaf/shiro">
    
    <!--带有权限 'user:add' 的才能看到-->
    <div shiro:hasPermission="user:add">
        <a th:href="@{/user/add}">add</a>
    </div>
    
        <!--带有权限 'user:update' 的才能看到-->
    <div shiro:hasPermission="user:update">
        <a th:href="@{/user/update}">update</a>
    </div>
    
</html>
```



> 使用session

```java
 Subject subject = SecurityUtils.getSubject();
Session session = subject.getSession();
session.setAttribute("loginUser", user.getName());  //添加session信息
```

html

```html
<div th:if="${session.loginUser== null}">  在这里判断session里的内容，来看显不显示
    <a th:href="@{/toLogin}">登录</a>
</div>
```



![image-20210701225440761](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210701225440.png)