a = int(input())
b = int(input())
c = int(input())
All = a + b + c
if 80 <= All <= 100:
    print('A')
elif 75 <= All  <= 79:
    print('B+')
elif 70 <= All  <= 74:
    print('B')
elif 65 <= All <= 69:
    print('C+')
elif 60 <= All <= 64:
    print('C')
elif 55 <= All <= 59:
    print('D+')
elif 50 <= All <= 54:
    print('D')
elif 0 <= All <= 49:
    print('F')
    