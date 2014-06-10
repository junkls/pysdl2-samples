"""
4_move_image.pyをCOP(Component-Oriented Programming)
を使って書いてみる
"""

import sys
import sdl2
import sdl2.ext
import time

BLACK = sdl2.ext.Color(0, 0, 0)

# レンダリングシステム
class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderer, self).__init__(window)

    def render(self, components):
        # 描画前に黒で埋める
        sdl2.ext.fill(self.surface, BLACK)
        super(SoftwareRenderer, self).render(components)


# Entityを継承したImageクラス
# 第1引数にworldを与える
# Entityは与えられたworldに属することになる
class Image(sdl2.ext.Entity):
    def __init__(self, world, sprite, x=0, y=0):
        self.sprite = sprite
        self.sprite.position = x, y


def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("タイトル", size=(640, 400))
    window.show()

    # Worldにはシステムを追加してあとでまとめて実行する
    world = sdl2.ext.World()

    # spriteの描画前に画面を黒で埋めるSoftwareRenderer
    spriterenderer = SoftwareRenderer(window)

    # worldにレンダリングシステムspriterendererを追加
    world.add_system(spriterenderer)

    # 画像を読み込み
    # スプライトを2つ作る
    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sp_im_1 = factory.from_image("4_image.jpg")
    sp_im_2 = factory.from_image("4_image.jpg")

    # 初期位置0, 0 と 0, 150
    im_1 = Image(world, sp_im_1, 0, 0)
    im_2 = Image(world, sp_im_2, 0, 150)
    x1, y1 = im_1.sprite.position
    x2, y2 = im_2.sprite.position

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break

            # キーが押されてたとき
            if event.type == sdl2.SDL_KEYDOWN:

                # im_1の操作 上下左右のカーソルキー
                if event.key.keysym.sym == sdl2.SDLK_UP:
                    y1 -= 10
                    im_1.sprite.position = x1, y1

                elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                    y1 += 10
                    im_1.sprite.position = x1, y1

                elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                    x1 -= 10
                    im_1.sprite.position = x1, y1

                elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    x1 += 10
                    im_1.sprite.position = x1, y1

                # im_2の操作 hjklで移動
                elif event.key.keysym.sym == sdl2.SDLK_k:
                    y2 -= 10
                    im_2.sprite.position = x2, y2

                elif event.key.keysym.sym == sdl2.SDLK_j:
                    y2 += 10
                    im_2.sprite.position = x2, y2

                elif event.key.keysym.sym == sdl2.SDLK_h:
                    x2 -= 10
                    im_2.sprite.position = x2, y2

                elif event.key.keysym.sym == sdl2.SDLK_l:
                    x2 += 10
                    im_2.sprite.position = x2, y2

        # worldにいれたシステムを処理
        world.process()
    return 0

if __name__ == "__main__":
    sys.exit(run())


