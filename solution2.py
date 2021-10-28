import sys  #for taking maximum integer value
A = []      
#function minSwap with integer retern swapp
def minSwaps(A,n):       
    swapp=sys.maxsize
    for i in range(0,n):
        B = A
        B = (B[-i:] + B[:-i]) #rotating the list by i
        count=0
        for i in range(1,len(B)): # implementation of insertition sort
            key=B[i]
            j=i
            while(j>0 and B[j-1]>key):
                B[j]=B[j-1]
                j=j-1
                count += 1 
                B[j]=key 
        if swapp > count: 
            swapp = count
    return(swapp)

#below is fuction calling
n = int(input("Enter number of elements : ")) #taking input elements in the list
 
for i in range(0, n):
    ele = int(input())
    A.append(ele)
print(minSwaps(A,n)) 
