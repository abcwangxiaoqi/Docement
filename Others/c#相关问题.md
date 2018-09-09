## HashTable、 Dictionary、ConcurrentDictionary区别

1. *Dictionary* 支持泛型 
    *HashTable*不支持泛型，非引用类型有装箱拆箱操作，影响效率
2. *ConcurrentDictionary* 在 *Dictionary* 加入了线程安全，Dictionary是非线程安全的类型，操作的时候需要对其进行线程安全处理，最简单的方式就是加锁(lock)。 

3. .Net4.0中 *ConcurrentDictionary* 是线程安全的字典。

+ 总结
    大数据插入*Dictionary*花费时间最少
    遍历*HashTable*最快是*Dictionary*的1/5,*ConcurrentDictionary*的1/10
    单线程建议用*Dictionary*，多线程建议用*ConcurrentDictionary*或者*HashTable*
    （Hashtable tab = Hashtable.Synchronized(new Hashtable());获得线程安全的对象）

+ *ConcurrentDictionary*如何保证线程安全
*ConcurrentDictionary*可以说是为了避免一个大锁锁住整个*Dictionary*带来的性能损失而出来的，当然也是采用空间换时间，不过这空间换得还是很值得的，一些object而已。原理在于*Dictionary*本质是是一个链表数组，只有在多线程同时操作到数组里同一个链表时才需要锁，所以就用到一个锁数组，每个锁罩着几个小弟(bucket及bucket内的链表元素)，这样多线程读写不同锁罩的区域的时候可以同时进行而不会等待，进而提高多线程性能。

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