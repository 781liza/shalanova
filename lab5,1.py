n = int(input())

if n < 2:
    print("Нужно хотя бы 2 точки")
else:
    points = [int(input()) for _ in range(n)]
    total_distance = 0
    for i in range(n - 1):
        total_distance += abs(points[i + 1] - points[i])
    print(total_distance)