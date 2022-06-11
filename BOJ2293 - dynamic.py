#https://www.acmicpc.net/problem/2293
#동전1
#dp테이블 활용한 다이나믹 프로그래밍

#dp테이블의 인덱스는 동전가치의 합을 의미, 인덱스에 저장된 숫자는 그 총가치를 만드는 경우의 수

#동전의 종류 n, 동전 가치의 합k
n, k = map(int, input().split())

#각동전의 가치
coinvalue = [int(input()) for _ in range(n)]
# print(coinvalue)

dp = [0 for _ in range(k+1)]
dp[0] = 1
# print(dp)

for i in coinvalue:
  for j in range(1, k+1):
    #· j값보다 동전의 가치가 크다면
    #     -  해당 동전 사용 못함
    #     - dp[j]=dp[j-1] 이므로 코드를 건드릴 필요 없음 
    #        ( 앞의 동전만 사용했을 때의 경우의 수와 동일하므로 숫자 변동 없음 )

    # · j값보다 동전의 가치가 작거나 같다면
    #    - 해당 동전 사용해야 함
    #       ( 그 동전의 값을 뺀 만큼을 만드는 경우의 수를 해당 경우의 수에 더해주어야 함)

    if j-i >= 0:
      dp[j] += dp[j-i]

print(dp[k]) 




