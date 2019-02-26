import pickle
def dataTranslate():
    f=open('data.txt','r')
    global data
    global doc
    doc=dict()
    data=f.read().split('\n')
    for i in data:
        k=i.split('/')
        doc[k[0]]={'age':int(k[1]),'part':k[2],'times':{}}
        with open('data.p','wb') as fw:
            pickle.dump(doc,fw)
dataTranslate()
