swap = input()
ball = ['1', '2', '3'] #ball in '1'

for i in swap.upper():
    if i == 'A':
        ball[0], ball[1] = ball[1], ball[0]
    elif i == 'B':
        ball[2], ball[1] = ball[1], ball[2]
    elif i == 'C':
        ball[0], ball[2] = ball[2], ball[0]

if ball[0] == '1':
    print('1')
if ball[1] == '1':
    print('2')
if ball[2] == '1':
    print('3')
