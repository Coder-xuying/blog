# 	七、Spring篇 

### 设计思想&Beans

#### **1、IOC 控制反转**

​		IoC（Inverse of Control:控制反转）是⼀种设计思想，就是将原本在程序中⼿动创建对象的控制权，交由Spring框架来管理。 IoC 在其他语⾔中也有应⽤，并⾮ Spring 特有。 

​		IoC 容器是 Spring⽤来实现 IoC 的载体， IoC 容器实际上就是个Map（key，value）,Map 中存放的是各种对象。将对象之间的相互依赖关系交给 IoC 容器来管理，并由 IoC 容器完成对象的注⼊。这样可以很⼤程度上简化应⽤的开发，把应⽤从复杂的依赖关系中解放出来。 IoC 容器就像是⼀个⼯⼚⼀样，当我们需要创建⼀个对象的时候，只需要配置好配置⽂件/注解即可，完全不⽤考虑对象是如何被创建出来的。



**DI 依赖注入**

​	DI:（Dependancy Injection：依赖注入)站在容器的角度，将对象创建依赖的其他对象注入到对象中。



#### **2、AOP 动态代理**

​		AOP(Aspect-Oriented Programming:⾯向切⾯编程)能够将那些与业务⽆关，却为业务模块所共同调⽤的逻辑或责任（例如事务处理、⽇志管理、权限控制等）封装起来，便于减少系统的重复代码，降低模块间的耦合度，并有利于未来的可拓展性和可维护性。

​		Spring AOP就是基于动态代理的，如果要代理的对象，实现了某个接⼝，那么Spring AOP会使⽤JDKProxy，去创建代理对象，⽽对于没有实现接⼝的对象，就⽆法使⽤ JDK Proxy 去进⾏代理了，这时候Spring AOP会使⽤基于asm框架字节流的Cglib动态代理 ，这时候Spring AOP会使⽤ Cglib ⽣成⼀个被代理对象的⼦类来作为代理。



#### **3、Bean生命周期** 

**单例对象：** singleton                    

总结：单例对象的生命周期和容器相同        

**多例对象：** prototype           

出生：使用对象时spring框架为我们创建            

活着：对象只要是在使用过程中就一直活着            

死亡：当对象长时间不用且没有其它对象引用时，由java的垃圾回收机制回收

<img src="https://s0.lgstatic.com/i/image3/M01/89/0C/Cgq2xl6WvHqAdmt4AABGAn2eSiI631.png" alt="img" style="zoom:67%;" />

IOC容器初始化加载Bean流程：

```java
@Override
public void refresh() throws BeansException, IllegalStateException { synchronized (this.startupShutdownMonitor) {
  // 第一步:刷新前的预处理 
  prepareRefresh();
  //第二步: 获取BeanFactory并注册到 BeanDefitionRegistry
  ConfigurableListableBeanFactory beanFactory = obtainFreshBeanFactory();
  // 第三步:加载BeanFactory的预准备工作(BeanFactory进行一些设置，比如context的类加载器等)
  prepareBeanFactory(beanFactory);
  try {
    // 第四步:完成BeanFactory准备工作后的前置处理工作 
    postProcessBeanFactory(beanFactory);
    // 第五步:实例化BeanFactoryPostProcessor接口的Bean 
    invokeBeanFactoryPostProcessors(beanFactory);
    // 第六步:注册BeanPostProcessor后置处理器，在创建bean的后执行 
    registerBeanPostProcessors(beanFactory);
    // 第七步:初始化MessageSource组件(做国际化功能;消息绑定，消息解析); 
    initMessageSource();
    // 第八步:注册初始化事件派发器 
    initApplicationEventMulticaster();
    // 第九步:子类重写这个方法，在容器刷新的时候可以自定义逻辑 
    onRefresh();
    // 第十步:注册应用的监听器。就是注册实现了ApplicationListener接口的监听器
    registerListeners();
    //第十一步:初始化所有剩下的非懒加载的单例bean 初始化创建非懒加载方式的单例Bean实例(未设置属性)
    finishBeanFactoryInitialization(beanFactory);
    //第十二步: 完成context的刷新。主要是调用LifecycleProcessor的onRefresh()方法，完成创建
    finishRefresh();
	}
  ……
} 
```

总结：

**四个阶段**

- 实例化 Instantiation
- 属性赋值 Populate
- 初始化 Initialization
- 销毁 Destruction

**多个扩展点**

- 影响多个Bean
  - BeanPostProcessor
  - InstantiationAwareBeanPostProcessor
- 影响单个Bean
  - Aware

**完整流程**  

1. 实例化一个Bean－－也就是我们常说的**new**；
2. 按照Spring上下文对实例化的Bean进行配置－－**也就是IOC注入**；
3. 如果这个Bean已经实现了BeanNameAware接口，会调用它实现的setBeanName(String)方法，也就是根据就是Spring配置文件中**Bean的id和name进行传递**
4. 如果这个Bean已经实现了BeanFactoryAware接口，会调用它实现setBeanFactory(BeanFactory)也就是Spring配置文件配置的**Spring工厂自身进行传递**；
5. 如果这个Bean已经实现了ApplicationContextAware接口，会调用setApplicationContext(ApplicationContext)方法，和4传递的信息一样但是因为ApplicationContext是BeanFactory的子接口，所以**更加灵活**
6. 如果这个Bean关联了BeanPostProcessor接口，将会调用postProcessBeforeInitialization()方法，BeanPostProcessor经常被用作是Bean内容的更改，由于这个是在Bean初始化结束时调用那个的方法，也可以被应用于**内存或缓存技**术
7. 如果Bean在Spring配置文件中配置了init-method属性会自动调用其配置的初始化方法。
8. 如果这个Bean关联了BeanPostProcessor接口，将会调用postProcessAfterInitialization()，**打印日志或者三级缓存技术里面的bean升级**
9. 以上工作完成以后就可以应用这个Bean了，那这个Bean是一个Singleton的，所以一般情况下我们调用同一个id的Bean会是在内容地址相同的实例，当然在Spring配置文件中也可以配置非Singleton，这里我们不做赘述。
10. 当Bean不再需要时，会经过清理阶段，如果Bean实现了DisposableBean这个接口，或者根据spring配置的destroy-method属性，调用实现的destroy()方法





