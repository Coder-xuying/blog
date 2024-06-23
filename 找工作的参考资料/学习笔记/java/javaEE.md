## 0、javaWeb

### 1、基本概念

#### 1.1 前言

web开发：

- 静态web
  - html,css
  - 提供给所有人看的数据不会发生变化
- 动态web
  - 每个人在不同的时间，不同的地点，看到的信息都不相同
  - 技术栈;Servlet/jsp, php

#### 1.2 、web应用程序

可以提供浏览器访问的程序

web应用程序编写成功后，要让外界访问，需要一个服务器统一管理。

#### 1.3 静态web

- *.htm,\*.html 都是网页的后缀，

静态web的缺点：

- web页面无法更新，所有用户看到的都是同一个页面
  - 轮播图，点击特效：伪动态-js
- 无法和数据库交互

#### 1.4 动态web

**缺点**：

- 服务器的动态资源出现错误，需要重新编写**后台程序**，重新发布
- 上面的意思就是停机

优点：

- 静态的缺点反过来



asp、jsp/Servlet、php

**PHP**：

- PHP开发速度很快，功能强大，跨平台，代码很简单
- **无法承载大访问量的情况**

**jsp/Servlet**：

- sun公司主推的B/S架构（浏览器和服务器）
- 基于java语言
- 可以承载三高问题
- 语法像ASP，加强竞争

### 2、Tomcat

文件夹的作用

![image-20210504211656692](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210504211656.png)

#### 1. Tomcat启动

启动、关闭



### 3、Http

Http超文本传输协议

- 端口号：80

Https

- 端口号：443

#### 3.1 两个时代

- http1.0
  - 客户端与web服务器连接后，只能获得一个web资源
- Http1.1
  - 客户端与web服务器连接后，可以获得多个web资源

#### 3.2 Http请求、响应

> 请求

```java
Request URL: https://www.baidu.com/    // 请求地址
Request Method: GET					// 请求方法 GET、POST
Status Code: 200 OK					// 状态码
Remote Address: 183.232.231.172:443  // ip地址
    
    
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie:    
```

- 请求行
  - 请求方式 GET、POST
  - 请求方式：GET、POST、DELETE、PUT
    - get能够携带的参数少，大小有限制，会在URL那里显示传入的参数，不安全，高效
    - Post参数多，大小无限制，不显示参数，安全，比get低效
- 请求头
  - Accept：告诉浏览器，支持的数据类型
  - Accept-Encoding  支持哪种编码
  - Accept-Language 语言环境
  - Cache-Control  缓存控制
  - Connection  告诉浏览器是断开还是保持连接

> 响应

```java
Cache-Control: private
Connection: keep-alive
Content-Encoding: gzip
Content-Type: text/html;charset=utf-8

Strict-Transport-Security: max-age=172800
Traceid: 1620301595071424231410286886689025270214
Transfer-Encoding: chunked

```

- 响应体
  - Accept：告诉浏览器，支持的数据类型
  - Accept-Encoding  支持哪种编码
  - Accept-Language 语言环境
  - Cache-Control  缓存控制
  - Connection  告诉浏览器是断开还是保持连接
  - Refresh：告诉客户端，多久刷新一次
  - Location：让网页重新定位
- 响应状态码
  - 200：请求响应成功
  - 3**：请求重定向
    - 重定向：直接
  - 404：找不到资源
  - 5xx：服务器代码错误 
    - 502：网关错误

### 4、Maven

#### 4.1项目架构管理工具

核心思想：约定大于配置

- 有约束不要去违反

Maven规定我们按照它的目录规范编写代码

#### 4.2 安装maven

下载maven并解压

修改环境变量

![image-20210506200740622](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210506200740.png)

```java
path里添加
- %MAVEN_HOME%\bin-
```

修改setting.xml

```xml
<localRepository>D:\environment\apache-maven-3.6.3\maven-repo</localRepository> <!--本地仓库的地址-->

<!--阿里云镜像-->
<mirrors>
	<mirror>
	  <id>aliyunmaven</id>
	  <mirrorOf>*</mirrorOf>
	  <name>阿里云公共仓库</name>
	  <url>https://maven.aliyun.com/repository/public</url>
	</mirror>
</mirrors>
```

#### 4.3 pom文件

