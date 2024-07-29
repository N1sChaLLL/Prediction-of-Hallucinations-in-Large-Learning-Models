#Accepting a 2D array
N = int(input("Enter the numbers of Rows and Columns (Square Matrix)"))
Matrix = []
def input1(Matrix):
    for i in range(N):
        a = []
        for j in range(N):
            a.append(int(input("Enter the element")))
        Matrix.append(a)

def print1(m):
    for i in range(N):
        for j in range(N):
            print((Matrix[i][j])**m,end=" ")
        print()
input1(Matrix)
m = int(input("Enter the power u want to apply for the matrix "))
print1(m)