import part_of_gryadka
import wrap

def create_repka(gryadka,product):
    x,y=part_of_gryadka.get_xy(gryadka)
    p= wrap.sprite.add("repka", x, y, product)
    wrap.sprite.set_size_percent(p, 40, 40)
    gryadka["busy"]=True
    return {"id": p, "col": 0, "size": 40,"gryadka":gryadka}



def rost(repka):
    if repka["col"] < 5:
        wrap.sprite.set_size_percent(repka["id"], repka["size"], repka["size"])
        repka["size"] += 10
        repka["col"] += 1


def collection_repka(rep):
    if rep["col"] == 5:
        wrap.sprite.remove(rep["id"])
        rep["gryadka"]["busy"] = False
        return True