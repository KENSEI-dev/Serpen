import array as arr
def bubble_sort(a,size):
    for i in range(size-1):
        for j in range(size-i-1):
            if a[j]>a[j+1]:#big to small (descending order logic)
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a
def selection_sort(a,size):
    for i in range(size-1):
        max_idx=i
        for j in range(i+1,size):
            if a[max_idx]<a[j]:
                max_idx=j
        if max_idx!=i:
            temp=a[max_idx]
            a[max_idx]=a[i]
            a[i]=temp
    return a
def lamuto (arr, low, high):

    if low>=high:
        return
    pivot=arr[high]
    j=low

    for i in range(low,high):
         if (arr[i]<=pivot):
             arr[i],arr[j]=arr[j],arr[i]
             j+=1

    arr[high], arr[j]=arr[j],arr[high]
    lamuto (arr, low,j-1)
    lamuto (arr,j+1,high)

    return arr

def linearSearch(a,size,s):
    for i in range(size):
        if s==a[i]:
            print("Element found!")
            return i
    print("Element not found")
    return -1
def binary_search(a,low,high,target):
    if low>high:
        return -1
    mid=low+(high-low)//2
    if a[mid]==target:
        return mid
    elif a[mid]<target:
        return binary_search(a,mid+1,high,target)
    else:
        return binary_search(a,low,mid-1,target)
size=int(input("Enter size: "))
raw_input = input("Enter the elements with spaces: ").split()
a = arr.array('i', [int(x) for x in raw_input[:size]])
print("Original array: ",a)
print("Sorted array: ",quick_sort(a,0,size))
'''bubble_sort(a,size)
print("Sorted Array:",bubble_sort(a,size))
print("Sorted array: ",selection_sort(a,size))
search_ele=int(input("ENter element to be searched: "))
print(f"Element found at {binary_search(a,0,size-1,search_ele)+1} position" if binary_search(a,0,size-1,search_ele) !=-1 else "Element Not Found")
pos = binary_search(a, 0, size-1, search_ele)
print(f"Element found at {pos+1} position" if pos != -1 else "Element Not Found")

#print(f"Element found at {linearSearch(a,size,search_ele)+1} position" if linearSearch(a,size,search_ele) !=-1 else "Element Not Found")

pos=linearSearch(a,size,search_ele)
if pos!=-1:
    print(f"Element found at {pos+1} position")
'''
test=[5,3,6,4,7,3,2,1,8]
print(lamuto(test, 0,len(test)-1))
