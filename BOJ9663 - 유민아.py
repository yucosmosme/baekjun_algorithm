#https://www.acmicpc.net/problem/9663
#N-Queen문제
#퀸은 상하좌우대각선 모두 이동 가능. 체스판안에서 칸수 제한 없음

#N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

#한번 쭉 들어갔다가 (방법1) 나와서 다시 또 쭉 들어갔다가(방법2) --> 이런 식으로 방법 몇개인지 찾는것 dfs

import math
from unittest import result


n = int(input())

# 아직 안놓임0, 퀸넣음 1, 퀸못놓음 -1
row = [0] * n

#방법의 수
result = 0

def isPositionOk(x):
  for i in range(x):
    # abs() 절대값 리턴
    print('row[x], row[i]', row[x], row[i])
    if row[x] == row[i] or abs(row[x] -  row[i]) == x - i:
      return False
  return True

def dfs(x):
  print('-------------------------',x,'행')
  global result
  
  # 가장 깊은 곳까지 들어갔음 -> 퀸을 모두 다 놓았음.
  if x == n:
    result += 1

  else:
    for i in range(n):
      print('---------',i,'열')
      row[x] = i
      # print('i:', i)
      # print('row[x]:',row[x])

      # 퀸 놓아도 되는거면 계속 깊게 탐색하고
      # 놓으면 안되는 자리면 다음 열로 넘어감(백트랙킹)
      if isPositionOk(x):
        dfs(x+1)

dfs(0)

print(result)