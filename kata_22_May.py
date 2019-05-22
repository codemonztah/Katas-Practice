
k =int(input("Num"))
arr=[1,2,3,4,5]



# Complete the findNumber function below.
def findNumber(arr, k):
    status=False
    for i in arr:
        if int(i) == k:
            status =True
            print("YES")
            
    if status ==False:
        print("NO")   

findNumber(arr,k)