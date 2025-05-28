import part_of_gryadka
import wrap

def create_repka(gryadka,product):
    x,y=part_of_gryadka.get_xy(gryadka)
    bottom=wrap.sprite.get_bottom(gryadka["id"])
    p= wrap.sprite.add("repka", x, y, product)
    a,b=calculation(p,gryadka["id"])
    wrap.sprite.set_size(p, a, b)
    wrap.sprite.move_bottom_to(p,bottom)
    gryadka["busy"]=True
    return {"id": p, "col": 0, "width":a ,"height":b ,"gryadka":gryadka}

def calculation(product,gryadka):
    width = wrap.sprite.get_width(gryadka)
    height = wrap.sprite.get_height(gryadka)
    wid_p=wrap.sprite.get_width(product)
    heig_p = wrap.sprite.get_height(product)

    width_product=(heig_p*width)/height
    height_product=(wid_p*height)/width
    st=heig_p/wid_p
    h_r=width*st
    return width, h_r



def rost(repka):

    width=wrap.sprite.get_width(repka["gryadka"]["id"])
    height=wrap.sprite.get_height(repka["gryadka"]["id"])

    if repka["col"] < 5 :
        #wrap.sprite.set_size(repka["id"], repka["width"], repka["height"])
        #repka["width"] += 8
        #repka["height"] += 8
        repka["col"] += 1
        bottom = wrap.sprite.get_bottom(repka["gryadka"]["id"])
        wrap.sprite.move_bottom_to(repka["id"], bottom)

def collection_repka(rep):
    if rep["col"] == 5:
        wrap.sprite.remove(rep["id"])
        rep["gryadka"]["busy"] = False
        return True