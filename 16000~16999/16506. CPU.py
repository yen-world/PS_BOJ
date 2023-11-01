N = int(input())

for i in range(N) :
    bit = ''
    opcode, rD, rA, rB = input().split()
    rD = int(rD)
    rA = int(rA)
    rB = int(rB)
    csharp = ''
    
    if opcode == "ADD":
        bit += '00000'
        csharp = bin(rB)[2:].zfill(3)+'0'
    elif opcode == "ADDC":
        bit += '00001'
        csharp = bin(rB)[2:].zfill(4)
    elif opcode == "SUB":
        bit += '00010'
        csharp = bin(rB)[2:].zfill(3)+'0'
    elif opcode == "SUBC":
        bit += '00011'
        csharp = bin(rB)[2:].zfill(4)
    elif opcode == "MOV":
        bit += '00100'
        csharp = bin(rB)[2:].zfill(3)+'0'
    elif opcode == "MOVC":
        bit += '00101'
        csharp = bin(rB)[2:].zfill(4)
    elif opcode == "AND":
        bit += '00110'
        csharp = bin(rB)[2:].zfill(3)+'0'
    elif opcode == "ANDC":
        bit += '00111'
        csharp = bin(rB)[2:].zfill(4)
    elif opcode == "OR":
        bit += '01000'
        csharp = bin(rB)[2:].zfill(3)+'0'
    elif opcode == "ORC":
        bit += '01001'
        csharp = bin(rB)[2:].zfill(4)
    elif opcode == "NOT":
        bit += '01010'
        csharp = bin(rB)[2:].zfill(3)+'0'
    elif opcode == "MULT":
        bit += '01100'
        csharp = bin(rB)[2:].zfill(3)+'0'
    elif opcode == "MULTC":
        bit += '01101'
        csharp = bin(rB)[2:].zfill(4)
    elif opcode == "LSFTL":
        bit += '01110'
        csharp = bin(rB)[2:].zfill(3)+'0'
    elif opcode == "LSFTLC":
        bit += '01111'
        csharp = bin(rB)[2:].zfill(4)
    elif opcode == "LSFTR":
        bit += '10000'
        csharp = bin(rB)[2:].zfill(3)+'0'
    elif opcode == "LSFTRC":
        bit += '10001'
        csharp = bin(rB)[2:].zfill(4)
    elif opcode == "ASFTR":
        bit += '10010'
        csharp = bin(rB)[2:].zfill(3)+'0'
    elif opcode == "ASFTRC":
        bit += '10011'
        csharp = bin(rB)[2:].zfill(4)
    elif opcode == "RL":
        bit += '10100'
        csharp = bin(rB)[2:].zfill(3)+'0'
    elif opcode == "RLC":
        bit += '10101'
        csharp = bin(rB)[2:].zfill(4)
    elif opcode == "RR":
        bit += '10110'
        csharp = bin(rB)[2:].zfill(3)+'0'
    elif opcode == "RRC":
        bit += '10111'
        csharp = bin(rB)[2:].zfill(4)
        

    bit += '0'

    bit += bin(rD)[2:].zfill(3)

    bit += bin(rA)[2:].zfill(3)

    bit += csharp

    print(bit)