#### **4**、Bean作用域

| 名称           | 作用域                                                       |
| -------------- | ------------------------------------------------------------ |
| **singleton**  | **单例对象，默认值的作用域**                                 |
| **prototype**  | **每次获取都会创建⼀个新的 bean 实例**                       |
| request        | 每⼀次HTTP请求都会产⽣⼀个新的bean，该bean仅在当前HTTP request内有效。 |
| session        | 在一次 HTTP session 中，容器将返回同一个实例                 |
| global-session | 将对象存入到web项目集群的session域中,若不存在集群,则global session相当于session |

默认作用域是singleton，多个线程访问同一个bean时会存在线程不安全问题

**保障线程安全方法：**

1. 在Bean对象中尽量避免定义可变的成员变量（不太现实）。

2. 在类中定义⼀个ThreadLocal成员变量，将需要的可变成员变量保存在 ThreadLocal 中

  **ThreadLocal**：

  ​		每个线程中都有一个自己的ThreadLocalMap类对象，可以将线程自己的对象保持到其中，各管各的，线程可以正确的访问到自己的对象。

  ​		将一个共用的ThreadLocal静态实例作为key，将不同对象的引用保存到不同线程的ThreadLocalMap中，然后**在线程执行的各处通过这个静态ThreadLocal实例的get()方法取得自己线程保存的那个对象**，避免了将这个对象作为参数传递的麻烦。



#### 5、循环依赖

​	循环依赖其实就是循环引用，也就是两个或者两个以上的 Bean 互相持有对方，最终形成闭环。比如A 依赖于B，B又依赖于A

Spring中循环依赖场景有: 

- prototype 原型 bean循环依赖

- 构造器的循环依赖（构造器注入）

- Field 属性的循环依赖（set注入）

  其中，构造器的循环依赖问题无法解决，在解决属性循环依赖时，可以使用懒加载，spring采用的是提前暴露对象的方法。

**懒加载@Lazy解决循环依赖问题**

​	Spring 启动的时候会把所有bean信息(包括XML和注解)解析转化成Spring能够识别的BeanDefinition并存到Hashmap里供下面的初始化时用，然后对每个 BeanDefinition 进行处理。普通 Bean 的初始化是在容器启动初始化阶段执行的，而被lazy-init=true修饰的 bean 则是在从容器里第一次进行**context.getBean() 时进行触发**。



**三级缓存解决循环依赖问题**

<img src="https://tva1.sinaimg.cn/large/0081Kckwly1glv7ivru2lj31980qcn13.jpg" alt="循环依赖问题" style="zoom: 33%;" />

1. Spring容器初始化ClassA通过构造器初始化对象后提前暴露到Spring容器中的singletonFactorys（三级缓存中）。

2. ClassA调用setClassB方法，Spring首先尝试从容器中获取ClassB，此时ClassB不存在Spring 容器中。

3. Spring容器初始化ClassB，ClasssB首先将自己暴露在三级缓存中，然后从Spring容器一级、二级、三级缓存中一次中获取ClassA 。

4. 获取到ClassA后将自己实例化放入单例池中，实例 ClassA通过Spring容器获取到ClassB，完成了自己对象初始化操作。

5. 这样ClassA和ClassB都完成了对象初始化操作，从而解决了循环依赖问题。

   

### Spring注解

#### 1、@SpringBoot 

​	**声明bean的注解**

​	**@Component** 通⽤的注解，可标注任意类为  Spring 组件

​	**@Service** 在业务逻辑层使用（service层）

​	**@Repository** 在数据访问层使用（dao层）

​	**@Controller** 在展现层使用，控制器的声明（controller层）

​	**注入bean的注解**

​	**@Autowired**：默认按照类型来装配注入，**@Qualifier**：可以改成名称

​	**@Resource**：默认按照名称来装配注入，JDK的注解，新版本已经弃用



**@Autowired注解原理** 

​		 @Autowired的使用简化了我们的开发，

​				实现 AutowiredAnnotationBeanPostProcessor 类，该类实现了 Spring 框架的一些扩展接口。
​				实现 BeanFactoryAware 接口使其内部持有了 BeanFactory（可轻松的获取需要依赖的的 Bean）。
​				实现 MergedBeanDefinitionPostProcessor 接口，实例化Bean 前获取到 里面的 @Autowired 信息并缓存下来；
​				实现 postProcessPropertyValues 接口， 实例化Bean 后从缓存取出注解信息，通过反射将依赖对象设置到 Bean 属性里面。



**@SpringBootApplication**

```java
@SpringBootApplication
public class JpaApplication {
    public static void main(String[] args) {
        SpringApplication.run(JpaApplication.class, args);
    }
}
```

**@SpringBootApplication**注解等同于下面三个注解：

- **@SpringBootConfiguration：** 底层是**Configuration**注解，说白了就是支持**JavaConfig**的方式来进行配置
- **@EnableAutoConfiguration：**开启**自动配置**功能
- **@ComponentScan：**就是**扫描**注解，默认是扫描**当前类下**的package

其中`@EnableAutoConfiguration`是关键(启用自动配置)，内部实际上就去加载`META-INF/spring.factories`文件的信息，然后筛选出以`EnableAutoConfiguration`为key的数据，加载到IOC容器中，实现自动配置功能！

它主要加载了@SpringBootApplication注解主配置类，这个@SpringBootApplication注解主配置类里边最主要的功能就是SpringBoot开启了一个@EnableAutoConfiguration注解的自动配置功能。

 **@EnableAutoConfiguration作用：**

它主要利用了一个

EnableAutoConfigurationImportSelector选择器给Spring容器中来导入一些组件。

```java
@Import(EnableAutoConfigurationImportSelector.class)
public @interface EnableAutoConfiguration 
```





#### **2、@SpringMVC**

