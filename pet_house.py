import time

import wrap

wrap.world.create_world(626, 352)
wrap.world.set_back_image("img.png")
wrap.add_sprite_dir("sprite")


# block1=wrap.sprite.add("mario-scenery",50,315,"block")
# block2=wrap.sprite.add("mario-scenery",97,315,"block")
# block3=wrap.sprite.add("mario-scenery",143,315,"block")
# block4=wrap.sprite.add("mario-scenery",190,315,"block")
#
# wrap.sprite.set_size_percent(block1, 140, 140)
# wrap.sprite.set_size_percent(block2, 140, 140)
# wrap.sprite.set_size_percent(block3, 140, 140)
# wrap.sprite.set_size_percent(block4, 140, 140)

def add_block(x, y):
    block = wrap.sprite.add("mario-scenery", x, y, "block")
    wrap.sprite.set_size_percent(block, 140, 140)
def block_row(x,y):
    for i in range(x,x+47*4,47):
        add_block(i,y)
block_row(50,315)
block_row(260,233)






spisok=[]
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def addition(pos_x, pos_y):
    if wrap.sprite.is_collide_point(block,pos_x,pos_y):
        repka = wrap.sprite.add("repka", x, y, "repka_bolshaya")
        wrap.sprite.set_size_percent(repka, 40, 40)
        spisok.append({"id": repka,"col":0,"size":40})



@wrap.always(1000)
def resize():
    for i in spisok:
        if i["col"]<5:
            wrap.sprite.set_size_percent(i["id"], i["size"], i["size"])
            i["size"] +=10
            i["col"]+=1