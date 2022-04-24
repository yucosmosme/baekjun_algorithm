#https://www.acmicpc.net/problem/2580
#스도쿠
#DFS(깊이우선탐색) + 백트랙킹으로 해결

# ① 먼저 문제에서 빈 칸은 0으로 주어지기 때문에
# graph의 0인칸의 위치정보(x, y)를 blank 리스트에 넣어준다.

# ② 첫 번째 빈칸에 1~9까지의 수 중 넣을 수 있는 수를 넣는다.
# 넣을 수 있는 수는 빈칸의 행,열,3x3정사각형에 없는 수임을 확인하자.
# 확인이 되면 그 빈칸에는 그 수를 넣어준다.

# ③ 그 다음 빈칸에 대해서도 같은 방법을 수행한다.

# ④ 마지막 빈칸까지 채우면 스도쿠를 완성하므로 맵을 출력한다.

import sys
# input = sys.stdin.readline()

graph = []
blank = []

n = 9

for _ in range(n):
  graph.append(list(map(int, input().split())))

#빈칸인 좌표들 리스트에 튜플 형태로 추가
for i in range(n):
  for j in range(n):
    if graph[i][j] == 0:
      blank.append((i, j))
print('blank:',blank)
# blank: [(0, 0), (1, 4), (1, 7), (2, 0), (2, 2), (3, 3), (4, 1), (4, 7), (5, 5), (6, 6), (6, 8), (7, 1), (7, 4), (8, 8)]

#x행에 있는 애들 중 a값이 있으면 true
def isOverwrapInRow(x, a):
  for i in range(n):
    if a == graph[x][i]:
      return True
  return False

#y열에 있는 애들 중 a값이 있으면 true
def isOverwrapInCol(y, a):
  for i in range(n):
    if a == graph[i][y]:
      return True
  return False

def isOverwrapInBox(x, y, a):
  #// : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
  nx = x // 3 * 3
  ny = y // 3 * 3
  for i in range(3):
    for j in range(3):
      if a == graph[nx+i][ny+j]:
        return True
  return False


def dfs(idx):
  print('빈칸리스트에서 ', idx, '번째인 아이::')

  #빈칸을 모두 체크했을때 결과 출력하고 프로그램 종료
  if idx == len(blank):
    for i in range(n):
      print(*graph[i])
    #프로그램 종료
    exit(0)
  
  #빈칸인 좌표에 들어갈 수 있는 값 1~9 루프를 돌면서
  #해당열이나 행 또는 3*3에 1~9중 루프도는 값이 모두 없을 경우에는
  #빈칸인 좌표에 해당 값으로 셋팅
  #그리고 그 다음 빈칸좌표를 대상으로 같은 작업 반복(재귀함수 호출 - idx +1) ===>>> DFS 깊이 우선 탐색!!!
  for i in range(1, n+1):
    # blank: [(0, 0), (1, 4), (1, 7), (2, 0), (2, 2), (3, 3), (4, 1), (4, 7), (5, 5), (6, 6), (6, 8), (7, 1), (7, 4), (8, 8)]
    x = blank[idx][0] #x좌표
    y = blank[idx][1] #y좌표
    print('빈칸인 (',x, y,') 좌표에 대해 ', i,'가 적합한지 확인:')

    # else일 경우 빈칸인 애들 계속 for문을 돌면서
    if isOverwrapInRow(x, i)==False and isOverwrapInCol(y, i)==False and isOverwrapInBox(x, y, i)==False:
      #빈칸 값 셋팅
      print('(',x, y,') 좌표에 대해 ', i,'로 셋팅')

      graph[x][y] = i 
      #다음 빈칸 값으로 재귀 호출 -> 여기서 계속 깊이있게 들어가다가 빈칸을 모두 체크하게 되면 프로그램 종료
      dfs(idx + 1)
      #정답이 없을경우에 대비해 초기화 (정답 있으면 위에서 프로그램 exit()시키기때문에 여기까지 안온다.)
      graph[x][y] = 0

#blank 리스트의 개수만큼 계속 for문을 돈다. (빈칸이 사라질때까지)
dfs(0)