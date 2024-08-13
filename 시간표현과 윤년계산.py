2번
h=int(input())
m=int(input())
sum=h*60+m
result=17*60+30-sum
print('%d hour %d minute'%(result//60,result%60))


year=int(input())
if year%4==0:
    if year%100==0:
        if year%400==0:
            print('True')
        else : print('False')
    else : print('True')
else : print('False')


def minmulti(a,b):
    c=1
    while c%a!=0 or c%b!=0:
        c+=1
    return c
n1=int(input())
n2=int(input())
print(minmulti(n1,n2))
    