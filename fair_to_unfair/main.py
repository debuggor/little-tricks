#实现100个人每个人有100块钱，每个人随机给一个人一块钱，看最后钱的分布情况
#-*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']  #显示中文
plt.rcParams['axes.unicode_minus'] = False   #显示负号

people = np.ones(100)*100
N = 100000 #次数

for i in range(N):
    index = np.random.randint(100, size=100)
    for j,k in zip(index,range(100)):
        if(people[k]!=0):
            people[k] -= 1
            people[j] +=1

people_new = np.sort(people)
plt.bar(left=range(1, 101), height=people_new, width=0.5, color='green')
plt.xlabel(u'资金分布从低到高')
plt.ylabel(u'N次后个人资金')
plt.title(u'100000次的分布情况')
plt.show()