```java
@Controller 声明该类为SpringMVC中的Controller
@RequestMapping 用于映射Web请求
@ResponseBody 支持将返回值放在response内，而不是一个页面，通常用户返回json数据
@RequestBody 允许request的参数在request体中，而不是在直接连接在地址后面。
@PathVariable 用于接收路径参数
@RequestMapping("/hello/{name}")申明的路径，将注解放在参数中前，即可获取该值，通常作为Restful的接口实现方法。
```

**SpringMVC原理** 

<img src="https://img-blog.csdn.net/20181022224058617?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2F3YWtlX2xxaA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" style="zoom: 50%;" />

1. 客户端（浏览器）发送请求，直接请求到  DispatcherServlet 。
2. DispatcherServlet 根据请求信息调⽤  HandlerMapping ，解析请求对应的  Handler 。
3. 解析到对应的  Handler （也就是  Controller 控制器）后，开始由HandlerAdapter 适配器处理。
4. HandlerAdapter 会根据  Handler 来调⽤真正的处理器开处理请求，并处理相应的业务逻辑。
5. 处理器处理完业务后，会返回⼀个  ModelAndView 对象， Model 是返回的数据对象
6. ViewResolver 会根据逻辑  View 查找实际的  View 。
7. DispaterServlet 把返回的  Model 传给  View （视图渲染）。
8. 把  View 返回给请求者（浏览器）



#### 3、@SpringMybatis

```java
@Insert ： 插入sql ,和xml insert sql语法完全一样
@Select ： 查询sql, 和xml select sql语法完全一样
@Update ： 更新sql, 和xml update sql语法完全一样
@Delete ： 删除sql, 和xml delete sql语法完全一样
@Param ： 入参
@Results ： 设置结果集合@Result ： 结果
@ResultMap ： 引用结果集合
@SelectKey ： 获取最新插入id 
```

**mybatis如何防止sql注入？**

​	简单的说就是#{}是经过预编译的，是安全的，**$**{}是未经过预编译的，仅仅是取变量的值，是非安全的，存在SQL注入。在编写mybatis的映射语句时，尽量采用**“#{xxx}”**这样的格式。如果需要实现动态传入表名、列名，还需要做如下修改：添加属性**statementType="STATEMENT"**，同时sql里的属有变量取值都改成**${xxxx}**



**Mybatis和Hibernate的区别** 

**Hibernate 框架：** 

​    **Hibernate**是一个开放源代码的对象关系映射框架,它对JDBC进行了非常轻量级的对象封装,建立对象与数据库表的映射。是一个全自动的、完全面向对象的持久层框架。

**Mybatis框架：**

​    **Mybatis**是一个开源对象关系映射框架，原名：ibatis,2010年由谷歌接管以后更名。是一个半自动化的持久层框架。

**区别：**

  **开发方面**

​    在项目开发过程当中，就速度而言：

​      hibernate开发中，sql语句已经被封装，直接可以使用，加快系统开发；

​      Mybatis 属于半自动化，sql需要手工完成，稍微繁琐；

​    但是，凡事都不是绝对的，如果对于庞大复杂的系统项目来说，复杂语句较多，hibernate 就不是好方案。

  **sql优化方面**

​    Hibernate 自动生成sql,有些语句较为繁琐，会多消耗一些性能；

​    Mybatis 手动编写sql，可以避免不需要的查询，提高系统性能；

  **对象管理比对**

​    Hibernate 是完整的对象-关系映射的框架，开发工程中，无需过多关注底层实现，只要去管理对象即可；

​    Mybatis 需要自行管理映射关系；



#### 4、@Transactional

```java
@EnableTransactionManagement 
@Transactional
```

注意事项：

​	①事务函数中不要处理耗时任务，会导致长期占有数据库连接。

​	②事务函数中不要处理无关业务，防止产生异常导致事务回滚。

**事务传播属性**

**1) REQUIRED（默认属性）** 如果存在一个事务，则支持当前事务。如果没有事务则开启一个新的事务。 

2) MANDATORY  支持当前事务，如果当前没有事务，就抛出异常。 

3) NEVER  以非事务方式执行，如果当前存在事务，则抛出异常。 

4) NOT_SUPPORTED  以非事务方式执行操作，如果当前存在事务，就把当前事务挂起。 

5) REQUIRES_NEW  新建事务，如果当前存在事务，把当前事务挂起。 

6) SUPPORTS  支持当前事务，如果当前没有事务，就以非事务方式执行。 

**7) NESTED** （**局部回滚**） 支持当前事务，新增Savepoint点，与当前事务同步提交或回滚。 **嵌套事务一个非常重要的概念就是内层事务依赖于外层事务。外层事务失败时，会回滚内层事务所做的动作。而内层事务操作失败并不会引起外层事务的回滚。**



### Spring源码阅读

#### **1、Spring中的设计模式** 