```xml
<?xml version="1.0" encoding="UTF-8"?>

<!--maven 版本和头文件-->
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

<!--  我们刚刚配置的gav-->
  <groupId>com.xy</groupId>
  <artifactId>javaWeb-02</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>war</packaging>
<!--  项目打包的方式
   jar包：java应用
   war包：javaweb应用
 -->

<!--配置-->
  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
<!--    编码版本-->
    <maven.compiler.source>1.7</maven.compiler.source>
    <maven.compiler.target>1.7</maven.compiler.target>
  </properties>

<!--  项目依赖-->
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
      <scope>test</scope>
    </dependency>
    
  </dependencies>

  <build>
    <finalName>javaWeb-02</finalName>
    <pluginManagement><!-- lock down plugins versions to avoid using Maven defaults (may be moved to parent pom) -->
      <plugins>
        <plugin>
          <artifactId>maven-clean-plugin</artifactId>
          <version>3.1.0</version>
        </plugin>
        <!-- see http://maven.apache.org/ref/current/maven-core/default-bindings.html#Plugin_bindings_for_war_packaging -->
        <plugin>
          <artifactId>maven-resources-plugin</artifactId>
          <version>3.0.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-compiler-plugin</artifactId>
          <version>3.8.0</version>
        </plugin>
        <plugin>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>2.22.1</version>
        </plugin>
        <plugin>
          <artifactId>maven-war-plugin</artifactId>
          <version>3.2.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-install-plugin</artifactId>
          <version>2.5.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-deploy-plugin</artifactId>
          <version>2.8.2</version>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>
</project>

```

Maven强大的地方在于，可以导入所有的依赖包



### 5、Servlet

#### 5.1、Servlet简介

- Servlet就是sun公司开发动态web的一门技术
- Sun在这些API中提供了一个接口叫做Servlet，如果想开发一个Servlet程序，只需要完成两个小步骤：
  - 编写一个类，实现Servlet接口
  - 把开发好的java类部署到web服务器中

#### 5.2、HelloServelt

==流程==

1. 新建一个maven项目，删去src，这个空的文件目录就是项目空间，可以在下面建module
   1. 父子项目
   2. 父项目的依赖子项目可以直接使用
2. 导入库

> javax.servlet

```xml
<dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>3.1.0</version>
            <scope>provided</scope>
        </dependency>

        <!-- https://mvnrepository.com/artifact/javax.servlet.jsp/javax.servlet.jsp-api -->
        <dependency>
            <groupId>javax.servlet.jsp</groupId>
            <artifactId>javax.servlet.jsp-api</artifactId>
            <version>2.3.1</version>
            <scope>provided</scope>
        </dependency>
```

3. 更新web.xml文件

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
     http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
  <display-name>Archetype Created Web Application</display-name>
