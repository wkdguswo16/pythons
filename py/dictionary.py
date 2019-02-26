import pickle

dic1={}
dic2={}
file1 = open("eng.p",'rb')
file2 = open("kor.p",'rb')
dic1=pickle.load(file1)
dic2=pickle.load(file2)
file1.close()
file2.close()
r=1
while r<=2:
    print('===파이썬 사전===\n모드를 선택하세요:\n1.번역 모드\n2.저장 모드\n3.종료')
    r=int(input('인수 입력:'))
    if r==1:
        l='y'
        while l=='y':
            let=input("번역할 단어를 입력하세요:")
            if let in dic1:
                print("결과:{}".format(dic1[let]))
            elif let in dic2:
                print("결과:{}".format(dic2[let]))
            else:
                print("입력한 값이 사전에는 없습니다")
            l=input("계속?(y/n):")
    elif r==2:
        l='y'
        while l=='y':
            eng=input("영어 입력:")
            kor=input("한글 입력:")
            dic1[eng]=kor
            dic2[kor]=eng
            l=input("계속?(y/n):")
        file1 = open("eng.p",'wb')
        file2 = open("kor.p",'wb')
        pickle.dump(dic1,file1)
        pickle.dump(dic2,file2)
        for key in sorted(dic1.keys()):
            print(key,dic1[key])
        file1.close()
        file2.close()
