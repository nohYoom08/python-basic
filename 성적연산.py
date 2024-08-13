Num_Student=4
Num_Subject=5

Identity=['Trump','Putin','Obama','Xijinping']
Grade=[['C','B','A','C','D'],
       ['F','D','C','D','B'],
       ['A','B','A','B','A'],
       ['A','A','B','C','D']]

Rank=[1,2,3,4]
Credit=[3,3,3,2,1]
Grade_Avg=[0.00]*Num_Student

for i in range(Num_Student):
    total_grade=0
    total_Credit=0
    for j in range(Num_Subject):
        if Grade[i][j]=='A' : total_grade += 4.0*Credit[j]
        elif Grade[i][j]=='B' : total_grade += 3.0*Credit[j]
        elif Grade[i][j]=='C' : total_grade += 2.0*Credit[j]
        elif Grade[i][j]=='D' : total_grade += 1.0*Credit[j]
        total_Credit+=Credit[j]
        
    Grade_Avg[i]=total_grade/total_Credit

for i in range(Num_Student):
    for j in range(i,Num_Student):
        if Grade_Avg[i]<Grade_Avg[j]:
            tmp=Grade_Avg[i]
            Grade_Avg[i]=Grade_Avg[j]
            Grade_Avg[j]=tmp
            tmp=Identity[i]
            Identity[i]=Identity[j]
            Identity[j]=tmp
            
for i in range(Num_Student):
    print("%d %s %.2f"%(Rank[i],Identity[i],Grade_Avg[i]))
