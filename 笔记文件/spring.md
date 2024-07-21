# Spring

#### 1.springboot的自动配置原理

自动装配可以简单理解为：**通过注解或者一些简单的配置就能在 Spring Boot 的帮助下实现某块功能。**

先看一下 SpringBoot 的核心注解 `SpringBootApplication`  

上面那个注解里面有 `@Configuration`、`@EnableAutoConfiguration`、`@ComponentScan` 注解的集合



- `@EnableAutoConfiguration`：启用 SpringBoot 的自动配置机制   **是实现自动装配的重要注解，我们以这个注解入手**
- `@Configuration`：允许在上下文中注册额外的 bean 或导入其他配置类
- `@ComponentScan`： 扫描被`@Component` (`@Service`,`@Controller`)注解的 bean，注解默认会扫描启动类所在的包下所有的类 ，可以自定义不扫描某些 bean。



@EnableAutoConfiguration 有AutoConfigurationImportSelector，

自动装配核心功能的实现实际是通过 `AutoConfigurationImportSelector`类。 加载自动装配类

`AutoConfigurationImportSelector` 类里面有个方法 (`selectImports`方法)，该方法主要用于**获取所有符合条件的类的全限定类名，这些类需要被加载到 IoC 容器中**。



#### [1.Spring AOP 和 AspectJ AOP 有什么区别？](https://snailclimb.gitee.io/javaguide/#/docs/system-design/framework/spring/Spring常见问题总结?id=spring-aop-和-aspectj-aop-有什么区别？)

**Spring AOP 属于运行时增强，而 AspectJ 是编译时增强。** Spring AOP 基于代理(Proxying)，而 AspectJ 基于字节码操作(Bytecode Manipulation)。

Spring AOP 已经集成了 AspectJ ，AspectJ 应该算的上是 Java 生态系统中最完整的 AOP 框架了。AspectJ 相比于 Spring AOP 功能更加强大，但是 Spring AOP 相对来说更简单，

如果我们的切面比较少，那么两者性能差异不大。但是，当切面太多的话，最好选择 AspectJ ，它比 Spring AOP 快很多





### SpringBean

#### springBean的作用域

- **singleton** : 唯一 bean 实例，Spring 中的 bean 默认都是单例的，对单例设计模式的应用。
- **prototype** : 每次请求都会创建一个新的 bean 实例。
- **request** : 每一次 HTTP 请求都会产生一个新的 bean，该 bean 仅在当前 HTTP request 内有效。
- **session** : 每一次 HTTP 请求都会产生一个新的 bean，该 bean 仅在当前 HTTP session 内有效。
- **global-session** ： 全局 session 作用域，仅仅在基于 portlet 的 web 应用中才有意义，Spring5 已经没有了。Portlet 是能够生成语义代码(例如：HTML)片段的小型 Java Web 插件。它们基于 portlet 容器，可以像 servlet 一样处理 HTTP 请求。但是，与 servlet 不同，每个 portlet 都有不同的会话。



#### [@Component 和 @Bean 的区别是什么？](https://snailclimb.gitee.io/javaguide/#/docs/system-design/framework/spring/Spring常见问题总结?id=component-和-bean-的区别是什么？)

1. `@Component` 注解作用于类，而`@Bean`注解作用于方法。
2. `@Component`通常是通过类路径扫描来自动侦测以及自动装配到 Spring 容器中（我们可以使用 `@ComponentScan` 注解定义要扫描的路径从中找出标识了需要装配的类自动装配到 Spring 的 bean 容器中）。`@Bean` 注解通常是我们在标有该注解的方法中定义产生这个 bean,`@Bean`告诉了 Spring 这是某个类的实例，当我需要用它的时候还给我。
3. `@Bean` 注解比 `@Component` 注解的自定义性更强，而且很多地方我们只能通过 `@Bean` 注解来注册 bean。比如当我们引用第三方库中的类需要装配到 `Spring`容器时，则只能通过 `@Bean`来实现。

#### Bean的生命周期

![image-20210908161818758](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210908161818.png)



#### Spring框架中有哪些设计模式

- **工厂设计模式** : Spring 使用工厂模式通过 `BeanFactory`、`ApplicationContext` 创建 bean 对象。
- **代理设计模式** : Spring AOP 功能的实现。
- **单例设计模式** : Spring 中的 Bean 默认都是单例的。

### [Spring 事务](https://snailclimb.gitee.io/javaguide/#/docs/system-design/framework/spring/Spring常见问题总结?id=spring-事务)

#### Spring 管理事务的方式有几种？

- **编程式事务** ： 在代码中硬编码(不推荐使用) : 通过 `TransactionTemplate`或者 `TransactionManager` 手动管理事务，实际应用中很少使用，但是对于你理解 Spring 事务管理原理有帮助。
- **声明式事务** ： 在 XML 配置文件中配置或者直接基于注解（推荐使用） : 实际是通过 AOP 实现（基于`@Transactional` 的全注解方式使用最多）



#### Spring事务的传播级别

****PROPAGATION_REQUIRED\**** ，默认的spring事务传播级别，如果上下文中已经存在事务，那么就加入到事务中执行，如果当前上下文中不存在事务，则新建事务执行。

****PROPAGATION_REQUIRES_NEW\**** ，每次都要一个新事务，该传播级别的特点是，每次都会新建一个事务，并且同时将上下文中的事务挂起，执行当前新建事务完成以后，上下文事务恢复再执行。

****PROPAGATION_SUPPORTS\**** ，如果上下文存在事务，则支持事务加入事务，如果没有事务，则使用非事务的方式执行。

****PROPAGATION_NOT_SUPPORTED\**** ，上下文中存在事务，则挂起事务，执行当前逻辑，结束后恢复上下文的事务。

****PROPAGATION_MANDATORY\**** ， 该级别的事务要求上下文中必须要存在事务，否则就会抛出异常！

****PROPAGATION_NEVER\****，上下文中不能存在事务，一旦有事务，就抛出runtime异常，强制停止执行！

****PROPAGATION_NESTED\**** ，如果上下文中存在事务，则嵌套事务执行，如果不存在事务，则新建事务。



> 什么是嵌套事务

子事务套在父事务中执行，子事务是父事务的一部分，在进入子事务之前，父事务建立一个回滚点，叫save point，然后执行子事务，这个子事务的执行也算是父事务的一部分，然后子事务执行结束，父事务继续执行。

- 如果子事务回滚，会发生什么？
  - 父事务会回滚到进入子事务前建立的save point，然后尝试其他的事务或者其他的业务逻辑，父事务之前的操作不会受到影响，更不会自动回滚
- 如果父事务回滚，会发生什么？
  - 父事务回滚，子事务也会跟着回滚！为什么呢，因为父事务结束之前，子事务是不会提交的，我们说子事务是父事务的一部分，正是这个道理。
- 事务的提交，是什么情况？
  - 子事务先提交，父事务再提交