# 입력: list , index
# 출력: 특정한 값의 위치를 돌려주는 알고리즘
#       리스트에 찾는 값이 없다면 -1
def search(list_s,search_n): # list , number
    for i in range(0,len(list_s)):
        if search_n == list_s[i]:
            return i

    return -1

v =[10, 15, 22, 30, 18, 22,50]
print(search(v,18))

# 찾는 값이 나오는 모든 위치를 리스트로 돌려주는 알고리즘
def searchs(list_s,search_list):
    for i in range(0,len(search_list)):
        if search_list == list_s[i]:
            search_list.append(list_s[i])
        return search_list

    return []

v =[10, 15, 22, 30, 18, 22,50]
s =[10, 22, 50]
print(searchs(v,s))

# O(n)

# 학생번호를 입력하면 학생 번호에 해당하는 이름을 순차 탐색으로 찾아 돌려주는 함수
# 해당하는 학생 번호 없으면 ? 반환
stu_no = [1,2,3,4,5]
stu_name=['muzi','con','neo','frodo','apeach']

def search_stu(stu_no):
    for i in range(1,(len(stu_name)+1)):
        if stu_no == i:
            return stu_name[i-1]

    return '?'

print(search_stu(2))
print(search_stu(100))
