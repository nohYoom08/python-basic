N=int(input())
city={}
cnt = 0

while cnt<N:
    name=input()
    pop=int(input())
    side=int(input())
    city[name]=pop/side
    cnt+=1

for key,value in city.items():
    if value==max(city.values()):
        max_key=key

print("Highest Population Density = %s, %.2f"%(max_key,max(city.values())))




n=int(input())
s_s=[]
s_avg=[]
for i in range(n):
    for j in range(3):
        score=int(input())
        s_s.append(score)
    s_avg.append(sum(s_s)/3)
    print("Student%d point = %d"%(i+1,s_avg[i]))
    s_s=[0]*3
for i in range(n):
    if s_avg[i]==max(s_avg):
        highest_stu=i+1

print("Highest Score Student =",highest_stu)
        


N=input()
x=list(N)		#(ABC받고 A,B,C) +int형은 이터러블하지 못해서 리스트화 안댐

cntup=cntdw=0

for i in range(len(x)):
    if 'A'<=x[i] and x[i]<='Z':
        cntup+=1
    elif 'a'<=x[i] and x[i]<='z':
        cntdw+=1
print("UPPER :",cntup)
print("LOWER :",cntdw)
     
