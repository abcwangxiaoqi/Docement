## 协程的迭代操作发生在什么时候  

******  

## assetbundle打包的几种压缩 

******  

## EditorApplicatiion.update 

在什么时候会调用update呢？下面是官网的稳定解释

```
CallbackFunction is used by EditorApplication.update, EditorApplication.modifierKeysChanged,
EditorApplication.playmodeStateChanged, and EditorApplication.hierarchyWindowChanged.
```
意思就是在 运行模式、hierarchy窗口、键盘输入改变时都会出发update

******  

## 解决物体速度过快不能检测碰撞问题 

**一般方法**：调整fixedupdate timer 和 调整碰撞体的厚度，但是对于速度过快的物体还是要失效。

**正经方法**：用发送射线的方式提前检测碰撞点，在update里判断是否到达碰撞点。

******  

## 角色穿墙或者互插的解决方案 

用Physics.SphereCast 球体投射

当胶囊物体投射时与碰撞体相交时，返回真，否则返回假。

**原理： 把你的角色当成一个球型包围的物体，以他为中心，像一个球体发射射线，如果射线检查到碰撞体那么就认为碰撞了，然后就该处理你自己的逻辑，比如让角色停止，反弹，等等**
******  

## 换装原理 

[Unity3D角色换装实现原理及步骤](https://blog.csdn.net/chinadana/article/details/50311205) 
[人物换装和捏脸](https://blog.csdn.net/a352614834/article/details/79435549?utm_source=blogxgwz0)

**设想一个男性角色有10套服装用来更换，而公用的骨骼是一套，因此在打包时仍然将这一套骨骼单独打包，然后再将其他所有的模型打包，一句话总结就是，一套骨骼对应N个模型，这N个模型都公用这一套骨骼，换装的实现实际上就是将相应的身体部分进行更换，比如要换一个手臂  则将新的手臂与身体上除了手臂以外的模型再进行一次网格合并，换句话说  要更换身体某一个部位，实际上就是更新了整个角色模型**

****** 

## 怎么防止特效 穿透 UI 

order layer

****** 

## MSAA SMAA FXAA 

**MSAA**还原度很高，但是费硬件。

**SMAA**是性耗比最佳的模式，用适量的资源得到比较满意的消除狗牙效果。  

[SMAA算法详解](https://blog.csdn.net/qezcwx11/article/details/78426052)

**FXAA**耗费最低，低配置开这种抗锯齿不卡，实际上是一种粗糙的模糊化处理。

******  

## IOS 和 Android 图片压缩格式

****** 

## IOS 渲染方面所做的优化

******  

#  粒子特效优化 

****** 

# 骨骼动画

[骨骼动画优化](http://liweizhaolili.blog.163.com/blog/static/162307442018211103921836)  

[[Unity 3D] Unity 3D 性能优化-粒子优化](https://blog.csdn.net/jiexuan357/article/details/52911385)

**骨骼动画原理**

******


# Linear 和 gammar 空间 

[聊聊Unity的Gamma校正以及线性工作流](https://www.cnblogs.com/murongxiaopifu/p/9001314.html)

******  


# 搜狐畅游 preparations 

1、缓存组建开发完成 
2、update 策略组建开发完成 
timer
frametimer
创建队列
销毁队列

3、shader 
4、特效优化 
5、同步组件化
6、loader组件化
7、熟悉lua--重要

******
