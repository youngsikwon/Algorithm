# 문제 제목 : 크로거
# 문제 난이도 : 중(Medium)
# 문제 유형 : 스택, 구현,스터디
# 추천 풀이 시간 : 40분


test_case = int(input())

for _ in range(test_case):
    data = input()
    left_stack = []
    right_stack = []

    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)

    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))
