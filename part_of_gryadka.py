import wrap

def create_block(x,y):
    block = wrap.sprite.add("mario-scenery", x, y, "block", False)
    wrap.sprite.set_size_percent(block, 140, 140)
    return {"id": block, "busy": False}