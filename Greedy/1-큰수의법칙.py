# 큰 수의 법칙 - 이코테

# n - 배열의 크기
# m - 총 더해지는 횟수
# k - 같은 수를 최대로 더할 수 있는 횟수
# n, m, k = map(int, input().split())
# nums = list(map(int, input().split()))

n, m, k = [5, 8, 3]
nums = [2, 4, 5, 4, 6]

nums.sort(reverse=True)

result = 0
result += (m // (k + 1)) * nums[0] * k # 첫번째로 큰 수 더하기 횟수
result += m % (k + 1) * nums[0]
result += (m // (k + 1)) * nums[1] # 두번째로 큰 수 더하기 횟수

