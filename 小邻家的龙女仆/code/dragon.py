import turtle as t
from PIL import Image
from PIL import ImageFilter
import numpy as np
import math
def SetTurtle(): 
    # 设置Turtle的画板
    t.setup(1000,1000)
    t.up()
    t.pensize(2)
    t.fillcolor('orange')
    t.pencolor('orange')
    t.speed(0) # 最大速度
    t.Turtle().screen.delay(0) # 最小延迟
def GetPicData(resolutionLost): 
    # 得到图片的灰度数据,resolutionLost是图片的分辨率损失，值越大，图片越不清晰，但画的越快
    im = Image.open('1.jpg') 
    im = im.resize((im.size[0] // resolutionLost,im.size[1] // resolutionLost))
    color = im.split()
    m2 = im.filter(ImageFilter.CONTOUR)
    mArray = np.array(m2.convert('L'))
    return mArray,m2.size,color
def DrawPics(angle,deltaAngle,size,anchor,resolutionLost,count):
    # 递归画图，angle初始朝向角度，deltaAngle递归改变角度，size图片占地大小，anchor图片固定锚点坐标
    # resolutionLost图片分辨率损失，count剩余递归调用次数
    if count == 0:
        return
    mArray,siz,color = GetPicData(resolutionLost)
    colorR = np.array(color[0])
    colorG = np.array(color[1])
    colorB = np.array(color[2])
    xRatio = size[0] / siz[0] # x轴方向上的放大比例系数，使图片能放缩到指定的size
    yRatio = size[1] / siz[1]
    defaultAngle = math.atan(size[0] / size[1] / 2) + math.pi / 2 
    thisAngle = defaultAngle + angle # 图片左上角的坐标相对于锚点的角度
    sizeLength = math.sqrt((size[0] / 2) ** 2 + size[1] ** 2)
    scanPositionX = math.cos(thisAngle) * sizeLength + anchor[0] # 图片左上角那个点的横坐标
    scanPositionY = math.sin(thisAngle) * sizeLength + anchor[1] # 图片左上角那个点的纵坐标
    for i in range(siz[1]): # 遍历图片灰度数组中每一个点
        for j in range(siz[0]):
            if i == int(siz[1] / 5) and j == int(siz[0] / 10): # 如果到达了指定的点，就递归画下一个图
                DrawPics(angle + deltaAngle,deltaAngle,(size[0] // 3 * 2,size[1] // 3 * 2)
                         ,(scanPositionX + j * math.cos(angle) * xRatio,scanPositionY + j * math.sin(angle) * yRatio)
                         ,resolutionLost + 1,count - 1)
            elif i == int(siz[1] / 5) and j == int(siz[0] * 9 / 10): # 如果到达了指定的点，就递归画下一个图
                DrawPics(angle - deltaAngle,deltaAngle,(size[0] // 3 * 2,size[1] // 3 * 2)
                         ,(scanPositionX + j * math.cos(angle) * xRatio,scanPositionY + j * math.sin(angle) * yRatio)
                         ,resolutionLost + 1,count - 1)
            if mArray[i,j] < 100: # 如果灰度值小于100，就在这个点的坐标上画一个点
                t.goto(scanPositionX + j * math.cos(angle) * xRatio,scanPositionY + j * math.sin(angle) * yRatio)
                t.pencolor((float(colorR[i,j]/255),float(colorG[i,j]/255),float(colorB[i,j]/255)))
                t.down()
                t.fd(1) # 画一笔
                t.up()
        scanPositionX = scanPositionX + math.sin(angle) * xRatio # 转到下一行，继续扫描图片灰度数据画图
        scanPositionY = scanPositionY - math.cos(angle) * yRatio
    t.hideturtle()
def Dragon():
    t.up()
    t.goto(-130,70) # d
    t.pensize(8)
    t.down()
    t.seth(0)
    t.fd(20)
    t.seth(-30)
    t.circle(-40,120)
    t.seth(180)
    t.fd(20)
    t.seth(110)
    t.fd(4)
    t.seth(0)
    t.fd(6)
    t.seth(90)
    t.fd(64)
    t.seth(-180)
    t.fd(4)
    t.up()
    t.goto(-80,50) # r
    t.pensize(8)
    t.down()
    t.seth(-90)
    t.fd(45)
    t.up()
    t.seth(0)
    t.fd(9)
    t.seth(90)
    t.pensize(6)
    t.down()
    t.fd(37)
    tt = t.clone()
    t.fd(8)
    tt.seth(60)
    tt.circle(-20,30)
    tt.hideturtle()
    t.up()
    t.goto(-50,40) # a
    t.down()
    t.seth(50)
    t.circle(-30,90)
    t.circle(-10,20)
    t.seth(-90)
    t.fd(20)
    t.circle(10,30)
    t.up()
    t.seth(-90)
    t.fd(10)
    t.seth(-180)
    t.down()
    t.circle(-20,50)
    t.seth(-110)
    t.circle(-10,30)
    t.circle(-20,90)
    t.seth(110)
    t.circle(-16,190)
    t.seth(90)
    t.fd(20)
    t.up()
    t.goto(20,47) # g
    t.down()
    t.seth(0)
    t.circle(-19,90)
    tt = t.clone()
    tt.fd(20)
    tt.circle(-17,180)
    tt.hideturtle()
    t.circle(-17,270)
    t.up()
    t.goto(60,35) # o
    t.down()
    t.begin_fill()
    t.circle(-10,360)
    t.end_fill()
    t.up()
    t.goto(80,50) # n
    t.pensize(8)
    t.down()
    t.seth(-90)
    t.fd(45)
    t.up()
    t.seth(0)
    t.fd(9)
    t.seth(90)
    t.pensize(6)
    t.down()
    t.fd(37)
    tt = t.clone()
    t.fd(8)
    tt.seth(60)
    tt.circle(-20,30)
    tt.seth(0)
    tt.fd(8)
    tt.circle(-10,90)
    tt.seth(-90)
    tt.fd(35)
    tt.hideturtle()
    t.up()
def main():
    SetTurtle()
    distance = 50
    for lookToAngle in (0,math.pi * 2 / 3,math.pi * 4 / 3): # 分别有三组递归画图，使图像围在一起
        DrawPics(lookToAngle,math.pi /6,(200,140),(math.cos(lookToAngle + math.pi / 2) * distance,math.sin(lookToAngle + math.pi / 2) * distance),3,4)
    Dragon()
    t.done()
main()