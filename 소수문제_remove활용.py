n = int(input())
l = list(range(2,n+1))
root = int(n**0.5)
for i in range(2,root+1):
           result =1
           count=1
           while result<n:
                      result = i*count
                      if count !=1 and result in l:
                                 l.remove(result)
                      count+=1
print(l)