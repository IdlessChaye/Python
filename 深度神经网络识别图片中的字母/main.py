# encoding=utf-8
from neural import *
from layers  import *
import os
import numpy as np
import time

def main():
    print("Welcome~\n")
    #-------对象建立-------#
    datalayer1 = Data('train.npy', 1024)  # 用于训练，batch_size设置为1024
    datalayer2 = Data('validate.npy', 10000)  # 用于验证，所以设置batch_size为10000,一次性计算所有的样例
    inner_layers = []
    inner_layers.append(FullyConnect(17 * 17, 20))
    inner_layers.append(Sigmoid())
    inner_layers.append(FullyConnect(20, 26))
    inner_layers.append(Sigmoid())
    losslayer = CrossEntropyLoss()
    accuracy = Accuracy()

    #-------系统初始化-------#
    if not os.path.exists('NeuralNetwork'):
        os.mkdir('NeuralNetwork')
        print('无初始神经网络数据，是否训练神经网络？Y/N')
        ans = input()
        if Ans(ans):
            TrainData(datalayer1,datalayer2,inner_layers,losslayer,accuracy)
    elif os.path.exists('NeuralNetwork/data.npy'):
        print('加载神经网络数据')
        LoadData(inner_layers)
        print('加载完毕')
    else:
        print('无初始神经网络数据，是否训练神经网络？(Y/N)')
        ans = input()
        if Ans(ans):
            TrainData(datalayer1,datalayer2,inner_layers,losslayer,accuracy)
        
    #-------主界面-------#
    xunhuan = True
    while xunhuan:
        print('\n您想做什么？\n1.训练神经网络\n2.测试神经网络\n3.退出系统\n请输入数字命令：',end = '')
        choice = input()
        if '1' in choice:
            print()
            TrainData(datalayer1,datalayer2,inner_layers,losslayer,accuracy)
        elif '2' in choice:
            notright = True
            while notright:
                print('\n请输入所要识别的图片编号（1~25000）:')
                try:
                    num = eval(input())
                    if num>=1 &num<=25000:
                        notright = False
                    else:
                        print('数字范围要在(1~25000）内才行 (╯‵□′)╯︵┻━┻ ')
                except:
                    print('额..刚才走神儿了，请重新输入')
                    continue
            x = datalayer1.x[num-1]
            y = datalayer1.y[num-1]
            print('您所选择的图片是：')
            for i in range(17):
                for j in range(17):
                    n = x[i*17+j]
                    if n[0] == 1:
                        print('*',end='')
                    else:
                        print(' ',end='')
                print()
            for layer in inner_layers:
                x = layer.forwardSingle(x)
            maxValue = x[0][0]
            maxindex = 0
            for i in range(len(x)):
                if x[i][0]>maxValue:
                    maxValue = x[i][0]
                    maxindex = i
            result = chr(ord('A')+maxindex)
            print('让我猜猜看……')
            time.sleep(1)
            print('是不是 {} ？(Y/N)'.format(result))
            ans = input()
            if Ans(ans):
                print('太好了~')
            else:
                print('emmmm...下次不会错了！')
        elif '3' in choice:
            xunhuan = False
        else:
            print('\n额..刚才走神儿了，请重新输入')
    print('\nSee you next time~')
                

def Ans(ans):   #当ans字符串内有N/n就返回False
    return ('N' not in ans) & ('n' not in ans)

def SaveData(inner_layers):
    path = 'NeuralNetwork/data.npy'
    try:
        np.save(path,[inner_layers[0].weights,inner_layers[0].bias,inner_layers[2].weights,inner_layers[2].bias])
        print('保存成功')
    except:
        print('Error in SaveData Function')

def LoadData(inner_layers):
    path = 'NeuralNetwork/data.npy'
    try:
        with open(path,'rb') as f:
            loaddata = np.load(f)
        inner_layers[0].weights = loaddata[0]
        inner_layers[0].bias = loaddata[1]
        inner_layers[2].weights = loaddata[2]
        inner_layers[2].bias = loaddata[3]
    except:
        print('Error in LoadData Function')
  
def TrainData(datalayer1,datalayer2,inner_layers,losslayer,accuracy):
    print('请输入训练回合数(正整数)')
    my_epochs = eval(input())
    try:
        train(datalayer1,datalayer2,inner_layers,losslayer,accuracy,epochs = my_epochs)
    except:
        train(datalayer1,datalayer2,inner_layers,losslayer,accuracy)
    print('\n是否保存数据？(Y/N)')
    ans = input()
    if Ans(ans):
        SaveData(inner_layers)
    else:
        print('不保存也罢')

if __name__ == '__main__':
    main()
