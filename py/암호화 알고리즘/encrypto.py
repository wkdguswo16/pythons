import random as r
import pickle
import base64 as b
import math as m
def shuffle(lis):
    repeat=1
    while True:
        rotate=2**repeat
        if rotate>len(lis):
            break
        else:
            for i in range(rotate):
                lis.insert(i,lis.pop(rotate-1))
            repeat+=1
    return lis

def shufflerev(lis):
    repeat=int(m.log(len(lis),2))
    while True:
        rotate=2**repeat
        if repeat==0:
            break
        else:
            for i in range(rotate):
                lis.insert(i,lis.pop(rotate-1))
            repeat-=1
    return lis

def dummy(lis,state):
    if state==True:
        dcount=r.randint(2,len(lis))
        k=list()
        for i in lis:
            k.append(i)
            try:
                if int(m.log(lis.index(i),dcount))==m.log(lis.index(i),dcount):
                    k.append(chr(r.randint(32,126)))
            except ValueError:
                pass        
        lis=k
        lis.append(chr(dcount+29))
        return lis
    elif state==False:
        dcount=ord(lis.pop(-1))-29
        save=''
        for i in range(len(lis)):
            if (i+1)%(dcount)!=0:
                save+=lis[i]
        lis=list(save)
        return lis
#def pass:

#def hyperbolic:

def encode(con,fe):
    fe=b.b64encode(fe.encode('utf-8'))
    
    fe=list(str(fe))
    shuffle(fe)
    fe.reverse()
    op=list()
    conlist=list()
    global enc
    enc=''
    for i in range(len(fe)):
        container=r.randint(0,95)
        conlist.append(container)
        op.append(con[container][i%complexepic][1][con[container][i%complexepic][0].index(fe[i])])
    for i in range(len(fe)):
        op.insert(i*2,chr(conlist[i]+32))
    shuffle(op)
    op.reverse()   
    for i in op:
        enc+=i
    return enc
def decode(con,fe):
    global dec
    dec=''
    no=''
    fe=list(fe)
    fe.reverse()
    shufflerev(fe)
    conlist=list()
    for i in range(int(len(fe)/2)):
        conlist.append(fe.pop(i))
    for i in range(len(fe)):
        dec+=con[ord(conlist[i])-32][i%complexepic][0][con[ord(conlist[i])-32][i%complexepic][1].index(fe[i])]
        dec=list(dec)
    dec.reverse()
    shufflerev(dec)
    if not(dec[0]=='b' and dec[1]=="'" and dec[-1]=="'"):
        return print('맞지 않은 정보입니다')
    for i in range(2,len(dec)-1):
        no+=dec[i]
    dec=no
    no=str(b.b64decode(no),encoding='utf-8')
    return no
print('암호화 및 복호화 알고리즘')

while True:
    try:
        data=''
        add=input('\n\n1.암호화\n2.복호화\n3.암호화코드 제작\n4.암호화코드 적용\n5.종료\n입력:')
        if add=='1' and con:
            end=input('1.암호화 파일 선택\n2.한줄 암호화\n입력:')
            if end=='1':
                path=input('파일 위치 선정:')
                f = open(path+'.txt', 'r')
                lines = f.readlines()
                data=''
                for line in lines:
                    data+=line
                f.close()
                print(encode(con,data))
            else:
                data=input('\n암호화 정보 입력:')
                print(encode(con,data))
            et=input("저장하시겠습니까?(y/n):")
            if et=='y':
                save=input('저장할 이름을 입력하세요:')
                f=open(save+'.txt','w')
                f.write(enc)
                f.close()
        elif add=='2' and con:
            ded=input('1.복호화 파일 선택\n2.한줄 복호화\n입력:')
            if ded=='1':
                path=input('\n\파일 위치 선정:')
                f = open(path+'.txt', 'r')
                lines = f.readlines()
                data=''
                for line in lines:
                    data+=line
                f.close()
                print(decode(con,data))
            else:
                data=input('\n복호화 정보 입력:')
                print(decode(con,data))
            et=input("저장하시겠습니까?(y/n):")
            if et=='y':
                save=input('저장할 이름을 입력하세요:')
                f=open(save+'.txt','w')
                f.write(dec)
                f.close()
        elif add=='3':
            complexepic=int(input('몇비트 암호화를 하시겠습니까?:'))
            con=list()
            for g in range(96):
                l=list()
                for p in range(complexepic):
                    t=[list(range(32,127)),list(r.sample(range(32, 127), 95))]
                    t[0].insert(0,10)
                    t[1].insert(r.randint(0,95),10)
                    for e in range(96):
                        t[0][e]=chr(t[0][e])
                        t[1][e]=chr(t[1][e])
                    l.append(t)
                con.append(l)
            name=input('저장할 이름을 입력하세요:')
            with open(name+".txt",'wb') as fw:
                pickle.dump(con,fw)
        elif add=='4':
            name=input('불러들일 암호화코드 이름을 입력하세요')
            with open(name+".txt","rb") as fr:
                con = pickle.load(fr)
                complexepic=len(con[0])
        elif add=='5':
            exit()

    except FileNotFoundError:
        print('파일 이름이 존재하지 않습니다')
        pass
    except NameError:
        print('먼저 암호화코드를 불러들어주세요')
        pass
    except IndexError:
        print('해석이 불가능한 구문이거나 문법오류입니다')
        pass
    except ValueError:
        print('올바른 값이 아닙니다')
        pass
    except pickle.UnpicklingError:
        print('해석용 구문이 아닙니다.')
    except TypeError:
        print('올바른 타입이 아닙니다')
    
