import time

import shop

import part_of_gryadka
import repka
import wrap

wrap.world.create_world(626, 352)
wrap.world.set_back_image("img.png")
wrap.add_sprite_dir("sprite")
text=wrap.sprite.add_text("10",600,25,font_size=40,text_color=[255,0,4])
col_money=10
level=0
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
spisok_icon=[]
spisok=[]
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def addition(pos_x, pos_y):
    global text, col_money
    rep=find_repka(pos_x,pos_y)
    if rep and repka.collection_repka(rep):
        spisok.remove(rep)
        col_money=col_money+10
        wrap.sprite_text.set_text(text,str(col_money))
        money()
    else:
        gryadka=find_free_gryadka(pos_x,pos_y)
        if gryadka and col_money>=3:
            spisok.append(repka.create_repka(gryadka))
            col_money=col_money-3
            wrap.sprite_text.set_text(text, str(col_money))

def find_repka(pos_x,pos_y):
    for i in spisok:
        if wrap.sprite.is_collide_point(i["id"], pos_x, pos_y):
            return i

def find_free_gryadka(pos_x,pos_y):
    for i in spisok_block:
        if wrap.sprite.is_collide_point(i["id"], pos_x, pos_y) and not i["busy"]:
            return i

@wrap.always(1000)
def resize():
    for i in spisok:
       repka.rost(i)

def money():
    global level, spisok_icon
    if col_money>=11 and level==0:
        level=level+1
        spisok_icon=shop.creating_shop()
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def choice_plant(pos_x,pos_y):
    shop.product_selection(spisok_icon,pos_x,pos_y)




