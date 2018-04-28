#문제 03 : 동명이인 찾기

#s = set()
#s.add(),discard()

list_p = ["Cindy","Kate","Leo","Cindy"]
find_same = set()
n = len(list_p)
for i in range(0,n-1): #i = 0,1,2,3
    #리스트의 마지막은 이미 다른 값과 다 비교했으므로 제외
    for j in range(i+1,n): #i= 2,3
        if list_p[i] == list_p[j]:
            find_same.add(list_p[i])

print(find_same)

#동명이인의 위치를 출력

list_p = ["Cindy","Kate","Leo","Cindy"]
find_same = set()
n = len(list_p)
for i in range(0,n-1): #i = 0,1,2,3
    #리스트의 마지막은 이미 다른 값과 다 비교했으므로 제외
    for j in range(i+1,n): #i= 2,3
        if list_p[i] == list_p[j]:
            find_same.add(i)
            find_same.add(j)

print(find_same)

#두명씩 짝을 짓기
list_p = ['coffee','cake','cookies','milk']
def pair(list_p):
    n = len(list_p)
    for i in range(0,n-1):
        for j in range(i+1,n):
            print(list_p[i]+'-'+list_p[j])
    
print(pair(list_p))
