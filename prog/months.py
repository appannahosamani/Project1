q=[]
months=['jan','feb','mar','apr','may','june','july','aug','sep','acto','nov','dec']
days=[31,28,31,30,31,30,31,31,30,31,30,31]

def addind_data(last_data):
    a=[]
    for i in range(1,last_data+1):
        a.append(i)
    return a

for i in range(0,len(months)):
    a={}
    a['months']=months[i]
    a['days']=addind_data(days[i])
    q.append(a)
 
print("Year cal=",q)

# a=[{'month':months[i], 'days':[j for j in range(days[i]+1)]} for i in range(len(months))]
# print("year cal:",a)