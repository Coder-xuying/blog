### springBoot 国际化

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