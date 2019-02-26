import turtle as t
from math import *
t.shape('circle')
t.speed(0)
y=0
prove=0
def pointer():
    t.penup()
    t.pensize(0.5)
    t.goto(-960,0)
    t.pendown()
    t.goto(960,0)
    t.penup()
    t.goto(0,540)
    t.pendown()
    t.goto(0,-540)


        
pointer()
k='y'
while k=='y':
    a=input('y에 대한 수식 입력:')
    t.penup()
    t.pensize(1)
    for i in range(1920):
        try:
            x=0.01*(i-960)
            exec(a)
            if not((x<-9.60 or x>9.60) or (y<-7.50 or y>7.50)):
                
                t.goto(x*100,y*100)
                
                t.pendown()
                
                if prove==1:
                    print("printing...")
                    prove=0
            else:
                if prove==0:
                    print("stay...")
                    prove=1
                
        except ValueError:
            t.penup()
        except ZeroDivisionError:
            t.penup()    
    k=input('계속?(y/n):')
    d=input('그래프를 정리할까요?(y/n):')
    if d=='y':
        t.clear()
        pointer()
