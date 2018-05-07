# gcd = Greatest Common Divisor
# 두 수의 약수 중에서 공통된 것을 찾아 그 중 최대값
def gcd(num1,num2):
     i = 0
     result = []
     i = min(num1,num2) #두 수 중 최소값 구하는 것
     while( i > 0):
         if num1 % i == 0 and num2 % i ==0:
             result.append(i)
             return(result)
         else:
             i = i - 1
             continue


print(gcd(4,6))
print(gcd(5,10))

# 입력: 두수
# 출력: 두수의 최대 공약수

def gcd(n1,n2):
    i = min(n1,n2)
    while True:
        if n1 % i == 0 and n2 % i == 0:
            return i
        i = i - 1

print(gcd(4,6))
print(gcd(4,6))

#Euclid gcd
#gcd(n1,n2) = gcd(b,a % b )
