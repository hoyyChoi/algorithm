# optimal binary search trees 알고리즘(파이썬)
print('검색할 데이터의 갯수는:')
n = int(input())
print('검색어 도출 확률들은(차례대로)?')
p = [0]
pp=([float(x) for x in input().split()])
p=p+pp
R = [[0]*(n+1) for i in range(n+2)]
minavg = 0

def optsearchtree(n,p,minavg,R):
    global A 
    A = [[0]*(n+1) for i in range(n+2)]

    for i in range(1,n+1):
        A[i][i-1]=0
        A[i][i]=p[i]
        R[i][i]=i
        R[i][i-1]=0

    A[n+1][n]=0
    R[n+1][n]=0

    for diagonal in range(1,n):
        for i in range(1,n-diagonal+1):
            j = i + diagonal
            A[i][j]= A[i][i-1] + A[i+1][j]
            R[i][j]=i
            sumP = 0
            for k in range(i,j+1):
                if(A[i][j]>A[i][k-1] + A[k+1][j]):
                    A[i][j] = A[i][k-1] + A[k+1][j]
                    R[i][j] =  k
                sumP = sumP + p[k]
            A[i][j] = A[i][j] + sumP
    
    minavg = A[1][n]
    return minavg     

searchtree = optsearchtree(n,p,minavg,R)


# 출력 부분
print('-----------------------------------------')
print("최적의 search time",searchtree)
print('-----------------------------------------')
print('A배열:')
for i in range(1,n+2):   
    for j in A[i]:
        print(j,end="      ")
    print()
print('-----------------------------------------')
print('R배열:')
for i in range(1,n+2):  
    for j in R[i]:
        print(j,end="      ")
    print()



