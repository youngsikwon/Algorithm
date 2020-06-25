# 문제 제목 : 수 찾기
# 문제 난이도 : 하
# 문제 유형 : 해시, 배열, 구현
# 추천 풀이 시간 20분
#
# # adia
#  - 1. 특정 정수의 등장 여부만을 간단히 체크하면 됩니다.
#  - 2. Python에서는 dictionary 자료형을 해시처럼 사용 할 수 있습니다.
#  - 3. 본 문제는 set 자료형을 이용해 더욱 간단히 풀 수 있습니다.

n = list(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))



for i in x:
    if i not in array:
        print('0')

    else:
        print('1')