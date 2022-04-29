#https://www.acmicpc.net/problem/2023

import sys
import math

N = int(sys.stdin.readline())

#문제에서 조건이 1부터 8자리까지니까
list = [[2,3,5,7],[],[],[],[],[],[],[],]
#한자리수일때 초기값(소수들) 세팅
start_prime = [1, 3, 7, 9]

#자릿수 0부터 3까지 포문돈다.
for n in range(N-1): 
  #해당 자릿수에 해당하는 소수의 개수만큼 포문 : 1자리수에는 4개 들어있음 -> 0 1 2 3 포문돈다.
  for i in range(len(list[n])):
    #해당 소수들 1,3,7,9 포문돈다.
    for j in start_prime:
      #list[0][0]== 2 -> 22 23 25 27
      x = list[n][i]*10 + j
      #소수 판별: 제곱근으로 판별
      #해당 숫자의 제곱근을 기준으로 약수들의 곱셈이 대칭적으로 이뤄짐 --> 약수가 있는지 검사 범위를 반쪽만 하면 검사 시간 줄일 수 있다.
      for d in range(2, int(x**0.5)+1):
        if x % d == 0:
          x = 0
          break
      if x != 0:
        list[n+1].append(x)

for i in list[N-1]:
  print(i)