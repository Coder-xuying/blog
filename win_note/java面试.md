### java集合

#### List

##### 1、ArrayList 线程安全的吗？ 如何把ArrayList变成线程安全

不是线程安全的，变成线程安全有下面几种方式

```java
// 使用Collections类的synchronizedList方法
1List<String> synchronizedList = Collections.synchronizedList(arrayList)

// 使用CopyOnWriteArrayList类代替ArrayList
CopyOnWriteArrayList<String> copyOnWriteArrayList = new CopyOnWriteArrayList<>(arrayList)
    
// 使用Vector类代替ArrayList
Vector<String> vector = new Vector<>(arrayList);
```

##### 2、为什么ArrayList不是线程安全的

```
add方法：
- 先判断新元素放到列表后面，size + 1 的长度是否大于数组的长度，如果大于就扩容
-  element[size++] = e 将数组的size位置设置值,size++
```

有三个问题：

- **size和add元素的数量不相等**：因为size++不是原子操作，线程1和线程2都拿到了size相同的值，然后将size+1 ，两个加完了同时覆盖size，就导致有一次没加上
- **索引越界**：当前size是9，然后数组容量是10，线程1和线程2同时走到size判断那里，然后就都不需要扩容，然后走到 element[size++] = e ，线程1先set，size变成10， 线程2set，就索引越界了
- **部分值为null**：和上面索引越界前面的步骤差不多，后面走到element[size++]  这里，同时给size 9的set值，然后size ++ ，发现size变成了11，size = 10的地方就是null值

##### 3、ArrayList的扩容机制

1.8中，如果用无参构造的话，初始数组容量为0，当第一次添加元素时才分配容量，默认的分配容量为10，当容量不足时（执行add，容量为size，添加size+1个元素时），执行扩容，默认扩容因子为1.5，也就是size的1.5倍，如果1.5倍< 最低容量，就以1.5倍扩容，否则就以最低容量进行扩容。

- 最低容量的值是： Math.max(size+1,默认值)，所以如果一开始指定容量设置比较小，就还是会用默认值10作为元素容量扩充
- 为什么用1.5倍因子，好像是最好的扩容是（1,2）之间的值，然后1.5的话，java可以利用位运算，可以减少运算时间和浮点数

##### 4、CopyWriteArrayList怎么实现线程安全的？