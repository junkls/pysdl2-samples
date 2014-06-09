"""
画像をカーソルキーで動かす
イベントループでカーソルキーが押された時に
sprite.positionを変更する

この方法だと移動前の描画は残ってしまう
"""

import sys
import sdl2
import sdl2.ext
import time

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("タイトル", size=(640, 400))
    window.show()

    # 背景用
    #factory_back = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    spriterender_back = sdl2.ext.SoftwareSpriteRenderSystem(window)

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

        # 描画
        spriterenderer.render(sprite)
    return 0

if __name__ == "__main__":
    # 正常に終了したらexit(0)で抜ける
    sys.exit(run())

