# C#


**禁止方法重载和类的继承**：$sealed$ 修饰符 

###List和数组类型区别

+ 数组类型的**BaseType都等于System.Array**，其内存分布是连续的，指针指向第一个内存地址，该地址里面记录了其数量，故该内存大小为4bit。
+ list的内存分布并不是连续的，是记录了一系列的指针集合，每个指针指向其分布的内存区域，是个双向链表的结构。

<br/>



### IO操作

+ 流创建覆盖之前的内容
    ```
    FileStream fs = new FileStream(path, FileMode.Create);
    ```

<br/>

******

## Question

### Q:为什么某些对象不能外部Set，但是外部还是可以修改呢？
A:
```
    class B
    {
        public int id;
    }

    class A
    {
        public List<string> strList { get; private set; }
        public B b { get; private set; }
    }

    static void main()
    {
        A a = new A();

        a.strList = null;//编译报错
        a.b = null;//编译报错

        a.strList.Add("1");//没问题
        a.b.id = 20;//没问题
    }
```
**解释：** **B是引用类型**，这里定义b只是一个**指针**，代表不能操作这个指针，所以当设置为null时编译会报错，而指针指向的对象我们可以操作，因为该对象内部的成员的可读写权限是交给对象本身的，指针不能控制，**List\<string\>** 同理


<br/>


### Q: int 和 int?

int?可设置为空，但不会产出gc

<br />

### Q: IDisposable 怎么使用？ 什么情况下回执行Dispose
A: 对于一些**非托管资源**，比如数据库链接对象等，需要实现IDisposable接口进行手动的垃圾回收,但CLR不会主动调用该方法。

使用方法：
```
using (CaryClass caryClass = new CaryClass())
{
    caryClass.DoSomething();
}

```
会在出using作用域的时候，执行Dispose

```
CaryClass caryClass = new CaryClass();
try
{
     caryClass.DoSomething();               
}
finally
{
     IDisposable disposable = caryClass as IDisposable;
     if (disposable != null)
         disposable.Dispose();
}
```
主动调用

[C#中IDisposable的用法](https://www.cnblogs.com/tiancai/p/6612444.html)

### Strunt怎么判断null呢

首先值类型不可能为null，那我们怎么可以像判断class一样判断为空呢

```
//DynamicMuteItem 为struct
DynamicMuteItem mItem;
......
......

//因为struct用于不能为空 所以无论如何都会有一个默认值，用这个判断空
if (mItem.Equals(default(DynamicMuteItem)))
{

}
```

<br/>

******