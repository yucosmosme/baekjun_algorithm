# https://www.acmicpc.net/problem/12865
# 분할가능한 배낭채우기문제 : 욕심쟁이
# 분할불가능한 배낭채우기 문제(0-1 배낭문제) : 동적프로그래밍
# 이거는 무게순으로 계속 for문을 돌면 매우 비효율적이므로
# 0부터 max 무게까지 모든 무게만큼의 DP테이블을 만들어서 계산한다. 

#물품의 수 N과 버틸 수 있는 무게 K
n, k = map(int, input().split())
# print(n, k)

#물건정보 담을 리스트
stuffList = []

#리스트에 튜플 형태로 추가
for _ in range(n):
  weight, value = map(int, input().split())
  stuffList.append((weight, value))
# print(stuffList)

#결과 저장할 dp테이블
d = [[0] * (k+1) for _ in range(n+1)]
# print(d)

for i in range(1, n+1):

  weight, value = stuffList[i-1]

  for j in range(1, k+1):
    # 무게 더 들어갈 수 있을때
    if weight <= j:
      # ((무게한도-넣으려는무게) 테이블에 저장된 거 + 새로운무게   VS   그 전꺼값) !!!!!!!!!!!!!!!!!!!!!
      d[i][j] = max(value + d[i-1][j-weight], d[i-1][j])

    #무게 더 들어갈 수 없을때는 그 전 value 그대로 
    else:
      d[i][j] = d[i-1][j]

print(d[n][k])