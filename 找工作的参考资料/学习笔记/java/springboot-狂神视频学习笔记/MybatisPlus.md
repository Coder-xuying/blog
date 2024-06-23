### MybatisPlus

#### 1、快速入门

```yml
spring:
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    username: root
    password: admin
    url: jdbc:mysql://localhost:3306/mybatisplus?characterEncoding=utf-8&useSSL=false
配置数据库
```

`UserMapper.java`

```java
#extends BaseMapper<User>  这里面是MybatisPlus写的方法，可以直接使用
@Repository
public interface UserMapper extends BaseMapper<User> {

}
```



#### 2、配置日志

```yml
mybatis-plus:
  configuration:
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
```

#### 3、CRUD扩展

##### 3.1 插入

> insert

```java
userMapper.insert(new User());
```

会发现这个ID，是自动生成的

**主键生成策略**：

> 默认 ID_WORKER 全局唯一id

**雪花算法**： 

snowflake是Twitter开源的分布式ID生成算法，结果是一个long型的ID。其核心思想是：使用41bit作为 毫秒数，10bit作为机器的ID（5个bit是数据中心，5个bit的机器ID），12bit作为毫秒内的流水号（意味 着每个节点在每毫秒可以产生 4096 个 ID），最后还有一个符号位，永远是0。可以保证几乎全球唯 一！

> 主键自增

我们需要配置主键自增：

```java
@TableId(type = IdType.AUTO)
private Long id;
```

==数据库字段一定要设置成自增！==

`IdType 类型`

```java

//数据库ID自增
AUTO(0),

//该类型为未设置主键类型 
NONE(1),

//用户输入ID
//该类型可以通过自己注册自动填充插件进行填充
INPUT(2),

/* 以下3种类型、只有当插入对象ID 为空，才自动填充。 */

//全局唯一ID (idWorker)
ID_WORKER(3),


//全局唯一ID (UUID)

UUID(4),

//字符串全局唯一ID (idWorker 的字符串表示)
ID_WORKER_STR(5);
```

##### 3.2 自动填充

创建时间、修改时间！这些个操作一遍都是自动化完成的，我们不希望手动更新！ 

阿里巴巴开发手册：所有的数据库表：gmt_create、gmt_modified几乎所有的表都要配置上！而且需 要自动化！

> 代码

1. 先在数据库中增加两个字段`gmt_create、gmt_modified`

2. 实体类中同步，并加入注解

   ```java
   @TableField(fill = FieldFill.INSERT)
   private Date createTime;
   
   @TableField(fill = FieldFill.UPDATE)
   private Date updateTime;
   ```

3. 编写处理器

   ```java
   @Component  //将处理器放入到bean中去
   public class MyDataHandler implements MetaObjectHandler {
       //插入时的填充策略
       @Override
       public void insertFill(MetaObject metaObject) {
           this.setFieldValByName("createTime", new Date(), metaObject);
           this.setFieldValByName("updateTime", new Date(), metaObject);
   
       }
   
       @Override
       public void updateFill(MetaObject metaObject) {
           this.setFieldValByName("updateTime", new Date(), metaObject);
       }
   }
   ```



##### 3.3 乐观锁

乐观锁 : 故名思意十分乐观，它总是认为不会出现问题，无论干什么不去上锁！如果出现了问题， 再次更新值测试 

悲观锁：故名思意十分悲观，它总是认为总是出现问题，无论干什么都会上锁！再去操作！

乐观锁实现方式：

- 取出记录，获取当前的version
- 更新时，where version = old_version
- 执行更新时，set version = new_version
- 如果version不对，就更新失败

springboot中怎么开启：

1. 给数据库增加version字段，默认值为1

2. 实体类更新

   ```java
   @Version
   private Integer version;	
   ```

