def linearSearch(a,target_value):
    n=0
    b=len(a)-1

    while n<=b:

        if target_value == a[n]:
            return n

        else :
            n=n+1

    return "value not found"            

a=[1,2,3,76,4,55,6,543,65,2,8,44,5]
target_value=int(input("enter value : "))
result=linearSearch(a,target_value)
print(result)