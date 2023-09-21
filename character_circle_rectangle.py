from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    pass

def run_rectangle():
    pass

while True:
    run_circle()
    run_rectangle()

close_canvas()

# 시작을 어떻게 해야하는가?
    # Tip. 크게 봐야 한다, 뼈대 만들기, 큰 단위로 자르기
    # Tip. 가장 먼저 뼈대라도 실행이 되는 프로그램을 만든다 (pass 이용)
    # ① 무한반복을 만든다
    # ② 쓸 함수를 만들어 놓고 나서 선언하러 간다