3. 注册组件

   ```java
   // 扫描我们的 mapper 文件夹
   @MapperScan("com.kuang.mapper")
   @EnableTransactionManagement
   @Configuration // 配置类
   public class MyBatisPlusConfig {
   // 注册乐观锁插件
       @Bean
       public OptimisticLockerInterceptor optimisticLockerInterceptor() {
       return new OptimisticLockerInterceptor();
       }
   }
   ```

4. 测试

==乐观锁本质就是修改一次version增加1，然后如果有多个线程抢占同一个资源，那么只生效一次，也就时version只+1一次。==

##### 3.4 查询操作

```java
// 测试批量查询！
@Test
public void testSelectByBatchId(){
    List<User> users = userMapper.selectBatchIds(Arrays.asList(1, 2, 3));
    users.forEach(System.out::println);
}

// 按条件查询之一使用map操作
@Test
public void testSelectByBatchIds(){
    HashMap<String, Object> map = new HashMap<>();
    // 自定义要查询
    map.put("name","狂神说Java");
    map.put("age",3);
    List<User> users = userMapper.selectByMap(map);
    users.forEach(System.out::println);
}
```

##### 3.5 分页查询

springboot配置：

1. 配置拦截器组件

   ```JAVA
   //在configuration 注解的那个类里面
   @Bean
   public PaginationInterceptor paginationInterceptor() {
       return new PaginationInterceptor();
   }
   ```

2. 直接使用page对象

   ```java
   @Test
   public void testPage(){
       // page（1，2） 参数 1：当前页，参数 2：显示的条数
       Page<User> page = new Page<>(1,3);
   
       //通过这个方法查询
       userMapper.selectPage(page,null);
   
       //调用page里的方法，获得查询的记录
       List<User> users = page.getRecords();
       users.forEach(System.out::println);
   }
   ```

   

##### 3.6 删除操作

> 普通的删除

 批量删除和map条件删除,直接调用方法即可

> 逻辑删除

- 数据库中并没有删除这个记录，而是用一个变量来让他失效，deleted   = 0  =》1
- 管理员是能看到所有的记录的

开启：

1. 在数据库表中添加一个`deleted`字段，默认值为0

2. 实体类中更新

   ```java
   @TableLogic //逻辑删除
   private Integer deleted;
   ```

3. 配置逻辑删除组件

   ```java
   @Bean
   public ISqlInjector sqlInjector() {
       return new LogicSqlInjector();
   }
   ```

4. application.properties 配置参数

   ```properties
   # 配置逻辑删除
   mybatis-plus.global-config.db-config.logic-delete-value= 1
   mybatis-plus.global-config.db-config.logic-not-delete-value= 0
   ```

5. 测试，直接使用方法就可以了，mybatisPlus会自动更改的。==逻辑删除的delete会直接变成update，更新deleted字段的值==

#### 4、性能分析插件

1. 导入插件

   ```java
   @Bean
   @Profile({"dev","test"})// 设置 dev test 环境开启，保证我们的效率
   public PerformanceInterceptor performanceInterceptor() {
       PerformanceInterceptor performanceInterceptor = new
           PerformanceInterceptor();
       performanceInterceptor.setMaxTime(100); // ms设置sql执行的最大时间，如果超过了则不执行
       performanceInterceptor.setFormat(true); // 是否格式化代码
       return performanceInterceptor;
   }
   ```

2. 修改配置环境：` spring.profiles.active = dev`

3. 直接测试即可

#### 5、条件构造器Wrapper

用来执行复杂SQl 语句

```java
@Test
void test1(){
    QueryWrapper<User> wrapper = new QueryWrapper<>();
	//链式编程
    wrapper
        .isNotNull("name")    //  isNotNull   不为空
        .ge("age", 10)       //ge  大于和等于
        ;

    List<User> list = userMapper.selectList(wrapper);
    list.forEach(System.out::println);
}


wrapper.eq("name","狂神说");   //eq 等于
wrapper.between("age",20,30);  //年龄在 20 到30之间
// 左和右 t%
wrapper
	.notLike("name","e")        // not like %e%  名字中不含有
	.likeRight("email","t");   //  right  : t%   left  %t

wrapper.inSql("id","select id from user where id<3");   // in查询

// 通过id进行排序
wrapper.orderByAsc("id");
```



