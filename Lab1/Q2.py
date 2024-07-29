#Taking the array input
A = eval(input("Enter a list to get the range of"))
def find_ranga(A):
    min = A[0]
    max = A[0]
    count = 0
    for i in range(0,len(A)):
        if A[i]<min:
            min = A[i]
    for i in range(0,len(A)):
        if A[i]>max:
            max = A[i]
    for i in range(0,len(A)):
        count+=1
    if (count<=3):
        print("Less than 3 elements list not allowed ")
    range1 = max - min
    print("The range of the following list is :",range1)

find_ranga(A)
    