</web-app>
```

4. 构建一个Servlet类

![image-20210521145433550](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210521145433.png)

```java
public class HelloServlet extends HttpServlet {
    //由于get或者post只是请求实现的不同方式，可以相互调用，业务逻辑都一样

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        PrintWriter writer = resp.getWriter();
        writer.print("HelloServlet");
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        super.doPost(req, resp);
    }
}
```

5. 编写Servlet的映射

   为什么需要映射：我们写的是java程序，浏览器要能够访问的话，就需要连接web服务器，所以需要在web服务中注册我们写的Servlet，还需要给一个浏览器能够访问的路径

   ```xml
     <servlet>
   <!--    这里的是注册服务的名称-->
       <servlet-name>hello</servlet-name>
       <servlet-class>com.xy.servlet.HelloServlet</servlet-class>
     </servlet>
   
     <servlet-mapping>
   <!--    这里对上面的名称进行映射-->
       <servlet-name>hello</servlet-name>
       <url-pattern>/hello</url-pattern>
     </servlet-mapping>
   ```

#### 5.3、Servlet运行原理

Servlet由web服务器调用，web服务器在收到外部浏览器的请求后，就调用

![image-20210521151313504](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210521151313.png)

#### 5.4、Mapping问题

- 一个Servlet可以对应一个路径

- 一个Servlet可以对应多个路径

  - ```xml
    <servlet-mapping>
    
      <servlet-name>hello</servlet-name>
      <url-pattern>/hello</url-pattern>
    </servlet-mapping>
    ```


        <servlet-mapping>
           
            <servlet-name>hello</servlet-name>
            <url-pattern>/hello2</url-pattern>
        </servlet-mapping>
    ```
      
    ```

- 一个Servlet可以指定通用映射

  - ```xml
        <servlet-mapping>
          
            <servlet-name>hello</servlet-name>
            <url-pattern>/hello/*</url-pattern>
        </servlet-mapping>
    ```

- 默认请求路径

  ```xml
  <servlet-mapping>
          <!--   注意这里就直接跳过.jsp文件了-->
          <servlet-name>hello</servlet-name>
          <url-pattern>/*</url-pattern>
  </servlet-mapping>
  ```

- 指定后缀

  - ```xml
    <!--  
    <servlet-mapping>
    
        <servlet-name>hello</servlet-name>
     		// 这里不能这样写，只能用下面的方式
        <url-pattern>/*.xy</url-pattern>
    </servlet-mapping>
      -->
    <servlet-mapping>
        <!--    这里对上面的名称进行映射-->
        <servlet-name>hello</servlet-name>
        <url-pattern>*.xy</url-pattern>
    </servlet-mapping>
    ```

- 这里有优先级的问题

  - 指定了固定映射的优先级最高，会使通用的失效

#### 5.5、ServletContext

web容器在启动的时候，为所有的Servlet创建了一个ServletContext对象，代表了当前的web应用；

作用：

- 共享数据

  我在这个Servlet中保存的数据，可以在另一个Servlet中拿到

  ```java
  ServletContext servletContext = this.getServletContext();
  servletContext.setAttribute("username","xuying");
  String username = (String) servletContext.getAttribute("username");
  ```

  

> 获取初始化参数

web.xml里

```xml
<context-param>
    <param-name>url</param-name>
    <param-value>jdbc:mysql://localhost:8080/book</param-value>
</context-param>
```

Servlet类获取初始化的参数

```java
ServletContext servletContext = this.getServletContext();
String url = servletContext.getInitParameter("url");
```

> 请求转发

```java
public class ServletDemo02 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        ServletContext context = this.getServletContext();
        context.getRequestDispatcher("/hello").forward(req,resp);
    }
}
```

将请求转发到/hello的服务。**请求转发的时候地址是不变的**。

![image-20210523164542572](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210523164542.png)

A向B寻求资源，但是这个只有C有，于是B去向C请求，然后C返回给B资源，B再返回资源给A。

重定向则不同：

- 重定向中，B告诉A，C才有这个，于是A又去请求C，C返回资源给A

> 读取资源文件

Properties类

- 在java目录下新建properties
- 在resources目录下新建properties

发现，都被打包到了同一个路径下:classes，我们俗称这个路径为classpath；

```java
protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    ServletContext context = this.getServletContext();
    InputStream is = context.getResourceAsStream("/WEB-INF/classes/db.properties");
    Properties properties = new Properties();
    properties.load(is);
    String username = properties.getProperty("username");
    resp.getWriter().print(username);
}
```

#### 5.6、HttpServletResponse

web服务器接收到客户端的http请求，针对这个请求，分别创建一个代表请求的HttpServletRequest和一个代表响应的HttpServletResponse

- 如果要获得客户请求过来的参数，HttpServletRequest
- 给客户端响应一些信息HttpServletResponse

##### 1.简单分类

> 负责向浏览器发送数据的方法

- ```java
  public PrintWriter getWriter()      // 写中文
  public ServletOutputStream getOutputStream()   //写平常的流
  ```

> 负责向浏览器发送响应头的方法

![image-20210523195428061](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210523195428.png)





##### 2.常见应用

> 下载文件

- 获取下载文件的路径
- 下载的文件名是啥
- 设置想办法让浏览器能够支持下载我们需要的东西
- 获取下载文件的输入流
- 获取缓冲区
- 获取outputStream对象
- 将FileOutputStream流写入到buffer缓冲区
- 使用outputStream将缓冲区的数据输出到客户端

```java
public class ServletDemo6  extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String realPath = "F:\\01-代码\\01-java\\javaWebLearn\\servlet-01\\target\\classes\\test.txt";
        System.out.println("下载的文件路径："+realPath);

        String fileName = realPath.substring(realPath.lastIndexOf("\\") + 1);
        // 当文件名为中文时，需要使用URLEncoder.encode 方法对文件名进行重新编码
        resp.setHeader("Content-Disposition","attachment;filename="+ URLEncoder.encode(fileName,"UTF-8"));
        FileInputStream in = new FileInputStream(realPath);
        int len =0;
        byte[] buffer = new byte[1024];

        ServletOutputStream outputStream = resp.getOutputStream();
        while ((len=in.read(buffer))>0){
            outputStream.write(buffer,0,len);
        }
        in.close();
        outputStream.close();
    }  
}
```

##### 3.验证码功能（走项目可以实现一下）

```java
public class ImageServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 如何让浏览器3秒自动刷新一次
        resp.setHeader("refresh","3");

        // 在内存中创建一个图片
        BufferedImage image = new BufferedImage(80, 20,BufferedImage.TYPE_INT_RGB);
        //得到图片
        Graphics2D painter = (Graphics2D) image.getGraphics();  //想当于一个笔
        //设置背景色
        painter.setColor(Color.WHITE);
        painter.fillRect(0,0,80,20);

        //给图片写数据
        // 给画笔换颜色
        painter.setColor(Color.BLACK);
        painter.setFont(new Font(null,Font.BOLD,20));
        painter.drawString(randomNum(),0,20);

        // 告诉浏览器这里用图片打开
        resp.setContentType("image/jpeg");
        // 让浏览器不要缓存
        resp.setDateHeader("expires",-1);
        resp.setHeader("Cache-Control","no-cache");


        //使用ImageIO类将图片写入response流
        ImageIO.write(image, "jpg",resp.getOutputStream());
    }

    //生成随机数
    public String randomNum(){
        Random random = new Random();
        // seed设置生成随机数的长度
        String num = random.nextInt(99999)+" ";
        StringBuffer sb = new StringBuffer();
        for(int i=0;i<5-num.length();i++){
            sb.append("0");
        }
        num = sb.toString()+num;
        return num;
    }
}

```

##### 4. 重定向 === 状态码302

```java
 resp.sendRedirect("/s1/hello");
```

==重定向一定要注意路径问题==

#### 5.7、HttpServletRequest

##### 1.获取前端传递的参数

```java
//后台接收中文乱码问题
req.setCharacterEncoding("UTF-8");
resp.setCharacterEncoding("UTF-8");

req.getParameter("username");
req.getParameterValues("hobbys");   //多个值的，比如前端里面的多选框传递过来的值
```

![image-20210524191216415](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210524191216.png)

##### 2.请求转发  === 状态码307

```java
// req.getContextPath() 前面的路径
//req.getContextPath()
// 请求转发自己带有项目的路径，不需要加上req.getContextPath()，重定向需要加上
req.getRequestDispatcher("/hello").forward(req,resp);
```

### 6、Cookie、Session

#### 6.1、会话

**会话**：用户打开一个浏览器，点击了很多超链接，访问多个web资源，关闭浏览器，这个过程可以称之为会话

**有状态的会话**：一个同学来过教室，下次再来，我们知道这个同学曾经来过。

类比解释：

![image-20210524193002995](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210524193003.png)

#### 6.2、保存会话的两种技术

cookie

- 客户端技术（响应，请求）

Session

- 服务器技术，利用这个技术，可以保存用户的会话信息。可以把信息或者数据放在Session中



#### 6.3 Cookie

```java
Cookie[] cookies = req.getCookies(); // 获取请求的cookie
cookie.getName();   // cookie的name
cookie.getValue();  // cookie的值
new Cookie("lastLoginTime", date);  // 新建一个cookie
cookie.setMaxAge(24*60*60);   	// 设置cookie的有效值，这里设置的是1天
resp.addCookie(lastLoginTime_Cookie); 	// 响应给客户端一个cookie
```

cookie一般会保存在本地的用户目下

==一个cookie是否存在上限？？？==

- 一个cookie只能保存一个信息；
- 一个web站点可以给浏览器发送多个cookie，最多存放20个cookie；
- Cookie大小有限制4kb；
- 300个cookie浏览器上限。

删除Cookie

- 不设置有效期，关闭浏览器，自动失效
- 设置有效期为0  ==  另一个服务，里面添加同名的cookie，并设置有效期为0，访问即可删除cookie

#### 6.4 Session

(cookie存放的东西有限，没有Session灵活)

什么是Session

- 服务器会给每一个用户(浏览器)创建一个Session对象
- 一个Session独占一个浏览器，只要浏览器没关，这个Session就存在
- 用户登录之后，整个网站都能访问  -》保存用户的信息



> 注销session

1. 手动注销

```java
HttpSession session = req.getSession();
session.removeAttribute("name");
session.invalidate();
```

2.web.xml配置Seesion的过期时间

```xml
<session-config>
    <!--        这里设置为10分钟就失效了-->
    <session-timeout>10</session-timeout>
</session-config>
```



> Session和Cookie的区别

- Cookie是吧用户的数据写给用户的浏览器，浏览器保存
- Session是吧用户的数据写到用户独占的Session中，服务器端保存(保存重要的信息，减少服务器资源的浪费)
- Session对象由服务创建

- Session中可以**存各种信息**(对象)

使用场景：

- 保存一个登录用户的信息
- 购物车信息
- 在整个网站中经常会使用的信息，将它保存在Session中

```java
//一些方法
session.setAttribute("name","");
session.getAttribute("name");
```

![image-20210524213910699](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210524213910.png)

### 7、JSP

#### 1. 原理

![image-20210525151748780](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210525151748.png)

实际上，在访问jsp文件的时候，是先把jsp编译成java文件(继承了HttpServlet)的类，也就是jsp本质是一个Servlet服务。

---

> jsp编译生成java文件

存在一些方法 == Servlet

```java
//初始化
  public void _jspInit() {
      
  }
//销毁
  public void _jspDestroy() {
  }
//JSPService
  public void _jspService(.HttpServletRequest request,HttpServletResponse response)
```

内部内置了很多对象

```java
final javax.servlet.jsp.PageContext pageContext;  //页面上下文
javax.servlet.http.HttpSession session = null;    //session
final javax.servlet.ServletContext application;   //applicationContext
final javax.servlet.ServletConfig config;         //config
javax.servlet.jsp.JspWriter out = null;           //out
final java.lang.Object page = this;               //page：当前
HttpServletRequest request                        //请求
HttpServletResponse response                      //响应
```



输出页面之前增加了一些代码

```java
response.setContentType("text/html");       //设置响应的页面类型
pageContext = _jspxFactory.getPageContext(this, request, response,
                                          null, true, 8192, true);
_jspx_page_context = pageContext;
application = pageContext.getServletContext();
config = pageContext.getServletConfig();
session = pageContext.getSession();
out = pageContext.getOut();
_jspx_out = out;
```

==编译的时候==

- 只要是 JAVA代码就会原封不动的输出；

  - 这里使用一些<%%>，jsp的标签来识别

- 如果是HTML代码，就会被转换为：

  - ```java
    out.write("<html>\r\n");
    ```

#### 2.使用

> 依赖的库

```xml
<dependencies>
    <!--        Servlet的库-->
    <dependency>
        <groupId>javax.servlet</groupId>
        <artifactId>javax.servlet-api</artifactId>
        <version>3.1.0</version>
        <scope>provided</scope>
    </dependency>

    <!-- jsp的库 -->
    <dependency>
        <groupId>javax.servlet.jsp</groupId>
        <artifactId>javax.servlet.jsp-api</artifactId>
        <version>2.3.1</version>
        <scope>provided</scope>
    </dependency>

    <!--JSTL表达式的依赖-->
    <dependency>
        <groupId>javax.servlet</groupId>
        <artifactId>jstl</artifactId>
        <version>1.2</version>
    </dependency>
    <!-- standard标签库的依赖 -->
    <dependency>
        <groupId>taglibs</groupId>
        <artifactId>standard</artifactId>
        <version>1.1.2</version>
    </dependency>
</dependencies>
```

#### 3.jsp基础语法

> 输出<%=

<%= 变量或者表达式%>

```jsp
<%-- 作用：用来将程序的输出，输出到客户端,下面是个列子，将时间输出到页面上了 --%>
<%= new java.util.Date()%>
```

> 脚本片段<%

里面可以写java代码

```jsp
<%
    int sum = 0;
    for (int i = 1; i <=100 ; i++) {
        sum+=i;
    }
    out.println("<h1>Sum="+sum+"</h1>");
%>
```

```jsp
 <%--在代码嵌入HTML元素  , 这里实现了一个for循环--%>
  

  <%
    for (int i = 0; i < 5; i++) {
  %>
   
		<h1>Hello,World  <%=i%> </h1>
  <%
    }
  %>
```

> jsp声明 <%!

```jsp
  <%!
    static {
      System.out.println("Loading Servlet!");
    }

    private int globalVar = 0;

    public void kuang(){
      System.out.println("进入了方法Kuang！");
    }
  %>
```

声明标签里面写的java代码会直接生成在jsp生成的java类里面。之前讲的标签里面写所有java代码，则是在jsp里的`_jspService()`方法里。

> jsp的注释

```jsp
<%--jsp的注释--%>
<!--html的注释-->
```

在浏览器看html的源码时，html的注释可以找到，jsp的注释是找不到的。

但是两个内容在页面展示上是都没有的。



#### 4.jsp指令

```jsp
<%@page args.... %>  //空格之后会有很多参数
<%@include file=""%>

<%--@include会将两个页面合二为一--%>

<%@include file="common/header.jsp"%>
<h1>网页主体</h1>

<%@include file="common/footer.jsp"%>

<hr>


<%--jSP标签
    jsp:include：拼接页面，本质还是三个
    --%>
<jsp:include page="/common/header.jsp"/>
<h1>网页主体</h1>
<jsp:include page="/common/footer.jsp"/>

```

<%@include file= 和<jsp:include page=的区别

- @include会将两个页面合二为一，就是直接在java代码中转成out.print了
  - 如果另外一个页面有个变量i，现在这个页面也有变量i，那么就会出错
- jsp:include 则是拼接页面，本质上是两个不同的页面放在一起
  - 如果另外一个页面有个变量i，现在这个页面也有变量i，这个不会出错，因为是各自页面的变量

xml定制错误页面

![image-20210525155050342](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210525155050.png)

#### 5.九大内置对象

- PageContext    存东西
- Request     存东西
- Response
- Session      存东西
- Application   【SerlvetContext】   存东西
- config    【SerlvetConfig】
- out
- page ，不用了解
- exception

```java
pageContext.setAttribute("name1","秦疆1号"); //保存的数据只在一个页面中有效
request.setAttribute("name2","秦疆2号"); //保存的数据只在一次请求中有效，请求转发会携带这个数据
session.setAttribute("name3","秦疆3号"); //保存的数据只在一次会话中有效，从打开浏览器到关闭浏览器
application.setAttribute("name4","秦疆4号");  //保存的数据只在服务器中有效，从打开服务器到关闭服务器
```

取数据的时候，从底层到高层(作用域)    page是最底层的，可以取到所有高层存储的数据

pageContext->request->session->application

#### 6.JSP标签、JSTL标签、EL表达式

> EL表达式：  ${ }

- **获取数据**
- **执行运算**
- **获取web开发的常用对象**



>JSP标签

```java
<%--jsp:include--%>

<%--
http://localhost:8080/jsptag.jsp?name=kuangshen&age=12
--%>

<jsp:forward page="/jsptag2.jsp">
    <jsp:param name="name" value="kuangshen"></jsp:param>
    <jsp:param name="age" value="12"></jsp:param>
</jsp:forward>
```

> JSTL标签

JSTL标签库的使用就是为了弥补HTML标签的不足；它自定义许多标签，可以供我们使用，标签的功能和Java代码一样！

核心标签

```jsp
  --引入标签库
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
```

![image-20210525205043301](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210525205043.png)

c:if

```jsp
<%--判断如果提交的用户名是管理员，则登录成功,var是来接受返回值的--%>
<c:if test="${param.username=='admin'}" var="isAdmin">
    <c:out value="管理员欢迎您！"/>
</c:if>

<%--自闭合标签--%>
<c:out value="${isAdmin}"/>
```

c:set c:choose c:when

```jsp
<%--定义一个变量score，值为85--%>
<c:set var="score" value="55"/>

<c:choose>
    <%--取出score的值进行比较--%>
    <c:when test="${score>=90}">
        你的成绩为优秀
    </c:when>
    <c:when test="${score>=80}">
        你的成绩为一般
    </c:when>
    <c:when test="${score>=70}">
        你的成绩为良好
    </c:when>
    <c:when test="${score<=60}">
        你的成绩为不及格
    </c:when>
</c:choose>

```

c:forEach

```java
<%

    ArrayList<String> people = new ArrayList<>();
    people.add(0,"张三");
    people.add(1,"李四");
    people.add(2,"王五");
    people.add(3,"赵六");
    people.add(4,"田六");
    request.setAttribute("list",people);
%>

<%--
var , 每一次遍历出来的变量
items, 要遍历的对象
begin,   哪里开始
end,     到哪里
step,   步长
--%>
   
<c:forEach var="people" items="${list}" begin="1" end="3" step="1" >
    <c:out value="${people}"/> <br>
</c:forEach>
```

### 8、MVC三层架构

什么是MVC：model  view  Controller 模型、视图、控制器

Model

- 业务处理：业务逻辑  （Service）
- 数据持久层：CURF  （DAO）

View

- 战术数据
- 提供链接发起Servlet请求  (form,a)

Controller (Servlet)

- 接收用户的请求 (req,session)
- 交给业务层处理对应的代码
- 控制视图的跳转

### 9、Filter过滤器

![image-20210526151059872](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210526151059.png)

过滤器其实和Servlet差不多。

Filter：过滤器 ，用来过滤网站的数据；

- 处理中文乱码
- 登录验证….

> 开发过程

写一个过滤器的类**继承**Filter(不要导错包)，重写三个方法

```java
package com.xy.filter;

import javax.servlet.*;
import java.io.IOException;

public class CharacterEncodingFilter implements Filter {
    @Override
    // 初始化
    public void init(FilterConfig filterConfig) throws ServletException {
        System.out.println("初始化======================");
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        response.setCharacterEncoding("utf-8");
        request.setCharacterEncoding("utf-8");
        response.setContentType("text/html; charset=utf-8");
        System.out.println("执行前");
        //放行,让请求继续走，不写，程序就被拦截停止了
        chain.doFilter(request,response);
        System.out.println("执行后");
    }

    @Override
    // 销毁
    public void destroy() {
        System.out.println("销毁=======");
    }
}
```

init()方法，随着tomcat的启动而执行，监听发起的Servlet请求

doFilter() 过滤器需要做的一些操作： chain.doFilter(request,response); 放行过滤器的语句，这样子才能让程序继续执行下去

destroy()    随着tomcat的关闭才执行



2.配置xml

```xml
<filter>
    <filter-name>CharacterEncodingFilter</filter-name>
    <filter-class>com.xy.filter.CharacterEncodingFilter</filter-class>
</filter>

<filter-mapping>
    <filter-name>CharacterEncodingFilter</filter-name>
    <!--  过滤这个路径下的请求，这个请求下的服务都会经过过滤器-->
    <url-pattern>/filter/*</url-pattern>
</filter-mapping>
```

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







## 4、Springboot

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



### 5、springBoot 国际化

>  准备工作

设置编码格式

![image-20210610110754725](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210610110754.png)

> 配置文件编写

1、在resources资源文件下新建一个i18n文件夹，存放国际化配置文件

2、建立一个login.properties文件，还有一个login_zh_CN.properties；发现IDEA自动识别了我们要做国际化操作；文件夹变了！

![image-20210610110800660](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210610110800.png)

3、我们可以在这上面去新建一个文件；我已经创建了一个en_US 了，这是美国的

![image-20210610110813259](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210610110813.png)

![image-20210610110821247](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210610110821.png)

4、我们可以开始编写配置了：

点开文件发现有两个视图

![image-20210610110829707](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210610110829.png)

在第二视图里，点击+ 添加属性：新建一个login.tip，可以看到边上有三个输入框

![image-20210610110840393](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210610110840.png)

添加一下首页的内容，然后依次添加其他页面的内容

![image-20210610110850744](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210610110850.png)

在`application.yml`中，把文件配置放进去  

```yml
spring:
  messages:
    basename: i18n.login
    #前端就能取里面的值了
```

> 配置页面国际化

thymeleaf取值操作为：#{...}   ==消息表达式  #{xxx}==

```html
<!DOCTYPE html>
<html lang="en"  xmlns:th="http://www.thymeleaf.org">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<meta name="description" content="">
		<meta name="author" content="">
		<title>Signin Template for Bootstrap</title>
		<!-- Bootstrap core CSS -->
		<link th:href="@{/css/bootstrap.min.css}" rel="stylesheet">
		<!-- Custom styles for this template -->
		<link th:href="@{/css/signin.css}" rel="stylesheet">
	</head>

	<body class="text-center">
		<form class="form-signin" th:action="@{/user/login}">
			<img class="mb-4" th:src="@{/img/bootstrap-solid.svg}" alt="" width="72" height="72">
<!--			thymeleaf 中 使用#{login.tip}  使其生效-->
			<h1 class="h3 mb-3 font-weight-normal" th:text="#{login.tip}">Please sign in</h1>
			<div th:text="${msg}"  style="color: red" ></div>

			<label class="sr-only">Username</label>
			<input type="text" name="username" class="form-control" th:placeholder="#{login.username}" required="" autofocus="">
			<label class="sr-only">Password</label>
			<input type="password" class="form-control" name="password" th:placeholder="#{login.password}" required="">
			<div class="checkbox mb-3">
				<label>
          <input type="checkbox" value="remember-me" th:text="#{login.remember}">
        </label>
			</div>

			<button class="btn btn-lg btn-primary btn-block" th:text="#{login.login}" type="submit">Sign in</button>
			<p class="mt-5 mb-3 text-muted">© 2017-2018</p>
			<a class="btn btn-sm" th:href="@{/(l='zh_CN')}">中文</a>
			<a class="btn btn-sm" th:href="@{/(l='en_US')}">English</a>
		</form>

	</body>

</html>
```

> 如何根据按钮自动切换中英

```html
//中英文的两个按钮
							// 括号代表传参
<a class="btn btn-sm" th:href="@{/(l='zh_CN')}">中文</a>
<a class="btn btn-sm" th:href="@{/(l='en_US')}">English</a>
```

在Spring中有一个国际化的Locale （区域信息对象）；里面有一个叫做LocaleResolver （获取区域信息对象）的解析器！

我们去自己写一个自己的LocaleResolver，可以在链接上携带区域信息！

```java
public class MyLocaleResolver implements LocaleResolver {
    @Override
    public Locale resolveLocale(HttpServletRequest request) {
        //前端传过来的地址的信息 l='zh_CN'
        String language = request.getParameter("l");
        // 如果没有获取到就使用系统默认的
        Locale locale = Locale.getDefault();
        
        //如果请求链接不为空
        if(!StringUtils.isEmpty(language)){
              //分割请求参数
            String[] split = language.split("_");
              //国家，地区
            locale = new Locale(split[0], split[1]);
        }
        return locale;
    }

    @Override
    public void setLocale(HttpServletRequest request, HttpServletResponse response, Locale locale) {

    }
}
```

为了让我们的区域化信息能够生效，我们需要再配置一下这个组件！在我们自己的MvcConofig下添加bean；放入spring容器中

```java
 @Bean
    public LocaleResolver localeResolver(){
        return new MyLocaleResolver();
    }
```

`我们自己配置的mvcConfig`

![image-20210610110902870](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210610110902.png)

### 6、任务

#### 1、异步任务

`异步任务`： 指的是多线程进行处理，一个线程浏览器页面显示，另一个处理方法里面的过程

使用两个注解就可以`@Async`  `@EnableAsync`

```java
@Service
@Async
public class AsyncService {
    public void hello(){

        System.out.println("数据正在处理");
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("数据处理成功");
        
    }
}
```

```java
@SpringBootApplication
@EnableAsync   //开启异步功能
public class Springboot09TaskApplication {

    public static void main(String[] args) {
        SpringApplication.run(Springboot09TaskApplication.class, args);
    }

}
```



#### 2、定时任务

同样两个注解 ：`@EnableScheduling`, `@Scheduled`  

```java
@SpringBootApplication
@EnableScheduling //开启定时功能
public class Springboot09TaskApplication {

    public static void main(String[] args) {
        SpringApplication.run(Springboot09TaskApplication.class, args);
    }

}
```

```java
@Service
public class ScheduledService {
    //cron 表达式
    // 秒 分 时 日 月 周
    @Scheduled(cron = "0 11 17 10 5 ? " )
    public void hello(){
        Date date = new Date();
        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
        String date_ = format.format(date);
        System.out.println("你被执行了"+ date_);
    }
}
```

**cron表达式**  设置定时任务的时间，

#### 3、邮件发送

`application.properties`

```properties
#使用qq邮箱的设置
spring.mail.username= 985670113@qq.com
spring.mail.password= cxsnnjngghtibfcb
spring.mail.host= smtp.qq.com


spring.mail.properties.mail.smtp.auth=true
spring.mail.properties.mail.smtp.starttls.enable=true
spring.mail.properties.mail.smtp.starttls.required=true
```

```java
#测试
@Autowired
JavaMailSenderImpl javaMailSender;

//普通邮件发送，固定格式
void contextLoads() {
    int flag = 0;
    SimpleMailMessage simpleMailMessage = new SimpleMailMessage();
    
    //设置标题
    simpleMailMessage.setSubject("徐颖测试邮件");
    
    //正文内容
    simpleMailMessage.setText("傻子");
    
    //发件人
    simpleMailMessage.setFrom("985670113@qq.com"); 
    
    //收件人
    simpleMailMessage.setTo("3194145353@qq.com");
 
    //发送
    javaMailSender.send(simpleMailMessage);

    }
```

```java
//复杂邮件
void contextLoads2() throws Exception{
    
    MimeMessage mimeMessage = javaMailSender.createMimeMessage();
    
    // true 代表开启html元素和附件功能    后面还能加编码 MimeMessageHelper(mimeMessage,true,"utf-8")
    MimeMessageHelper helper = new MimeMessageHelper(mimeMessage,true);
    
    //设置标题
    helper.setSubject("徐颖测试");
    
    //正文内容  ,true 开启html
    helper.setText("<h1>hello</h1>", true);
    
    //添加附件  
    helper.addAttachment("1.jpg", new File("C:\\Users\\xuying\\Pictures\\1.jpg"));
	
    //同上
    helper.setTo("985670113@qq.com");
    helper.setFrom("985670113@qq.com");

    javaMailSender.send(mimeMessage);
}
```

### 7、Springboot 集成Swagger

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

### 、分布式Dubbo + Zookeper

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



#### 3.Dubbo+Zookeeper实战小Demo(补充狂神说新版Dubbo)

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



## 5、springboot实战总结



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