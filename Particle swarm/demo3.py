#粒子群优化算法自己实现 加入惯性权重因子
#目标函数min x**2+y**2+2*x+2*y+z**2+z*2-10
#-*- coding:utf-8 -*-

import numpy as np
import random
import matplotlib.pyplot as plt

plt.style.use('ggplot')
#可调参数
n = 10  #初始粒子的数目
c1 = 2 #粒子自身学习因子
c2 = 2 #粒子全局学习因子
N = 1000 #迭代次数
e = 0.00001 #精度
w = 1 #惯性权重因子


x_lim = [-100,100]
y_lim = [-100,100]
z_lim = [-100,100]

x = np.linspace(x_lim[0],x_lim[1],n)
y = np.linspace(y_lim[0],y_lim[1],n)
z = np.linspace(z_lim[0],z_lim[1],n)

x_tem,y_tem,z_tem= np.meshgrid(x,y,z)
x_ = np.array(x_tem).reshape(n**3)
y_ = np.array(y_tem).reshape(n**3)
z_ = np.array(z_tem).reshape(n**3)

points = [[i,j,k] for i,j,k in zip(x_,y_,z_)]

def fun(x,y,z):
    return x**2+y**2+2*x+2*y+z**2+2*z-15

v =[[0,0,0]]*n**3   #初始化速度
p = points     #粒子自身的最优位置
pg = [1,2,1]    #全局最优位置
min_ = fun(5,5,5)   #初始化目标
p_z = [fun(i, j,k) for i, j,k in points]  #初始每个粒子所处位置的情况
min_result = []

for m in range(N):
    min_result.append(min_)
    #更新pg
    for i,j,k in points:
        if(fun(i,j,k)<min_):
            min_ = fun(i,j,k)
            pg = [i,j,k]

    #遍历每个粒子
    for num in range(n):
        for i,wd in enumerate(points[num]):
            random.seed()
            k1 = np.random.rand()
            k2 = np.random.rand()
            w = w*0.99
            v[num][i] = w*v[num][i] + c1*k1*(p[num][i]-wd) + c2*k2*(pg[i]-wd) #更新速度

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
        tem = fun(points[num][0],points[num][1],points[num][2])
        if(tem<p_z[num]):
            p[num] = points[num]

    if(m>50):  #在进行10次迭代后进行判断，若满足要求了，就结束迭代
        if ((min_result[-50] - min_result[-1]) < e):
            break

print(min_)   #三维加入惯性权重因子后的结果-17.9999999995  真实结果-18.0
plt.plot(min_result)
plt.show()

