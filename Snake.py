import os
import random
import keyboard
import time
STATE = 1
height = 30
width = 75
empty = ' '
sbody = '☐'
food = 'O'
sx,sy = 38,15
tx,ty = 37,15
turn_points = [[1,0]]
dir=[1,0]
grow = False
score = 0
screen=[[empty for _ in range(height)] for _ in range(width)]
screen[sx][sy]=sbody
screen[tx][ty]=sbody
for i in range(width):
        for j in range(height):
            screen[i][j]=empty
fx = random.randint(0,width-1)
fy = random.randint(0,height-1)
while(screen[fx][fy]!=empty):
    fx = random.randint(0,width-1)
    fy = random.randint(0,height-1)
screen[fx][fy]=food
def update(screen,sx,sy,tx,ty,score,STATE,turn_points,v):
    grow = False
    sx+=v[0]
    sy+=v[1]
    sx%=width
    sy%=height
    if screen[sx][sy]==empty:
        screen[sx][sy]=sbody
    elif screen[sx][sy]==food:
        screen[sx][sy]=sbody
        grow = True
        score+=1
        fx = random.randint(0,width-1)
        fy = random.randint(0,height-1)
        while(screen[fx][fy]!=empty):
            fx = random.randint(0,width-1)
            fy = random.randint(0,height-1)
        screen[fx][fy] = food
    elif screen[sx][sy] == sbody:
       STATE = 0
    if grow == False:
        if(screen[(tx+turn_points[0][0])%width][(ty+turn_points[0][1])%height] != '☐' and len(turn_points)>1):
                turn_points.pop(0)
        tx+=turn_points[0][0]
        ty+=turn_points[0][1]
        tx%=width
        ty%=height
        if(screen[tx][ty] == sbody):
            screen[tx][ty]=empty
    else:
         grow = False
    return screen,sx,sy,tx,ty,score,STATE,turn_points
def print_Screen(S):
    print('score : ' , score)
    for i in range(len(S[0])):
        for j in range(len(S)):
            print(S[j][i],end=' ')
        print()
a = input("Set to full screen")
while(STATE):
    #a = input("Next")
    os.system('cls')
    
    print_Screen(screen)
    dir_ = dir
    time.sleep(0.2)
    if keyboard.is_pressed('left') and dir[0]!=1:
        dir=[-1,0]
    elif keyboard.is_pressed('right') and dir[0]!=-1:
        dir=[1,0]
    elif keyboard.is_pressed('up') and dir[1]!=1:
        dir=[0,-1]
    elif keyboard.is_pressed('down') and dir[1]!=-1 :
        dir=[0, 1]

    #print(screen[tx][ty],turn_points)
    if dir!=dir_:
         turn_points.append(dir)
    screen,sx,sy,tx,ty,score,STATE,turn_points=update(screen,sx,sy,tx,ty,score,STATE,turn_points,turn_points[-1])
os.system('cls')
print("GAME OVER")
print_Screen(screen)
    
    