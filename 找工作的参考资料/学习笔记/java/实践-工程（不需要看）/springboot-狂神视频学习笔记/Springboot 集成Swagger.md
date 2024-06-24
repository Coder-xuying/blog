### Springboot 集成Swagger

#### 1、导入依赖

```xml
<!-- https://mvnrepository.com/artifact/io.springfox/springfox-swagger2 -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>


<!-- https://mvnrepository.com/artifact/io.springfox/springfox-swagger-ui -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.9.2</version>
</dependency>

```

> 开启

```java
@Configuration
@EnableSwagger2
public class SwaggerConfig {

}
```

http://localhost:8080/swagger-ui.html  访问即可

#### 2、配置Swagger

`SwaggerConfig.java`

```java
package com.xy.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;
import org.springframework.core.env.Profiles;
import org.springframework.stereotype.Controller;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.service.VendorExtension;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;
import java.util.ArrayList;

@Configuration
@EnableSwagger2
public class SwaggerConfig {

    @Bean
    public Docket docket(Environment environment){
        /**Environment environment  来判断外部环境配置
         * Profiles.of("dev", "test");  是否在这两个环境下
         * environment.acceptsProfiles(profiles);  如果在，这里就是true，反之则为false
         */
        Profiles profiles = Profiles.of("dev", "test");
        boolean flag = environment.acceptsProfiles(profiles);

        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(apiInfo())
                // .enable(false)  是否启动Swagger  如果为false则无法在浏览器中访问Swagger
                .select()
                /**
                 * RequestHandlerSelectors 扫描的方法
                 * basePackage()：扫描指定包  com.xy.controller
                 * any() 扫描所有
                 * none() 不扫描
                 * withClassAnnotation() 扫描类上的注解，参数是注解的反射对象  Controller.class
                 * withMethodAnnotation() 扫描方法上的注解
                 */
                .apis(RequestHandlerSelectors.basePackage("com.xy.controller"))
                .paths(PathSelectors.ant("/xy/*"))   //指定扫描的路径    /xy 请求
                .build()
                ;
    }

    private ApiInfo apiInfo(){
        Contact contact = new Contact("徐颖 ", "www.xuying.com", "985670");

        return  new ApiInfo("徐颖的SwaggerAPI文档",
                "Api Documentation",
                "1.0", "https://xuyingcool.github.io/",
                contact, "Apache 2.0",
                "http://www.apache.org/licenses/LICENSE-2.0",
                new ArrayList<VendorExtension>()
        );

    }
}

```

#### 3、各种注解

##### **Contoller 里的注解**

```java
@GetMapping("hello2")
@ApiOperation("带参数的hello")
public String hello(@ApiParam("用户名的属性") String username){
    return "hello"+ username;
}
```

```java
@ApiOperation("带参数的hello")
```

![image-20210610110932706](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210610110932.png)

```java
public String hello(@ApiParam("用户名的属性") String username){
    return "hello"+ username;
}
```

![image-20210610110939600](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210610110939.png)

##### 实体类的注解

```java
#controller类里面的必须返回实体类才能将api文档放进Swagger页面里
# return new User();

@PostMapping("testPojo")
public User testUser(){
    return new User();
}
```

```java
@ApiModel("用户类")
public class User {
    @ApiModelProperty("账号")
    public String username;

    @ApiModelProperty("密码")
    public String password;
}
```

![image-20210610111010235](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210610111010.png)