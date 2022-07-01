n = int(input()) # 학생 수

students = [] # 학생 정보 리스트
for _ in range(n):
  students.append(input().split())

# 리스트 정렬
students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 이름만 출력
for student in students:
  print(student[0])