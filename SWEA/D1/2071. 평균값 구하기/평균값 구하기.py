T = int(input())

for test_case in range(1, T + 1):
    n = map(int, input().split())
    s = sum(n)
    result = round(s / 10)
    print(f"#{test_case} {result}")