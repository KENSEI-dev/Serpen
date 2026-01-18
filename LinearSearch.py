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
def quick_sort(a,low,high):
    if low<high:
        pivot_idx=partition(a,low,high)
    quick_sort(a,low,pivot_idx-1)
    quick_sort(a,pivot_idx+1,high)
def partition(a,low,high):
    pivot=a[high]
    i=low-1
    for j in range(low,high-1):
        if a[j]>pivot:
            i+=1
        else:
            if a[i]>a[j]:
                temp=a[j]
                a[j]=a[i]
                a[i]=temp
    temp=a[i+1]
    a[i+1]=a[high]
    a[high]=temp
    return i+1

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