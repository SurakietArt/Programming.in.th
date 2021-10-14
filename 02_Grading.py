a = int(input())
b = int(input())
c = int(input())
grade = a+b+c
if grade in range(80,101):
    print('A')
elif grade in range(75,80):
    print('B+')
elif grade in range(70,75):
    print('B')
elif grade in range(65,70):
    print('C+')
elif grade in range(60,65):
    print('C')
elif grade in range(55,60):
    print('D+')
elif grade in range(50,60):
    print('D')
elif grade in range(0,50):
    print('F')