#11번
X=[]
Y=[]
for i in range(5):
    x=int(input())
    X.append(x)
    
    y=int(input())
    Y.append(y)

max_side=0
max_x1=max_x2=max_y1=max_y2=0

for i in range(4):
    for j in range(i+1,5):
        side_r=(X[i]-X[j])*(Y[i]-Y[j])
        if side_r<0:
            side_r=-side_r

        if max_side<side_r:
            max_side=side_r
            
            max_x1=X[i]
            max_y1=Y[i]

            max_x2=X[j]
            max_y2=Y[j]

            
            if(X[i]<X[j]):
                sml_x=X[i]
                big_x=X[j]
                
            else:
                sml_x=X[j]
                big_x=X[i]

            if(Y[i]<Y[j]):
                sml_y=Y[i]
                big_y=Y[j]

            else:
                sml_y=Y[j]
                big_y=Y[i]


cnt=0

for i in range(5):
    if (sml_x<X[i] and X[i]<big_x
    and sml_y<Y[i] and Y[i]<big_y):
        cnt+=1

print("Max area =",max_side)
print("Point1 X = %d, Y = %d"%(max_x1,max_y1))
print("Point2 X = %d, Y = %d"%(max_x2,max_y2))
print("Count =",cnt)




#19번
end_money=int(input())
total=int(input())
day=cnt=0


while True:
    day+=1
    for i in range(1,total+1):
        if total%i==0:
            cnt+=1
            
    if cnt>=50:
        total=3*total
    elif cnt>=30:
        total=2*total+10000
    else:
        total=2*total+100

    if total>=end_money:
        break

    cnt=0

print("Day =",day)
print("Money =",total)



#20번
n=int(input())
price=int(input())

total=0

for i in range(n):
    page=int(input())
    if page>=250:
        total+=250*price
    else:
        total+=page*price

print("Total =",total)




#22번
n=int(input())
P=[]
M=[]
for i in range(n):
    N=int(input())
    if N>0:
        P.append(N)
    else:
        M.append(N)

for i in range(len(P)):
    M.append(P[i])

print("Sort =",end=" ")

for i in range(len(M)):
    print(M[i],end="")



#29번
n=int(input())
cnt=sum1=sum2=0
while n>0:
    cnt+=1
    if cnt%2==0:
        sum2+=n%10
    else:
        sum1+=n%10
    n//=10

sum1**=3
sum2**=3

SUM1=SUM2=0

while sum1>0 or sum2>0:
    SUM1+=sum1%10
    SUM2+=sum2%10
    sum1//=10
    sum2//=10

print("sum1 =",SUM1)
print("sum2 =",SUM2)





#30번
N=int(input())
M=N
ten=1

while M>=ten:
    ten*=10


if N==(M**2)%ten:
    print("YES")
else:
    print("NO")


#31번
n=int(input())
m=n
summ=0
fac=1

while m>0:
    seat=m%10
    for i in range(1,seat+1):
        fac*=i
    summ+=fac
    fac=1
    m//=10

if n==summ:
    print("True")
else:
    print("False")
//초기화 종류 다른거 구분




#32번
n=int(input())
ELDER=NORMAL=0
for i in range(n):
    elder=0
    num=int(input())
    point=num*0.4
    for j in range(num):
        age=int(input())
        if age>=65:
            elder+=1
    if elder>=point:
        print("Elderly House")
        ELDER+=1
    else:
        print("Normal House")
        NORMAL+=1

print("Elderly House =",ELDER)
print("Normal House =",NORMAL)




#33번
S=[]

while True:
    N=input()
    if N=='end':
        n=int(input())
        break
    S.append(N)

print("Crypto = ",end="")

for i in range(len(S)):
    if ord(S[i])+n > ord('Z'):
        S[i]=chr(ord(S[i])+n-26)
        
    else:
        S[i]=chr(ord(S[i])+n)
        
    print(S[i],end="")


#파이썬의 변수는 적어도 "문자 or 정수 및 실수" 이렇게 나뉜다. 이 둘 중 하나를 확실히 해줘야함



