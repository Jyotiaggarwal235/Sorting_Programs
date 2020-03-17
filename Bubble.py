def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
arr = []
n=int(input("Enter size of array="))
print("Enter elements=")
for i in range(0,n):
    m=int(input())
    arr.append(m)
print(arr)    
 
bubbleSort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print(arr[i])