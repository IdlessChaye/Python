# encoding=utf-8
from layers import *

def train(datalayer1,datalayer2,inner_layers,losslayer,accuracy,epochs=20,learnrate=1):
    for layer in inner_layers:
        layer.lr = learnrate  # 为所有中间层设置学习速率
    print('start training')
    for i in range(epochs):
        print('epochs:', i)
        losssum = 0
        iters = 0
        while True:
            data, pos = datalayer1.forward()  # 从数据层取出数据
            x, label = data
            for layer in inner_layers:  # 前向计算
                x = layer.forward(x)

            loss = losslayer.forward(x, label)  # 调用损失层forward函数计算损失函数值
            losssum += loss
            iters += 1
            d = losslayer.backward()  # 调用损失层backward函数曾计算将要反向传播的梯度

            for layer in inner_layers[::-1]:  # 反向传播
                d = layer.backward(d)

            if pos == 0:  # 一个epoch完成后进行准确率测试
                data, _ = datalayer2.forward()
                x, label = data
                for layer in inner_layers:
                    x = layer.forward(x)
                accu = accuracy.forward(x, label)  # 调用准确率层forward()函数求出准确率
                print( 'loss:', losssum / iters)
                print('accuracy:', accu)
                break
    print('training over~')

