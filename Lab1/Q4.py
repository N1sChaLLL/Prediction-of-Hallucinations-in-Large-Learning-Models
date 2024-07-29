#Taking the input as string
A = str(input("Enter a string to get the occurences counted "))
def occur(A):
    count = 0
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if (A[i]==A[j]):
                count+=1

occur(A)
