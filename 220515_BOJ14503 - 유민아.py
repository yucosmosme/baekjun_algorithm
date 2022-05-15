# https://www.acmicpc.net/problem/14503
# 로봇청소기

# 세로칸수, 가로칸수
n, m = map(int, input().split())

#로봇청소기 위치 (r,c), 바라보는 방향 d : 0 북쪽 1 동쪽 2 남쪽 3 서쪽
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
# print(graph)

# 바라보는 방향 d : 0 북쪽 1 동쪽 2 남쪽 3 서쪽에 맞게 인덱스 셋팅

# 틀린거!!! # 시계 반대방향으로 돌도록 순서 셋팅해야 함!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 방향이 다 막혀있으면 ??????????????

nx, ny = [-1,0,1,0], [0,1,0,-1]

count = 0

while True:

  global graph
  global count

  # 현재 로봇 위치 청소
  # 청소하면 2로 셋팅
  graph[x][y] = 2
  count += 1
  # 회전 횟수
  turnTime= 0

  # 지정한 방향 순서대로 돈다.
  for i in range(direction, direction+4):
    # 북쪽부터 돌면 0 1 2 3인데 다른 위치부터 돌면 2 3 4 5 이런식으로 nx,ny 인덱스를 초과하므로 초과되지 않게 맞춰준다.

    if turnTime == 3 :
      exit

    if i >=4 : 
      i %= 4

    dx, dy = nx[i]+x, ny[i]+y

    turnTime += 1

    # 위치 범위 내에 있고, 빈곳만 청소
    if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 0 :
      # 청소하면 2로 셋팅
      # graph[dx][dy] = 2
      # count += 1
      # dfs(dx,dy, i)
      break

dfs(r-1,c-1,d)

# print(graph)
print(count)

for i in graph:
  print(i)
# 1 1 1 1 1 1 1 1 1 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 1 1 1 1 0 1
# 1 0 0 1 1 0 0 0 0 1
# 1 0 1 1 0 0 0 0 0 1
# 1 2 2 2 0 0 0 0 0 1
# 1 0 0 2 0 0 0 1 0 1
# 1 0 0 0 0 0 1 1 0 1
# 1 0 0 0 0 0 1 1 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1