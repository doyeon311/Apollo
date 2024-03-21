# 성적이 낮은 순으로 학생 출력하기

# n명
n = int(input())

students = []
for _ in range(n):
  name, score = input().split()
  students.append((name, int(score)))

students.sort(key=lambda x: x[1])

for name, _ in students:
  print(name, end=" ")