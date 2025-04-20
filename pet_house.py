import time

import part_of_gryadka
import repka
import wrap

wrap.world.create_world(626, 352)
wrap.world.set_back_image("img.png")
wrap.add_sprite_dir("sprite")


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
    rep=find_repka(pos_x,pos_y)
    if rep:
        repka.collection_repka(rep)
        spisok.remove(rep)


    gryadka=find_free_gryadka(pos_x,pos_y)
    if gryadka:
        spisok.append(repka.create_repka(gryadka))


def find_repka(pos_x,pos_y):
    for i in spisok:
        if wrap.sprite.is_collide_point(i["id"], pos_x, pos_y):
            return i

def find_free_gryadka(pos_x,pos_y):
    for i in spisok_block:
        if wrap.sprite.is_collide_point(i["id"], pos_x, pos_y) and not i["busy"]:
            return i


#@wrap.always(100)
#def resize():
 #  print(spisok)

@wrap.always(1000)
def resize():
    for i in spisok:
       repka.rost(i)



