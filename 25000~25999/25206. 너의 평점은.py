result = 0
sum_value = 0.0
P_count = 0
for i in range(20):
    subject, credit, grade = map(str, input().split())
    credit = float(credit)
    sum_value += credit
    if grade == 'A+':
        result += credit * 4.5
    elif grade == 'A0':
        result += credit * 4.0
    elif grade == 'B+':
        result += credit * 3.5
    elif grade == 'B0':
        result += credit * 3.0
    elif grade == 'C+':
        result += credit * 2.5
    elif grade == 'C0':
        result += credit * 2.0
    elif grade == 'D+':
        result += credit * 1.5
    elif grade == 'D0':
        result += credit * 1.0
    elif grade == 'F':
        result += credit * 0.0
    elif grade == 'P':
        P_count += credit
print("%.6f" % (result/(sum_value-P_count)))
