import array as array
def hoare(arr,lo,hi):
    pi=arr[lo]
    i=lo+1
    j=hi
    while True:
        while arr[j]>=pi and i<=j:
            j-=1
        while i<=hi and i<=j and arr[i]<=pi:
            i+=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[lo],arr[j]=arr[j],arr[lo]
    return j

def lomuto(arr,lo,hi):
    pi=arr[hi]
    i=lo-1
    for j in range(lo,hi):
        if arr[j]<=pi:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[hi]=arr[hi],arr[i+1]
    return i+1


def quick_sort(arr,lo,hi):
    if lo<hi:
        pi=lomuto(arr,lo,hi)
        quick_sort(arr,lo,pi-1)
        quick_sort(arr,pi+1,hi) 

if __name__=="__main__":
    size=int(input("Enter size of array:"))
    arr=array.array('i',[int(x) for x in input("Enter numbers separated with comma: ").split(',')])
    quick_sort(arr,0,size-1)
    print("Sorted array: ",arr)
