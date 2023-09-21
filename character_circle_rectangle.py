from pico2d import *
import math

# import os
# os.chdir('C:\\GithubFiles\\2020152020DONGGEUN\\Drill02_new')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render_frame(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01) 
    

def run_circle():
    print('CIRCLE')

    # 원 회전
    cx, cy, r = 400, 300, 200
    for deg in range(0,360,1):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        render_frame(x, y)

def run_rectangle():
    print('RECTANGLE')
    
    for x in range(50, 750+1, 10):
        render_frame(x, 90)

    for x in range(750, 50-1, -10):
        render_frame(x, 550)

while True:
    #run_circle()
    run_rectangle()
    break;

close_canvas()



# 시작을 어떻게 해야하는가?
    # Tip. 크게 봐야 한다, 뼈대 만들기, 큰 단위로 자르기
    # Tip. 가장 먼저 뼈대라도 실행이 되는 프로그램을 만든다 (pass 이용)
    # ① 무한반복을 만든다
    # ② 쓸 함수를 먼저 만들어 놓고 나서 선언하러 간다

# Tip. while문보다는 for문을 쓰는 것을 추천
# Tip. 매개변수는 가능한 변수 1개로 정리
# Tip. 함수 1개 만들고 나서 정상동작 확인되면, main문에서 주석처리
    # "test read time"을 줄이기 위함
# Tip. 특정 코드(한/두줄 코드)가 정확히 동작하는 것을 확인할 때 IDLE Shell을 이용한다.
    # 역시 "test read time"을 줄이기 위함
# Tip. 반복되는 코드가 보일 시, 함수로 선언하여 사용한다
# Tip. 수정된 코드가 앞 코드를 건드릴 경우, 잘 동작하는지 재확인한다.
