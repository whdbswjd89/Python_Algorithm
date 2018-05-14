# Tower of Hanoi
# 입력: n
# 기둥: 3
# 출력: 총 옮기는 순서
# 출발 , 도착 , 중간지점
def hanoi(n,start_pos,finish_pos,stopby_pos):
    if n == 1:
        print(start_pos,'->',finish_pos)
        return
    # start -> stopby
    hanoi(n-1,start_pos,stopby_pos,finish_pos)
    print(start_pos,'->',finish_pos)
    # stopby -> finish
    hanoi(n-1,stopby_pos,finish_pos,start_pos)

# 원반 갯수, 1번 -> 3번 -> 5번
def hanoi_count(n):
    return 2 ** n - 1

print('---n=1---')
hanoi(1,1,3,2)
print('count',hanoi_count(1))
print('---n=2---')
hanoi(2,1,3,2)
print('count',hanoi_count(2))
print('---n=3---')
hanoi(3,1,3,2)
print('count',hanoi_count(3))
