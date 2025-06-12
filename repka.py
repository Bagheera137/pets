import part_of_gryadka
import wrap

def create_repka(gryadka,product):
    x,y=part_of_gryadka.get_xy(gryadka)
    bottom=wrap.sprite.get_bottom(gryadka["id"])
    p= wrap.sprite.add("repka", x, y, product)
    a,b=calculation(p,gryadka["id"])
    wrap.sprite.set_size(p, 0, 0)
    wrap.sprite.move_bottom_to(p,bottom)
    gryadka["busy"]=True
    return {"id": p, "col": 0, "width":0 ,"height":0 ,"gryadka":gryadka,"final_width":a,"final_height":b}

def calculation(product,gryadka):
    width = wrap.sprite.get_width(gryadka)
    height = wrap.sprite.get_height(gryadka)
    wid_p=wrap.sprite.get_width(product)
    heig_p = wrap.sprite.get_height(product)

    h_p=(heig_p*width)/wid_p
    if h_p<2*height:
        return width,h_p
    else:
        w_p=(wid_p*height*2)/heig_p
        return w_p,height*2


def rost(repka):

    width=wrap.sprite.get_width(repka["gryadka"]["id"])
    height=wrap.sprite.get_height(repka["gryadka"]["id"])

    if repka["col"] < 5 :
        w=repka["final_width"]/5
        h=repka["final_height"]/5
        repka["width"] += w
        repka["height"] += h
        repka["col"] += 1
        wrap.sprite.set_size(repka["id"], repka["width"], repka["height"])
        bottom = wrap.sprite.get_bottom(repka["gryadka"]["id"])
        wrap.sprite.move_bottom_to(repka["id"], bottom)

def collection_repka(rep):
    if rep["col"] == 5:
        wrap.sprite.remove(rep["id"])
        rep["gryadka"]["busy"] = False
        return True