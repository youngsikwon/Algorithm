def solution(board, moves):
    moved = []
    count = 0
    for x in moves:
        for i in range(len(board)): #board's row
            c = x-1    #choosed cul
            if board[i][c] != 0:
                got = board[i][c]
                board[i][c] = 0
                if len(moved) == 0:
                    moved.append(got)
                elif len(moved) > 0 and got != moved[-1]:
                    moved.append(got)
                else:
                    count += 1
                    del moved[-1]
                break
    return count*2






## 1. 뽑기가 뽑아서 옮기는 리스트를 moved라고 하고 빈 리스트로 지정
## 2. moves 요소 x 대해 board의 i, x-1 (x는 행 번호니까 인덱스로 하라면 -1) (x-1 에 대해 i 가 쭉 반복)에 인형이 있따면
   ## 요소가 0이 아니라면) 그 인형(값을 got에 저장)을 board에서 없애고(0으로 바꿔줌

## 3. 잡은 got을 빈 리스트 moved에 옮겨줌. 이 때 두 번째 got이상 부터 만약 moved에 있는 값과 got이 같다면 같은 모양 인형이 두개 쌓인 거니까
 ## board에서 그 인형값은 없애주고 count + 1 함. 만약 같은 값이 아니라면 got을 moved에 append 해줌

## 4. break를 걸어서 만약에 i열에서 찾으면 그 다음을 찾지 않게 해줌 (가장 위에 것만 뽑아가니까)

## 5. count의 2배 리턴 (count는 인형쌍이 한번 사라질 때마다 하나씩 올라감으로)

##---------------------------------------------------------------------------------------------------------
def solution2(board, moves):
    stacklist = []
    answer = 0



    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0




                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break


    return answer