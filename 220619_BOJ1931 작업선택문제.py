# https://www.acmicpc.net/problem/1931
# 회의실 배정

n = int(input())
schedule = []

for _ in range(n):
	s, e = map(int, input().split())
	schedule.append([s, e])

# print(schedule)
# 시작 시간을 기준으로 오름차순
schedule.sort(key = lambda x: x[0])
# print(schedule)
# 끝나는 시간을 기준으로 다시 오름차순
schedule.sort(key = lambda x: x[1])
# print(schedule)

maxUser = 1 #최대 회의 개수
lastTime = schedule[0][1]

for i in range(1, n):
	#print(schedule[i])
	if schedule[i][0] >= lastTime:
		maxUser += 1
		lastTime = schedule[i][1]	
print(maxUser)