oper1 = int(input())
oper2 = int(input())

print(oper1 * int(oper2 % 100 % 10))
print(oper1 * int(oper2 % 100 / 10))
print(oper1 * int(oper2 / 100))
print(oper1 * oper2)
