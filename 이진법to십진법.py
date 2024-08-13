n=int(input())
two=1
sum=0
while n>0:
    seat = n%10
    if (seat == 1):
        sum+=two
    n//=10
    two*=2
print(int(sum))
