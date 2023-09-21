from pico2d import *
import os

os.chdir('C:\\GithubFiles\\2020152020DONGGEUN\\Drill02_new')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')

    # 그림 그리기
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400, 90)
    delay(1)    
    pass

def run_rectangle():
    print('RECTANGLE')
    pass

while True:
    run_circle()
    run_rectangle()
    break;

close_canvas()

# 시작을 어떻게 해야하는가?
    # Tip. 크게 봐야 한다, 뼈대 만들기, 큰 단위로 자르기
    # Tip. 가장 먼저 뼈대라도 실행이 되는 프로그램을 만든다 (pass 이용)
    # ① 무한반복을 만든다
    # ② 쓸 함수를 만들어 놓고 나서 선언하러 간다
