n=int(input())
grade={}
cnt=0
while cnt<n:
    name=input()
    score=int(input())
    grade[name] = score
    cnt+=1
final_name=input()
print('%s\'s score = %d'%(final_name,grade[final_name]))



n=int(input())
student={}
while n!=0:
    if n==1:
        name=input()
        score=int(input())
        student[name]=score

    elif n==2:
        name=input()
        if (name not in student)==True:
            print('No student')
        else:
            print('Name = %s, Score = %d'%(name,student[name]))
    n=int(input())



3번 my답
n=int(input())
density={}
cnt=0
while cnt<n:
    city=input()
    surf=int(input())
    pop=int(input())
    density[city]=surf/pop
    cnt+=1
HD=max(density)
print('Highest Population Density = %s, %.2f'%(HD,density[HD]))





#3번 답
n=int(input())
density={}
cnt=0
while cnt<n:
    city=input()
    surf=int(input())
    pop=int(input())
    density[city]=surf/pop
    cnt+=1

max = 0

for key,value in city.items():
    if max < value:
        max=value
        max_key=key

print('Highest Population Density = %s, %.2f'%(max_key,max))




n=int(input())
tel={}
while True:
    if n==1:
        name = input()
        num = input()
        tel[name]=num

    elif n==2:
        name=input()
        if (name not in tel)==True:
            print('Do not find!')
        else:
            num=input()
            tel[name]=num
    
    elif n==0:
        name=input()
        if (name not in tel)==True:
            print('System error!')
        else :
            print(tel[name])
        break
    n=int(input())