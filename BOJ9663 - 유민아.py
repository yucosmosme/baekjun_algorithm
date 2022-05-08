#https://www.acmicpc.net/problem/9663
#N-Queen문제
#퀸은 상하좌우대각선 모두 이동 가능. 체스판안에서 칸수 제한 없음

#N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

#한번 쭉 들어갔다가 (방법1) 나와서 다시 또 쭉 들어갔다가(방법2) --> 이런 식으로 방법 몇개인지 찾는것 dfs

import math

n = int(input())

# 퀸은 한 행에 최대 한 개만 놓을 수 있으므로
# 퀸이 놓인 위치를 보는 (2차원 배열)을 쓸 필요 없이 
# 퀸이 놓인 위치를 행인덱스에 들어간 열값으로 셋팅 (1차원 배열)
# row[i] = j 이면 퀸은 (i, j) 위치에 들어감
row = [0] * n

# 퀸을 놓는 방법의 수
result = 0

# 퀸을 놓아도 되는지 판별
def isPositionOk(x):
  # 0행부터 차례로 퀸을 채우고 있으므로 판별하려는 행 x 보다 큰 값은 볼 필요가 없음.
  # isPositionOk(0)은 for문을 안돌음. -> 바로 return true 해서 1번행으로 넘어가게 된다.
  for i in range(x):
    # 1. 같은 열에 이미 퀸이 있는지 확인 (row[x]는 x행에 퀸이 놓인 y열을 표기. 만약 다른 행에 같은 열값이 들어있다면 퀸이 한 열에 중복되는 것이므로 퀸을 놓을 수 없다.)
    # 2. 대각선 왼쪽 위, 오른쪽 위에 이미 퀸이 있는지 확인.
    # 만일 판별하려는 위치가 (4,3)이면 대각선 왼쪽 위의 값은 (3,2)(2,1)(1,0) 이렇게 되고, 오른쪽 위의 값은 (5,2)(6,1)(7,0) 이런 식으로 된다
    # 모두 (4,3)에서 값을 빼면 (1,1) (2,2) (3,3),,,, (-1,1)(-2,2)(-3,3) 이런 식으로 절대값을 붙이면 행값과 열값이 같은 값이 나온다. 
    # 이 조건을 만족한다면
    print('x: ', x, 'i: ', i) 
    if row[x] == row[i] or abs(row[x] -  row[i]) == abs(x - i):
      return False
  return True

# 0행부터 행 기준으로 판별 시작
def dfs(x):
  print('-------------------------',x,'행')
  print('row::', row)
  global result
  print('result: ', result)
  
  # 행을 모두 다 돌았으면 종료 (가장 깊은 곳까지 들어갔음 -> 퀸을 모두 다 놓았음.)
  if x == n:
    result += 1
    return

  else:
    # 열을 기준으로 루프 돈다.
    for i in range(n):
      print('---------',i,'열')

      # 먼저 퀸을 (x,i)위치에 놓는다.
      row[x] = i
      # print('i:', i)
      # print('row[x]:',row[x])

      # 퀸 놓아도 되는 자리인지 판별
      # 놓아도 되는 자리이면 다음 행으로 넘어가고 (계속 깊게 탐색) 안되는 자리면 다음 열로 넘어감(백트랙킹)
      if isPositionOk(x):
        dfs(x+1)

dfs(0)
print(result)