import time

import part_of_gryadka
import repka
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
spisok_block=[]


def block_row(x,y,col):
    for i in range(x,x+47*col,47):
        spisok_block.append(part_of_gryadka.create_block(i,y))
block_row(50,315,4)
block_row(260,233,4)
block_row(50,233,4)
block_row(260,315,4)
block_row(473,233,3)
block_row(473,315,3)


spisok=[]
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def addition(pos_x, pos_y):
    for i in spisok_block:
        if wrap.sprite.is_collide_point(i["id"],pos_x,pos_y) and not i["busy"]:
            x=wrap.sprite.get_x(i["id"])
            y= wrap.sprite.get_y(i["id"])
            i["busy"]=True
            spisok.append(repka.create_repka(x,y))
            print(spisok)
            break
        else:
            for i in spisok:
                if wrap.sprite.is_collide_point(i["id"], pos_x, pos_y):
                    wrap.sprite.remove(i["id"])
                    spisok.remove(i)
                    print(spisok)

#@wrap.always(100)
#def resize():
 #  print(spisok)

@wrap.always(1000)
def resize():
    for i in spisok:
       repka.rost(i)



