#https://www.acmicpc.net/problem/2133
#타일채우기
#3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구하라.
#참고: https://suri78.tistory.com/103

n = int(input())

d = [0] * 31
d[2] = 3

#두개씩 이동. 홀수면 타일 못채움
for i in range(4, n+1, 2):
  d[i] =  2 + 3*d[i-2] + sum(d[:i-2])*2 

print(d[n])