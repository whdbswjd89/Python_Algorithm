#문제 01 : 1부터 n까지의 합
n = int(input())
sum = 0
for i in range(1,n+1):
     sum = sum + i  #case1
     #sum = (n*(n + 1)) // 2  #case2
print(sum)

#함수
def total_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

n = int(input())
print(total_sum(n))

#제곱합 구하는 함수
def double_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**2
    return sum

print(double_sum(n))
