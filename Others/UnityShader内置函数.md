## ComputeScreenPos  

看该函数的命名第一直觉是该函数返回的是屏幕空间下的坐标值，但是该函数返回的是齐次坐标下的屏幕坐标值  

**ComputeScreenPos**返回的值是齐次坐标系下的屏幕坐标值，其范围为[0, w]。那么为什么Unity要这么做呢？Unity的本意是希望你把该坐标值用作tex2Dproj指令的参数值，tex2Dproj会在对纹理采样前除以w分量。

[Unity Shader中的ComputeScreenPos函数](https://www.jianshu.com/p/df878a386bec)  

******