#### 6、代码自动生成

直接套用模板，修改一下数据库和需要映射的表就可以了

```java
package com.xy;

import com.baomidou.mybatisplus.annotation.DbType;
import com.baomidou.mybatisplus.annotation.FieldFill;
import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.generator.AutoGenerator;
import com.baomidou.mybatisplus.generator.config.DataSourceConfig;
import com.baomidou.mybatisplus.generator.config.GlobalConfig;
import com.baomidou.mybatisplus.generator.config.PackageConfig;
import com.baomidou.mybatisplus.generator.config.StrategyConfig;
import com.baomidou.mybatisplus.generator.config.po.TableFill;
import com.baomidou.mybatisplus.generator.config.rules.DateType;
import com.baomidou.mybatisplus.generator.config.rules.NamingStrategy;

import java.util.ArrayList;

public class CodeGenerate {
    public static void main(String[] args) {
        // 需要构建一个 代码自动生成器 对象
        AutoGenerator autoGenerator = new AutoGenerator();

        // 配置策略

        // 1、全局配置
        GlobalConfig gc = new GlobalConfig();
        //获取当前项目的路径
        String projectPath = System.getProperty("user.dir");
        //生成文件的位置
        gc.setOutputDir(projectPath+"/src/main/java");
        gc.setAuthor("xuying");
        gc.setOpen(false);
        gc.setFileOverride(false); // 是否覆盖文件
        gc.setServiceName("%sService"); // 去掉Service的I前缀
        gc.setIdType(IdType.ID_WORKER);   //ID的策略
        gc.setDateType(DateType.ONLY_DATE); 
        gc.setSwagger2(true);   //是否开启Swagger
        autoGenerator.setGlobalConfig(gc);

        //2、设置数据源
        DataSourceConfig dsc = new DataSourceConfig();
        dsc.setUrl("jdbc:mysql://localhost:3306/mybatisplus?characterEncoding=utf-8&useSSL=false");
        dsc.setDriverName("com.mysql.jdbc.Driver");
        dsc.setUsername("root");
        dsc.setPassword("admin");
        dsc.setDbType(DbType.MYSQL);
        autoGenerator.setDataSource(dsc);

        //3、包的配置
        PackageConfig pc = new PackageConfig();
        // 模块名称
        pc.setModuleName("blog");
        pc.setParent("com.xy");
        pc.setEntity("pojo");
        pc.setMapper("mapper");
        pc.setService("service");
        pc.setController("controller");
        autoGenerator.setPackageInfo(pc);
        
        //4、策略配置
        StrategyConfig strategy = new StrategyConfig();
        //要映射的表名，即给哪个表创建代码，可以批量
        strategy.setInclude("teacher");  

        //下划线转驼峰命名
        strategy.setNaming(NamingStrategy.underline_to_camel);
        strategy.setColumnNaming(NamingStrategy.underline_to_camel);
        // 自动lombok的配置
        strategy.setEntityLombokModel(true); 
        strategy.setLogicDeleteFieldName("deleted");

        // 5、自动填充配置
        TableFill gmtCreate = new TableFill("gmt_create", FieldFill.INSERT);
        TableFill gmtModified = new TableFill("gmt_modified", FieldFill.INSERT_UPDATE);
        ArrayList<TableFill> tableFills = new ArrayList<>();
        tableFills.add(gmtCreate);
        tableFills.add(gmtModified);
        strategy.setTableFillList(tableFills);

        //6、乐观锁
        strategy.setVersionFieldName("version");

        strategy.setRestControllerStyle(true);
        
        //localhost:8080/hello_id_2 mpg.setStrategy(strategy);
        strategy.setControllerMappingHyphenStyle(true); 
        autoGenerator.setStrategy(strategy);
        autoGenerator.execute();
    }
}

```

