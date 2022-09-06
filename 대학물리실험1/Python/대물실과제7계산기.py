f = "1"

while f != "0" :

    a = list()
    b = list()
    c = list()
    d = list()

    hap = 0

    print("-------------------------------------")
    print("대학물리실험 7. 뉴턴 2법칙 보고서 V3")
    print("-------------------------------------")

    print("m1을 입력하세요 : ", end = '')
    m1 = float(input())
    print("m2를 입력하세요 : ", end = '')
    m2 = float(input())

    print()

    for i in range(3) :
        print(i + 1, "회 - t3를 입력하세요 : ", end = '')
        c.append(float(input()))
        print(i + 1, "회 - V1을 입력하세요 : ", end = '')
        a.append(float(input()))
        print(i + 1, "회 - V2를 입력하세요 : ", end = '')
        b.append(float(input()))

        print()

        d.append((b[i] - a[i]) / c[i])
        hap = hap + d[i]

    for i in range(3) :
        if d[i] < 1 :
            print(i + 1, "회 a값은 ", round(d[i], 4), " 입니다")
        else :
            print(i + 1, "회 a값은 ", round(d[i], 3), " 입니다")

    hap = hap / 3;

    e = m2 / (m1 + m2) * 9.8

    if hap < 1 :
        print("\n실험 a의 평균은 ", round(hap, 4), " 입니다")
    else :
        print("실험 a의 평균은 ", round(hap, 3), " 입니다")

    if e < 1 :
        print("이론 a값은 ", round(e, 2), " 입니다")
    else :
        print("이론 a값은 ", round(e, 1), " 입니다")

    print("a값 오차는 ", round((e - hap) / e * 100), "% 입니다\n")

    print("아무 키나 입력하면 다시 시작됩니다.")
    print("0 을 입력하면 종료됩니다.")
    print("입력 (0을 입력하면 종료) : ", end = '')
    f = input()

    print("\n")
