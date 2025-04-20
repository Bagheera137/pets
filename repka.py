import part_of_gryadka
import wrap

def create_repka(gryadka):
    x,y=part_of_gryadka.get_xy(gryadka)
    repka = wrap.sprite.add("repka", x, y, "repka_bolshaya")
    wrap.sprite.set_size_percent(repka, 40, 40)
    gryadka["busy"]=True
    return {"id": repka, "col": 0, "size": 40,"gryadka":gryadka}

def rost(repka):
    if repka["col"] < 5:
        wrap.sprite.set_size_percent(repka["id"], repka["size"], repka["size"])
        repka["size"] += 10
        repka["col"] += 1

def collection_repka(rep):
    wrap.sprite.remove(rep["id"])
    rep["gryadka"]["busy"] = False