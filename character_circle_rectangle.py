from pico2d imoprt *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while True:
    run_circle()
    run_retangle()

close_canvas()

# 시작을 어떻게 해야하는가?
    # Tip. 크게 봐야 한다, 뼈대 만들기, 큰 단위로 자르기
    # ① 무한반복을 만든다
    # ② 쓸 함수를 만들어 놓고 나서 선언하러 간다
