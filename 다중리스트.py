#1번
n=int(input())
ten=[]

for i in range(1,10):
    ten.append(n*i%10)
    
ten.sort()
ten=set(ten)
ten=list(ten)

print(ten)



#2번
people={}
n=int(input())
for i in range(n):
    name=input()
    height=int(input())
    weight=int(input())
    people[name]=[height,weight]

print(people)

for key in people.keys():
    bmi=people[key][1]/(people[key][0]/100)**2
    people[key]=bmi

people=list(people.items())

for i in range(n):
    people[i]=list(people[i])


for i in range(n):
    for j in range(i,n):
        if people[i][1]<people[j][1]:
            tmp=people[i][0]
            people[i][0]=people[j][0]
            people[j][0]=tmp
            
            tmp=people[i][1]
            people[i][1]=people[j][1]
            people[j][1]=tmp

for i in range(n):
    print(people[i][0])




