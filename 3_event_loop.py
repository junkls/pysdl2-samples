"""
イベントループを作る
"""

import sys
import sdl2
import sdl2.ext
import time

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("タイトル", size=(640, 400))
    window.show()

    # sdl2.SDL_QUITでループから抜け出す
    running = True
    while running:
        # get_eventsでイベントキューのすべてのイベントを取得
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
    return 0

if __name__ == "__main__":
    # 正常に終了したらexit(0)で抜ける
    sys.exit(run())