#34번
L=[]

while True:
    n=int(input())
    if n==0:
        break
    
    L.append(n)

L.sort()

for i in range(len(L)):
    if L[i]%2==0:
        L[i]*=2
    else:
        L[i]**=2

print("List =",end="")
print(L)



#35번
M={}
for i in range(3):
    name=input()
    price=int(input())
    M[name]=price

num=int(input())
summ=0

for i in range(num):
    name=input()
    summ+=M[name]

print("Total =",summ)




#36번
strike=spare=total=0

for i in range(5):
    print("Set",i+1)
    score=0
    n1=int(input())
    if spare==1:
        spare=strike=0
        if n1<12:
            score+=2*n1
            total+=2*n1
            
            n2=int(input())

            score+=n2
            total+=n2
            
            if n1+n2==12:
                spare=1
        else:
            score+=2*n1
            total+=2*n1
            strike=1

    elif strike==1:
        spare=strike=0
        
        if n1<12:
            n2=int(input())
            score+=2*(n1+n2)
            total+=2*(n1+n2)
            
            if n1+n2==12:
                spare=1
                
        else:
            score+=2*n1
            total+=2*n1
            strike=1
    
    else:
        if n1<12:
            n2=int(input())

            score+=n1+n2
            total+=n1+n2
            
            if n1+n2==12:
                spare=1
        else:
            score+=n1
            total+=n1
            strike=1

    print("Set %d Score = %d"%(i+1,score))
print("Total Score =",total)
#n1 입력 받고 스패어 여부, 스트라이크 여부, none
#이후 n1이 12여부
#이후 n1+n2가 12여부


#36번 개선안
strike=spare=total=0

for i in range(5):
    print("Set",i+1)
    score=0
    n1=int(input())
    if spare==1:
        spare=strike=0
        if n1<12:
            score+=2*n1
            
            n2=int(input())

            score+=n2
            
            if n1+n2==12:
                spare=1
        else:
            score+=2*n1
            strike=1

    elif strike==1:
        spare=strike=0
        
        if n1<12:
            n2=int(input())
            score+=2*(n1+n2)
            
            if n1+n2==12:
                spare=1
                
        else:
            score+=2*n1
            strike=1
    
    else:
        if n1<12:
            n2=int(input())

            score+=n1+n2
            
            if n1+n2==12:
                spare=1
        else:
            score+=n1
            strike=1
            
    total+=score

    print("Set %d Score = %d"%(i+1,score))
print("Total Score =",total)
    


#37번
Menu=[]
CNT=[]
cnt=0
f=0

while True:
    num=int(input())
    
    if num==0:
        break

    if num==1:

        book=input()

        while True: //이차원에서는 in, not in 못하니까 얄짤없이 그냥 
            for i in range(len(Menu)):
                if book in Menu[i]:
                    f=1
                    break
            if f==1:
                print("Book name is duplicated")
                book=input()
                
            elif f==0:
                break

            f=0 #무한루프 과감하게 활용

        writer=input()
        Menu.append([book,writer])
        print("New book added")
        CNT.append(1) #하나씩 추가 될 때마다 관련 정보 리스트도 같이 추가

    elif num==2:
        for i in range(len(Menu)): #일단 중첩리스트의 길이는 1차원 기준으로 len 가능
            print("Book Id = %d. Name = %s. Author = %s. Rental = %d"
                  %(i+1,Menu[i][0],Menu[i][1],1-CNT[i])) //리스트의 의미를 다르게 해석해서 응용가능
            

    elif num==3:
        N=int(input())
        if 0<N and N<=len(Menu): #문제 속에 숨겨진 2중 조건문 파악
            if CNT[N-1]==1:
                CNT[N-1]=0
                print("Rental Success")
            else:
                print("Rental Fail")               
            
        else:
            print("Rental Fail")

    elif num==4:
        M=int(input())
        
        if 0<M and M<=len(Menu):
            if CNT[M-1]==0:
                CNT[M-1]=1
                print("Return Success")
            else:
                print("Return Fail")   
        
        else:
            print("Return Fail")
