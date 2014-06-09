"""
テキストの表示

2_show_image.pyと同じような流れでテキストを表示する
"""
import sdl2
import sdl2.ext
import time

sdl2.ext.init()
window = sdl2.ext.Window("テキストの表示", size=(640, 400))
window.show()

# フォントを読み込む
meiryo = sdl2.ext.FontManager("C:\Windows\Fonts\meiryo.ttc")
# テキストをsurfaceに
text_surface = meiryo.render("テキストを表示してみる。Hello world")

# surfaceからspriteをつくる
factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
sprite = factory.from_surface(text_surface)

spriterenderer = factory.create_sprite_render_system(window)
spriterenderer.render(sprite)

time.sleep(3)
