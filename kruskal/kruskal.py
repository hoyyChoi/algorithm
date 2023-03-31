#kruskal 알고리즘(파이썬)

print('vertex의 개수는:')
n = int(input())
print('edge의 개수는:')
m = int(input())
U = [[0]*2 for i in range(n+1)]
F=[]
E = []
print('edge 시작, 종점, 가중치(차례대로):')
for i in range(1,m+1):
    p=([int(x) for x in input().split()])
    E.append(p)


def kruskal(n,m,E,F):
    indexE = 1
    indexF = 1

    for i in range(m-1):
        for j in range(i+1,m):
            if(E[i][2]>E[j][2]):
                temp = E[i]
                E[i]=E[j]
                E[j]=temp
    E.insert(0,[0,0,0])
  
    for i in range(1,n+1):
        zero = [0,0,0]
        F.append(zero)
    
    initial(n)

    while(indexE<len(E) and indexF<=n-1):
        i = E[indexE][0]
        j = E[indexE][1]
        p = find(i)
        q = find(j)
        if(not equal(p,q)):
            merge(p,q)
            F[indexF] = E[indexE]
            indexF+=1
       
        indexE+=1
    
    return F



def initial(n):
    for i in range(1,n+1):
        makeset(i)

def makeset(i):
    U[i][0] = i
    U[i][1]=0

def find(i):
    j=i
    while(U[j][0] != j):
        j = U[j][0]
    return j

def merge(p,q):
    if(U[p][1] == U[q][1]):
        U[p][1]+=1
        U[q][0] = p
    elif(U[p][1]<U[q][1]):
        U[p][0]=q
    else:
        U[q][0]=p

def equal(p,q):
    if(p==q):
        return True
    else:
        return False


kruskalF = kruskal(n,m,E,F)


# 출력 부분
print('----------------')
print('MST:')
for i in range(1,n):   
    print("[",kruskalF[i][0],",",kruskalF[i][1],"]",",",kruskalF[i][2])
    print()