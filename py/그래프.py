import turtle as t
import math as m
t.shape('circle')
t.speed(20)


def pointer():
    t.clear()
    t.penup()
    t.pensize(0.5)
    t.goto(-960,0)
    t.pendown()
    t.goto(960,0)
    t.penup()
    t.goto(0,540)
    t.pendown()
    t.goto(0,-540)

def graph(y):
    t.penup()
    t.pensize(2)
    y=y*200
    for i in range(1,y):
        x=0.01*(i-(y/2))
        d = pow(2,x)*x
        t.goto(x*100,d*100)
        t.pendown()
        e=t.position()
        if e[1]>540:
            break
    t.penup()
    x=-0.5*m.sqrt(2)
    d=pow(2,x)*x
    t.goto(x*100,d*100-10)
    t.pendown()
    t.circle(10)
def graphlog(y):
    t.penup()
    t.pensize(2)
    y=y*100
    for i in range(1,y):
        x=0.01*i
        d = m.log(x,2)

        t.goto(x*100,d*100)
        t.pendown()

def graphk(y):
    t.penup()
    t.pensize(2)
    y=y*200
    for i in range(1,y):
        x=0.01*(i-(y/2))
        if x!=0:    
            d = 2/x
            t.goto(x*100,d*100)
        t.pendown()

def graphd(y):
    t.penup()
    t.pensize(2)
    y=y*200
    for i in range(1,y):
        x=0.01*(i-(y/2))
        d = m.sin(x)
        t.goto(x*100,d*100)
        t.pendown()
        e=t.position()
        if e[0]>960:
            break
def grapht(y):
    t.penup()
    t.pensize(2)
    y=y*200
    for i in range(1,y):
        x=0.01*(i-(y/2))
        if i%2==0:
            d = m.sin(x)
        elif x!=0:
            d = 2/x
        t.goto(x*100,d*100)
        t.pendown()
        e=t.position()
        if e[0]>960:
            break
pointer()

