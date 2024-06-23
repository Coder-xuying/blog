## SSM整合基本配置

#### Maven配置

**包依赖：**

```xml
   <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
        </dependency>
       
         <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.12</version>
        </dependency>
       
        <!--数据库驱动-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>5.1.47</version>
        </dependency>
       
        <!-- 数据库连接池 -->
        <dependency>
            <groupId>com.mchange</groupId>
            <artifactId>c3p0</artifactId>
            <version>0.9.5.2</version>
        </dependency>
       
        <!--Servlet - JSP -->
        <dependency>
            <groupId>javax.servlet.jsp</groupId>
            <artifactId>jsp-api</artifactId>
            <version>2.1</version>
        </dependency>
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>servlet-api</artifactId>
            <version>3.0-alpha-1</version>
        </dependency>
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>jstl</artifactId>
            <version>1.2</version>
        </dependency>

        <!--Mybatis-->
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
       
        <!--Spring-->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-webmvc</artifactId>
            <version>5.1.9.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-jdbc</artifactId>
            <version>5.1.9.RELEASE</version>
        </dependency>

      
    </dependencies>
```

**静态资源过滤问题**

```xml
<!--静态资源-->
    <build>
        <resources>
            <resource>
                <directory>src/main/java</directory>
                <includes>
                    <include>**/*.properties</include>
                    <include>**/*.xml</include>
                </includes>
                <filtering>false</filtering>
            </resource>
            <resource>
                <directory>src/main/resources</directory>
                <includes>
                    <include>**/*.properties</include>
                    <include>**/*.xml</include>
                </includes>
                <filtering>false</filtering>
            </resource>
        </resources>
    </build>
```



#### Model层

**`database.properties`**:数据库连接的配置

```properties
jdbc.driver=com.mysql.cj.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:3306/ssmbuild?serverTimezone=UTC&characterEncoding=utf8
jdbc.username=root
jdbc.password=root
```

**`mybatis-config.xml`:**mybatis的设置

别名和XXXmapper文件

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>

    <typeAliases>
        <package name="com.xy.pojo"/>
    </typeAliases>
    <mappers>
        <mapper class="com.xy.mapper.BookMapper"/>
    </mappers>
</configuration>
```



**`spring-dao.xml`** :spring整合mybatis：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">

<!--    读取数据库配置文件-->
    <context:property-placeholder location="classpath:database.properties"/>
<!--    数据库连接池-->
    <bean id="dataSource"
          class="com.mchange.v2.c3p0.ComboPooledDataSource">
        <!-- 配置连接池属性 -->
        <property name="driverClass" value="${jdbc.driver}"/>
        <property name="jdbcUrl" value="${jdbc.url}"/>
        <property name="user" value="${jdbc.username}"/>
        <property name="password" value="${jdbc.password}"/>
        <!-- 关闭连接后不自动commit -->
        <property name="autoCommitOnClose" value="false"/>
    </bean>

<!--  sqlSessionfactory -->
    <bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
        <property name="dataSource" ref="dataSource"/>
        
        <!--  绑定mybatis的配置文件 -->
        <property name="configLocation" value="classpath:mybatis-config.xml"/>
    </bean>

      <!--  配置dao接口扫描包，动态实现Dao接口注入到spring容器中 -->
    <bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
        <property name="sqlSessionFactoryBeanName" value="sqlSessionFactory"/>
      <!--   这个用的是ref
  		<property name="sqlSessionFactoryBean" ref="sqlSessionFactory"/>  
		-->
        <property name="basePackage" value="com.xy.mapper"/>
    </bean>

</beans>
```

接口：

`XXMapper.java` 接口

```java
//@Param指定传过来参数的名字，在实现的xml文件中可以在数据库语句中使用
public interface BookMapper {
	// 增加
     int addBook(Books book);
    // 删除
     int deleteBook(@Param("bookID") int id);
    // 修改
    int updateBook(Books book);
    // 查询
    List<Books> getBooks();
    // 查询
    Books getBookByID(@Param("bookID") int id);
}
```

接口实现:

