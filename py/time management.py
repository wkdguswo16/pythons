import pickle
import time as t
from datetime import date as d

def dataTranslate(text):
    f=open(text+'.txt','r')
    global data
    global doc
    doc=dict()
    data=f.read().split('\n')
    data.sort()
    f.close()
    for i in data:
        k=i.split('/')
        doc[k[0]]={'part':k[1],'times':[]}

def datasave(doc):
        with open('data.p','wb') as fw:
            pickle.dump(doc,fw)

def kakao(text):
    f=open(text+'.txt','r',encoding='UTF8')
    global texts
    texts=f.read().split('\n')
    f.close()

def param(tex):
    ke=list()
    for i in tex.split():
        ke.append(i.replace('[','').replace(']',''))
    return ke

def datemanage(i,date):
    if i[1]=='오후':                    
        i[2]=[int(i[2].split(':')[0])+12,int(i[2].split(':')[1])]
    else:
        i[2]=[int(i[2].split(':')[0]),int(i[2].split(':')[1])]
    if i[2][0]==12 or i[2][0]==24:
        i[2][0]-=12            
    i[3]=int(i[3].split('/')[0])
    i[1]=date
    return i

def datasort(conv):
    date=list()
    for i in conv:
        try:
            if len(i)==6 and i[0]=='---------------':
                date=i[1:4]
            elif (len(i)==4 and len(i[3].split('/'))==2):
                praydata.append(datemanage(i,date))
            elif len(i)==5 and len(i[4].split('/'))==2:
                i[0]=i[0]+i.pop(1)
                i[3]=i[3].split('/')[0]
                praydata.append(datemanage(i,date)) 

        except ValueError:
            pass

def intodata(praydata,doc):
    for i in praydata:
        doc[i[0]]['times'].append({'year':int(i[1][0].replace('년','')),'month':int(i[1][1].replace('월','')),'date':int(i[1][2].replace('일','')),'hour':i[2][0],'minute':i[2][1],'time':i[3]})
    return doc
def personalFind(doc,name):
	for i in doc.items():
		if i[0]==name:
			return i
	return none
def pdriver(doc,search):
    a=list()
    b=['year','month','date','hour','minute','time']
    for i in sorted(doc.items()):
        for j in range(len(i[1]['times'])):
            check=True
            for k in range(6):
                
                if not(i[1]['times'][j][b[k]]==search[k] or search[k]==True):
                    check=False
            if check==True:
                a.append([i[0],i[1]['times'][j]])
    return a

def prayed(doc,state):
    ssum=0
    global count
    count=0
    for i in doc.items():
        for j in range(len(i[1]['times'])):
            ssum+=i[1]['times'][j]['time']
            count+=1
    if state=='sum':
        return ssum
    elif state=='ave':
        return ssum/count
    elif type(state)==int:
        return (ssum/state)
def weeksum(doc,date):
	k=pdriver(doc,'date',date)[0][0]
	s=0
	for i in pdriver(doc,'date',date):
		if i[0]!=k:
			print(k,s)
			s=0
			k=i[0]
		s+=i[1]['time']
	print(k,s)

conv=list()
praydata=list()
date=list()
dataTranslate('data')
kakao('kakao')
for i in texts:
    conv.append(param(i))
datasort(conv)
intodata(praydata,doc)
datasave(doc)
print('총합:',prayed(doc,'sum'),'평균:',round(prayed(doc,'ave'),3),'목표 달성률:',str(round(prayed(doc,10000)*100,2))+'%')
datasave(doc)
