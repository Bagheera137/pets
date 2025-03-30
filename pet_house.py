import time

import wrap

wrap.world.create_world(626, 352)
wrap.world.set_back_image("img.png")
wrap.add_sprite_dir("sprite")


spisok=[]
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def addition(pos_x, pos_y):
    repka = wrap.sprite.add("repka", pos_x, pos_y, "repka_bolshaya")
    wrap.sprite.set_size_percent(repka, 40, 40)
    spisok.append({"id": repka,"col":0,"x":40})



@wrap.always(1000)
def resize():
    for i in spisok:
        if i["col"]<5:
            wrap.sprite.set_size_percent(i["id"], i["x"], i["x"])
            i["x"] +=10
            i["col"]+=1