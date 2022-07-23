n=int(input())
arr=[int(i) for i in input().split()]
x=int(input())
counter=0

for i in range(n-2):
    j=i+1
    k=n-1
    while(j<k):
        if arr[i]+arr[j]+arr[k]==x:
            counter=counter+1
            j=j+1
            k=k-1
        elif arr[i]+arr[j]+arr[k]<x:
            j=j+1
        elif arr[i]+arr[j]+arr[k]>x: 
            k=k-1   
print(counter)            
