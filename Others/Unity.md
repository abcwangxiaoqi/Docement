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

