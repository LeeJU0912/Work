a = []
b = []
c = []
sum = 0

print("-------------------------------------")
print("대학물리실험 5. 중력가속도측정 보고서")
print("-------------------------------------")

for i in range(5):
    print(i + 1, "회 - v1을 입력하세요 : ", end='')
    a.append(float(input()))
    print(i + 1, "회 - v2을 입력하세요 : ", end='')
    b.append(float(input()))
    c.append(((b[i] * b[i]) - (a[i] * a[i])) / 1.6)
    sum += c[i]

print("\n")

for i in range(5):
    print(i + 1, "회 a값은 ", round(c[i], 4), " 입니다")

sum = sum / 5

g = sum / (0.0225 / 1)

print("\na의 평균은 ", round(sum, 4), " 입니다")
print("\ng의 실험값은 ", round(g, 3), " 입니다")
