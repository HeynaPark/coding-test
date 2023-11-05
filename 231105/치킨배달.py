import sys

input = sys.stdin.readline

n,m  = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))


print(city)
#m개를 선택해서 치킨거리가 최소값이 나왔을때 그 최소값을 출력한다.
