## HashTable、 Dictionary、ConcurrentDictionary区别

1. *Dictionary* 支持泛型 
    *HashTable*不支持泛型，非引用类型有装箱拆箱操作，影响效率
2. *ConcurrentDictionary* 在 *Dictionary* 加入了线程安全，Dictionary是非线程安全的类型，操作的时候需要对其进行线程安全处理，最简单的方式就是加锁(lock)。 

3. .Net4.0中 *ConcurrentDictionary* 是线程安全的字典。

+ 总结
    大数据插入*Dictionary*花费时间最少
    遍历*HashTable*最快是*Dictionary*的1/5,*ConcurrentDictionary*的1/10
    单线程建议用*Dictionary*，多线程建议用*ConcurrentDictionary*或者*HashTable*
    （Hashtable tab = Hashtable.Synchronized(new Hashtable());获得线程安全的对象）

+ *ConcurrentDictionary*如何保证线程安全
*ConcurrentDictionary*可以说是为了避免一个大锁锁住整个*Dictionary*带来的性能损失而出来的，当然也是采用空间换时间，不过这空间换得还是很值得的，一些object而已。原理在于*Dictionary*本质是是一个链表数组，只有在多线程同时操作到数组里同一个链表时才需要锁，所以就用到一个锁数组，每个锁罩着几个小弟(bucket及bucket内的链表元素)，这样多线程读写不同锁罩的区域的时候可以同时进行而不会等待，进而提高多线程性能。  

**注意**：用struct或者class左key的时候要重载散列函数(hashcode方法)和equal方法，合理实现，否则底层将所有的内部字段都当作object处理来生成hashcode，这将引起不必要的装箱拆箱操作，产生gc。

> 
[ConcurrentDictionary源码分析](https://www.cnblogs.com/brookshi/p/5583892.html)
[C#中字典集合HashTable、Dictionary、ConcurrentDictionary三者区别](https://blog.csdn.net/yinghuolsx/article/details/72952857)
******

## 单例模式锁的问题
使用双重锁检查实现线程安全
```
// Bad code! Do not use!
public sealed class Singleton
{
    private volatile static Singleton instance = null;//volatile 可以禁止
    private static readonly object padlock = new object();

    Singleton()
    {
    }

    public static Singleton Instance
    {
        get
        {
            if (instance == null)
            {
                lock (padlock)
                {
                    if (instance == null)
                    {
                        instance = new Singleton();
                    }
                }
            }
            return instance;
        }
    }
}
```  
这样一种设计可以保证只产生一个实例，并且只会在初始化的时候加同步锁
volatile表明属性将被多个线程同时访问，告知编译器不要按照单线程访问的方式去优化该字段，线程会监听字段变更，但是不保证字段访问总是顺序执行  

[C# 单例模式的多种简单实现](https://www.cnblogs.com/zh7791/p/7930342.html)  

******  

## sleep和wait区别  

sleep和wait都是使线程暂时停止执行的方法，但它们有很大的不同。

1. sleep是线程类Thread 的方法，它是使当前线程暂时睡眠，可以放在任何位置。而wait，它是使当前线程暂时放弃对象的使用权进行等待，必须放在同步方法或同步块里。
2. Sleep使用的时候，线程并不会放弃对象的使用权，即不会释放对象锁，所以在同步方法或同步块中使用sleep，一个线程访问时，其他的线程也是无法访问的。而wait是会释放对象锁的，就是当前线程放弃对象的使用权，让其他的线程可以访问。
3. 线程执行wait方法时，需要其他线程调用Monitor.Pulse()或者Monitor.PulseAll()进行唤醒或者说是通知等待的队列。而sleep只是暂时休眠一定时间，时间到了之后，自动恢复运行，不需另外的线程唤醒.  

******  

## 闭包问题  

C#中通常通过匿名函数和lamada表达式来实现闭包。

**原因**
编译器将闭包引用的局部变量转换为匿名类型的字段，导致了局部变量分配在堆中。

**分析**
匿名函数不同于命名方法，可以访问它门外围作用域的局部变量和环境。**而只要匿名函数有效，即使变量已经离开了作用域，这个变量的生命周期也会随之扩展**。这个现象被称为闭包。

**条件**
闭包是将一些执行语句的封装，可以将封装的结果像对象一样传递，在传递时,这个封装依然能够访问到原上下文。 
形成闭包有一些值得总结的非必要条件： 
1. 嵌套定义的函数。 
2. 匿名函数。 
3. 将函数作为参数或者返回值。 
4. 在.NET中，可以通过匿名委托形成闭包：函数可以作为参数传递，也可以作为返回值返回，或者作为函数变量。而在.NET中，这都可以通过委托来实现。这些是实现闭包的前提。

**避免闭包陷阱**
如何避免闭包陷阱呢？C#中普遍的做法是，将匿名函数引用的变量用一个临时变量保存下来，然后在匿名函数中使用临时变量。

[C# 闭包问题-你被”坑“过吗？](https://www.cnblogs.com/HQFZ/p/4903400.html)
[C# 闭包解析](https://blog.csdn.net/cjolj/article/details/60868305)
[C# 从CIL代码了解委托，匿名方法，Lambda 表达式和闭包本质](http://www.cnblogs.com/max198727/p/3436220.html)

******  

##  IEumerable接口 IEumerator接口 

IEnumerable 只是表明某个对象能够被枚举，真正的工作是由IEnumerator的Current、 MoveNext、Reset完成的，为什么要有2个不同的接口来作枚举呢?主要是考虑到被枚举的对象会有多个独立的客户端调用。

在现实应用中，对于集合以及枚举这些集合的需求非常普遍， 因此在.NET中集合所依赖的接口被设计为公共的。想要实现对象的枚举就必须继承IEnumerable接口。

1. 一个Collection要支持foreach方式的遍历，必须实现IEnumerable接口（亦即，必须以某种方式返回IEnumerator object）。

2. IEnumerator object具体实现了iterator（通过MoveNext()，Reset()，Current）。

3. 从这两个接口的用词选择上，也可以看出其不同：IEnumerable是一个声明式的接口，声明实现该接口的class是“可枚举（enumerable）”的，但并没有说明如何实现枚举器（iterator）；IEnumerator是一个实现式的接口，IEnumerator object就是一个iterator。

4. IEnumerable和IEnumerator通过IEnumerable的GetEnumerator()方法建立了连接，client可以通过IEnumerable的GetEnumerator()得到IEnumerator object，在这个意义上，将GetEnumerator()看作IEnumerator object的factory method也未尝不可。

[介绍一下IEnumerator 和 IEnumberator](https://www.jobui.com/mianshiti/it/sharp/4414/)

******  

