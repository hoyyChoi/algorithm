# Dijkstra 알고리즘(파이썬)
print('vertex의 개수는:')
n = int(input())
print('edge의 개수는:')
m = int(input())
F=[]
W = [[0]*(n+1) for i in range(n+1)]

for i in range(n+1):
    for j in range (n+1):
        W[i][j] = 9999
        if(i==j):
            W[i][j]=0

print('edge 시작, 종점, 가중치(차례대로):')
for i in range(1,m+1):
    start = 0
    end = 0
    weight = 0
    pp = [start,end,weight]
    p=([int(x) for x in input().split()])
    pp = p
    W[pp[0]][pp[1]] = pp[2]


def dijkstra(n, W, F):
    touch = [0]*(n+1)
    length = [0]*(n+1)
    k=1
    vnear = 0
    global Fweight
    Fweight=[]

    for i in range (2,n+1):
        touch[i] = 1
        length[i] = W[1][i]

    while(k<n):
        min = 9999;
        for i in range(2,n+1):
            if(0<= length[i] <=min):
                min = length[i]
                vnear = i
        
        edge1 = touch[vnear]
        edge2 = vnear
        edgeF = [edge1,edge2]
        edgeW = W[edge1][edge2]
        F.append(edgeF)
        Fweight.append(edgeW)

        for i in range(2,n+1):
            if(length[vnear]+W[vnear][i] < length[i]):
                length[i] = length[vnear] + W[vnear][i]
                touch[i]=vnear
        length[vnear] = -1
        k=k+1

    return F

Farray = dijkstra(n,W,F)

# 출력 부분
print('----------------')
print('F배열(가중치):')
for i in range(n-1):   
    print(F[i],end=" ")
    print(Fweight[i])
    print()