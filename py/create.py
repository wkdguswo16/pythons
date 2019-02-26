import pickle
dic1={}
dic2={}
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
print(dic1)
file1.close()
file2.close()
