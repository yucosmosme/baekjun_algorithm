#https://www.acmicpc.net/problem/7576
#토마토

#깊이 우선 탐색의 개념
# 루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에
# 해당 분기를 완벽하게 탐색하는 방식을 말합니다.
# 예를 들어, 미로찾기를 할 때 최대한 한 방향으로 갈 수 있을 때까지 쭉 가다가
# 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서
# 그 갈림길부터 다시 다른 방향으로 탐색을 진행하는 것이 깊이 우선 탐색 방식이라고 할 수 있습니다.

# 너비 우선 탐색의 개념
# 루트 노드(혹은 다른 임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방법으로,
# 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법입니다.
# 주로 두 노드 사이의 최단 경로를 찾고 싶을 때 이 방법을 선택합니다.
# ex) 지구 상에 존재하는 모든 친구 관계를 그래프로 표현한 후 Sam과 Eddie사이에 존재하는 경로를 찾는 경우
# 문제에서 '최소일수', '주변의 토마토들을 익힘' 이라는 말을 봐서 bfs 문제임
# 익은 토마토만 큐에 넣음 -> 큐 하나씩 빼면서 주변에 토마토를 익힌다. 
# 이때 익혀지는 토마토는 큐 토마토의 값 +1을 계속 해줌으로써 소요 날짜를 계산한다.
# 큐가 빌때까지 반복. -> 날짜 print

#Bfs는 queue 사용
from collections import deque
import queue

#가로칸수m, 세로칸수n
m,n = map(int, input().split())

#토마토 상태 받아옴
table = [list(map(int, input().split())) for _ in range(n)]
# print('table',table)

queue = deque([])

#왼오아위
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#토마토가 익는데 걸리는 시간
countDay = 0

#큐에 익은 토마토 위치 추가
for i in range(n):
  for j in range(m):
    if table[i][j] == 1:
      queue.append([i, j])

#bfs함수. 한번 다 돌고 나온다. 재귀 안함. 
def bfs():
  while queue:
    #익은 토마토 좌표에서 꺼내고
    x, y =queue.popleft()
    #동서남북으로 익힐 토마토 있는지 찾음
    for i in range(4):
      #이동한 좌표
      nx, ny  = x + dx[i] , y + dy[i]
      #이동한 좌표가 범위 안에 있고, 안익은 토마토이면
      if 0 <= nx < n and 0 <= ny < m and table[nx][ny] == 0:
        #1씩 증가시켜서 나온 최대값이 걸리는 최소 시간 !!!!
        table[nx][ny] = table[x][y] + 1
        queue.append([nx, ny])

bfs()

for i in table:
  for j in i:
    if j == 0:
      #안익은 토마토가 있음
      print(-1)
      exit(0)
  countDay = max(countDay, max(i)) #2차원이므로 이중으로 확인

#1부터 시작했으니 1 빼줌
print(countDay -1)