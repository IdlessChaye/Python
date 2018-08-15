# Python_小林家的龙女仆
## 效果图
![finalOutputPicture](https://github.com/IdlessChaye/Python/blob/master/%E5%B0%8F%E9%82%BB%E5%AE%B6%E7%9A%84%E9%BE%99%E5%A5%B3%E4%BB%86/dragon.png?raw=true)
## 用到的图片素材
![samplePicture](https://github.com/IdlessChaye/Python/blob/master/%E5%B0%8F%E9%82%BB%E5%AE%B6%E7%9A%84%E9%BE%99%E5%A5%B3%E4%BB%86/code/1.jpg)
## 用到的模块
- turtle
- Image (PIL)
- ImageFilter (PIL)
- numpy
- math
## 基本思想
- 运用PIL库提取图片的数据，递归画图。
DrawPics
- (angle,deltaAngle,size,anchor,resolutionLost,count)。此函数实现递归画图，angle初始朝向角度，deltaAngle递归改变角度，size画板上图片大小，anchor图片固定锚点，resolutionLost图片分辨率损失，count剩余递归调用次数。
- 这个函数的设计思想就是在得到图片灰度数据的情况下，利用turtle库可以在指定位置上画图的特点，设置图片的位移（anchor），尺寸（size），旋转角度（angle）来进行递归画图。
- 再运用turtle库画出英文字母Dragon突出主题。
