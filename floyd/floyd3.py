#플로이드 알고리즘 (파이썬)

# 입력부분
print('입력할 데이터의 크기는 :')
n = int(input())
print('입력할 데이터 작성 (무한대는 99로 입력)')
W = [[int(x) for x in input().split()] for y in range(n)]

D = [[99]*n for i in range(n)] # D 배열 생성 (W배열과 같은 크기로 만든다.)
P = [[99]*n for i in range(n)] # P 배열 생성 (W배열과 같은 크기로 만든다.)


#플로이드 알고리즘 함수
def floyd2(n, W, D, P):   
  for i in range(1,n+1):  
   for j in range(1,n+1):
     P[i-1][j-1]=0  #P배열 0으로 초기화
 
  D=W  # W배열을 D배열에 대입

  for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(D[i-  1][k-1] + D[k-1][j-1] < D[i-1][j-1]):
                P[i-1][j-1]=k
                D[i-1][j-1] = D[i-1][k-1] + D[k-1][j-1]

  return D


#플로이드 알고리즘을 통해 구해낸 P배열을 이용해 거치는 정점 구하는 함수
def path(q,r):
  if(P[q-1][r-1] != 0):
    path(q,P[q-1][r-1])
    print ("v:",P[q-1][r-1])
    path(P[q-1][r-1],r)

  
Dfloyd = floyd2(n,W,D,P)


# 출력 부분
print('-----------------------------------------')
print('D배열:')
for i in Dfloyd:   #최단 경로 길이가 포함된 D배열 출력
    for j in i:
        print(j,end="      ")
    print()

print('-----------------------------------------')
print('최단경로를 상에 놓여있는 정점 출력')
print('출발 VERTEX')
a = int(input())
print('도착 VERTEX')
b = int(input())
print('v:',a)
path(a,b)         #최단경로 상에 놓여있는 정점들 출력
print('v:',b)


