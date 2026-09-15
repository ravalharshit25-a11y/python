def binarySearch(a,target_value):
    low=0
    high=len(a)-1

    while low<=high:
        mid=(low+high)//2

        if a[mid]== target_value:
            return mid

        elif a[mid] > target_value :
                high=mid-1
                
        else :
            low=mid+1

    return "value not available"                

a=[1,20,33,34,43,44,53,56,63,68,74,83,87]
target_value=int(input("enter your value"))
result=binarySearch(a,target_value)
print(result)