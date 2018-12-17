#!/usr/bin/env/python3



"""tile.py: Describtion of how to place size(a,b)bricks on a size(m,n)wall.



__author__ = "QiuWeiJie"

__pkuid__  = "1800011802"

__email__  = "qiuweijie2000@pku.edu.cn"

"""

if (m * n) % (a * b) != 0:
    print("无法铺出砖")
else:
    wall = [([0] * m) for i in range(n)]   #定义墙
    
    def conflict(wall,p,q):                   #定义判断是否铺重的conflict函数
        c = True
        for p in range(n):
            for q in range(m):
                if wall[p][q] == 2:
                    c = False
                    break
        return c

    #判断是否能横铺砖的函数
    def hengpu_judge(wall,p,q):
        if q + a > m or p + b > n:
            return False
        else:
            wall1 = hengpu(wall,p,q)
            return conflict(wall1,p,q)
    
    #从找到的地方开始横着铺
    def hengpu(wall,p,q):
        brick = []
        for x in range(p,p + b):
            for y in range(q,q + a):
                wall[x][y] = wall[x][y] + 1
                k = y * m + x
                brick.append(k)
        return brick ,wall
    
    #拆掉横铺的砖，为纵铺做准备
    def hengchai(wall,p,q):
        for x in range(p,p + b):
            for y in range(q,q + a):
                walll[x][y] = walll[x][y] - 1
        return wall
    
    #判断是否能纵铺砖的函数
    def zongpu_judge(wall,p,q):
        if q + b > m or p + a > n:
            return False
        else:
            wall1 = zongpu(wall,p,q)
            return conflict(wall1,p,q)
    
    #从找到的地方开始纵向铺
    def zongpu(wall,p,q):
        brick = []
        for x in range(p,p + a):
            for y in range(q,q + b):
                wall[x][y] = wall[x][y] + 1
                k = y * m + x
                brick.append(k)
        return brick,wall
    
    #拆掉纵铺的砖
    def zongchai(wall,p,q):
        for x in range(p,p + b):
            for y in range(q,q + a):
                walll[x][y] = walll[x][y] - 1
        return wall
    

    def puzhuan(ans,alls):  #开始铺砖
        global wall
        if wall == [([1] * m) for i in range(n)]:    #如果已经铺完，直接输出结果
            alls.extend([ans[:]])
        else:
            for p in range(n):   #找到第一个未铺砖的地方(p,q)
                for q in range(m):
                    if wall[p][q] == 0:
                        if hengpu_judge(wall,p,q):
                            wall = hengpu(wall,p,q)[0]
                            ans.append(hengpu(wall,p,q)[1])
                            puzhuan(ans,alls)
                            wall = hengchai(wall,p,q)
                            ans.pop()
                        if zongpu_judge(wall,p,q):
                            wall = zongpu(wall,p,q)[0]
                            ans.append(zongpu(wall,p,q)[1])
                            puzhuan(ans,alls)
                            wall = zongchai(wall,p,q)
                            ans.pop()
                            

                            
def main():
    m = int(input("请输入墙的长："))  #有几列
    n = int(input("请输入墙的宽："))  #有几行
    a = int(input("请输入砖的长："))
    b = int(input("请输入砖的宽："))

answ=[]
KK=(m*n)//(a*b)
puzhuan([None]*KK,answ)
print(answ)

if _name_ == '_main_':
    main()    
    
#用turtle画出墙上位置的表格
import turtle as t 
w=1080
h=720
u=v=0 
t.setup(w,h)
t.reset()
t.screensize(w,h,"white")
t.clear()
kuang=h/c
chang=w/r  #坐标系转换
x=u-w/2
y=v+h/2
def x_h(u):    
    return(u-w/2)
def y_h(v):    
    return(v+h/2)  
def huaheng(x,y):    
    t.penup()    
    t.goto(x,y)    
    t.pendown()    
    t.forward(w)    
    t.penup()    
    pass 
def huashu(x,y):    
    t.penup()    
    t.goto(x,y)    
    t.pendown()    
    t.right(90)    
    t.forward(h)    
    t.left(90)    
    t.penup()  
for i in range(0,n-1):    
    x=x_h(0)    
    y=y-kuang    
    huaheng(x,y)
for j in range(0,m-1):    
    x=x+chang        
    y=y_h(0)        
    huashu(x,y)

