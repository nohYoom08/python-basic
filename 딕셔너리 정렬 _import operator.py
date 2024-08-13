import operator


a={3:32,7:64,8:43}
print(a.values())
data1=sorted(a.items(),key=operator.itemgetter(1))
data2=sorted(a.items(),key=operator.itemgetter(0))

print(data1)
print(data2)