`XXXMapper.xml`:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Confg 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.xy.mapper.BookMapper">
    <insert id="addBook" parameterType="com.xy.pojo.Books">
        insert into books (bookName, bookCounts, detail) VALUES (#{bookName},#{bookCount},#{bookCount})
    </insert>

    <delete id="deleteBook" parameterType="java.lang.Integer">
        delete from books where bookID = #{bookID}
    </delete>
    
    <update id=" updateBook" parameterType="Books">
        update books
        set bookName = #{bookName} ,bookCounts = #{bookCount} ,detail = #{detail}
        where bookID = #{bookID}
    </update>
    
    <select id="getBooks" resultType="Books">
        select * from books
    </select>

    <select id="getBookByID"  resultType="Books">
        select * from books where bookID = #{bookID}
    </select>
    
</mapper>
```

#### Controller层

`BookService.java`

```java
public interface BookService {
    //    增加
    int addBook(Books book);
    //删除
    int  deleteBook( int id);
    //update one book
    int updateBook(Books book);
    // get all books
    List<Books> getBooks();
    //
    Books getBookByID( int id);
}
```

`BookServiceImpl.java`

```java
import java.util.List;

public class BookServiceImpl implements BookService {
    private BookMapper bookMapper;
    
    public void setBookMapper(BookMapper bookMapper) {
        this.bookMapper = bookMapper;
    }

    public int addBook(Books book) {
        return bookMapper.addBook(book);
    }

    public int deleteBook(int id) {
        return bookMapper.deleteBook(id);
    }

    public int updateBook(Books book) {
        return bookMapper.updateBook(book);
    }

    public List<Books> getBooks() {
        return bookMapper.getBooks();
    }

    public Books getBookByID(int id) {
        return bookMapper.getBookByID(id);
    }
}
```

装入bean中：

`spring-service.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">

    <context:component-scan base-package="com.xy.service"/>

    <bean id="BookServiceImpl" class="com.xy.service.BookServiceImpl">
      <property name="bookMapper" ref="bookMapper"/>
    </bean>

    <!-- 声明式事务-->
    <bean class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
        <property name="dataSource" ref="dataSource"/>
    </bean>

</beans>
```

`BookController.java`

```java
@Controller
@RequestMapping("Book")
public class BookController {
    @Autowired
    @Qualifier("BookServiceImpl")
    private BookService bookService;

    @RequestMapping("/allBook")
    public String list(Model model){
        List<Books> books = bookService.getBooks();
        model.addAttribute("list", books);
        return "allBook";
    }
}
```



#### View层

`spring-mvc.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:mvc="http://www.springframework.org/schema/mvc"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/mvc https://www.springframework.org/schema/mvc/spring-mvc.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">

<!--    1.开启注解驱动-->
    <mvc:annotation-driven/>
<!--    2.静态资源默认servlet配置-->
    <mvc:default-servlet-handler/>
<!--    3.扫描web相关的bean-->
    <context:component-scan base-package="com.xy.controller"/>
<!--    4.配置视图解析器 -->
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/jsp/"/>
        <property name="suffix" value=".jsp"/>
    </bean>
    
</beans>
```


总体`applicationContext.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <import resource="spring-dao.xml"/>
    <import resource="spring-mvc.xml"/>
    <import resource="spring-service.xml"/>
</beans>
```

`web.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
    <!--DispatcherServlet-->
    <servlet>
        <servlet-name>DispatcherServlet</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <!--一定要注意:我们这里加载的是总的配置文件-->
            <param-value>classpath:applicationContext.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>
    
    <servlet-mapping>
        <servlet-name>DispatcherServlet</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
    
    
    
    <!--encodingFilter 过滤器，解决乱码问题-->
    <filter>
        <filter-name>encodingFilter</filter-name>
        <filter-class>
            org.springframework.web.filter.CharacterEncodingFilter
        </filter-class>
        <init-param>
            <param-name>encoding</param-name>
            <param-value>utf-8</param-value>
        </init-param>
    </filter>
    <filter-mapping>
        <filter-name>encodingFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
    
    <!--Session过期时间-->
    <session-config>
        <session-timeout>15</session-timeout>
    </session-config>
</web-app>

```


