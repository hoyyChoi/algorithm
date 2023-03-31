
# [5,2,3,4,6,7,8]
print('입력할 행렬의 개수 :')
n = int(input())
print('행렬 크기 작성')
d = [int(x) for x in input().split()]
P = [[0]*n for i in range(n)];

def minmult(n, d, P):
    M = [[0]*n for i in range(n)];
    
    for diagonal in range(1,n):
        for i in range(1,n-diagonal+1):
            j = i + diagonal;
            M[i-1][j-1] = 999999;
            for k in range(i,j):
                if(M[i-1][k-1]+M[k][j-1]+(d[i-1]*d[k]*d[j])<M[i-1][j-1]):
                    M[i-1][j-1] = M[i-1][k-1]+M[k][j-1]+(d[i-1]*d[k]*d[j]);
                    P[i-1][j-1] = k;

    return M

def order(i,j):
    if(i==j):
        print("A%d" %i,end='')
    else:
        k=P[i-1][j-1]
        print('(',end='')
        order(i,k)
        order(k+1,j)
        print(')',end='')




a = minmult(n,d,P)
for i in a:  
    for j in i:
        print(j,end="      ")
    print()
print("최적의 곱셈 횟수 :",a[0][n-1])

print("------------------------")
print('최적의 곱셈 순서 방법')
print('첫 행렬 :')
a = int(input())
print('끝 행렬 :')
b = int(input())
order(a,b)