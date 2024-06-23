## js



#### 数据类型

##### 对象

若干个键值对

```js
var 对象名 = {
    属性名：属性值,
}

var person = {
    name : "xt",
    age : 11,
    sex : '男'
}
```

动态的增删属性

```js
delete person.name
person.hah  = "test"
```

##### 流程控制

forEach循环

```js

var arr = [1,2,1,3,5,6,8];
// forEach循环
arr.forEach(function (value) {
    console.log(value)
})
console.log("=====")

// for in
for (num in arr){
    console.log(arr[num]);
}
//for of   es6新特性
for (num of arr){
    console.log(num);
}
```



##### Map 和 Set

使用 for of  遍历  ，用的是iterator



#### 函数

##### 变量的作用域

存在函数嵌套，变量由内向外查找

##### 全局函数

##### 规定

由于我们的所有全局变量都会绑定到window上，如果不同的js文件，使用了相同的全局变量，则很容易产生冲突

```js
<!--        自己定义一个唯一全局变量-->
var xy_win = {};
xy_win.name = "xy";
xy_win.add = function (a,b) {
    return a+b;
}
```



##### 局部作用域 let

解决局部作用域冲突的问题



##### 常量 const

以前的常量只要是大写字母定义的就是，但是这个值是可以修改的

ES6中引入 const 修饰词  

##### apply() 

可以控制this的指向

函数名.apply(xxx,[参数])  xx是this 指向的对象·

#### 3.内部对象 

##### 3.1 Date对象

> 方法

```js
now = new Date();
now.getFullYear();      //年
now.getMonth();         //月  0~11
now.getDate();          //日
now.getDay();           //星期
now.getHours();         //小时
now.getMinutes();       //分
now.getTime();          //时间戳
```

> 转换

```js
now.toDateString()
//"Sat May 23 2020"
now.toLocaleDateString()
//"2020/5/23"
now.toGMTString()
//"Sat, 23 May 2020 03:00:46 GMT"
```

##### 3.2 json 

```js
var xuying  = {
    name: "xuyi",
    age:12,
    date: {
        hello:"test",
        hel : "你好"
    }
}
JSON.stringify(xuying)   //转化为json对象

//{"name":"xuyi","age":12,"date":{"hello":"test","hel":"你好"}}  JSON对象  ,都有""

JSON.parse(xx)  //解析JSON对象
```

#### 4、面向对象编程

1、原型

```js
function Student(name) {
    this.name = name;
}
student.prototype.hello = function () {
    alert("test");
}


class Student{
    constructor(name) {
        this.name = name
    }

    hello(){
        alert("hello")
    }
}

// 本质还是 proto 为 Student
class xiaohong extends Student{
    constructor(name,age) {
        super(name);  // 调用父类的构造方法
        this.age = age;
    }
}
```

#### 5、操作BOM对象

> 浏览器介绍

BOM：浏览器对象模型

- IE   
- chrome
- fireFox
- safari

> window 

window代表浏览器窗口

> navigator

`navigator `封装了浏览器的信息

不建议使用`navigator`，因为会被人为修改

> screen

screen 代表屏幕

> location(重要)

`location`当前页面的URL信息

```js
location.host
"www.baidu.com"

location.href
"https://www.baidu.com/"

location.protocol
"https:"

location.assign("xx")   设置新的地址

location.reload  //刷新
```



> document

代表当前的页面，HTML  DOM文档树

`document.cookie`  获取cookie

> history

代表浏览器的历史记录

```js
history.back()
history.forward（）
```

#### 6、操作DOM对象

> 核心

浏览器网页就是一个DOM树形结构

- 更新
- 遍历
- 删除
- 添加

要操作一个Dom节点，必须要获得这个Dom节点

```js
document.getElementsByTagName("h1")  //标签选择器
document.getElementById()  			//
document.getElementsByClassName()	//
```



> 更新

```js
//操作文本
id.innerText = '123'  //修改文本的值
id.innerHTML  = '<h1>123<h1>'   //


//操作css
id.style.xxx = xxx
```

> 删除

删除节点的步骤，先获取父节点，再删除自己

> 插入节点

