n=int(input())
k=int(input())
sum=0
arr=[]
for i in range(1,n+1):
    arr.append(i)
print(arr)
for j in range(k):
    sum+=arr[j]
print(sum)
    
