#Backtracking knapsack 알고리즘(파이썬)

print('아이템의 개수는:')
n = int(input())
print('가방의 용량은:')
W = int(input())
print('아이템의 값어치를 차례대로 작성:')
p=([int(x) for x in input().split()])
print('아이템의 무게를 차례대로 작성:')
w=([int(x) for x in input().split()])

bestset = [0]*(n+1)
include = [0]*(n+1)
maxprofit = 0


def pwsort(p,w):   # p배열과 w배열 정렬하는 함수
    div = []
    all = []
    for i in range(n):
        divitem= p[i]/w[i]
        div.append(divitem)
    
    for k in range(n):
        element = []
        element.append(p[k])
        element.append(w[k])
        element.append(div[k])
        all.append(element)

    for i in range(n-1):
        for j in range(i+1,n):
            if(all[i][2]<all[j][2]):
                temp = all[i]
                all[i]=all[j]
                all[j]=temp
    a=0
    for arr in all:
        while(a<n):
            p[a] = arr[0]
            w[a] = arr[1]
            a+=1
            break

pwsort(p,w)
p.insert(0,0)
w.insert(0,0)


def knapsack(i, profit, weight):
    global maxprofit

    if(weight <= W and profit > maxprofit):
        global numbest
        maxzprofit = profit
        numbest = i
        for a in range(numbest+1):
            bestset[a] = include[a]


    if(promising(i, profit, weight)):
        print(maxprofit)
        include[i+1] = "yes"
        knapsack(i+1, profit+p[i+1],weight+w[i+1])
        include[i+1]="no"
        knapsack(i+1,profit,weight) #그 부분해당 노드를 포함 안하니까 더하기가 없다.


def promising(i, profit, weight):
        if(weight>=W):
            return False
        else:
            j = i+1
            bound = profit
            totweight = weight
            while(j<= n and totweight+w[j] <= W):
                totweight = totweight +w[j]
                bound = bound + p[j]
                j+=1
        k=j

        if(k<=n):
            bound = bound +(W-totweight) * p[k]/w[k]
    
        return bound >maxprofit 
    
knapsack(0, 0, 0)

print("---------------")
print("< bestset 출력 >")
for i in range(1,numbest+1):
    print(i,":",bestset[i])
    print()