如果我们获得的是个空的节点，可以直接innerHTML 添加（这会覆盖之前的值），如果不是空的

```js

var js  =  document.createElement("script");   //创建标签
js.setAttribute("type","text/javascript");   //设置属性

id.appendChild()

.insertBefore()



```

#### 7、操作表单

- 文本框  text
- 下拉框  select
- 单选框  radio
- 多选框  checkbox
- 隐藏域  hidden
- 密码框  password
- 。。。。。

> 获得要提交的信息

```html
<form action="post">
    <span>
        用户名：
    </span>

    <input type="text" id="username">
    <div></div>
    <span>性别</span>:
    <input type="radio" name="sex" value="man" id="boy">男
    <input type="radio" name="sex" value="woman" id="girl">女
</form>
<script>
    var input = document.getElementById("username");
    let boy_radio = document.getElementById('boy');
    let girl_radio = document.getElementById('girl');
   

    //查看返回的结果是否为true，boy_radio.checked  
</script>
```

> 提交表单

```js
<form action="" id="form-test">
    <input type="text" name="test">
    <button type ="button" onclick="submit()">submit</button>
</form>

<script>
    function submit() {
        var form = document.getElementById("form-test");
        form.submit();
    }
</script>
```

方式二

```js
<form action="" id="form-test2" onsubmit="submit()">
    <input type="text" name="test">
    <button type ="submit">submit2</button>
</form>

<script>

    function submit2() {
        var form = document.getElementById("form-test2");
        return true;
    }
</script>
```

`return true·` 就表示提交，false就不提交

> 密码

```js
<script>
    function aaa() {
        var uname = document.getElementById("username");
        var upwd  = document.getElementById("password");


        upwd.value = "xxx"; //可以用加密修改密码  ，不过会造成前端密码加长的瞬间
        //优化
        /**   <input type="hidden" id="crypto-password" name="crypto-password">
         *    var uCPwd  = document.getElementById("crypto-passwor");
         *     uCPwd.value = "xxx";
         *
         */

        return false;

    }
</script>
```

#### 8、jquery

> 选择器

- 标签   `$('p')`
- id    `$('#xxx')`
- 类` $('.xxx')`

