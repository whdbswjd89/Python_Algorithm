# 문제03: factorial 구하는 문제

#factorial: n!
num  = int(input())
sum = 1
for i in range(1,num+1):
    sum  = sum * i

print(sum)

#재귀 호출: 어떤 함수 안에서 자기 자신을 부르는 것
#재귀 호출이 정상적으로 작동하려면 종료조건이 필요
#factorial을 구하고 다시 factorial구함: n! = n * (n-1)!

#연속한 숫자의 곱을 구하는 함수n = int(input())
def fact(num):
    sum = 1
    for i in range(1,num):
        sum = sum * i
    return sum * num

print(fact(5))

#factorial함수를 이용한 연속한 숫자의 곱을 구하는 함수
def factorial(n):
    if n <= 1: #종료조건
        return 1
    return n * factorial(n-1) #더 작은 값으로 자기 자신을 호출

print(factorial(5))

#1부터 n까지의 합 구하기를 재귀 호출로 만들기
#5까지 합
def sum_fac(n):
    if n == 0:  #종료조건 0이면
        return 0  #0값 return
    return n + sum_fac(n-1)#더 작은 값으로 자기 자신을 호출

print(sum_fac(5))

#숫자 n개 중에서 최대값 찾기 재귀호출로 만들기
def max_fac(l,n): #list = a, number= n
    if n == 1: #1개일때는
        return l[0] #그 한개가 최대값
    max_value = max_fac(l,n-1) #더 작은 값으로 자기자신을 호출 
    if max_value > l[n-1]:
        return max_value
    else:
        return l[n-1]
l = [11,6,57,88,33,90,35]
n = len(l)

print(max_fac(l,n))
