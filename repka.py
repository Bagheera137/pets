import part_of_gryadka
import wrap

def create_repka(gryadka,product):
    width = wrap.sprite.get_width(gryadka["id"])
    height = wrap.sprite.get_height(gryadka["id"])
    print(width)
    x,y=part_of_gryadka.get_xy(gryadka)
    bottom=wrap.sprite.get_bottom(gryadka["id"])
    p= wrap.sprite.add("repka", x, y, product)
    wrap.sprite.set_size(p, width / 2, height)
    wrap.sprite.move_bottom_to(p,bottom)
    gryadka["busy"]=True
    return {"id": p, "col": 0, "width":width/2 ,"height":height ,"gryadka":gryadka}



def rost(repka):

    width=wrap.sprite.get_width(repka["gryadka"]["id"])
    height=wrap.sprite.get_height(repka["gryadka"]["id"])

    if repka["col"] < 5 :
        wrap.sprite.set_size(repka["id"], repka["width"], repka["height"])
        repka["width"] += 8
        repka["height"] += 8
        repka["col"] += 1
        bottom = wrap.sprite.get_bottom(repka["gryadka"]["id"])
        wrap.sprite.move_bottom_to(repka["id"], bottom)

def collection_repka(rep):
    if rep["col"] == 5:
        wrap.sprite.remove(rep["id"])
        rep["gryadka"]["busy"] = False
        return True