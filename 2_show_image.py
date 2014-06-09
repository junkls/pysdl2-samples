"""
画像を表示させる

流れ
1. windowをつくる
2. factoryをつくる
3. factory.from_image("画像")からspriteをつくる
4. factory(window)からSpriteRenderSystemをつくる
5. SpriteRenderSystem.render(sprite)で描画
"""

import sdl2.ext
import time

# 初期化
sdl2.ext.init()

# windowをつくる
window = sdl2.ext.Window("画像の表示", size=(800, 600))
window.show()

# spriteオブジェクトを作るfactory
# factoryからspriteオブジェクト(2_image.jpg)をつくる
factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
sprite = factory.from_image("2_image.jpg")

# factoryから新しいSpriteRenderSystemをつくる
# renderメソッドでspriteオブジェクトを描画する
spriterenderer = factory.create_sprite_render_system(window)
spriterenderer.render(sprite)

# 2秒待つ
time.sleep(2)

# spriteオブジェクトの描画位置の変更
sprite.position = 100, 100
spriterenderer.render(sprite)

# 2秒待つ
time.sleep(2)
