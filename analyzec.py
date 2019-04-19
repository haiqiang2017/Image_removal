import os,sys
def make(names):
    s=range(names)
    return s

def find(x,s):
    if x!=s[x]:
        s[x]=find(s[x],s)
    return s[x]


def union(x,y,s):
    s[x]=find(x,s)
    s[y]=find(y,s)
    if s[x]==s[y]:
        return
    else:
        s[x]=s[y]

def hamming(h1, h2):
    h, d = 0, h1 ^ h2
#    print d
    while d:
#        print d,d-1,d&(d-1)
        h += 1
        d &= d - 1
    return h

data=[]
linesa=open("info2.txt").readlines()
for line in linesa:
    data.append(int(line.split(" ")[-1]))
length=len(linesa)
#$print data[:100]
lines=open("output_2")
s=make(length)
for line in lines:
    array=line.split(" ")
    union(int(array[0]),int(array[1]),s)
for i in range(length):
    find(i,s)
cnt=0
out=open("keep_2",'w')
for i in range(length):
    if s[i]==i:
        cnt+=1
        out.write(linesa[i])

print cnt
#    print hamming(data[int(array[0])],data[int(array[1])])


