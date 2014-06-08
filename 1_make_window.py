"""
ウインドウを出して、隠して、また出す
"""

# sdl2.ext ... SDL2のpython extentions pysdl2の基本となる
import sdl2.ext 
import time

# 640x400のウインドウを作る
window = sdl2.ext.Window("タイトル", size=(640, 400))

# 640x400のウインドウを表示
window.show()

# 1秒待つ
time.sleep(1)

# 最大化して表示
#window.maximize()

# 最小化して表示
#window.minimize()

# ウインドウを隠す
window.hide()

# 1秒待って表示
time.sleep(1)
window.show()
time.sleep(1)