参考：[spring中的设计模式](https://mp.weixin.qq.com/s?__biz=Mzg2OTA0Njk0OA==&mid=2247485303&idx=1&sn=9e4626a1e3f001f9b0d84a6fa0cff04a&chksm=cea248bcf9d5c1aaf48b67cc52bac74eb29d6037848d6cf213b0e5466f2d1fda970db700ba41&token=255050878&lang=zh_CN%23rd)

**单例设计模式 :** Spring 中的 Bean 默认都是单例的。

**⼯⼚设计模式 :** Spring使⽤⼯⼚模式通过  BeanFactory 、 ApplicationContext 创建bean 对象。

**代理设计模式 :** Spring AOP 功能的实现。

**观察者模式：** Spring 事件驱动模型就是观察者模式很经典的⼀个应⽤。

**适配器模式：**Spring AOP 的增强或通知(Advice)使⽤到了适配器模式、spring MVC 中也是⽤到了适配器模式适配 Controller 。











# 八、SpringCloud篇

#### Why SpringCloud

> ​	Spring cloud 是一系列框架的有序集合。它利用 spring boot 的开发便利性巧妙地简化了分布式系统基础设施的开发，如**服务发现注册**、**配置中心**、**消息总线**、**负载均衡**、**断路器**、**数据监控**等，都可以用 spring boot 的开发风格做到一键启动和部署。

| SpringCloud（微服务解决方案）    | Dubbo（分布式服务治理框架） |
| -------------------------------- | --------------------------- |
| Rest API （轻量、灵活、swagger） | RPC远程调用（高效、耦合）   |
| Eureka、Nacos                    | Zookeeper                   |
| 使用方便                         | 性能好                      |
| 即将推出SpringCloud2.0           | 断档5年后17年重启           |

​	SpringBoot是Spring推出用于解决传统框架配置文件冗余,装配组件繁杂的基于Maven的解决方案,**旨在快速搭建单个微服务**，SpringCloud是依赖于SpringBoot的,而SpringBoot并不是依赖与SpringCloud,甚至还可以和Dubbo进行优秀的整合开发

​	MartinFlower 提出的微服务之间是通过RestFulApi进行通信，具体实现

- RestTemplate：基于HTTP协议
- Feign：封装了ribbon和Hystrix 、RestTemplate 简化了客户端开发工作量
- RPC：基于TCP协议，序列化和传输效率提升明显
- MQ：异步解耦微服务之间的调用

<img src="https://tva1.sinaimg.cn/large/0081Kckwly1gmawejgpgwj30ht0bnt9d.jpg" alt="img" style="zoom:67%;" />

#### Spring Boot

> Spring Boot 通过**简单的步骤**就可以创建一个 Spring 应用。
>
> Spring Boot 为 Spring 整合第三方框架提供了**开箱即用功能**。
>
> Spring Boot 的核心思想是**约定大于配置**。

**Spring Boot 解决的问题**

- 搭建后端框架时需要手动添加 Maven 配置，涉及很多 XML 配置文件，增加了搭建难度和时间成本。

- 将项目编译成 war 包，部署到 Tomcat 中，项目部署依赖 Tomcat，这样非常不方便。

- 应用监控做的比较简单，通常都是通过一个没有任何逻辑的接口来判断应用的存活状态。

**Spring Boot 优点**

**自动装配：**Spring Boot 会根据某些规则对所有配置的 Bean 进行初始化。可以减少了很多重复性的工作。

​	比如使用 MongoDB 时，只需加入 MongoDB 的 Starter 包，然后配置  的连接信息，就可以直接使用 MongoTemplate 自动装配来操作数据库了。简化了 Maven Jar 包的依赖，降低了烦琐配置的出错几率。

**内嵌容器：**Spring Boot 应用程序可以不用部署到外部容器中，比如 Tomcat。

​	应用程序可以直接通过 Maven 命令编译成可执行的 jar 包，通过 java-jar 命令启动即可，非常方便。

**应用监控：**Spring Boot 中自带监控功能 Actuator，可以实现对程序内部运行情况进行监控，

​	比如 Bean 加载情况、环境变量、日志信息、线程信息等。当然也可以自定义跟业务相关的监控，通过Actuator 的端点信息进行暴露。

```java
spring-boot-starter-web          //用于快速构建基于 Spring MVC 的 Web 项目。
spring-boot-starter-data-redis   //用于快速整合并操作 Redis。
spring-boot-starter-data-mongodb //用于对 MongoDB 的集成。
spring-boot-starter-data-jpa     //用于操作 MySQL。
```

**自定义一个Starter**

1. 创建 Starter 项目，定义 Starter 需要的配置（Properties）类，比如数据库的连接信息；

2. 编写自动配置类，自动配置类就是获取配置，根据配置来自动装配 Bean；

3. 编写 spring.factories 文件加载自动配置类，Spring 启动的时候会扫描 spring.factories 文件，；

4. 编写配置提示文件 spring-configuration-metadata.json（不是必须的），在添加配置的时候，我们想要知道具体的配置项是什么作用，可以通过编写提示文件来提示；

5. 在项目中引入自定义 Starter 的 Maven 依赖，增加配置值后即可使用。

**Spring Boot Admin**（将 actuator 提供的数据进行可视化）

- 显示应用程序的监控状态、查看 JVM 和线程信息

- 应用程序上下线监控  

- 可视化的查看日志、动态切换日志级别

- HTTP 请求信息跟踪等实用功能



#### GateWay / Zuul

> GateWay⽬标是取代Netflflix Zuul，它基于Spring5.0+SpringBoot2.0+WebFlux等技术开发，提供**统⼀的路由**⽅式（反向代理）并且基于 **Filter**(定义过滤器对请求过滤，完成⼀些功能) 链的⽅式提供了⽹关基本的功能，例如：鉴权、流量控制、熔断、路径重写、⽇志监控。

**组成：**

- **路由route：** ⽹关最基础的⼯作单元。路由由⼀个ID、⼀个⽬标URL、⼀系列的断⾔（匹配条件判断）和Filter过滤器组成。如果断⾔为true，则匹配该路由。

- **断⾔predicates：**参考了Java8中的断⾔Predicate，匹配Http请求中的所有内容（类似于nginx中的location匹配⼀样），如果断⾔与请求相匹配则路由。

- **过滤器filter：**标准的Spring webFilter，使⽤过滤器在请求之前或者之后执⾏业务逻辑。

  请求前`pre`类型过滤器：做**参数校验**、**权限校验**、**流量监控**、**⽇志输出**、**协议转换**等，

  请求前`post`类型的过滤器：做**响应内容**、**响应头**的修改、**⽇志的输出**、**流量监控**等。

<img src="https://tva1.sinaimg.cn/large/0081Kckwly1gmc49l9babj31do0n7n13.jpg" alt="image-20210105001419761" style="zoom: 50%;" />

**GateWayFilter** 应⽤到单个路由路由上 、**GlobalFilter** 应⽤到所有的路由上











#### Eureka / Zookeeper

> 服务注册中⼼本质上是为了解耦服务提供者和服务消费者，为了⽀持弹性扩缩容特性，⼀个微服务的提供者的数量和分布往往是动态变化的。

<img src="https://tva1.sinaimg.cn/large/0081Kckwly1gmawwm3k7bj30o80ecq3u.jpg" alt="image-20210103231405882" style="zoom: 50%;" />

| 区别   | Zookeeper        | Eureka                       | Nacos              |
| ------ | ---------------- | ---------------------------- | ------------------ |
| CAP    | CP               | AP                           | CP/AP切换          |
| 可用性 | 选举期间不可用   | 自我保护机制，数据不是最新的 |                    |
| 组成   | Leader和Follower | 节点平等                     |                    |
| 优势   | 分布式协调       | 注册与发现                   | 注册中心和配置中心 |
| 底层   | 进程             | 服务                         | Jar包              |

**Eureka**通过**⼼跳检测**、**健康检查**和**客户端缓存**等机制，提⾼系统的灵活性、可伸缩性和可⽤性。

<img src="https://tva1.sinaimg.cn/large/0081Kckwly1gmaxc493qyj30ji0a6mxx.jpg" alt="image-20210103232900353" style="zoom:67%;" />

1. us-east-1c、us-east-1d，us-east-1e代表不同的机房，**每⼀个Eureka Server都是⼀个集群**。
2. Service作为服务提供者向Eureka中注册服务，Eureka接受到注册事件会在**集群和分区中进⾏数据同步**，Client作为消费端（服务消费者）可以从Eureka中获取到服务注册信息，进⾏服务调⽤。
3. 微服务启动后，会周期性地向Eureka**发送⼼跳**（默认周期为30秒）以续约⾃⼰的信息
4. Eureka在⼀定时间内**（默认90秒）没有接收**到某个微服务节点的⼼跳，Eureka将会注销该微服务节点
5. Eureka Client**会缓存Eureka Server中的信息**。即使所有的Eureka Server节点都宕掉，服务消费者依然可以使⽤缓存中的信息找到服务提供者



**Eureka缓存**

> 新服务上线后，服务消费者**不能立即访问**到刚上线的新服务，需要过⼀段时间后才能访问？或是将服务下线后，服务还是会被调⽤到，⼀段时候后**才彻底停⽌服务**，访问前期会导致频繁报错！

<img src="https://tva1.sinaimg.cn/large/0081Kckwly1gmaxmk97q0j30vw0j6gmu.jpg" alt="image-20210103233902439" style="zoom:50%;" />

​	服务注册到注册中⼼后，服务实例信息是**存储在Registry表**中的，也就是内存中。但Eureka为了提⾼响应速度，在内部做了优化，加⼊了两层的缓存结构，将Client需要的实例信息，直接缓存起来，获取的时候直接从缓存中拿数据然后响应给 Client。 

- 第⼀层缓存是**readOnlyCacheMap**，采⽤**ConcurrentHashMap**来存储数据的，主要负责定时与readWriteCacheMap进⾏数据同步，默认同步时间为 **30** 秒⼀次。

- 第⼆层缓存是**readWriteCacheMap**，采⽤**Guava**来实现缓存。缓存过期时间默认为**180**秒，当服务**下线、过期、注册、状态变更**等操作都会清除此缓存中的数据。

- 如果两级缓存都无法查询，会**触发缓存的加载**，从存储层拉取数据到缓存中，然后再返回给 Client。

  Eureka之所以设计⼆级缓存机制，也是为了**提⾼ Eureka Server 的响应速度**，缺点是缓存会导致 Client**获取不到最新的服务实例信息**，然后导致⽆法快速发现新的服务和已下线的服务。

**解决方案**

- 我们可以**缩短读缓存的更新时间**让服务发现变得更加及时，或者**直接将只读缓存关闭**，同时可以缩短客户端如ribbon服务的定时刷新间隔，多级缓存也导致C层⾯（数据⼀致性）很薄弱。
- Eureka Server 中会有**定时任务去检测失效**的服务，将服务实例信息从注册表中移除，也可以将这个失效检测的**时间缩短**，这样服务下线后就能够及时从注册表中清除。

**自我保护机制开启条件**

- 期望最小每分钟能够续租的次数（实例* 频率 * 比例==10* 2 *0.85）
- 期望的服务实例数量（10）

**健康检查**

- Eureka Client 会定时发送心跳给 Eureka Server 来证明自己处于健康的状态

- 集成SBA以后可以把所有健康状态信息一并返回给eureka

  

#### Feign / Ribbon

- Feign 可以与 Eureka 和 Ribbon 组合使用以支持负载均衡，
- Feign 可以与 Hystrix 组合使用，支持熔断回退
- Feign 可以与ProtoBuf实现快速的RPC调用

<img src="https://tva1.sinaimg.cn/large/0081Kckwly1gmbxsh2rfnj30uo0fgmxz.jpg" alt="img" style="zoom:80%;" />

- **InvocationHandlerFactory 代理**

  采用 JDK 的动态代理方式生成代理对象，当我们调用这个接口，实际上是要去调用远程的 HTTP API

- **Contract 契约组件**

  比如请求类型是 GET 还是 POST，请求的 URI 是什么

- **Encoder 编码组件 \ Decoder 解码组件**

  通过该组件我们可以将请求信息采用指定的编码方式进行编解码后传输

- **Logger 日志记录**

  负责 Feign 中记录日志的，可以指定 Logger 的级别以及自定义日志的输出

- **Client 请求执行组件**

  负责 HTTP 请求执行的组件，Feign 中默认的 Client 是通过 JDK 的 HttpURLConnection 来发起请求的，在每次发送请求的时候，都会创建新的 HttpURLConnection 链接，Feign 的性能会很差，可以通过扩展该接口，使用 Apache HttpClient 等基于连接池的高性能 HTTP 客户端。

- **Retryer 重试组件**

  负责重试的组件，Feign 内置了重试器，当 HTTP 请求出现 IO 异常时，Feign 会限定一个最大重试次数来进行重试操作。

- **RequestInterceptor 请求拦截器**

  可以为 Feign 添加多个拦截器，在请求执行前设置一些扩展的参数信息。

**Feign最佳使用技巧**

- 继承特性

- 拦截器

  比如添加指定的请求头信息，这个可以用在服务间传递某些信息的时候。

- GET 请求多参数传递

- 日志配置

  FULL 会输出全部完整的请求信息。

- 异常解码器

  异常解码器中可以获取异常信息，而不是简单的一个code，然后转换成对应的异常对象返回。

- 源码查看是如何继承Hystrix

  HystrixFeign.builder 中可以看到继承了 Feign 的 Builder，增加了 Hystrix的SetterFactory， build 方法里，对 invocationHandlerFactory 进行了重写， create 的时候**返回HystrixInvocationHandler**， 在 invoke 的时候**会将请求包装成 HystrixCommand** 去执行，这里就自然的集成了 Hystrix



**Ribbon**

<img src="http://s0.lgstatic.com/i/image2/M01/93/96/CgotOV2Nux-AO2PcAAEcl4M1Zi4629.png" alt="img" style="zoom: 50%;" />



**使用方式**

- **原生 API**，Ribbon 是 Netflix 开源的，没有使用 Spring Cloud，需要使用 Ribbon 的原生 API。

- **Ribbon + RestTemplate**，整合Spring Cloud 后，可以基于 RestTemplate 提供负载均衡的服务

- **Ribbon + Feign**

  <img src="http://s0.lgstatic.com/i/image2/M01/93/76/CgoB5l2NuyCALoefAAAdV1DlSHY088.png" alt="img" style="zoom: 67%;" />

**负载均衡算法**

- RoundRobinRule 是**轮询的算法**，A和B轮流选择。

- RandomRule 是**随机算法**，这个就比较简单了，在服务列表中随机选取。

- BestAvailableRule 选择一个最**小的并发请求 server**

**自定义负载均衡算法**

- 实现 Irule 接口
- 继承 AbstractLoadBalancerRule 类

**自定义负载均衡使用场景**（核心）

- **灰度发布**

  灰度发布是能够平滑过渡的一种发布方式，在发布过程中，先发布一部分应用，让指定的用户使用刚发布的应用，等到测试没有问题后，再将其他的全部应用发布。如果新发布的有问题，只需要将这部分恢复即可，不用恢复所有的应用。

- **多版本隔离**

  多版本隔离跟灰度发布类似，为了兼容或者过度，某些应用会有多个版本，这个时候如何保证 1.0 版本的客户端不会调用到 1.1 版本的服务，就是我们需要考虑的问题。

- **故障隔离**

  当线上某个实例发生故障后，为了不影响用户，我们一般都会先留存证据，比如：线程信息、JVM 信息等，然后将这个实例重启或直接停止。然后线下根据一些信息分析故障原因，如果我能做到故障隔离，就可以直接将出问题的实例隔离，不让正常的用户请求访问到这个出问题的实例，只让指定的用户访问，这样就可以单独用特定的用户来对这个出问题的实例进行测试、故障分析等。



#### Hystrix / Sentinel

**服务雪崩场景**

自己即是服务消费者，同时也是服务提供者，同步调用等待结果导致资源耗尽

**解决方案**

服务方：扩容、限流，排查代码问题，增加硬件监控

消费方：使用Hystrix资源隔离，熔断降级，快速失败

<img src="https://tva1.sinaimg.cn/large/0081Kckwly1gmby7y9ykzj30wr0ehac5.jpg" alt="img" style="zoom:150%;" />

**Hystrix断路保护器的作用**

- **封装请求**会将用户的操作进行统一封装，统一封装的目的在于进行统一控制。
- **资源隔离限流**会将对应的资源按照指定的类型进行隔离，比如**线程池**和**信号量**。
  - 计数器限流，例如5秒内技术1000请求，超数后限流，未超数重新计数
  - 滑动窗口限流，解决计数器不够精确的问题，把一个窗口拆分多滚动窗口
  - 令牌桶限流，类似景区售票，售票的速度是固定的，拿到令牌才能去处理请求
  - 漏桶限流，生产者消费者模型，实现了恒定速度处理请求，能够绝对防止突发流量
- **失败回退**其实是一个备用的方案，就是说当请求失败后，有没有备用方案来满足这个请求的需求。
- **断路器**这个是**最核心**的，，如果断路器处于打开的状态，那么所有请求都将失败，执行回退逻辑。如果断路器处于关闭状态，那么请求将会被正常执行。有些场景我们需要手动**打开断路器强制降级**。
- **指标监控**会对请求的生**命周期进行监控**，请求成功、失败、超时、拒绝等状态，都会被监控起来。

**Hystrix使用上遇到的坑**

- 配置可以对接**配置中心**进行动态调整

  Hystrix 的配置项非常多，如果不对接配置中心，所有的配置只能在代码里修改，在集群部署的难以应对紧急情况，我们项目只设置一个 CommandKey，其他的都在配置中心进行指定，紧急情况如需隔离部分请求时，只需在配置中心进行修改以后，强制更新即可。

- 回退逻辑中可以**手动埋点**或者通过**输出日志**进行告警

  当请求失败或者超时，会执行回退逻辑，如果有大量的回退，则证明某些服务出问题了，这个时候我们可以在回退的逻辑中进行埋点操作，上报数据给监控系统，也可以输出回退的日志，统一由日志收集的程序去进行处理，这些方式都可以将问题暴露出去，然后通过实时数据分析进行告警操作

- 用 **ThreadLocal**配合**线程池隔离**模式需当心

  当我们用了线程池隔离模式的时候，被隔离的方法会包装成一个 Command 丢入到独立的线程池中进行执行，这个时候就是从 A 线程切换到了 B 线程，ThreadLocal 的数据就会丢失

- **Gateway中**多用信号量隔离

  网关是所有请求的入口，路由的服务数量会很多，几十个到上百个都有可能，如果用线程池隔离，那么需要创建上百个独立的线程池，开销太大，用信号量隔离开销就小很多，还能起到限流的作用。

  

[^常见问题]: Hystrix的超时时间要⼤于Ribbon的超时时间，因为Hystrix将请求包装了起来，特别需要注意的是，如果Ribbon开启了重试机制，⽐如重试3 次，Ribbon 的超时为 1 秒，那么Hystrix 的超时时间应该⼤于 3 秒，否则就会出现 Ribbon 还在重试中，⽽ Hystrix 已经超时的现象。



**Sentinel** 

> Sentinel是⼀个⾯向云原⽣微服务的流量控制、熔断降级组件。
>
> 替代Hystrix，针对问题：服务雪崩、服务降级、服务熔断、服务限流

Hystrix区别：

- 独⽴可部署Dashboard（基于 Spring Boot 开发）控制台组件
- 不依赖任何框架/库，减少代码开发，通过UI界⾯配置即可完成细粒度控制

<img src="https://tva1.sinaimg.cn/large/0081Kckwly1gmbza4zixbj30kl09sq4p.jpg" alt="image-20210104212151598" style="zoom:80%;" />

**丰富的应⽤场景**：Sentinel 承接了阿⾥巴巴近 10 年的双⼗⼀⼤促流量的核⼼场景，例如秒杀、消息削峰填⾕、集群流量控制、实时熔断下游不可⽤应⽤等。

**完备的实时监控**：可以看到500 台以下规模的集群的汇总也可以看到单机的秒级数据。

**⼴泛的开源⽣态：**与 SpringCloud、Dubbo的整合。您只需要引⼊相应的依赖并进⾏简单的配置即可快速地接⼊ Sentinel。

**区别：**

- Sentinel不会像Hystrix那样放过⼀个请求尝试⾃我修复，就是明明确确按照时间窗⼝来，熔断触发后，时间窗⼝内拒绝请求，时间窗⼝后就恢复。
- Sentinel Dashboard中添加的规则数据存储在内存，微服务停掉规则数据就消失，在⽣产环境下不合适。可以将Sentinel规则数据持久化到Nacos配置中⼼，让微服务从Nacos获取。

| #              | Sentinel                                       | Hystrix                       |
| -------------- | ---------------------------------------------- | ----------------------------- |
| 隔离策略       | 信号量隔离                                     | 线程池隔离/信号量隔离         |
| 熔断降级策略   | 基于响应时间或失败比率                         | 基于失败比率                  |
| 实时指标实现   | 滑动窗口                                       | 滑动窗口（基于 RxJava）       |
| 扩展性         | 多个扩展点                                     | 插件的形式                    |
| 限流           | 基于 QPS，支持基于调用关系的限流               | 不支持                        |
| 流量整形       | 支持慢启动、匀速器模式                         | 不支持                        |
| 系统负载保护   | 支持                                           | 不支持                        |
| 控制台         | 开箱即用，可配置规则、查看秒级监控、机器发现等 | 不完善                        |
| 常见框架的适配 | Servlet、Spring Cloud、Dubbo、gRPC             | Servlet、Spring Cloud Netflix |





#### Config / Nacos

> Nacos是阿⾥巴巴开源的⼀个针对微服务架构中**服务发现**、**配置管理**和**服务管理平台**。
>
> Nacos就是**注册中⼼+配置中⼼**的组合（Nacos=Eureka+Confifig+Bus）

**Nacos**功能特性

- 服务发现与健康检查
- 动态配置管理
- 动态DNS服务
- 服务和元数据管理

**保护阈值：**

当服务A健康实例数/总实例数 < 保护阈值 的时候，说明健康实例真的不多了，这个时候保护阈值会被触发（状态true），nacos将会把该服务所有的实例信息（健康的+不健康的）全部提供给消费者，消费者可能访问到不健康的实例，请求失败，但这样也⽐造成雪崩要好，牺牲了⼀些请求，保证了整个系统的⼀个可⽤。

**Nacos** 数据模型（领域模型）

- **Namespace** 代表不同的环境，如开发dev、测试test、⽣产环境prod
- **Group** 代表某项⽬，⽐如爪哇云项⽬
- **Service** 某个项⽬中具体xxx服务
- **DataId** 某个项⽬中具体的xxx配置⽂件

可以通过 Spring Cloud 原⽣注解 `@RefreshScope` 实现配置⾃动更新



#### Bus / Stream

> Spring Cloud Stream 消息驱动组件帮助我们更快速，更⽅便的去构建**消息驱动**微服务的
>
> 本质：屏蔽掉了底层不同**MQ**消息中间件之间的差异，统⼀了**MQ**的编程模型，降低了学习、开发、维护**MQ**的成本，⽬前⽀持Rabbit、Kafka两种消息



#### **Sleuth / Zipkin**

**全链路追踪**

<img src="https://tva1.sinaimg.cn/large/0081Kckwly1gmc3avezqrj30xb0lw76z.jpg" alt="image-20210104234058218" style="zoom:67%;" />

**Trace ID**：当请求发送到分布式系统的⼊⼝端点时，Sleuth为该请求创建⼀个唯⼀的跟踪标识Trace ID，在分布式系统内部流转的时候，框架始终保持该唯⼀标识，直到返回给请求⽅

**Span ID**：为了统计各处理单元的时间延迟，当请求到达各个服务组件时，也是通过⼀个唯⼀标识SpanID来标记它的开始，具体过程以及结束。

Spring Cloud Sleuth （追踪服务框架）可以追踪服务之间的调⽤，Sleuth可以记录⼀个服务请求经过哪些服务、服务处理时⻓等，根据这些，我们能够理清各微服务间的调⽤关系及进⾏问题追踪分析。

**耗时分析**：通过 Sleuth 了解采样请求的耗时，分析服务性能问题（哪些服务调⽤⽐较耗时）

**链路优化**：发现频繁调⽤的服务，针对性优化等

**聚合展示**：数据信息发送给 Zipkin 进⾏聚合，利⽤ Zipkin 存储并展示数据。



### **安全认证**

- Session

  认证中最常用的一种方式，也是最简单的。存在**多节点session丢失**的情况，可通过**nginx粘性Cookie**和Redis集中式Session存储解决

- HTTP Basic Authentication 

  服务端针对请求头中base64加密的Authorization 和用户名和密码进行**校验**。

- Token

  Session 只是一个 key，**会话信息存储在后端**。而 Token 中会存储用户的信息，然后通过加密算法进行加密，只有服务端才能解密，**服务端拿到 Token 后进行解密获取用户信息**。

- JWT认证

> JWT（JSON Web Token）用户提供用户名和密码给认证服务器，服务器验证用户提交信息的合法性；如果验证成功，会产生并返回一个 Token，用户可以使用这个 Token 访问服务器上受保护的资源。

<img src="http://s0.lgstatic.com/i/image2/M01/AB/87/CgotOV3WUG2ARl98AAD_xcd-ElM857.png" alt="img" style="zoom:70%;" />

1. 认证服务提供认证的 API，校验用户信息，返回认证结果
2. 通过JWTUtils中的RSA算法，生成JWT token，token里封装用户id和有效期
3. 服务间参数通过请求头进行传递，服务内部通过 ThreadLocal 进行上下文传递。
4. Hystrix导致ThreadLocal失效的问题可以通过，重写 Hystrix 的 Callable 方法，传递需要的数据。

**Token最佳实践**

- 设置**较短（合理）的过期时间**。

- 注销的 Token **及时清除**（放入 Redis 中做一层过滤）。

  虽然不能修改 Token 的信息，但是能在验证层面做一层过滤来进行处理。

- 监控 Token 的**使用频率**。

  为了防止数据被别人爬取，最常见的就是监控使用频率，程序写出来的爬虫程序访问频率是有迹可循的 

- 核心功能敏感操作可以使用**动态验证**（验证码）。

  比如提现的功能，要求在提现时再次进行验证码的验证，防止不是本人操作。

- **网络环境、浏览器**信息等识别。

  银行 APP 对环境有很高的要求，使用时如果断网，APP 会自动退出，重新登录，因为网络环境跟之前使用的不一样了，还有一些浏览器的信息之类的判断，这些都是可以用来保证后端 API 的安全。

- **加密密钥**支持动态修改。

  如果 Token 的加密密钥泄露了，也就意味着别人可以伪造你的 Token，可以将密钥存储在配置中心，以支持动态修改刷新，需要注意的是建议在流量低峰的时候去做更换的操作，否则 Token 全部失效，所有在线的请求都会重新申请 Token，并发量会比较大。



### 灰度发布

**痛点：**

- 服务数量多，业务变动频繁，一周一发布

- 灰度发布能降低发布失败风险，**减少影响范围**

  通过灰度发布，先让一部分用户体验新的服务，或者只让测试人员进行测试，等功能正常后再全部发布，这样能降低发布失败带来的影响范围。 

- 当发布出现故障时，可以**快速回滚**，不影响用户

  灰度后如果发现这个节点有问题，那么只需回滚这个节点即可，当然不回滚也没关系，通过灰度策略隔离，也不会影响正常用户

可以通过Ribbon的负载均衡策略进行灰度发布，可以使用更可靠的Discovery

**Discovery**

> 基于Discovery 服务注册发现、Ribbon 负载均衡、Feign 和 RestTemplate 调用等组件的企业级微服务开源解决方案，包括灰度发布、灰度路由、服务隔离等功能

<img src="https://s0.lgstatic.com/i/image3/M01/54/41/CgpOIF3nXSaAB9bRAAE8rktrUyY037.png" alt="img" style="zoom:50%;" />

1. 首先将需要发布的服务从转发过程中移除，等流量剔除之后再发布。

2. 部分机器中的版本进行升级，用户默认还是请求老的服务，通过版本来支持测试请求。

3. 测试完成之后，让新的版本接收正常流量，然后部署下一个节点，以此类推。

```java
grayVersions = {"discovery-article-service":["1.01"]}
```



### 多版本隔离



<img src="https://s0.lgstatic.com/i/image3/M01/54/41/Cgq2xl3nXSeAZMTOAAE2sCaIhPE668.png" alt="img" style="zoom:50%;" />



**本地复用测试服务**-Eureka Zone亮点

​	**region** 地理上的分区，比如北京、上海等

​	**zone** 可以简单理解为 region 内的具体机房

​	在调用的过程中会优先选择相同的 zone 发起调用，当找不到相同名称的 zone 时会选择其他的 zone 进行调用，我们可以利用这个特性来解决本地需要启动多个服务的问题。

[^]: 当你访问修改的服务 A 时，这个服务依赖了 B、C 两个服务，B 和 C 本地没有启动，B 和 C 找不到相同的 zone 就会选择其他的 zone 进行调用，也就是会调用到测试环境部署的 B 和 C 服务，这样一来就解决了本地部署多个服务的问题。



#### **各组件调优**

当你对网关进行压测时，会发现并发量一直上不去，错误率也很高。因为你用的是默认配置，这个时候我们就需要去调整配置以达到最优的效果。

首先我们可以对容器进行调优，最常见的就是**内置的 Tomcat** 容器了，

```java
server.tomcat.accept-count //请求队列排队数
server.tomcat.max-threads //最大线程数
server.tomcat.max-connections //最大连接数
```

**Hystrix** 的信号量（semaphore）隔离模式，并发量上不去很大的原因都在这里，信号量默认值是 100，也就是最大并发只有 100，超过 100 就得等待。

```java
//信号量
zuul.semaphore.max-semaphores //信号量：最大并发数
//线程池
hystrix.threadpool.default.coreSize //最大线程数
hystrix.threadpool.default.maximumSize //队列的大
hystrix.threadpool.default.maxQueueSize //等参数
```

配置**Gateway**并发信息，

```java
gateway.host.max-per-route-connections //每个路由的连接数 
gateway.host.max-total-connections //总连接数
```

调整**Ribbon** 的并发配置，

```java
ribbon.MaxConnectionsPerHost //单服务并发数
ribbon.MaxTotalConnections   //总并发数
```

修改**Feign**默认的HttpURLConnection 替换成 httpclient 来提高性能

```java
feign.httpclient.max-connections-per-route//每个路由的连接数
feign.httpclient.max-connections //总连接数
```

Gateway+配置中心实现动态路由

Feign+配置中心实现动态日志