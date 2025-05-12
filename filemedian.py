f=open("fileprograms/input2.txt",'r')
a=[]
for i in f:
    w=i.split()
    for t in w:
        n=int(t)
        a.append(n)
print(a)
a.sort()
m=len(a)//2
if(len(a)%2==0):
    median=(a[m]+a[m-1])/2
else:
    median=a[m]
print("Median is:",median)
