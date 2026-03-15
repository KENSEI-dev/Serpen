"""
n=int(input("Enter a number: "))
a=2+(n-1)*10
print(a)
"""


"""
list=[]
for i in range(size):
    if arr[i]== target:
        list.append(i)
        break
for j in range(size-1,0,-1):
    if arr[j]==target:
        list.append(j)
        break
if not list:
    print("-1 -1")
else:
    print(*list)

def firs_occurence(arr,target):
    lo,hi=0, len(arr)-1
    result=-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]==target:
            result=mid
            hi=mid-1
        elif arr[mid]>target:
            hi=mid-1
        else:
            lo=mid+1
    return result
def last_occurance(arr,target):
    lo,hi=0,len(arr)-1
    result=-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]==target:
            result=mid
            lo=mid+1
        elif arr[mid]<target:
            lo=mid+1
        else:
            hi=mid-1
    return result 
size=int(input(""))
arr=[int(x) for x in input().split()]
target=int(input())
first=firs_occurence(arr, target)
last=last_occurance(arr,target)
if first==-1:
    print("-1 -1")
else:
    print(first,last)
"""


def read_grid(m,grid):
    for _ in range(m):
        row=input().split()
        grid.append(row)
def alter_grid(grid,m,n):
    for i in range(m):
        for j in range(n):
            ch = grid[i][j]
            if ch=='O':
                grid[i][j]='X'
def print_grid(grid,m):
    for i in range(m):
        print(' '.join(grid[i]))
def check_grid(grid):
    m=len(grid)
    n=len(grid[0])
    list=[]
    for i in range(m):
        for j in range(n):
            if i==0 or i==m-1 or j==0 or j==n-1:
                list.append(grid[i][j])
    return list
m,n=map(int,input().split())
grid=[]
read_grid(m,grid)
print()
boundary_chars = check_grid(grid)            

found_O_on_boundary = False
for ch in boundary_chars:                    
    if ch == 'O':
        found_O_on_boundary = True
        break

if found_O_on_boundary:
    print_grid(grid, m)                      
else:
    alter_grid(grid, m, n)                  
    print_grid(grid, m)     