文档：[jquery](http://jquery.cuishifeng.cn/id.html)



> 按属性查找

![image-20210628145735070](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210628145735.png)

> 事件

鼠标事件、键盘事件、







#### 10、ajax





## Vue



### 1.Vue常用7个属性

- el属性
- data属性
- template属性
- methods属性
- render属性
- computed属性
- watch属性

### 1.vue

MV VM  （MVC演变来的） Model View  ViewModel

双向绑定 == 》 view的值从model这里取。 Model可以根据view改变



架构图

![image-20210629155401330](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210629155401.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="https://cdn.staticfile.org/vue/2.2.2/vue.min.js">
    </script>
</head>
<body>

<!-- view 层 模板-->
<div id="app">
    {{name}}
</div>

<script>
    var vm = new Vue({
        el : "#app" ,  // el:element
        // Model
        data : {
            name: "hello ,Vue"
        }
    });

   
</script>

</body>
</html>
```

在前端修改`vm.name`的时候，可以不刷新页面，前端显示也改变



![image-20210629155612631](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210629155612.png)



> 小结

两个模块`el` , `data` 

el不能挂在到<html>和<body>上。 可以用其他的选择器来识别vue的挂在位置



### 2.指令` v-xxxxx`

> v-text

![image-20210630152313355](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210630152313.png)

> v-html

和v-text差不多，但是如果message 是能够解析成html的字符串，就会被解析



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="https://cdn.staticfile.org/vue/2.2.2/vue.min.js">
    </script>
</head>
<body>

<!-- view 层 模板-->
<div class="app2" id="app">
  
    <p v-text="message"></p>
     <p v-html="message"></p>   
</div> 
 
<script>
    var vm = new Vue({
        el : "#app" , 
        data : {
           message: '<a href="#">测试</a>'
        } 
    });
</script>

</body>
</html>
```

> v-bind

`v-bind` 绑定

```html
<span v-bind:title="name">
    鼠标悬停查看绑定的信息
</span>
```

> if else

```js
<div id="app">
    // ok是true的话就显示
  <h1 v-if="ok">YES</h1>
 
  <h1 v-else>YES</h1>
</div>
```

`v-if` ` v-else-if` `v-else`

> for

```html
<!-- view 层 模板-->
<div id="app">
    <li v-for="item in items"> {{item.message}}</li>
</div>

<script>
    var vm = new Vue({
        el : "#app" ,  // el:element
        data : {
            items : [
                {message:"xy1"},
                {message:"xy2"}
            ]
        }
    });

</script>
```

> v-show

根据表达式的真假，切换元素的显示和隐藏

```html
<div id="app">
     <a href="" v-show="age>18">成人</a>
     <a href="" v-show="age<18">未成年</a>
</div>

<script>
    var vm = new Vue({
        el : "#app" ,  // el:element
        data:{
            age : 17
        }
    });
</script>
```



### 3.事件 - `v-on`

```html
<div id="app">
     <button v-on:click="sayHi">click</button>
</div>

<script>
    var vm = new Vue({
        el : "#app" ,  // el:element
        data:{
            message : "xuying"
        },
        methods :{  // 方法必须定义在method的方法中，不然绑定不到
            sayHi : function () {
                alert("你好"+this.message)
            }
        }
    });

</script>
```

![image-20210630153806303](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210630153806.png)



![image-20210630160946660](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210630160946.png)

### 4、双向绑定



```html
<!-- view 层 模板-->
<div id="app">
     输入的文本：<input type="text" v-model="message"> {{ message}}
</div>

<script>
    var vm = new Vue({
        el : "#app" ,  // el:element
        data:{
            message : ""
        }
    });

</script>
```

```html
<!-- view 层 模板-->
<div id="app">
    <input type="radio"  value="11" v-model="sex">男
    <input type="radio" value="22" v-model="sex">女
    {{sex}}
</div>

<script>
    var vm = new Vue({
        el : "#app" ,  // el:element
        data:{
            message : "",
            sex: ""
        }
    });
</script>
```



![image-20210629162857155](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210629162857.png)



### 5、组件 ` Vue.component`

```html
<div id="app">
    <xuying></xuying>
</div>


<script>
    // 定义一个Vue组件
    Vue.component("xuying",{
        template: '<h1>Hello</h1>'
    })

    var vm = new Vue({
        el : "#app" ,  
    });
</script>
```

```html
<div id="app">
    <xuying v-for ="item in items" v-bind:data="item"></xuying>
<!--    <li v-for="item in items">{{items}}</li>-->
</div>


<script>
    // 定义一个Vue组件
    Vue.component("xuying",{
        props: ['data'],
        template: '<li>{{data}}</li>'
    });

    var vm = new Vue({
        el : "#app" ,
        data:{
            items:[1,2,3]
        }
    });
</script>
```

把data绑定到item传递给compnent，用props接收

### 6、网络通信



![image-20210630171150280](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210630171150.png)

Axios用来实现ajax异步通信

```js
// 定义一个Vue组件

<div id="app">
    <div>{{info.url}}</div>
</div>

var vm = new Vue({
    el : "#app" ,
    // 这里的data是个函数，和之前的属性不一样。这里的data用来返回钩子函数获取的值
    data(){
        return{
            // 这个用来接收axio的数据
            info: ""
        }
    },
    mounted(){ // 钩子函数
        // axios请求，链式编程
        axios.get('data.json').then(response=>(this.info = response.data));
    }
});
```

`data.json`

```json
{
  "name": "xuying",
  "url" : "www.baidu.com"
}
```

### 7、计算属性

可以看成是缓存，

```js
<div id="app">
    <p>{{currentTime1()}}</p>
    <p>{{currentTime2}}</p>
</div>


<script>
    // 定义一个Vue组件


    var vm = new Vue({
        el : "#app" ,
        data:{
            message:""
        },
        methods:{
            currentTime1: function () {
                return Date.now();
            }
        },
        //
        // 计算属性
        // 这里的值会被缓存到内存中，下次调用这个属性值不会改变
        computed:{
            currentTime2: function () {
                // this.message;  如果将这个放进去，我们每次修改message，就会调用这个方法，缓存就会被更新
                return Date.now();
            }
        }
    });
</script>
```





![image-20210629215318718](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210629215318.png)



### 8、插槽

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <script src="https://cdn.staticfile.org/vue/2.2.2/vue.min.js">
    </script>

    <script src="https://cdn.staticfile.org/axios/0.18.0/axios.min.js"></script>
</head>
<body>

<div id="app">
    <todo >
        <todo-title></todo-title>
        <todo-items v-for="(item,index) in items"
                    v-bind:index="index" v-bind:message="item"
        v-on:remove="removeList()"></todo-items>
    </todo>
</div>


</body>
<script>
    var html = `<div>
                    <slot></slot>
                    <ul>
                        <slot></slot>
                    </ul>
                </div>`;
    Vue.component("todo",{
        template: html
    });
    Vue.component("todo-title",{
        template: '<div> 标题</div>'
    });
    Vue.component("todo-items",{
        props:['message','index'],  // 这里绑定下面的methods的方法
        template: '<li>{{message}} <button @click="remove2">删除</button></li> ',
        methods:{
            remove2: function () {
                // 通过这里的  this.$emit  将removemethods里的remove2方法和v-on的remove方法绑定
                this.$emit('remove');
            }
        }
    });

    var vm = new Vue({
        el: "#app",
        data:{
            items: ["java","python","linux"]
        },
        methods: {
            removeList: function (index) {
                this.items.splice(index,1); // 删除下标，1是删除这个几个
            }
        }
    })
</script>

</html>
```





里面涉及到了组件和vue实例之间不同方法的相互调用。用到了`this.$emit`

![image-20210629224903732](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210629224903.png)



### 9、vue-cli

先安装node.js ，里面自带有npm

- 配置淘宝的数据源cnpm `npm install cnpm -g`





> 创建vue项目

```bash
vue init  webpack myvue


npm install
```



#### 1、配置文件

```

```

webpack.conf.js![image-20210630105823607](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210630105823.png)





#### 2.webpack



webpack - 打包



webpack --watch  监控打包（热部署）





> 解释

自己写一个 `hello.js`   可以把这个看成是java里面自己写的方法类。里面有三个方法`exports`相当于public，导入这个类的时候，让其他类可以调用到这个方法

```js

exports.hello = function () {
    document.write("<h1>hello1</h1>");
}

exports.hello2 = function () {
    document.write("<h1>hello1</h1>");
}

exports.hello3 = function () {
    document.write("<h1>hello1</h1>");
}
```

`main.js ` `require` 相当于java里的import . 就将方法类导入进来了，复制给test对象。使用test对象调用其中的某一个方法

```js
var test = require("./hello");  
test.hello()
```

创建一个webpcak.config.js配置文件  。。  模块化导出.最后这个输出的my.js就相当于打包成了一个可以运行的jar包，main函数就是entry里面设定的js文件

```js
module.exports={
    entry:"./js/main.js", // 入口相当于main函数
    output:{
        filename: "my.js"  // 输出的文件位置  ,
    }
}
```



最后创建index.html  导入那个jar包( 就是直接执行，导入的js方法)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="dist/my.js"></script> 
</head>
<body>

</body>
</html>
```

### 10、vue-router 路由

```bash
npm install vue-router --save-dev   // install vue-router
```

然后写组件

比如`content.vue`  (相当)

```vue
 
<!--组件展示的内容-->
<template>
  <h1>content page</h1>
</template>

<script>
    
//把组件暴露出去，这样的话就能够将组件插入
    export default {
        name: "content"
    }
</script>

<!--加了scoped之后，只在当前页面生效-->
<style scoped>
</style>
```

`Main.vue` 同上

写一个路由配置.就和我们写controller一样

我们写在`router/index.js`里面

```js
import Vue from "vue";
import VueRouter from "vue-router";

//必须先将组件导入建立
import Content from "../components/content"
import Main from "../components/Main"
Vue.use(VueRouter);

//配置导出路由
export default new VueRouter({
  // controller层
  routes:[
    {
      //router's path，相当于写了一个@RequestMapping
      path:'/content',
      name:'content',
      component:Content  // 这里是返回的展示界面
    },
    // 同上
    {
      path: '/main',
      name:'main',
      component: Main
    }
  ]
});

```

`App.vue`这里是我们的主入口

```vue
<template>
  <div id="app">
    <h1>Vue Router</h1>
      <!--    to就是href-->
    <router-link to="/main">home page</router-link>
    <router-link to="/content">content page</router-link>
      
<!--  router-view展示视图的  -->
    <router-view></router-view>
  </div>

</template>

<script>
  import Content from './components/content'

export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

点击连接，router-view就会展示该组件的内容

### 11、vue-element

创建项目

```bash
vue init webpack hello-vue  // 都选no，自己安装

#这里用的是新版本的vue-3
#使用命令
vue create hello-world
#然后使用下面的命令
npm install vue-router --save-dev  
npm i element-ui -S
#安装sass加载器
cnpm install sass-loader  --save-dev
#之后可能会有版本冲突，这里用这个版本，后面有错，可以看提示修改版本
cnpm install node-sass@4.14.1
#安装所有的依赖
npm install
```

> npm命令解释

![image-20210701101151071](https://xy-picgo.oss-cn-shenzhen.aliyuncs.com/20210701101151.png)



> 项目的结构创建完毕

创建结构`router` `components` 文件



components下

`Main.vue`

```vue
<template>
    <h1>Main</h1>
</template>
<script>
    export default {
        name: "Main"
    }
</script>
<style scoped>
</style>
```

`Login.vue`

```js
<template>
    <div>
        <el-form ref="loginForm" :model="form" :rules="rules" label-width="80px" class="login-box">
            <h3 class="login-title">欢迎登录</h3>
            <el-form-item label="账号" prop="username">
                <el-input type="text" placeholder="请输入账号" v-model="form.username"/>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input type="password" placeholder="请输入密码" v-model="form.password"/>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" v-on:click="onSubmit('loginForm')">登录</el-button>
            </el-form-item>
        </el-form>

        <el-dialog
                title="温馨提示"
                :visible.sync="dialogVisible"
                width="30%">
            <span>请输入账号和密码</span>
            <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
        </el-dialog>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                form: {
                    username: '',
                    password: ''
                },

                // 表单验证，需要在 el-form-item 元素中增加 prop 属性
                rules: {
                    username: [
                        {required: true, message: '账号不可为空', trigger: 'blur'}
                    ],
                    password: [
                        {required: true, message: '密码不可为空', trigger: 'blur'}
                    ]
                },

                // 对话框显示和隐藏
                dialogVisible: false
            }
        },
        methods: {
            onSubmit(formName) {
                // 为表单绑定验证功能
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        // 使用 vue-router 路由到指定页面，该方式称之为编程式导航
                        this.$router.push("/main");
                    } else {
                        this.dialogVisible = true;
                        return false;
                    }
                });
            }
        }
    }
</script>

<style lang="scss" scoped>
    .login-box {
        border: 1px solid #DCDFE6;
        width: 350px;
        margin: 180px auto;
        padding: 35px 35px 15px 35px;
        border-radius: 5px;
        -webkit-border-radius: 5px;
        -moz-border-radius: 5px;
        box-shadow: 0 0 25px #909399;
    }

    .login-title {
        text-align: center;
        margin: 0 auto 40px auto;
        color: #303133;
    }
</style>
```

router文件下

路由的配置文件`index.js `   里面的一个都不能错。。

```js
import Vue from 'vue'
import VueRouter from 'vue-router';
import Login from "../components/Login";
import Main from "../components/Main"
Vue.use(VueRouter);

export default new VueRouter({
    routes :[
        {
            path: "/login",
            component: Login
        },
        {
            path: "/main",
            component: Main
        }
    ]
});
```

`main.js`

```js
import Vue from 'vue'
import App from './App.vue'
// 这里会自动去router目录下扫描所有的router
import router from './router'

// 结合上element-ui的css样式
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI);

Vue.config.productionTip = false

new Vue({
    //注意这里直接写router就行
  router,
  render: h => h(App)
}).$mount('#app')

```

