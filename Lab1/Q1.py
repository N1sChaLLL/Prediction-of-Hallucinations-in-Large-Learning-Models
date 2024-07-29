#The input list 
A = [2,7,4,1,3,6,9]
def find_pairs(A):
    count = 0
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if (A[i]+A[j]==10):
                print(A[i],A[j])
                count+=1
    print("The number of pairs are",count)
find_pairs(A)
