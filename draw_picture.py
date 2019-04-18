#!/usr/bin/python evn

import re
import numpy as  np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"'examples: https://matplotlib.org/gallery/index.html'"
def draw_scatter(s):
    "'params: n: 点的数量,int; s: 点的大小,int'"
    
    data = np.loadtxt(r'D:\Work\projects\draw_pic_test.txt',encoding='utf-8')
    x1 = data[:, 1]  #横坐标
    x2 = data[:, 2]
    y1 = data[:, 0]   #纵坐标

    fig = plt.figure()     #创建画图窗口
    ax=fig.add_subplot(1, 1, 1)
    ax.set_title('VAF')
    ax.set_xlabel('dot')
    ax.set_ylabel('freq')
    #画散点图
    ax.scatter(y1, x1, s=s, color='blue', marker='.')
    ax.scatter(y1, x2, s=s, color='yellow', marker='*')
    plt.xlim(xmin=0)
    plt.show()


def draw_barchart():
    #柱形图
    "'A bar plot with errorbars and height labels on individual bars'"

    x1=(20,35,30,35,27)
    x2=(25,32,34,20,25)
    ind=np.arange(len(x1)) #the locations for the groups
    width=0.35   #the width of the bars

    ax=plt.subplot()
    rects1 = ax.bar(ind - width/2, x1,width, color='skyblue', label='group1')
    rects1 = ax.bar(ind + width / 2, x1, width, color='indianred', label='group2')

    ax.set_ylabel('y')
    ax.set_title('by group')
    ax.set_xticks(ind)
    ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
    ax.legend()
    plt.show()


if __name__=='__main__':
    draw_scatter(5)
    # draw_barchart()








def draw_3D():
    #3D图
    fig = plt.figure()
    ax = Axes3D(fig)
    n=256
    x = np.arange(-4, 4, 0.25)
    y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2+Y**2)
    Z = np.sin(R)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
    ax.contour(X, Y, Z, zdim='z', offset=-2, cmap='rainbow')
    ax.set_zlim(-2,2)
    plt.show()


