# 问题记录  

## 类的实例化

Class A

A a;
A * a = new a(); 
以上两种方式皆可实现类的实例化，有new的区别在于：
1. 前者在堆栈中分配内存，后者为动态内存分配，在一般应用中是没有什么区别的，但动态内存分配会使对象的可控性增强。
2. 不加new在堆栈中分配内存
3. 大程序用new，小程序直接申请
4. 只是把对象分配在堆栈内存中
5. new必须delete删除，不用new系统会自动回收内存

******  

## * & 

引用的声明方法：类型标识符 &引用名=目标变量名；

```
char ch;
char &rp=ch;//rp 引用ch
```
>
获取指针
```
char* _ch = &ch;// & 获取指针地址
```

>
解指针
```
char _chr = *_ch; //*_ch接指针  _ch为指针地址
```

**注意：**
******  

## 智能指针  

******

## 虚函数表

[C++虚函数表详细解释及实例分析](https://blog.csdn.net/sunshinewave/article/details/51079204?utm_source=blogxgwz0)

******  

## 裸指针  

******  

## 指针函数  

******  

## 左引用 右引用   

******  

## vector和list的区别

**vector**
　　vector与数组类似，拥有一段连续的内存空间，并且起始地址不变。便于随机访问，时间复杂度为$O（1）$，但因为内存空间是连续的，所以在进入插入和删除操作时，会造成内存块的拷贝，时间复杂度为$O（n）$。

　　此外，当数组内存空间不足，会采取扩容，通过重新申请一块更大的内存空间进行内存拷贝。

**List**
　　list底层是由双向链表实现的，因此内存空间不是连续的。根据链表的实现原理，List查询效率较低，时间复杂度为$O（n）$，但插入和删除效率较高。只需要在插入的地方更改指针的指向即可，不用移动数据。 

****** 

## 数组、ArrayList和List三者的区别 

**List** 是针对特定类型、任意长度的。

**Array** 是针对任意类型、固定长度的。

**ArrayList** 是针对任意类型、任意长度的。

**总结：**
+ 数组的容量是固定的，您只能一次获取或设置一个元素的值，而ArrayList或List<T>的容量可根据需要自动扩充、修改、删除或插入数据。

+ 数组可以具有多个维度，而 ArrayList或 List< T> 始终只具有一个维度。但是，您可以轻松创建数组列表或列表的列表。特定类型（Object 除外）的数组 的性能优于 ArrayList的性能。 这是因为 ArrayList的元素属于 Object 类型；所以在存储或检索值类型时通常发生装箱和取消装箱操作。不过，在不需要重新分配时（即最初的容量十分接近列表的最大容量），List< T> 的性能与同类型的数组十分相近。
    
+ 在决定使用 List<T> 还是使用ArrayList 类（两者具有类似的功能）时，记住List<T> 类在大多数情况下执行得更好并且是类型安全的。如果对List< T> 类的类型T 使用引用类型，则两个类的行为是完全相同的。但是，如果对类型T使用值类型，则需要考虑实现和装箱问题。

******  

## 右值引用  

一个左值表达式代表的是**对象本身**，而右值表达式代表的是**对象的值**；变量也是左值。

[【原创】深入理解c++的右值引用](https://www.cnblogs.com/cposture/p/4927712.html)
[C++右值引用浅析](https://www.cnblogs.com/concurrency/p/4066304.html)

******  

## lua gc 

[Lua GC 的源码剖析 (1)](https://blog.codingnow.com/2011/03/lua_gc_1.html)
[Lua GC 的源码剖析 (2)](https://blog.codingnow.com/2011/03/lua_gc_2.html) 
[Lua GC 的源码剖析 (3)](https://blog.codingnow.com/2011/03/lua_gc_3.html) 
[Lua GC 的源码剖析 (4)](https://blog.codingnow.com/2011/03/lua_gc_4.html)
[Lua GC 的源码剖析 (5)](https://blog.codingnow.com/2011/03/lua_gc_5.html)

******  

## protobuffer 压缩算法  

******  

## lua 虚拟机  

******  

## lua和mono如何通讯

******  

##  TCP/UDP/可靠UDP  

KCP 了解

[可靠 UDP 传输](https://blog.codingnow.com/2016/03/reliable_udp.html#comments)

******