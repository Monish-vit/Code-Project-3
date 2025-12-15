def bubblesort(a,n):
    for j in range(0,n-1):
        for i in range(0,n-1):
            if(a[i] > a[i+1]):
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
    return(a)

arr = []
n = int(input("Enter n: "))
for i in range(0,n):
    arr.append(int(input()))
print(bubblesort(arr,n))