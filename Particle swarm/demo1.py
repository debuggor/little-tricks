#粒子群优化算法自己实现
#目标函数min x**2+y**2+2*x+2*y-10
#-*- coding:utf-8 -*-

import numpy as np
import random
import matplotlib.pyplot as plt

plt.style.use('ggplot')
#可调参数
n = 100  #初始粒子的数目
c1 = 2 #粒子自身学习因子
c2 = 2 #粒子全局学习因子
N = 500 #迭代次数
e = 0.00001 #精度

x_lim = [-100,100]
y_lim = [-100,100]

x = np.linspace(x_lim[0],x_lim[1],int(np.sqrt(n)))
y = np.linspace(y_lim[0],y_lim[1],int(np.sqrt(n)))
x_tem,y_tem= np.meshgrid(x,y)
x_ = np.array(x_tem).reshape(n)
y_ = np.array(y_tem).reshape(n)
points = [[i,j] for i,j in zip(x_,y_)]

def fun(x,y):
    return x**2+y**2+2*x+2*y-10

v =[[0,0]]*n   #初始化速度
p = points     #粒子自身的最优位置
pg = [1,2]    #全局最优位置
min_ = fun(5,5)   #初始化目标
p_z = [fun(i, j) for i, j in points]  #初始每个粒子所处位置的情况
min_result = []

for m in range(N):
    min_result.append(min_)
    #更新pg
    for i,j in points:
        if(fun(i,j)<min_):
            min_ = fun(i,j)
            pg = [i,j]

    #遍历每个粒子
    for num in range(n):
        for i,w in enumerate(points[num]):
            random.seed()
            k1 = np.random.rand()
            k2 = np.random.rand()
            v[num][i] = v[num][i] + c1*k1*(p[num][i]-w) + c2*k2*(pg[i]-w) #更新速度

            #限制速度范围
            if(v[num][i]>5):
                v[num][i] = 5
            elif(v[num][i]<-5):
                v[num][i]=-5

            points[num][i] = points[num][i]+v[num][i]  #更新位置
            #限制位置
            if(points[num][i]>10):
                points[num][i] = 10
            elif(points[num][i]<-10):
                points[num][i] = -10

        #更新粒子自身位置
        tem = fun(points[num][0],points[num][1])
        if(tem<p_z[num]):
            p[num] = points[num]

    if(m>10):  #在进行10次迭代后进行判断，若满足要求了，就结束迭代
        if ((min_result[-9] - min_result[-1]) < e):
            break

print(min_)   #-11.9871503624 很接近最小值-12了
plt.plot(min_result)
plt.show()

