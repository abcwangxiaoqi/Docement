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
意思就是在 运行模式、hierarchy窗口、键盘输入改变时都会出发update

******  

