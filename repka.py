
import wrap
def create_repka(x,y):
    repka = wrap.sprite.add("repka", x, y, "repka_bolshaya")
    wrap.sprite.set_size_percent(repka, 40, 40)
    return {"id": repka, "col": 0, "size": 40}

def rost(repka):
    if repka["col"] < 5:
        wrap.sprite.set_size_percent(repka["id"], repka["size"], repka["size"])
        repka["size"] += 10
        repka["col"] += 1
