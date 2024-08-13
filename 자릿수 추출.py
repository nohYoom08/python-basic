n=int(input())
result=0
while n>0:
    result*=10
    result +=n%10
    n=n//10
print('Result = ',result)