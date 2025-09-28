import os
import random
import keyboard
import time
STATE = 1
speed = 1
HEIGHT = 30
WIDTH = 75
EMPTY = ' '
SBODY = '☐'
FOOD = '\b🥚'
VITAMIN_D = '\b🔴'
FOODS=[FOOD,VITAMIN_D]
t_decay = 0
nfspawn = 0 #no: of food spawn
sx,sy = 38,15
tx,ty = 37,15
turn_points  = [[1,0]]
dir=[1,0]
grow = False
score = 0
screen=[[EMPTY for _ in range(HEIGHT)] for _ in range(WIDTH)]
screen[sx][sy]=SBODY
screen[tx][ty]=SBODY
for i in range(WIDTH):
        for j in range(HEIGHT):
            screen[i][j]=EMPTY
food_note='EAT ME!'
vit_note='EAT YOUR VITAMINS ON TIME!'

def spawn_food(fn = 0):
    fx = random.randint(0,WIDTH-1)
    fy = random.randint(0,HEIGHT-1)
    while(screen[fx][fy]!=EMPTY):
        fx = random.randint(0,WIDTH-1)
        fy = random.randint(0,HEIGHT-1)
    screen[fx][fy] = FOOD
    if(fn):
        for l in range(len(food_note)):
            screen[(fx+1+l)%WIDTH][fy]=food_note[l]
def spawn_vit(fn = 0):
    fx = random.randint(0,WIDTH-1)
    fy = random.randint(0,HEIGHT-1)
    while(screen[fx][fy]!=EMPTY):
        fx = random.randint(0,WIDTH-1)
        fy = random.randint(0,HEIGHT-1)
    screen[fx][fy] = VITAMIN_D
    if(fn):
        for l in range(len(food_note)):
            screen[(fx+1+l)%WIDTH][fy]=food_note[l]
def update(screen,sx,sy,tx,ty,score,t_decay,nfspawn,STATE,turn_points,v):
    grow = False
    sx+=v[0]
    sy+=v[1]
    sx%=WIDTH
    sy%=HEIGHT
    if t_decay>0: t_decay-=1
    if screen[sx][sy]==EMPTY:
        screen[sx][sy]=SBODY
    elif screen[sx][sy] in FOODS or screen[sx][sy] in food_note:
        if(screen[sx][sy] in FOODS):
            nfspawn+=1
            score+=1 + (screen[sx][sy]==VITAMIN_D)*((t_decay-t_decay%5)/5)
            if((screen[sx][sy]==VITAMIN_D)):t_decay = 0
            grow = True
            if nfspawn%5!=0:
                spawn_food()
            else:
                t_decay = 50
                spawn_vit()
        screen[sx][sy]=SBODY
    elif screen[sx][sy] == SBODY:
       STATE = 0
    if(screen[(tx+turn_points[0][0])%WIDTH][(ty+turn_points[0][1])%HEIGHT] != SBODY and len(turn_points)>1):
                turn_points.pop(0)
    if grow == False:
        tx+=turn_points[0][0]
        ty+=turn_points[0][1]
        tx%=WIDTH
        ty%=HEIGHT
        if(screen[tx][ty] == SBODY):
            screen[tx][ty]=EMPTY
    else:
         grow = False
    return screen,sx,sy,tx,ty,score,t_decay,nfspawn,STATE,turn_points
def print_Screen(S):
    print('score : ' , score)
    if t_decay>0:
        for _ in range(t_decay): print('🟥',end='')
    else:
        print('Controls : ↑ ↓ → ← space')
    for i in range(len(S[0])):
        for j in range(len(S)):
            print(S[j][i],end=' ')
        print()
input("Press Enter to start (Set to full screen first)...")
spawn_food(1)
while(STATE):
    os.system('cls' if os.name == 'nt' else 'clear')
    print_Screen(screen)

    dir_ = dir
    if keyboard.is_pressed('space'):
        time.sleep(0.05/speed)
    else:
        time.sleep(0.2/speed)
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
    screen,sx,sy,tx,ty,score,t_decay,nfspawn,STATE,turn_points=update(screen,sx,sy,tx,ty,score,t_decay,nfspawn,STATE,turn_points,turn_points[-1])
os.system('cls' if os.name == 'nt' else 'clear')
print("GAME OVER !")
print_Screen(screen)
input("Press Enter to exit...")

    
    
