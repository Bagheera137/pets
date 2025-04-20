import wrap

def create_block(x,y):
    block = wrap.sprite.add("mario-scenery", x, y, "block", False)
    wrap.sprite.set_size_percent(block, 140, 140)
    return {"id": block, "busy":False}

def get_xy(gryadka):
    x = wrap.sprite.get_x(gryadka["id"])
    y = wrap.sprite.get_y(gryadka["id"])
    return x,y