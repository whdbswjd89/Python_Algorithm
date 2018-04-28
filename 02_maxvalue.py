#문제 02: 최대값 찾기

#리스트 []
list_m = [1,10,20,30,66,99,100]
max_num = list_m[0]
n = len(list_m)
for i in range(1,n):
    if list_m[i] > max_num:
        max_num = list_m[i]

print(max_num)

#함수
def max_value(list_m):
    max_num = list_m[0]
    n = len(list_m)
    for i in range(1,n):
        if list_m[i] > max_num:  #최소값은 list_m[i] < min_num
            max_num = list_m[i]
    return max_num

list_m = [1,10,30,50,60,70,23,99,100]
print(max_value(list_m))

#최대값 위치 구하기
list_m = [1,10,20,30,66,99,100]
max_num_idx = 0
n = len(list_m)
for i in range(1,n):
    if list_m[i] > list_m[max_num_idx]:
        max_num_idx = i
print(max_num_idx)
