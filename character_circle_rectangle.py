from pico2d import *
import math
# import os

# os.chdir('C:\\GithubFiles\\2020152020DONGGEUN\\Drill02_new')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')

    # 원 회전
    cx, cy, r = 400, 300, 200
    for deg in range(0,360,1):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01) 

def run_rectangle():
    print('RECTANGLE')
    for x in range(50,750+1, 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        delay(0.01)

while True:
    # run_circle()
    run_rectangle()
    break;

close_canvas()

# 시작을 어떻게 해야하는가?
    # Tip. 크게 봐야 한다, 뼈대 만들기, 큰 단위로 자르기
    # Tip. 가장 먼저 뼈대라도 실행이 되는 프로그램을 만든다 (pass 이용)
    # ① 무한반복을 만든다
    # ② 쓸 함수를 만들어 놓고 나서 선언하러 간다

# Tip. while문보다는 for문을 쓰는 것을 추천
# Tip. 매개변수는 가능한 변수 1개로
# Tip. 함수 1개 만들고 나서 정상동작 확인되면, main문에서 주석처리
    # "test read time"을 줄이기 위함
    

