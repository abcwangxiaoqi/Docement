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

**注意**：用struct或者class左key的时候要重载散列函数(hashcode方法)和equal方法，合理实现，否则底层将所有的内部字段都当作object处理来生成hashcode，这将引起不必要的装箱拆箱操作，产生gc。

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

## 多线程  

**锁**

**原子性操作** 

**线程池**

**如何避免死锁** 

**发生死锁怎么解锁**  

******  

## struct 和 class 区别

[C#详解struct和class的区别](https://blog.csdn.net/qiaoquan3/article/details/51234208)

******  

## override重写 和 overload重载 区别

[C# 重载（overload）与重写(override)](https://blog.csdn.net/yl2isoft/article/details/16369291)

******  

## const 和 readonly 区别

const 静态常量
readonly 动态常量

**静态常量（Const）** 是指编译器在编译时候会对常量进行解析，并将常量的值替换成初始化的那个值。
**动态常量（Readonly）** 的值则是在运行的那一刻才获得的，编译器编译期间将其标示为只读常量，而不用常量的值代替，**这样动态常量不必在声明的时候就初始化，而可以延迟到构造函数中初始化。** 

[C#基本知识点-Readonly和Const的区别](https://www.cnblogs.com/daidaibao/p/4214268.html)


<br/>

+ **const：** 静态常量，也称编译时常量(compile-time constants)，属于类型级，通过类名直接访问，被所有对象共享！

    　　a、叫编译时常量的原因是它编译时会将其替换为所对应的值；

    　　b、静态常量在速度上会稍稍快一些，但是灵活性却比动态常量差一些；

    　　c、静态常量，隐式是静态的，即被static隐式修饰过，不能再用static重复修饰，

    　　d、在声明时初始化；

    　　e、静态常量只能被声明为简单的数据类型(内建的int和浮点型)、枚举或字符串。

    　　f、应用场合例如:Math.PI的定义（要声明一些从不改变且处处唯一的常量，就应该使用静态常量）

 <br/>

+ **readonly：** 动态常量，也称运行时常量(runtime constants)，属于对象级，通过对象访问。

    　　a、而动态常量的值是在运行时获得的；

    　　b、动态常量在性能上稍差一点，但是灵活性好比前者好；

    　　c、readonly可以被static修饰，这时的static readonly和const非常相似；

    　　d、在声明是初始化，在构造函数里初始化；（static readonly常量，如果在构造函数内指定初始值，则必须是静态无参构造函数；）

    　　e、动态常量可以是任意的数据类型。

    　　f、应用场合例如：SqlHelper类的连接字符串定义

**二者最大的差别在于：** 静态常量在编译时会将其换为对应的值，这就意味着对于不同的程序集来说，当你改变静态常量的时候需要将其重新编译，否则常量的值不会发生变化，可能引发潜在的问题，而动态常量就不会有这种情况，此时推荐使用static readonly，因为其是运行时赋值，当常量值被更改，运行时也随之更改。

 

+ **static：** 本不应该把static与前两者放在一起区别对待的，但是static经常和它们搅在一起，所有这里特别把它拿来说个事。static的意义与const和readonly迥然不同，static是指所修饰的成员与类型有关，而与对象无关。

    　　 静态字段和静态构造方法，通常适用于于一些不会经常变化而又频繁使用的数据，比如连接字符串，配置信息等，进行一次读取，以后就可以方便的使用了，同时也节约了托管资源，因为对于静态成员，一个静态字段只标识一个存储位置。

    　　 非静态方法可以访问类中的任何成员，静态方法只能访问类中的静态成员。

 

总结：const是编译时常量，readonly是运行时常量；cosnt较高效，readonly较灵活。在应用上以static readonly代替const，以平衡const在灵活性上的不足，同时克服编译器优化cosnt性能，所带来的程序集引用不一致问题.

******  

## equal 和 == 区别 

**==操作符判断的是堆栈中的值，Equlas判断的是堆中的值。**

C#提供值类型和引用类型，值类型存储在栈上，**故用==判断是直接判断其值是否相等，因为值类型不存在堆中的数据**，因此值类型的Equals也是判断数据。即，**对于值类型而言，==与Equals相同，均是判断其值是否相等。**

对于引用类型而言，其栈中存储的是对象的引用，**那么==就是比较两个引用是否相等**；Equals函数则是比较两个对象在堆中的数据是否一样，**即两个引用类型是否是对同一个对象的引用**。

******
