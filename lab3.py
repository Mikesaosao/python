import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as np
from pylab import *
import time

x0=[]
y0=[]
bucket=[]

class Node(object):
    def __init__ (self,x,dx,ymax,next=None):
        self.x=x
        self.dx=dx
        self.ymax=ymax
        self.next=next


class nodelink(object):
    def __init__(self,y):
        self.head=Node(0,0,0)
        self.tail=self.head
        self.y=y
    def size(self):
        tmp=self.head
        k=1
        while tmp is not None:
            tmp=tmp.next
            k+=1
        return k
    #添加元素
    def append(self,x,dx,y):
        data=Node(x,dx,y)
        if data is None:
            return None
        else:
            
                self.tail.next=data
                self.tail=data
             
    #排序
    def sort(self):
        tmp=self.head.next
        nt=[]
        while tmp is not None:
            nt.append(tmp)
            tmp=tmp.next
        #不必排序
        if len(nt)==0 or len(nt)==1:
            return
        n=len(nt)
        i=0
        while i<n-1:
            j=i+1
            while j<n:
                if nt[j].x<nt[i].x:
                    tmp=nt[j]
                    nt[j]=nt[i]
                    nt[i]=tmp
                j+=1
            i+=1
        t0=self.head
        t0.next=nt[0]
        i=0
        while i<n-1:
            nt[i].next=nt[i+1]
            i+=1
        nt[n-1].next=None
        
    
#找出ymin
def findYmin(y):
    yt=y[0]
    for i in y:
        if i<yt:
            yt=i
    return yt

#找出ymax
def findYmax(y):
   
    yt=y[0]
    for i in y:
        if i>yt:
            yt=i
    return yt
    
#新边表
def NET():
    print("请输入顶点个数:")
    n=(int)(input())
    '''
    i=0
    #按照顺序输入顶点坐标
    while i<n:
        print("请输入x:")
        x0.append((int)(input()))
        print("请输入y:")
        y0.append((int)(input()))
        i+=1
    '''
   
    i=0
    while i<len(x0):
        plt.scatter(x0[i],y0[i],c='b')
        i+=1
    ymin=findYmin(y0)
    ymax=findYmax(y0)
    ytk=ymin
    #初始化bucket
    while ytk<=ymax:
        bucket.append(nodelink(ytk))
        ytk+=1
    
    #开始建立NET
    k=0
    for yy in y0:
        for bu in bucket:
            if bu.y==yy:
                ytt=bu
        #当是第一个元素时
        if k==0:
            if y0[1]>yy:
                ymx=y0[1]
                dx=((float)(x0[1]-x0[0]))/((float)(y0[1]-y0[0]))
                ytt.append(x0[0],dx,ymx)
                #print(ytt.shead().dx)
            if y0[n-1]>yy:
                ymx=y0[n-1]
                dx=((float)(x0[n-1]-x0[0]))/((float)(y0[n-1]-y0[0]))
                ytt.append(x0[0],dx,ymx)
            
        #当时最后一个元素时
        elif k==n-1:
            if y0[n-2]>yy:
                ymx=y0[n-2]
                dx=((float)(x0[n-2]-x0[n-1]))/((float)(y0[n-2]-y0[n-1]))
                ytt.append(x0[n-1],dx,ymx)
            if y0[0]>yy:
                ymx=y0[0]
                dx=((float)(x0[n-1]-x0[0]))/((float)(y0[n-1]-y0[0]))
                ytt.append(x0[n-1],dx,ymx)
        #中间元素时
        else:
            if y0[k-1]>yy:
                ymx=y0[k-1]
                dx=((float)(x0[k-1]-x0[k]))/((float)(y0[k-1]-y0[k]))
                ytt.append(x0[k],dx,ymx)

            if y0[k+1]>yy:
                ymx=y0[k+1]
                dx=((float)(x0[k+1]-x0[k]))/((float)(y0[k+1]-y0[k]))
                ytt.append(x0[k],dx,ymx)
        k+=1
    #for tm in bucket:
    #   tm.sort()
#活性边表
def AET():
    #因为最低点不需改变，所以从第二个点开始
    k=1
    while k<(len(bucket)-1):
        ktmp=bucket[k-1].head
        ktmp=ktmp.next
        while ktmp is not None:     
            if bucket[k].y<ktmp.ymax:
                x=(int)(ktmp.x+ktmp.dx+0.5)
                dx=ktmp.dx
                ymax=ktmp.ymax
                bucket[k].append(x,dx,ymax)
            ktmp=ktmp.next
        k+=1
        
#画出AET表
def printAet():
    for i in bucket:
        tmp=i.head
        tmp=tmp.next
        print(i.y,end="|")
        while tmp is not None:
            print(tmp.x,end=" ")
            print(tmp.dx,end=" ")
            print(tmp.ymax,end="||")
            tmp=tmp.next
        print("\n")

#开始扫描填充
def draw():
    #画出所有的顶点
    
    #画出边界
    for bct in bucket:
        tmp=bct.head.next
        while tmp is not None:
            plt.scatter(tmp.x,bct.y,c='b')
            tmp=tmp.next
    for bct in bucket:
        tmp=bct.head.next
        k=True
        while tmp is not None:

            if k is True:
                x=tmp.x
                while x<tmp.next.x:
                    plt.scatter(x,bct.y,c='r')
                    plt.pause(0.1)
                    x=x+1
            tmp=tmp.next
            k=not k
            

if __name__=="__main__":
     #找出最小y值对应编号

    x0=[5,2,2,5,11,11]
    y0=[1,2,7,5,8,3]
    
    plt.grid()
    NET()
    AET()
    #排序
    for i in bucket:
        i.sort()
    printAet()
    draw()
    plt.show()

    
        
        
