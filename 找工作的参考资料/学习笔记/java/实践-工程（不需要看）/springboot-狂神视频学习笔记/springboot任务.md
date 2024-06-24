### 任务

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

