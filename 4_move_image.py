"""
画像をカーソルキーで動かす
イベントループでカーソルキーが押された時に
sprite.positionを変更する

描画前に画面を黒く埋めて直前の画像を消す
"""

import sys
import sdl2
import sdl2.ext
import time

BLACK = sdl2.ext.Color(0, 0, 0)

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("タイトル", size=(640, 400))
    window.show()

    # 画像を読み込み
    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sprite = factory.from_image("4_image.jpg")
    # 初期位置 (0, 0)
    x, y = 0, 0
    sprite.position = x, y
    # rendererを作る
    spriterenderer = factory.create_sprite_render_system(window)

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            # キーが押されてたとき
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_UP:
                    y -= 10
                    sprite.position = x, y

                elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                    y += 10
                    sprite.position = x, y

                elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                    x -= 10
                    sprite.position = x, y

                elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    x += 10
                    sprite.position = x, y

        # 移動前の画像を消すために黒で埋めとく
        sdl2.ext.fill(spriterenderer.surface, BLACK)
        # 描画
        spriterenderer.render(sprite)
    return 0

if __name__ == "__main__":
    sys.exit(run())

