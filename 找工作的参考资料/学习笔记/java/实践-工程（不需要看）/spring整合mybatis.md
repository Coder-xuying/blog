### spring整合mybatis

**spring-mybatisxml**

负责数据库的配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<!--  配置数据源  -->
    <bean id="datasource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
        <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
        <property name="url" value="jdbc:mysql://localhost:3306/how2java?characterEncoding=UTF-8"/>
        <property name="username" value="root"/>
        <property name="password" value="admin"/>
    </bean>

    <!--        sqlSessionFactory-->
    <bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
        <property name="dataSource" ref="datasource"/>
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

**applicationContext.xml**

专注于spring的注册

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
<!--    dataSource-->
    <import resource="spring-dao.xml"/>

    <bean id="userMapperImpl" class="com.xy.mapper.UserMapperImpl">
        <property name="sqlSession" ref="sqlSessionTemplate"/>
    </bean>

</beans>
```

**UserMapper.java**

```java
public interface UserMapper {
    List<User> userList();
}
```

 **UserMapperImpl.java **

整合多了一个实现类

```java
public class UserMapperImpl implements UserMapper {
    private SqlSessionTemplate sqlSession;

    public void setSqlSession(SqlSessionTemplate sqlSession) {
        this.sqlSession = sqlSession;
    }
    @Override
    public List<User> userList() {
        UserMapper mapper = sqlSession.getMapper(UserMapper.class);
        //直接return这个方法
        return mapper.userList();
    }
}
```

**Test**

```java
//测试
ApplicationContext applicationContext = new ClassPathXmlApplicationContext("ApplicationContext.xml");
        UserMapper mapper = applicationContext.getBean("userMapperImpl", UserMapper.class);
        List<User> users = mapper.userList();
```



